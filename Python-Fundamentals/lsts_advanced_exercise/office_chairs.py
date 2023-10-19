def free_chairs(rooms):
    num_free_chairs = 0
    for room in range(1, rooms + 1):
        chairs, visitors = input().split()
        total_diff = len(chairs) - int(visitors)
        if total_diff < 0:
            print(f"{abs(total_diff)} more chairs needed in room {room}")
        num_free_chairs += total_diff
    return num_free_chairs

n = int(input())
total_free_rooms = free_chairs(n)
if total_free_rooms >= 0:
    print(f"Game On, {total_free_rooms} free chairs left")





