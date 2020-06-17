from backend.data import actions


def main():
    try:
        [action.set_user_val_on_cmdline() for action in actions]
    except ValueError:
        print("format error")
        return
    for action in actions:
        if action.user_val > action.optimal:
            print(action.advice_format.format(action.optimal))


if __name__ == '__main__':
    main()
