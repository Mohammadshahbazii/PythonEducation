# رشته DNA ورودی
dna_sequence = "ATGTCGATGTGCATGTGCTCGATG"

# 1. تقسیم رشته به کدون‌های ۳ حرفی
codons = []
for i in range(0, len(dna_sequence), 3):
    codon = dna_sequence[i:i+3]
    if len(codon) == 3:  # فقط کدون‌های کامل را بگیر
        codons.append(codon)

print("کدون‌های استخراج شده:")
print(codons)

# 2. شمارش فراوانی هر کدون با استفاده از دیکشنری
codon_count = {}
for codon in codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1

print("\nفراوانی هر کدون:")
for codon, count in codon_count.items():
    print(f"{codon}: {count} بار")