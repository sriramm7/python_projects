def is_palindrome(number):
    # Convert number to string
    str_num = str(number)
    # Compare original string with its reverse
    return str_num == str_num[::-1]

# Input from user
try:
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
except ValueError:
    print("Invalid input! Please enter an integer.")
