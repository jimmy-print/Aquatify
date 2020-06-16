from constants import actions, queries


def input_generator():
    for action, query in zip(actions, queries):
        yield action, int(input('%s\n' % query))


def main():
    try:
        print(dict(input_generator()))
    except ValueError:
        print("Please enter only integers.")


if __name__ == '__main__':
    main()
