n = int(input())

for index in range(1, n + 1):
    message = int(input())

    if message == 88:
        print(f"Hello")
    elif message == 86:
        print(f"How are you?")
    elif message < 88:
        print(f"GREAT!")
    elif message > 88:
        print(f"Bye.")






