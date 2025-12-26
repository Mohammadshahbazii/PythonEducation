# لیست آرا
votes = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", 
         "Candidate B"]

print("🗳️ لیست آرا:")
print("=" * 40)
for i, vote in enumerate(votes, 1):
    print(f"{i:2}. {vote}")
print(f"\nتعداد کل آرا: {len(votes)}")

print("\n" + "="*50 + "\n")

# 1. شمارش آرا با استفاده از دیکشنری
vote_count = {}

for candidate in votes:
    if candidate in vote_count:
        vote_count[candidate] += 1
    else:
        vote_count[candidate] = 1

# 2. نمایش نتایج شمارش
print("📊 نتایج شمارش آرا:")
print("=" * 30)

# مرتب‌سازی نامزدها بر اساس تعداد آرا (نزولی)
sorted_candidates = sorted(vote_count.items(), key=lambda x: x[1], reverse=True)

for candidate, count in sorted_candidates:
    percentage = (count / len(votes)) * 100
    print(f"{candidate:15}: {count:2} رأی ({percentage:5.1f}%)")

# 3. تعیین برنده
print("\n" + "="*50)
print("🏆 نتیجه انتخابات:")
print("=" * 50)

winner = sorted_candidates[0][0]
winner_votes = sorted_candidates[0][1]

# بررسی تساوی
if len(sorted_candidates) > 1 and sorted_candidates[0][1] == sorted_candidates[1][1]:
    print("❗ نتیجه: تساوی بین نامزدها!")
    print("\nنامزدهای برتر:")
    for candidate, count in sorted_candidates:
        if count == winner_votes:
            print(f"  • {candidate} با {count} رأی")
else:
    print(f"✅ برنده: {winner} با {winner_votes} رأی")
    
    # نمایش اختلاف با نفر دوم
    if len(sorted_candidates) > 1:
        second_place = sorted_candidates[1][1]
        difference = winner_votes - second_place
        print(f"📊 اختلاف با نفر دوم: {difference} رأی")

# 4. نمایش نمودار میله‌ای
print("\n📈 نمودار میله‌ای آرا:")
print("-" * 40)

max_votes = max(vote_count.values())
for candidate, count in sorted_candidates:
    # محاسبه طول میله
    bar_length = int((count / max_votes) * 30)
    bar = "█" * bar_length
    
    percentage = (count / len(votes)) * 100
    print(f"{candidate:15}: {bar} {count:2} رأی ({percentage:5.1f}%)")

# 5. نمایش دیکشنری نهایی
print("\n📋 دیکشنری نهایی vote_count:")
print("=" * 30)
print(vote_count)