lenght = int(input())
width = int(input())
hight = int(input())
percet = float(input())

capacity = lenght * width * hight
capacity_lt = capacity * 0.001
needed_lt = capacity_lt * (1-percet / 100)

print(needed_lt)
