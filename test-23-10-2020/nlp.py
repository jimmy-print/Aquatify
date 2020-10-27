import json

def return_action_type(sentence):
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
    print(frequency.values())
    if count > 1:
        print('duplicate(s) exists, ambiguous')
    else:
        pass
        # todo problem reverse lookup dict since no duplicate(s) of the frequency values exist(s)

    return frequency