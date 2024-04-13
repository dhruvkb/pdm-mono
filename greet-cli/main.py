from greet import get_hello_msg


def main():
    name = input("Enter your name: ") or None
    print(get_hello_msg(name))


if __name__ == "__main__":
    main()
