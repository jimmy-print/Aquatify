import json
from word2number import w2n

with open('data/data.json') as f:
    d = json.load(f)
with open('data/number_words.json') as f:
    d_num_words = json.load(f)

def _get_all_keywords(action_type):
    dd = d[action_type]
    for unit in dd:
        if unit[0] != '_':
            for word in dd[unit]['keywords']:
                yield word

def _get_keywords_for_action_type(action_type):
    dd = d[action_type]
    out = {}
    for unit in dd:
        if unit != 'generic' and unit[0] != '_':
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
        for keyword in keywords:
            if keyword in s:
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

class CatcherException(Exception): pass

def get_num(s, accept_nw):
    num = None
    # scan for actual numbers, 1 2 3 123
    for word in s.split():
        try:
            num = float(word)
        except ValueError:
            pass

    # now try to find words like one, two, hundred
    if num is None:
        num = _get_biggest_number(s)

    # finally try to find once twice and thrice
    # this only applies to certain action_types,
    # which is specified in data.json. for example
    # you can't drink twice but you can shower twice.
    if num is None:
        # check if action_type accepts once twice thrice
        if accept_nw:
            if _get_number_word(s) is not None:
                raise CatcherException(_get_number_word(s))
        raise RuntimeError('no number')

    return num

def _get_number_word(s):
    for word in s.split():
        for key, val in d_num_words.items():
            if word == key:
                # Returns the first value.
                # 'i shower twice thrice' -> 2.0
                return float(val)

def _get_biggest_number(s):
    def _gen_combos(s):
        size = len(s)
        for tmp_size in range(1, size + 1):
            for i in range(size):
                yield s[slice(i, i + tmp_size)]

    nums = []
    for combo in _gen_combos(s):
        try:
            nums.append(w2n.word_to_num(combo))
        except ValueError:
            pass
        except IndexError:
            # Internal error in w2n
            # (likely caused by bad number, eg thousand hundred)
            # NOTE: If the user actually puts in, "I drink thousand hundred
            # liters of water", that will cause the code to set the user's
            # num value to thousand as that is the maximum number value in
            # the sentence.
            pass

    if len(nums) > 0:
        return max(nums)
    else:
        return None

def get_accept_nw_or_not(action_type):
    if d[action_type]['_accept_nw'] == 'True':
        return True
    return False

def get_type_num_unit(s):
    action_type = get_type(s)
    accept_nw = get_accept_nw_or_not(action_type)
    try:
        num = get_num(s, accept_nw)
        unit = get_unit(s, action_type)
    except CatcherException as e:
        num = float(str(e))
        unit = 'times'

    return action_type, num, unit

def get_optimal(action_type, unit):
    return d[action_type][unit]['optimal']
