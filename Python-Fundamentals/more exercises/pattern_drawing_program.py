print("Pattern Drawing Program")

print("1. Draw a Triangle")
print("2. Draw a Rectangle")
print(f"3. Draw a Pyramid")
print(f"4. Quit")

input_line = input(f"Enter your choise (1/2/3/4)")
while input_line != "Quit":
    if input_line == "4":
        print(f"Goodbye!")
        break

    n = int(input_line)

    if n == 1:
        rows = int(input(f"Enter the number of rows for the triangle:"))

        for i in range(1, rows + 1):
            for num in range(0, i):

                print("*", end='')

            print()

    elif n == 2:
        rows = int(input(f"Enter the number of rows for the triangle:"))
        cols = int(input(f"Enter the number of columns for the rectangle:"))

        for row in range(1, rows + 1):
            for col in range(0, cols):

                print("*", end='')

            print()

    elif n == 3:

        rows = int(input(f"Enter the number of rows for the pyramid:"))

        n = 0

        for i in range(1, rows + 1):
            for space in range(rows - i):
                print(" ", end='')

            while n != (2 * i - 1):
                print("*", end='')

                n += 1

            n = 0

            print()

    input_line = input(f"Enter your choise (1/2/3/4)")