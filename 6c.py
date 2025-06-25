import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate x values
np.random.seed(0)  # For reproducibility
x = np.linspace(-10, 10, 15)

# Step 2: Generate y values with noise
true_y = 2 * x**2 + 3 * x + 1
noise = np.random.normal(0, 10, size=x.shape)  # Add Gaussian noise
y_noisy = true_y + noise

# Step 3: Fit a 2nd-degree polynomial
coefficients = np.polyfit(x, y_noisy, 2)
poly_func = np.poly1d(coefficients)

# Step 4: Plot original and fitted data
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly_func(x_fit)

plt.scatter(x, y_noisy, label="Noisy Data", color='red')
plt.plot(x_fit, y_fit, label="Fitted Polynomial", color='blue')
plt.title("Polynomial Fit to Noisy Data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Output coefficients
print("Fitted polynomial coefficients (a, b, c):", coefficients)