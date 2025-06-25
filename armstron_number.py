def is_armstrong(number):
    # Convert number to string to extract digits easily
    digits = [int(d) for d in str(number)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)

    # Display the digits
    print(f"Digits of {number}: {digits}")
    print(f"Sum of digits^{power}: {armstrong_sum}")

    return armstrong_sum == number

# Example usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
