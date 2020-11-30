import json
from word2number import w2n

with open('data/data.json') as f:
    d = json.load(f)
with open('data/number_words.json') as f:
    d_num_words = json.load(f)

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
        num = _get_biggest_number(s)

    if num is None:
        raise RuntimeError('no number')

    return num

def _get_number_word(s):
    # TODO each action type should either accept times values (once, twice)
    # or not. For example I can say I shower twice but I can't say I drink twice.
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

def get_type_num_unit(s):
    action_type = get_type(s)
    num = get_num(s)
    unit = get_unit(s, action_type)

    return action_type, num, unit

def get_optimal(action_type, unit):
    return d[action_type][unit]['optimal']
