def get_proper_divisors(n):
    """Returns a list of proper divisors of n (excluding n itself)."""
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(n):
    """Checks if the number is abundant."""
    divisors = get_proper_divisors(n)
    total = sum(divisors)
    print(f"Proper divisors of {n}: {divisors}")
    print(f"Sum of proper divisors: {total}")
    return total > n

# Example usage
number = int(input("Enter a number: "))
if is_abundant(number):
    print(f"{number} is an Abundant number.")
else:
    print(f"{number} is NOT an Abundant number.")