import numpy as np

def get_matrix():
    print("Enter elements of 2x2 matrix row-wise:")
    a11 = float(input("Enter element [1][1]: "))
    a12 = float(input("Enter element [1][2]: "))
    a21 = float(input("Enter element [2][1]: "))
    a22 = float(input("Enter element [2][2]: "))
    return np.array([[a11, a12], [a21, a22]])

def display_menu():
    print("\nMENU")
    print("1. Transpose of the matrix")
    print("2. Determinant of the matrix")
    print("3. Inverse of the matrix")
    print("4. Exit")

def main():
    matrix = get_matrix()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("Transpose of the matrix:")
            print(np.transpose(matrix))
        elif choice == '2':
            det = np.linalg.det(matrix)
            print(f"Determinant of the matrix: {det}")
        elif choice == '3':
            det = np.linalg.det(matrix)
            if det == 0:
                print("Inverse not possible. Determinant is zero.")
            else:
                print("Inverse of the matrix:")
                print(np.linalg.inv(matrix))
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
