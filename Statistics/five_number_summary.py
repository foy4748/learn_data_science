import numpy as np

dataset = np.array([15, 22, 30, 35, 40, 50, 60, 70, 80, 90])

min_val = np.min(dataset)
q1     = np.percentile(dataset,25)
median = np.median(dataset)
q3     = np.percentile(dataset,75)
max_val = np.max(dataset)

print(f"Min: {min_val}")
print(f"Q1: {q1}")
print(f"Median: {median}")
print(f"Q3: {q3}")
print(f"Max: {max_val}")
