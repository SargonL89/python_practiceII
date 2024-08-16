def main():
    greeting = input("Greeting: ").lower().strip()
    value(greeting)


def value(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()