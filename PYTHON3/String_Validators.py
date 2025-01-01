if __name__ == '__main__':
    s = input()
    print(True if len([ch for ch in s if ch.isalnum()])>0 else False)
    print(True if len([ch for ch in s if ch.isalpha()])>0 else False)
    print(True if len([ch for ch in s if ch.isdigit()])>0 else False)
    print(True if len([ch for ch in s if ch.islower()])>0 else False)
    print(True if len([ch for ch in s if ch.isupper()])>0 else False)
