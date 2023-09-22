import math

record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

swim = distance_meters * time_seconds
every_15_meters = math.floor(distance_meters / 15) * 12.5
time = swim + every_15_meters

if record_seconds <= time:
    final_time = time - record_seconds
    print(f"No, he failed! He was {final_time:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")

