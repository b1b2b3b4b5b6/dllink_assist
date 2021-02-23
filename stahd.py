'''
Author: your name
Date: 2021-02-22 16:54:23
LastEditTime: 2021-02-22 16:54:38
LastEditors: your name
Description: In User Settings Edit
FilePath: \dllink_assist\stahd.py
'''


def get_status(refresh=True):

    if True == refresh:
        tool.capture_screenshot()
    ope_list = []
    status = []
    for obj in jump_list:
        res = tool.find_img(tool.get_screenshot(), obj['img'])
        if res == None:
            continue

        if obj['act_name'] == tool.Operation.CLICK:
            ope = tool.Operation()
            ope.ope_name = obj['ope_name']
            ope.act_name = obj['act_name']
            ope.cv_res = res
            ope_list.append(ope)
            status_list.append(obj['status'])
            logging.debug(f'found jump ope {ope}')

    if len(ope_list) > 0:
        return (status, ope_list)

    for obj in status_list:
        res = tool.find_img(tool.get_screenshot(), obj['img'])
        if res == None:
            continue
        status_list.append(obj['status'])

    for obj in ope_list:
        common_items = set.intersection(*map(set, [status_list, obj[status]]))
        if len(common_items) <= 0:
            continue

        if obj['act_name'] == tool.Operation.CLICK:
            ope = tool.Operation()
            ope.ope_name = obj['ope_name']
            ope.act_name = obj['act_name']
            ope.cv_res = [obj['xy'], [0, 0]]
            ope_list.append(ope)
        elif obj['act_name'] == tool.Operation.SLIDE:
            ope = tool.Operation()
            ope.ope_name = obj['ope_name']
            ope.act_name = obj['act_name']
            ope.cv_res = obj['xy']
            ope_list.append(ope)
    return (status_list, ope_list)


def goto_status(status):
    so = get_status(True)
    if len(status) <= 0:
