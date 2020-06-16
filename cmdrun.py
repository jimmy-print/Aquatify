from data import actions


def main():
    try:
        [action.get_user_val() for action in actions]
    except ValueError:
        print("format error")
        return
    for action in actions:
        if action.user_val > action.optimal:
            print(action.advice_format.format(action.optimal))


if __name__ == '__main__':
    main()
