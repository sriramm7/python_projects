def compute_expression(n):
    if n % 3 == 0:
        return 2 * n ** 2 + 1
    else:
        return 3 * n + 5

# Get input from user
num = int(input("Enter an integer: "))

# Compute and display result
result = compute_expression(num)
print(f"Result: {result}")