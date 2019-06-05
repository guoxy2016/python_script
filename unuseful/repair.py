# coding=utf-8
import json
map = {1:'integration.txt', 2: 'car-3d-bbox-v2.txt', 3: 'lane-segmentation.txt', 4: 'multiple-choice.txt',
       5: 'pointCloudTracking.txt', 6: 'segmentation.txt'}
file = map[6]
s = json.load(open(file))
# u = {'tagsType': {'3dbox':{'tags':[{'id':'car', 'children':[{'id':'position1', 'children':[{'id':'xw1', 'name':'香甜'}]}]}]}}}
# u = {'tagList': {'pick-up': ''}}
# u = {'laneConfig':[{'id':'road1', 'name':'来大路'}]}
# u = {'laneConfig':{'id':'roads'}}
# u = {'bboxConfig':''}
# u = {'tagsType':{'3dbox':{"property":[{'id':'1', 'name':'被遮挡需改', 'default':True},{'id':'0', 'name':'biexiugai', 'children':[{'id':'0', 'name':'ceshi', 'default':False}]}]}}}
# u = {'colorBlock':{'building':{'data':[{'id':'hello'}]}}}
u = {'colorBlock':{'building':{'index':1000000000000}}}
# u = {'tagsType': {'static':{'props':{'prop1':{'children':[{'id':'pick-up', 'color': 'bule'}]}}}}}
# u = {'questions':[{},{"choices":[u'0=右侧尾灯不可见']}]}
# u = {'questions':[{"choices":""},{"choices":[u'0=右侧尾灯不可见']}, {"choices":{}, "title":u'没有表土'}]}
# u = {'tagsType': {'static':{'tags':[{'id':'car', 'children':[{'id':'position1', 'children':[{'id':'xw1', 'name':'香甜'}]}]}]}}}


def update_ui_config(source, update):
    # 如果是字典
    if isinstance(source, dict) and isinstance(update, dict):
        # 修改字段中只有id 就删除这个
        if len(update) == 1 and update.get('id'):
            return source
        # 遍历字典
        for key in update:
            # 如果原来的这层json中有这个建
            if key in source:
                # 如果更新的字段的值是''就删除这个字段
                if update[key] == '':
                    source.pop(key, None)
                # 其他情况
                else:
                    # 如果下一层是一个列表或字典递归调用
                    if isinstance(update[key], (dict, list)):
                        update_ui_config(source[key], update[key])
                    # 如果是字符类型, 整数,浮点数就升级
                    elif isinstance(update[key], (str, int, float)):
                        source[key] = update[key]
            else:
                # 如果这个键不在本层中就追加到本层中
                source.update(update)
    # 如果是列表
    elif isinstance(source, list) and isinstance(update, list):
        # 分别获取原始的和覆盖的下一级的id和索引
        sor_id_dict, sor_flag = get_list_id(source)
        upd_id_dict, upd_flag = get_list_id(update)
        # 如果下一级能获取到id
        if sor_flag and upd_flag:
            # 遍历升级字典
            for upd_id in upd_id_dict:
                # 如果升级字典中的id在原始的id中
                if upd_id in sor_id_dict:
                    # 递归调用
                    data = update_ui_config(source=source[sor_id_dict[upd_id]], update=update[upd_id_dict[upd_id]])
                    # 如果返回内内容就证明应该被删除
                    if data:
                        source.remove(data)
                # 如果升级字典中的id不在原始的id中
                else:
                    source.append(update[upd_id_dict[upd_id]])
        # 没有id的情况
        else:
            # 遍历升级的内容
            for upd in update:
                # 下一层的内容不空
                if upd:
                    if update.index(upd) <= len(source) - 1:
                        if isinstance(upd, dict) and isinstance(source[update.index(upd)], dict):
                            # 递归调用
                            data = update_ui_config(source=source[update.index(upd)], update=update[update.index(upd)])
                            if data:
                                source.remove(data)
                        # 如果不是字典
                        else:
                            # 把新的东西添加到原json中
                            if upd not in source:
                                source.append(upd)
                            else:
                                source.remove(upd)
                    # 如果升级的长度比原来的长添加.
                    else:
                        for upd in update[len(source):]:
                            source.append(upd)


def get_list_id(data_list):
    id_dict = {}
    for data in data_list:
        if isinstance(data, dict) and 'id' in data:
            id_dict[data['id']]=data_list.index(data)
    return id_dict, id_dict != {}


update_ui_config(s, u)
json.dump(s, open('ch' + file.replace('.txt', '.json'), 'w'))