x = input('Weight: ')
y = input('(L)bs or (K)g: ')
if y.upper() == " l ":
    con = 0.45 * int(x)
    print(f"you are {con} kgs")
else:
    con = int(x)/0.45
    print(f"you are {con} pounds")
