# ماتریس ورودی
matrix = [
    [0, 0, 5],
    [0, 2, 0],
    [4, 0, 0]
]

print("📊 ماتریس اصلی:")
print("=" * 30)
for row in matrix:
    print(row)
print()

# 1. تبدیل ماتریس به دیکشنری
sparse_dict = {}

for i in range(len(matrix)):  # شمارش سطرها
    for j in range(len(matrix[i])):  # شمارش ستون‌ها
        value = matrix[i][j]
        if value != 0:  # فقط مقادیر غیرصفر ذخیره می‌شوند
            sparse_dict[(i, j)] = value

print("🗂️ دیکشنری ماتریس پراکنده:")
print("=" * 30)

# نمایش دیکشنری به صورت مرتب
for (row, col), value in sorted(sparse_dict.items()):
    print(f"مکان ({row}, {col}): {value}")

# 2. محاسبه آمار
print("\n📈 آمار:")
print("=" * 30)

total_elements = len(matrix) * len(matrix[0])
non_zero_elements = len(sparse_dict)
zero_elements = total_elements - non_zero_elements
sparsity = (zero_elements / total_elements) * 100

print(f"ابعاد ماتریس: {len(matrix)} × {len(matrix[0])}")
print(f"تعداد کل عناصر: {total_elements}")
print(f"تعداد عناصر غیرصفر: {non_zero_elements}")
print(f"تعداد عناصر صفر: {zero_elements}")
print(f"درجه پراکندگی: {sparsity:.1f}%")

print(f"\n💾 صرفه‌جویی در حافظه:")
original_memory = total_elements * 4  # فرض: هر عدد 4 بایت
sparse_memory = non_zero_elements * 12  # فرض: هر ورودی دیکشنری 12 بایت (8 برای تاپل + 4 برای مقدار)
saving = ((original_memory - sparse_memory) / original_memory) * 100

print(f"حافظه مورد نیاز ماتریس کامل: {original_memory} بایت")
print(f"حافظه مورد نیاز ماتریس پراکنده: {sparse_memory} بایت")
print(f"صرفه‌جویی: {saving:.1f}%" if saving > 0 else f"افزایش مصرف: {-saving:.1f}%")

# 3. نمایش ماتریس به صورت گرافیکی
print("\n🎯 نمایش ماتریس:")
print("=" * 30)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        value = matrix[i][j]
        if value == 0:
            print(" . ", end="")
        else:
            print(f"{value:2d} ", end="")
    print()