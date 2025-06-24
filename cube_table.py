"""prints the table of the cube of the number"""
def cube_table(number):
    """Prints the table of the cube of the number"""
    cube = number ** 3
    for i in range(1, 11):
        print(f"{cube} x {i} = {cube * i}")

print("cube table of number ")
table = cube_table(40)