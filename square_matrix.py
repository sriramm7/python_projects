import random

def generate_matrix(n):
    matrix = [[random.randint(100, 500) for _ in range(n)] for _ in range(n)]
    return matrix

def print_matrix(matrix):
    print("Generated Matrix:")
    for row in matrix:
        formatted_row = '  '.join(f"{num:>4}" for num in row)
        print(formatted_row)

# Get user input
n = int(input("Enter the size of the square matrix (n): "))

# Generate and print matrix
matrix = generate_matrix(n)
print_matrix(matrix)
4