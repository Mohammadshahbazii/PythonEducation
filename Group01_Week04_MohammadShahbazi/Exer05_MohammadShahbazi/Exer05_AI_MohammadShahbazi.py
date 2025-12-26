# لیست فایل‌های ورودی
files = ["report.pdf", "image.png", "data.csv", "logo.png", "notes.txt", 
         "thesis.pdf"]

print("لیست فایل‌های ورودی:")
for i, file in enumerate(files, 1):
    print(f"{i:2}. {file}")

print("\n" + "="*50 + "\n")

# 1. استخراج پسوند هر فایل
print("استخراج پسوندها:")
file_extensions = []
for file in files:
    # پیدا کردن آخرین نقطه و استخراج پسوند
    if '.' in file:
        extension = file.split('.')[-1]
        file_extensions.append(extension)
        print(f"{file} → .{extension}")
    else:
        print(f"{file} → بدون پسوند")

print("\n" + "="*50 + "\n")

# 2. ایجاد دیکشنری برای گروه‌بندی
files_by_extension = {}

for file in files:
    # استخراج پسوند
    if '.' in file:
        extension = file.split('.')[-1]
    else:
        extension = "no_extension"  # برای فایل‌های بدون پسوند
    
    # اضافه کردن فایل به دیکشنری
    if extension in files_by_extension:
        files_by_extension[extension].append(file)
    else:
        files_by_extension[extension] = [file]

# 3. نمایش نتایج
print("گروه‌بندی فایل‌ها بر اساس پسوند:")
print("="*50)

# مرتب‌سازی بر اساس پسوند
for extension in sorted(files_by_extension.keys()):
    file_list = files_by_extension[extension]
    print(f"\n📁 پسوند .{extension} ({len(file_list)} فایل):")
    for file in file_list:
        print(f"   • {file}")

# 4. آمار کلی
print("\n" + "="*50)
print("📊 آمار کلی:")
print("="*50)

total_files = len(files)
unique_extensions = len(files_by_extension)

print(f"تعداد کل فایل‌ها: {total_files}")
print(f"تعداد پسوندهای منحصر به فرد: {unique_extensions}")

# محاسبه تعداد فایل‌ها در هر گروه
print(f"\nتوزیع فایل‌ها بر اساس پسوند:")
for extension in sorted(files_by_extension.keys()):
    count = len(files_by_extension[extension])
    percentage = (count / total_files) * 100
    bar = "█" * int(percentage / 5)  # نمودار میله‌ای
    print(f"  .{extension:8}: {count:2} فایل ({percentage:5.1f}%) {bar}")