# Input student's marks
marks = float(input("Enter the student's marks: "))

# Define pass criteria (e.g., 35 or more is a pass)
is_pass = marks >= 35

# Display result
print(f"Pass status: {is_pass}")
if is_pass:
    print("Result: The student has passed.")
else:
    print("Result: The student has failed.")