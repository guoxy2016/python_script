import os
import re
from urllib.parse import parse_qsl, urlencode
from urllib.request import urlopen

from dotenv import load_dotenv
from flask import Flask, redirect, url_for, request, jsonify, json, session
from werkzeug.security import gen_salt

load_dotenv('.env')

app = Flask(__name__)

app.secret_key = 'secret-key'
# TODO 更改服务器名称
# app.config['SERVER_NAME'] = None

client_id = os.getenv('QQ_CLIENT_ID')
client_secret = os.getenv('QQ_CLIENT_SECRET')
api_base_url = 'https://graph.qq.com/user/'
authorize_url = 'https://graph.qq.com/oauth2.0/authorize?'
access_token_url = 'https://graph.qq.com/oauth2.0/token?'
open_id_url = 'https://graph.qq.com/oauth2.0/me?'
current_state = None


@app.route('/')
def index():
    return '<h1>QQ登陆测试</h1><a href="%s">qq登陆</a>' % url_for('oauth_qq_login')


@app.route('/login/qq')
def oauth_qq_login():
    redirect_uri = url_for('oauth_qq_callback', _external=True)
    state = gen_salt(10)
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'state': state,
        'scope': 'get_user_info',
        # 'display': '',
    }
    url = authorize_url + urlencode(params)
    global current_state
    current_state = state
    return redirect(url)


# TODO 更改回调地址.
@app.route('/callback/qq')
def oauth_qq_callback():
    redirect_uri = url_for('oauth_qq_callback', _external=True)
    code = request.args.get('code')
    state = request.args.get('state')

    # TODO 这里校验state
    global current_state
    state_check = (state == current_state)
    #####################################

    access_token_params = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri
    }
    access_token_response = urlopen(access_token_url + urlencode(access_token_params))
    asr_text = access_token_response.read().decode()
    comp = re.compile(r'{.*}')
    result = comp.search(asr_text)
    if result:
        callback_json = result.group()
        error_data = json.loads(callback_json)
        return jsonify(error_data)
    resp_data = dict(parse_qsl(asr_text))
    access_token = resp_data.get('access_token')
    expires_in = resp_data.get('expires_in')
    refresh_token = resp_data.get('refresh_token')

    # TODO 这里存储access_token, expires_in, refresh_token

    open_id_params = {
        'access_token': access_token
    }
    open_id_response = urlopen(open_id_url + urlencode(open_id_params))
    oir_text = open_id_response.read().decode()
    comp = re.compile(r'{.*}')
    result = comp.search(oir_text)
    callback_json = result.group()
    oi_data = json.loads(callback_json)
    openid = oi_data.get('openid')
    client_id_ = oi_data.get('client_id')
    # TODO 这里保存openid,
    session.update(
        expires_in=expires_in,
        refresh_token=refresh_token,
        state_check=state_check,
        openid=openid,
        client_id=client_id_,
        access_token=access_token
    )
    # return redirect(url_for('get_qq_user_info'))
    return jsonify(expires_in=expires_in, refresh_token=refresh_token, state_check=state_check, openid=openid,
                   client_id=client_id_, access_token=access_token)


@app.route('/ref_token')
def refresh():
    params = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": session['refresh_token']
    }
    access_token_response = urlopen(access_token_url + urlencode(params))
    asr_text = access_token_response.read().decode()
    comp = re.compile(r'{.*}')
    result = comp.search(asr_text)
    if result:
        callback_json = result.group()
        error_data = json.loads(callback_json)
        return jsonify(error_data)
    resp_data = dict(parse_qsl(asr_text))
    access_token = resp_data.get('access_token')
    expires_in = resp_data.get('expires_in')
    refresh_token = resp_data.get('refresh_token')
    return jsonify(access_token=access_token, expires_in=expires_in, refresh_token=refresh_token)


@app.route('/info')
def get_qq_user_info():
    params = {
        'access_token': session['access_token'],
        'oauth_consumer_key': '12345',
        'openid': session['openid']
    }
    url = api_base_url + 'get_user_info'
    response = urlopen(url + urlencode(params))
    print(url)
    return response.read().decode()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
