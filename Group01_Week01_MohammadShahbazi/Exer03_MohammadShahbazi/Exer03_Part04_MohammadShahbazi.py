amount = int(input("مقدار پول را وارد کنید: "))

coin_10tomans = amount // 10
remaining = amount % 10

coin_5tomans = remaining // 5
remaining = remaining % 5

coin_1toman = remaining

print("برای خرد کردن", amount, "تومان:")
print(coin_10tomans, "سکه 10 تومانی")
print(coin_5tomans, "سکه 5 تومانی")
print(coin_1toman, "سکه 1 تومانی")
