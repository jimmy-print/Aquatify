import data
from constants import actions, queries


def input_generator():
    for action, query in zip(actions, queries):
        yield action, int(input('%s\n' % query))


def main():
    user = dict(input_generator())
    for action in user:
        if user[action] > data.optimal[action]:
            print("%s is bad" % action)
        else:
            print("%s is good" % action)


if __name__ == '__main__':
    main()
