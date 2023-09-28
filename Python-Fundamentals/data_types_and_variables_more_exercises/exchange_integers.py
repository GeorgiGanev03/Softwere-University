int_1 = int(input())
int_2 = int(input())

temp = 0

print(f"Before:")
print(f"a = {int_1}")
print(f"b = {int_2}")

temp = int_1
int_1 = int_2
int_2 = temp

print(f"After:")
print(f"a = {int_1}")
print(f"b = {int_2}")



