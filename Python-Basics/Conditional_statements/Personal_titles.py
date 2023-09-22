age = float(input())
m_or_f = input()

if age < 16:
    if m_or_f == "m":
        print("Master")
if age >= 16:
    if m_or_f == "m":
        print("Mr.")
if age < 16:
    if m_or_f == "f":
        print("Miss")
if age >= 16:
    if m_or_f == "f":
        print("Ms.")




