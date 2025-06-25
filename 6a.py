import numpy as np

# Step 1: Generate two lists of 10 random integers between 1 and 100
np.random.seed(0)  # For reproducibility (optional)
list1 = np.random.randint(1, 101, size=10)
list2 = np.random.randint(1, 101, size=10)

# Step 2: Calculate mean and median
mean1 = np.mean(list1)
median1 = np.median(list1)

mean2 = np.mean(list2)
median2 = np.median(list2)

# Step 3: Print results
print("List 1:", list1)
print("Mean 1:", mean1)
print("Median 1:", median1)
print()
print("List 2:", list2)
print("Mean 2:", mean2)
print("Median 2:", median2)
print()

# Step 4: Compare
print("Comparison:")
print("Mean: List 1 > List 2" if mean1 > mean2 else "Mean: List 2 > List 1" if mean2 > mean1 else "Mean: Both are equal")
print("Median: List 1 > List 2" if median1 > median2 else "Median: List 2 > List 1" if median2 > median1 else "Median: Both are equal")

