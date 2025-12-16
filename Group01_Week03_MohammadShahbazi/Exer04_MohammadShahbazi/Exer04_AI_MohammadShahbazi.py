keywords_A = {"Reason", "Logic", "Ethics", "Mind", "Belief"}
keywords_B = {"Mind", "Knowledge", "Belief", "Truth", "Logic"}

# 1. Keywords only in A
only_in_A = keywords_A - keywords_B
print("Keywords only in philosopher A:", sorted(only_in_A))  # sorted for consistent order

# 2. Common keywords (intersection)
common_keywords = keywords_A & keywords_B
print("Common keywords in both philosophers:", sorted(common_keywords))

# 3. All unique keywords (union)
all_unique_keywords = keywords_A | keywords_B
print("All unique keywords from both philosophers:", sorted(all_unique_keywords))