weight = input("Please Enter your weight: ")
unit   = input('(L)bs or (K)g: ')
if unit.upper()=="L":
    converted= weight * 0.45
print(f "You are {converted} Kilos")
else:
    converted = weight / 0.45


