version_string = [int(digit) for digit in input().split(".")]

version_string[-1] += 1

for index in range(len(version_string) - 1, -1, -1):
    if version_string[index] > 9:
        version_string[index] = 0
        if index -1 >= 0:
            version_string[index - 1] += 1

print(*version_string, sep=".")

version_string = [int(digit) for digit in input().split(".")]
version_string[-1] += 1

#for iteration in range(0, 3):
    #if version_string[-1] > 9:
        #version_string[-1] = 0
        #version_string[1] += 1
    #if version_string[1] > 9:
        #version_string[1] = 0
        #version_string[0] += 1
#print(*version_string, sep=".")