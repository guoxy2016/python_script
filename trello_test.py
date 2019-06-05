# coding=utf-8

import json
import requests
from trello import TrelloApi

APIKEY = '9faada868f5938a7495739632c03da13'
TOKEN = '6a1b7c832f28f3d60540067e52e4dff625e328075854fc322002af94c1e8afc5'
BOARDID = 'nXxwAWoR'


def change_iteam_status(card_id, checklist_id, checkitem_id, state):
    resp = requests.put("https://trello.com/1/cards/%s/checklist/%s/checkItem/%s" % (card_id, checklist_id, checkitem_id),
                        params=dict(key='9faada868f5938a7495739632c03da13',
                                    token='6a1b7c832f28f3d60540067e52e4dff625e328075854fc322002af94c1e8afc5'),
                        data=dict(state=state))
    resp.raise_for_status()
    return json.loads(resp.content)


print change_iteam_status('5bc851413a8b6472c7af9fcf', '5bc8514ac9b53e77a86ac422', '5bc85156d872417d57615080', 'complete')
# tre = TrelloApi(apikey=APIKEY, token=TOKEN)
# board_content = tre.boards.get(board_id=BOARDID, cards='visible')
# card_id_list = []
# for card in board_content.get('cards'):
#     # if 'detection' in card.get('name'):
#         card_id_list.append(card.get('id'))
#
# for card_id in card_id_list:
#     state = False
#     detail = tre.cards.get(card_id, checklists='all', checkItemState_fields='imcomplete')
#     print detail
    # for checklists in detail.get('checklists', []):
    #     card_id = checklists.get('idCard', )
    #     for item in checklists.get('checkItems', []):
    #         if item.get('state') != 'complete':
    #             # change_iteam_status(card_id, item.get('idChecklist'), item.get('id'), 'complete')
    #             print item.get('name')
    #             state = True
    #             break
    #     if state :break
    # if state : break


#
#
# for i in result:
#     print change_iteam_status(i['card_id'], i['checklist_id'], i['checkitem_id'], 'complete', None)

