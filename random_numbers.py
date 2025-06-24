"""Creating random numbers"""

import matplotlib.pyplot as plt
import random

def generate_random_numbers(n, lower_bound, upper_bound):
    """Generate a list of n random numbers within the specified bounds."""
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

numbers = generate_random_numbers(50, 1, 100)
print("Random Numbers:", numbers)

def plot_random_numbers(numbers):
    """Plot the generated random numbers."""
    plt.figure(figsize=(10, 5))
    plt.plot(numbers, marker='o', linestyle='-', color='b')
    plt.title('Random Numbers Plot')
    plt.xlabel('Index')
    plt.ylabel('Random Number')
    plt.grid(True)
    plt.show()

frequecy_plot = plot_random_numbers(numbers)
