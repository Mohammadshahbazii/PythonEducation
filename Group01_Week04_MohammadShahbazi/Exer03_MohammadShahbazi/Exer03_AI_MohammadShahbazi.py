# داده‌های اولیه
inventory = {
    "CPU": {"price": 35, "stock": 5},
    "Ram": {"price": 10, "stock": 2},
    "Mouse": {"price": 5, "stock": 10},
    "Hard": {"price": 12, "stock": 0}
}

orders = ["CPU", "Ram", "Ram", "Ram", "Hard", "Mouse", "Mouse"]

# متغیرهای اولیه
customer_budget = 100  # بودجه اولیه مشتری
items_purchased = []   # لیست کالاهای خریداری شده
items_failed = []      # لیست کالاهای ناموفق
remaining_budget = customer_budget  # بودجه باقیمانده

# پردازش سفارشات
print("پردازش سفارشات:")
print("=" * 50)

for item in orders:
    print(f"\nسفارش: {item}")
    print(f"موجودی کالا: {inventory[item]['stock']} - قیمت: {inventory[item]['price']}")
    print(f"بودجه فعلی: {remaining_budget}")
    
    # بررسی موجودی و بودجه
    if inventory[item]["stock"] > 0 and inventory[item]["price"] <= remaining_budget:
        # پردازش خرید موفق
        inventory[item]["stock"] -= 1  # کاهش موجودی
        remaining_budget -= inventory[item]["price"]  # کسر از بودجه
        items_purchased.append(item)  # اضافه به لیست خریداری‌شده
        
        print(f"✅ خرید موفق: {item}")
        print(f"   موجودی جدید {item}: {inventory[item]['stock']}")
        print(f"   بودجه جدید: {remaining_budget}")
    else:
        # خرید ناموفق
        items_failed.append(item)  # اضافه به لیست ناموفق
        
        if inventory[item]["stock"] <= 0:
            print(f"❌ خرید ناموفق: {item} - عدم موجودی")
        else:
            print(f"❌ خرید ناموفق: {item} - بودجه ناکافی")
            print(f"   قیمت: {inventory[item]['price']} > بودجه: {remaining_budget}")

print("\n" + "=" * 50)
print("\nنتایج نهایی:")
print("=" * 50)

# نمایش نتایج
print(f"\nبودجه اولیه: {customer_budget}")
print(f"بودجه باقیمانده: {remaining_budget}")
print(f"مبلغ کل هزینه شده: {customer_budget - remaining_budget}")

print(f"\nکالاهای خریداری شده ({len(items_purchased)}):")
if items_purchased:
    # شمارش تعداد هر کالا
    from collections import Counter
    purchased_counts = Counter(items_purchased)
    for item, count in purchased_counts.items():
        print(f"  - {item}: {count} عدد (قیمت واحد: {inventory[item]['price']})")
else:
    print("  هیچ کالایی خریداری نشد")

print(f"\nکالاهای خریداری نشده ({len(items_failed)}):")
if items_failed:
    failed_counts = Counter(items_failed)
    for item, count in failed_counts.items():
        reason = "عدم موجودی" if inventory[item]["stock"] <= 0 else "بودجه ناکافی"
        print(f"  - {item}: {count} عدد ({reason})")
else:
    print("  تمام سفارشات با موفقیت پردازش شدند")

print(f"\nوضعیت نهایی موجودی انبار:")
print("-" * 30)
for item, details in inventory.items():
    print(f"{item}: {details['stock']} عدد - قیمت: {details['price']}")