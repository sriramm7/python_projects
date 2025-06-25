# Input year
year = int(input("Enter a year: "))

# Check leap year using if...else
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")