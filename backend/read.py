import json
import os
from . import action_type

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'actions.json')) as f:
    json_dict = json.loads(f.read())


def get_actions():
    for name, action in json_dict.items():
        yield action_type.UserAction(
            name,
            action['query'],
            action['advice_format'],
            action['optimal'],
            action['unit']
        )


actions = tuple(get_actions())
