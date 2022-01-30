def main():
    with open(file='users.txt', mode="r", encoding="utf-8") as f:
        text = f.read()
    print(text)


if __name__ == '__main__':
    main()
