# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define your data points (x and y)
x = np.array([0, 1, 2, 3, 4, 5])         # X-axis values
y = np.array([2.1, 2.9, 3.7, 4.1, 5.3, 6.8])  # Y-axis values

# Step 2: Fit a polynomial of desired degree (e.g., 1 for linear)
degree = 1
coefficients = np.polyfit(x, y, degree)

# Step 3: Create the polynomial function using the coefficients
polynomial = np.poly1d(coefficients)

# Step 4: Generate x values for plotting the fitted curve smoothly
x_fit = np.linspace(min(x), max(x), 100)
y_fit = polynomial(x_fit)  # Compute y values for fitted line

# Step 5: Plot the original data points
plt.scatter(x, y, color='blue', label='Original Data')

# Step 6: Plot the fitted polynomial line
plt.plot(x_fit, y_fit, color='red', label=f'Fitted Degree {degree} Line')

# Step 7: Add plot labels and legend
plt.title('Polynomial Fit Using polyfit()')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()


# Step 8: Show the plot
plt.show()

# Step 9: Print the fitted coefficients
print("Fitted Polynomial Coefficients:", coefficients)
print("Fitted Polynomial Equation:")
print(polynomial)