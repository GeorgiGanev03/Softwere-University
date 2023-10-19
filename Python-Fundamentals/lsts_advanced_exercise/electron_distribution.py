n = int(input())
shells = []
for electron in range(1, n + 1):
    result = 2 * electron**2
    if result <= n:
        shells.append(result)
        n -= result
    else:
        shells.append(n)
        break
print(shells)