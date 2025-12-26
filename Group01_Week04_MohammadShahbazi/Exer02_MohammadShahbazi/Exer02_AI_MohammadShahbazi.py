# داده‌های ورودی
students_grades = {
    "Ali": [18, 19, 17, 18],
    "Sara": [20, 15, 12, 14],
    "Reza": [10, 9, 11, 12],
    "Mina": [18, 19, 20, 19]
}

# 1. محاسبه معدل هر دانشجو
print("معدل هر دانشجو:")
for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}: {average:.2f}")

print("\n" + "="*50 + "\n")

# 2. تعیین وضعیت بر اساس معدل
print("وضعیت هر دانشجو:")
students_status = {}  # دیکشنری جدید برای ذخیره نتایج

for student, grades in students_grades.items():
    # محاسبه معدل
    average = sum(grades) / len(grades)
    
    # تعیین وضعیت
    if average >= 17:
        status = "Excellent"
    elif 12 <= average < 17:
        status = "Normal"
    else:  # average < 12
        status = "Conditional"
    
    # نمایش نتیجه
    print(f"{student}: معدل = {average:.2f} → وضعیت: {status}")
    
    # ذخیره در دیکشنری جدید
    students_status[student] = {
        "average": round(average, 2),  # معدل با دو رقم اعشار
        "status": status
    }

print("\n" + "="*50 + "\n")

# 3. نمایش دیکشنری نهایی
print("دیکشنری نهایی (students_status):")
for student, info in students_status.items():
    print(f"{student}: {info}")