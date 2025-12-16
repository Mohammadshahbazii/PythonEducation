samples = ["P45210820", "B78900825", "P11050901", "B33120822", "P90010915"]

# Extract the middle 4 digits 
sample_ids = [sample[1:5] for sample in samples]

print(sample_ids)