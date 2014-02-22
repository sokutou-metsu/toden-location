# -*- coding: utf-8-unix -*-
u"""データソース
"""

STOP_CODE_TABLE = {
    '9901': u'三ノ輪橋',
    '9902': u'荒川一中前',
    '9903': u'荒川区役所前',
    '9904': u'荒川二丁目',
    '9905': u'荒川七丁目',
    '9906': u'町屋駅前',
    '9907': u'町屋二丁目',
    '9908': u'東尾久三丁目',
    '9909': u'熊野前',
    '9910': u'宮ノ前',
    '9911': u'小台',
    '9912': u'荒川遊園地前',
    '9913': u'荒川車庫前',
    '9914': u'梶原',
    '9915': u'栄町',
    '9916': u'王子駅前',
    '9917': u'飛鳥山',
    '9918': u'滝野川一丁目',
    '9919': u'西ヶ原四丁目',
    '9920': u'新庚申塚',
    '9921': u'庚申塚',
    '9922': u'巣鴨新田',
    '9923': u'大塚駅前',
    '9924': u'向原',
    '9925': u'東池袋四丁目',
    '9926': u'都電雑司ヶ谷',
    '9927': u'鬼子母神前',
    '9928': u'学習院下',
    '9929': u'面影橋',
    '9930': u'早稲田'
}

def get_stop_name(code):
    u"""停留所名称を取得する
    """
    return STOP_CODE_TABLE.get(code, None)

def find_stop_code(name):
    u"""停留所名称からコードを探す
    """
    for k, v in STOP_CODE_TABLE.items():
        if name == v:
            return k
    return None

_FROM_MINOWA_TO_OJI = 0
_FROM_OJI_TO_WASEDA = 1
_FROM_WASEDA_TO_OJI = 2
_FROM_OJI_TO_MINOWA = 3

_DIRECTION_TABLE = {
    656: _FROM_MINOWA_TO_OJI,
    676: _FROM_MINOWA_TO_OJI,
    103: _FROM_OJI_TO_WASEDA,
    123: _FROM_OJI_TO_WASEDA,
    58: _FROM_WASEDA_TO_OJI,
    78: _FROM_WASEDA_TO_OJI,
    708: _FROM_OJI_TO_MINOWA,
    728: _FROM_OJI_TO_MINOWA
}

def _get_direction(val):
    if val not in _DIRECTION_TABLE:
        return None
    return _DIRECTION_TABLE[val]

STOP = 1
MOVE = 2

FOR_WASEDA = 1
FOR_MINOWA = 2

