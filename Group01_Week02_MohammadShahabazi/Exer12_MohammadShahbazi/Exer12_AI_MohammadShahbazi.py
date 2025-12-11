def find_longest_g_sequence(dna):
    """
    پیدا کردن طولانی‌ترین دنباله متوالی از حرف G در رشته DNA
    """
    max_length = 0
    current_length = 0
    positions = []  # برای ذخیره موقعیت شروع دنباله‌ها
    
    for i, char in enumerate(dna):
        if char == 'G':
            current_length += 1
            if current_length == 1:  # شروع یک دنباله جدید
                start_pos = i
        else:
            if current_length > 0:
                positions.append((start_pos, current_length))
                if current_length > max_length:
                    max_length = current_length
            current_length = 0
    
    # بررسی آخرین دنباله
    if current_length > 0:
        positions.append((len(dna) - current_length, current_length))
        if current_length > max_length:
            max_length = current_length
    
    return max_length, positions

# دریافت ورودی از کاربر
print("بررسی رشته DNA برای تکرارهای متوالی G")
print("-" * 50)

while True:
    dna_input = input("لطفا رشته DNA را وارد کنید (فقط حروف A, C, G, T): ").upper()
    
    # اعتبارسنجی ورودی
    valid_chars = set('ACGT')
    if all(char in valid_chars for char in dna_input):
        break
    else:
        print("❌ ورودی نامعتبر! فقط حروف A, C, G, T مجاز هستند.")
        print("مثال معتبر: ATGGGGGCGTGG")

# پیدا کردن طولانی‌ترین دنباله G
max_g, all_sequences = find_longest_g_sequence(dna_input)

# نمایش نتایج
print("\n" + "="*60)
print(f"🔍 تحلیل رشته DNA: {dna_input}")
print(f"طول رشته: {len(dna_input)} کاراکتر")
print("-"*60)

# نمایش تمام دنباله‌های G
if all_sequences:
    print("\nتمام دنباله‌های G پیدا شده:")
    for idx, (start, length) in enumerate(all_sequences, 1):
        is_longest = " ★" if length == max_g else ""
        sequence = dna_input[start:start+length]
        print(f"{idx}. موقعیت {start+1}-{start+length}: '{sequence}' (طول: {length}){is_longest}")
else:
    print("\n⚠️ هیچ حرف G در رشته پیدا نشد!")

print("-"*60)
print(f"\n📊 بیشترین تعداد Gهای متوالی: {max_g}")

if max_g > 0:
    # پیدا کردن اولین دنباله با بیشترین طول
    longest_seq = ""
    for start, length in all_sequences:
        if length == max_g:
            longest_seq = dna_input[start:start+length]
            print(f"نمونه دنباله با بیشترین طول: '{longest_seq}'")
            break
    
    # تحلیل بیماری (فرضی)
    if max_g >= 5:
        print("🔴 هشدار: احتمال بیماری به دلیل تکرار بیش از حد G وجود دارد!")
    elif max_g >= 3:
        print("🟡 توجه: تکرار Gها در حد متوسط است.")
    else:
        print("🟢 وضعیت: تکرار Gها طبیعی است.")