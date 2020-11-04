import json

def figure(sentence):
    with open('keywords.json') as f:
        keywords = json.loads(f.read())

    frequency = {}

    for consume_type in keywords:
        count = 0
        for keyword in keywords[consume_type]:
            for word in sentence.split():
                if word == keyword:
                    count += 1
        frequency[consume_type] = count

    m = max(frequency.values())
    count = 0
    for val in frequency.values():
        if val == m:
            count += 1

    if count > 1:
        raise RuntimeError(f'{frequency}') 

    keys = tuple(frequency.keys())
    vals = tuple(frequency.values())

    return keys[vals.index(m)]
