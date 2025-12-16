vibration_data = [0.15, 0.33, 0.40, 0.40, 0.10, 0.22, 0.40, 0.15, 0.22, 0.15]

# Step 1: Get unique values
unique_values = list(set(vibration_data))

# Step 2: Sort in descending order
unique_values_sorted = sorted(unique_values, reverse=True)

# Step 3: Count unique values
unique_count = len(unique_values_sorted)

print("Unique values (sorted descending):", unique_values_sorted)
print("Number of unique values:", unique_count)