import json
from word2number import w2n

with open('data/new.json') as f:
    d = json.load(f)

def _get_all_keywords(action_type):
    dd = d[action_type]
    for unit in dd:
        for word in dd[unit]['keywords']:
            yield word

def _get_keywords_for_action_type(action_type):
    dd = d[action_type]
    out = {}
    for unit in dd:
        if unit != 'generic':
            out[unit] = dd[unit]['keywords']
    return out

def get_type(s):
    freq = {}
    for action_type in d.keys(): 
        tmp = 0
        for keyword in _get_all_keywords(action_type):
            for word in s.split():
                if word == keyword:
                    tmp += 1
        freq[action_type] = tmp

    m = max(freq.values())
    
    if len(freq.values()) == 1 and m == 0:
        raise RuntimeError(f'only 1 action_type exists and its frequency is 0 {freq}')

    count = 0
    for val in freq.values():
        if val == m:
            count += 1

    if count > 1 and m == 0:
        raise RuntimeError(f'all action_types did not match {freq}')

    if count > 1:
        raise RuntimeError(f'ambiguous action_type frequecy {freq}')

    keys = tuple(freq.keys())
    vals = tuple(freq.values())

    return keys[vals.index(m)]

def get_unit(s, action_type):
    freq = {}
    for unit, keywords in _get_keywords_for_action_type(action_type).items():
        tmp = 0
        for word in s.split():
            for keyword in keywords:
                if word == keyword:
                    tmp += 1
        freq[unit] = tmp

    m = max(freq.values())

    if len(freq.values()) == 1 and m == 0:
        raise RuntimeError(f'only 1 unit exists and its frequency is 0 {freq}')
    
    count = 0
    for val in freq.values():
        if val == m:
            count += 1

    if count > 1 and m == 0:
        raise RuntimeError(f'all units did not match {freq}')

    if count > 1:
        raise RuntimeError(f'ambiguous units frequency {freq}')

    keys = tuple(freq.keys())
    vals = tuple(freq.values())

    return keys[vals.index(m)]

def get_num(s):
    num = None
    for word in s.split():
        try:
            num = float(word)
        except ValueError:
            pass

    if num is None:
        raise RuntimeError('no number')

    return num

def get_type_num_unit(s):
    action_type = get_type(s)
    num = get_num(s)
    unit = get_unit(s, action_type)

    return action_type, num, unit

def get_optimal(action_type, unit):
    return d[action_type][unit]['optimal']
