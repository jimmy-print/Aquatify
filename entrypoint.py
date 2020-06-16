import data
from constants import actions, queries, should


def input_generator():
    for action, query in zip(actions, queries):
        yield action, int(input('%s\n' % query))


def main():
    user = dict(input_generator())
    for i, action in enumerate(user):
        if user[action] > data.optimal[action]:
            print(should[i])


if __name__ == '__main__':
    main()
