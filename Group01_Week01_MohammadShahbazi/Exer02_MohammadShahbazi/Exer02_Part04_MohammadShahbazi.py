number = input("لطفاً یک عدد وارد کنید: ")

# حذف علامت منفی اگر وجود داشته باشد
if number.startswith('-'):
    number = number[1:]

digit_count = len(number)

print("تعداد رقم‌ها:", digit_count)
