print("we want to show count of frequently codons in a DNA sequence with using dictionary")
dna_sequence = "ATGTCGATGTGCATGTGCTCGATG"

codons_list = {}

for i in range(0, len(dna_sequence), 3):
    codon = dna_sequence[i:i+3]
    if len(codon) == 3:  # Ensure the codon is complete
        if codon in codons_list:
            codons_list[codon] += 1
        else:
            codons_list[codon] = 1

print(codons_list)