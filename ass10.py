import numpy as np

# Create a 1D array from 1 to 10
arr = np.arange(1, 11)

# Perform slicing
print("Original array:", arr)
print("Sliced array:", arr[2:7])

# Statistical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting - add 5 to every element
arr = arr + 5
print("After broadcasting (+5):", arr)