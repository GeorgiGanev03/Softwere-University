n = int(input())

for index in range(1, n + 1):
    strings = input()

    if "," in strings or "." in strings or "_" in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")

