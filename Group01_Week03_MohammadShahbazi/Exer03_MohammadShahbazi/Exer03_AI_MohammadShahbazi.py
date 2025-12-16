problem_time = [55, 40, 28, 35, 8, 30, 60, 12, 45, 25]

# Step 1: Identify complex problems (time > 30 minutes)
complex_times = [time for time in problem_time if time > 30]

# Step 2: Count complex problems
complex_count = len(complex_times)

# Step 3: Total time spent on complex problems (in minutes)
total_minutes_complex = sum(complex_times)

# Step 4: Convert total minutes to hours and minutes
hours = total_minutes_complex // 60
minutes = total_minutes_complex % 60

print("Complex problem times (minutes):", complex_times)
print("Number of complex problems:", complex_count)
print("Total time on complex problems:", total_minutes_complex, "minutes")
print(f"Which is: {hours} hours and {minutes} minutes")