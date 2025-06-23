def is_palindrome(seq):
    return seq == seq[::-1]

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Accept matrix size
n = int(input("Enter size of the square matrix: "))

# Accept matrix elements
print(f"Enter the {n}x{n} matrix:")
matrix = []
for _ in range(n):
    row = input().strip().split()
    matrix.append(row)

print("\nInput Matrix:")
print_matrix(matrix)

# Check palindrome rows
palindrome_rows = []
non_palindrome_rows = []

for i in range(n):
    if is_palindrome(matrix[i]):
        palindrome_rows.append(i)
    else:
        non_palindrome_rows.append(i)

# Check palindrome columns
palindrome_columns = []
non_palindrome_columns = []

for j in range(n):
    col = [matrix[i][j] for i in range(n)]
    if is_palindrome(col):
        palindrome_columns.append(j)
    else:
        non_palindrome_columns.append(j)

# Display results
print("\nPalindrome Rows:", palindrome_rows if palindrome_rows else "None")
print("Non-palindrome Rows:", non_palindrome_rows if non_palindrome_rows else "None")

print("\nPalindrome Columns:", palindrome_columns if palindrome_columns else "None")
print("Non-palindrome Columns:", non_palindrome_columns if non_palindrome_columns else "None")