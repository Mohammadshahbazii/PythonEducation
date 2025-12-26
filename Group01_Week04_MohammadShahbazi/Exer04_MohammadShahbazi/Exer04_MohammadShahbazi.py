text = "Math is great. Math is fun! We love Math."

text = text.lower().replace('.', '').replace('!', '')

words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)