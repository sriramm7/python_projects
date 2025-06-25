import math

def g(a, b, c):
    # Ensure all inputs are positive
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All inputs must be positive numbers.")

    numerator = math.log(a + b ** 2)
    denominator = math.sqrt(c ** 2 + 1)
    return numerator / denominator

# Example usage
try:
    a = float(input("Enter a positive number for a: "))
    b = float(input("Enter a positive number for b: "))
    c = float(input("Enter a positive number for c: "))
    
    result = g(a, b, c)
    print(f"g({a}, {b}, {c}) = {result:.4f}")
except ValueError as e:
    print("Error:", e)
