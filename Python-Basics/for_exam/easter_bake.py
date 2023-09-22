import math
import sys

number = int(input())

sugar_count = 0
flour_count = 0
sugar_gr = 0
flour_gr = 0

greatest_sugar = -sys.maxsize
greatest_flour = -sys.maxsize

for gram in range(1, number + 1):

    sugar = int(input())
    sugar_gr += sugar

    flour = int(input())
    flour_gr += flour

    if sugar > greatest_sugar:
        greatest_sugar = sugar

    if flour > greatest_flour:
        greatest_flour = flour

sugar_count = sugar_gr / 950
flour_count = flour_gr / 750

print(f"Sugar: {math.ceil(sugar_count)}")
print(f"Flour: {math.ceil(flour_count)}")
print(f"Max used flour is {greatest_flour} grams, max used sugar is {greatest_sugar} grams.")
