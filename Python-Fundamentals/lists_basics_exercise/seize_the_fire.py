level = input().split("#")
amount_of_water = int(input())

cell_bool = False

effort = 0
total_fire = 0

print(f"Cells:")
for cell in level:
    cell_info = cell.split(" = ")
    type_of_fire = cell_info[0]
    value_of_cell = int(cell_info[1])

    cell_bool = False
    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            cell_bool = True

    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            cell_bool = True

    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            cell_bool = True

    if cell_bool:
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            effort += value_of_cell * 0.25
            total_fire += value_of_cell

            print(f" - {value_of_cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
