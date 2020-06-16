from constants import actions


def foo_generator():
    for action in actions:
        yield input("%s? " % action)


def main():
    print(set(foo_generator()))


if __name__ == '__main__':
    main()
