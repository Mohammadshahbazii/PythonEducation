# متن ورودی
text = "Math is great. Math is fun! We love Math."

print("متن اصلی:")
print(text)
print("\n" + "=" * 50 + "\n")

# 1. حذف علائم نگارش
import string

# ایجاد جدول ترجمه برای حذف علائم نگارش
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)

print("متن پس از حذف علائم نگارش:")
print(clean_text)

# 2. تبدیل به حروف کوچک
lower_text = clean_text.lower()

print("\nمتن پس از تبدیل به حروف کوچک:")
print(lower_text)

# 3. تقسیم متن به کلمات
words = lower_text.split()

print(f"\nلیست کلمات (تعداد: {len(words)}):")
print(words)

# 4. شمارش تکرار هر کلمه با استفاده از دیکشنری
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\n" + "=" * 50)
print("نتایج شمارش کلمات:")
print("=" * 50)

# 5. نمایش نتایج
print(f"\nتعداد کل کلمات: {len(words)}")
print(f"تعداد کلمات منحصر به فرد: {len(word_count)}")

print("\nتکرار هر کلمه:")
print("-" * 30)

# مرتب‌سازی بر اساس تعداد تکرار (نزولی)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count} بار")

# محاسبه درصد هر کلمه
print("\nدرصد هر کلمه:")
print("-" * 30)
for word, count in sorted_words:
    percentage = (count / len(words)) * 100
    print(f"{word}: {percentage:.1f}% ({count} از {len(words)})")