_POSITION_TABLE = {
    _FROM_MINOWA_TO_OJI: {
        1111: (STOP, FOR_WASEDA, '9901', None),
        1078: (MOVE, FOR_WASEDA, '9901', '9902'),
        1045: (STOP, FOR_WASEDA, '9902', None),
        1010: (MOVE, FOR_WASEDA, '9902', '9903'),
        976: (STOP, FOR_WASEDA, '9903', None),
        941: (MOVE, FOR_WASEDA, '9903', '9904'),
        907: (STOP, FOR_WASEDA, '9904', None),
        873: (MOVE, FOR_WASEDA, '9904', '9905'),
        839: (STOP, FOR_WASEDA, '9905', None),
        807: (MOVE, FOR_WASEDA, '9905', '9906'),
        775: (STOP, FOR_WASEDA, '9906', None),
        739: (MOVE, FOR_WASEDA, '9906', '9907'),
        704: (STOP, FOR_WASEDA, '9907', None),
        671: (MOVE, FOR_WASEDA, '9907', '9908'),
        639: (STOP, FOR_WASEDA, '9908', None),
        603: (MOVE, FOR_WASEDA, '9908', '9909'),
        567: (STOP, FOR_WASEDA, '9909', None),
        533: (MOVE, FOR_WASEDA, '9909', '9910'),
        499: (STOP, FOR_WASEDA, '9910', None),
        465: (MOVE, FOR_WASEDA, '9910', '9911'),
        432: (STOP, FOR_WASEDA, '9911', None),
        398: (MOVE, FOR_WASEDA, '9911', '9912'),
        364: (STOP, FOR_WASEDA, '9912', None),
        330: (MOVE, FOR_WASEDA, '9912', '9913'),
        297: (STOP, FOR_WASEDA, '9913', None),
        261: (MOVE, FOR_WASEDA, '9913', '9914'),
        225: (STOP, FOR_WASEDA, '9914', None),
        191: (MOVE, FOR_WASEDA, '9914', '9915'),
        157: (STOP, FOR_WASEDA, '9915', None)
    },
    _FROM_OJI_TO_WASEDA: {
        118: (MOVE, FOR_WASEDA, '9915', '9916'),
        163: (STOP, FOR_WASEDA, '9916', None),
        189: (MOVE, FOR_WASEDA, '9916', '9917'),
        196: (MOVE, FOR_WASEDA, '9916', '9917'),
        229: (STOP, FOR_WASEDA, '9917', None),
        263: (MOVE, FOR_WASEDA, '9917', '9918'),
        297: (STOP, FOR_WASEDA, '9918', None),
        331: (MOVE, FOR_WASEDA, '9918', '9919'),
        365: (STOP, FOR_WASEDA, '9919', None),
        398: (MOVE, FOR_WASEDA, '9919', '9920'),
        431: (STOP, FOR_WASEDA, '9920', None),
        466: (MOVE, FOR_WASEDA, '9920', '9921'),
        501: (STOP, FOR_WASEDA, '9921', None),
        538: (MOVE, FOR_WASEDA, '9921', '9922'),
        575: (STOP, FOR_WASEDA, '9922', None),
        606: (MOVE, FOR_WASEDA, '9922', '9923'),
        638: (STOP, FOR_WASEDA, '9923', None),
        665: (MOVE, FOR_WASEDA, '9923', '9924'),
        672: (MOVE, FOR_WASEDA, '9923', '9924'),
        706: (STOP, FOR_WASEDA, '9924', None),
        739: (MOVE, FOR_WASEDA, '9924', '9925'),
        773: (STOP, FOR_WASEDA, '9925', None),
        809: (MOVE, FOR_WASEDA, '9925', '9926'),
        846: (STOP, FOR_WASEDA, '9926', None),
        878: (MOVE, FOR_WASEDA, '9926', '9927'),
        911: (STOP, FOR_WASEDA, '9927', None),
        944: (MOVE, FOR_WASEDA, '9927', '9928'),
        976: (STOP, FOR_WASEDA, '9928', None),
        1011: (MOVE, FOR_WASEDA, '9928', '9929'),
        1045: (STOP, FOR_WASEDA, '9929', None),
        1080: (MOVE, FOR_WASEDA, '9929', '9930')
    },
    _FROM_WASEDA_TO_OJI: {
        1114: (STOP, FOR_MINOWA, '9930', None),
        1078: (MOVE, FOR_MINOWA, '9930', '9929'),
        1043: (STOP, FOR_MINOWA, '9929', None),
        1009: (MOVE, FOR_MINOWA, '9929', '9928'),
        976: (STOP, FOR_MINOWA, '9928', None),
        942: (MOVE, FOR_MINOWA, '9928', '9927'),
        909: (STOP, FOR_MINOWA, '9927', None),
        876: (MOVE, FOR_MINOWA, '9927', '9926'),
        844: (STOP, FOR_MINOWA, '9926', None),
        807: (MOVE, FOR_MINOWA, '9926', '9925'),
        771: (STOP, FOR_MINOWA, '9925', None),
        737: (MOVE, FOR_MINOWA, '9925', '9924'),
        704: (STOP, FOR_MINOWA, '9924', None),
        670: (MOVE, FOR_MINOWA, '9924', '9923'),
        636: (STOP, FOR_MINOWA, '9923', None),
        604: (MOVE, FOR_MINOWA, '9923', '9922'),
        573: (STOP, FOR_MINOWA, '9922', None),
        536: (MOVE, FOR_MINOWA, '9922', '9921'),
        499: (STOP, FOR_MINOWA, '9921', None),
        464: (MOVE, FOR_MINOWA, '9921', '9920'),
        429: (STOP, FOR_MINOWA, '9920', None),
        396: (MOVE, FOR_MINOWA, '9920', '9919'),
        363: (STOP, FOR_MINOWA, '9919', None),
        329: (MOVE, FOR_MINOWA, '9919', '9918'),
        295: (STOP, FOR_MINOWA, '9918', None),
        261: (MOVE, FOR_MINOWA, '9918', '9917'),
        227: (STOP, FOR_MINOWA, '9917', None),
        201: (MOVE, FOR_MINOWA, '9917', '9916'),
        194: (MOVE, FOR_MINOWA, '9917', '9916'),
        161: (STOP, FOR_MINOWA, '9916', None)
    },
    _FROM_OJI_TO_MINOWA: {
        107: (MOVE, FOR_MINOWA, '9916', '9915'),
        114: (MOVE, FOR_MINOWA, '9916', '9915'),
        159: (STOP, FOR_MINOWA, '9915', None),
        193: (MOVE, FOR_MINOWA, '9915', '9914'),
        227: (STOP, FOR_MINOWA, '9914', None),
        263: (MOVE, FOR_MINOWA, '9914', '9913'),
        299: (STOP, FOR_MINOWA, '9913', None),
        332: (MOVE, FOR_MINOWA, '9913', '9912'),
        366: (STOP, FOR_MINOWA, '9912', None),
        393: (MOVE, FOR_MINOWA, '9912', '9911'),
        400: (MOVE, FOR_MINOWA, '9912', '9911'),
        434: (STOP, FOR_MINOWA, '9911', None),
        467: (MOVE, FOR_MINOWA, '9911', '9910'),
        501: (STOP, FOR_MINOWA, '9910', None),
        535: (MOVE, FOR_MINOWA, '9910', '9909'),
        569: (STOP, FOR_MINOWA, '9909', None),
        605: (MOVE, FOR_MINOWA, '9909', '9908'),
        641: (STOP, FOR_MINOWA, '9908', None),
        673: (MOVE, FOR_MINOWA, '9908', '9907'),
        706: (STOP, FOR_MINOWA, '9907', None),
        741: (MOVE, FOR_MINOWA, '9907', '9906'),
        777: (STOP, FOR_MINOWA, '9906', None),
        809: (MOVE, FOR_MINOWA, '9906', '9905'),
        841: (STOP, FOR_MINOWA, '9905', None),
        875: (MOVE, FOR_MINOWA, '9905', '9904'),
        909: (STOP, FOR_MINOWA, '9904', None),
        943: (MOVE, FOR_MINOWA, '9904', '9903'),
        978: (STOP, FOR_MINOWA, '9903', None),
        1012: (MOVE, FOR_MINOWA, '9903', '9902'),
        1047: (STOP, FOR_MINOWA, '9902', None),
        1080: (MOVE, FOR_MINOWA, '9902', '9901'),
    }
}

def _get_position_table(direction):
    return _POSITION_TABLE[direction]

def get_position(top, left):
    direction = _get_direction(left)
    if direction is None:
        return None
    table = _get_position_table(direction)
    if top not in table:
        return None
    return table.get(top, None)
