def main():
    with open(file='users.txt', mode="r", encoding="utf-8") as f:
        # text = f.read() # まるごと
        # text = f.readlines() # 行ごと
        text = f.read().split('\n')  # 分かれるけど最後に殻ができる

    for user in text[:-1]:
        name, age = user.split(",")
        print(name, age, sep=":")


if __name__ == '__main__':
    main()
