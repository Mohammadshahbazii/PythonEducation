# راه حل با حلقه while
height = 1000  # سانتیمتر
bounces = 0

print("شبیه‌سازی نوسان توپ")
print("=" * 50)
print(f"ارتفاع اولیه: {height} سانتیمتر ({height/100:.1f} متر)")

while height >= 10:
    bounces += 1
    height = height * 0.8  # کاهش 20٪
    
    print(f"برخورد {bounces:2d}: ارتفاع جدید = {height:7.1f} سانتیمتر ({height/100:.2f} متر)")

print("=" * 50)
print(f"\nنتیجه: توپ {bounces} بار نوسان کرد")
print(f"ارتفاع نهایی: {height:.1f} سانتیمتر که کمتر از 10 سانتیمتر است")

# محاسبه ارتفاع پس از هر برخورد به صورت تحلیلی
print("\n📊 ارتفاع پس از هر برخورد:")
height = 1000
for i in range(bounces + 1):
    if i == 0:
        print(f"قبل از برخورد: {height:7.1f} سانتیمتر")
    else:
        height = height * 0.8
        status = "(آخرین)" if i == bounces else ""
        print(f"پس از برخورد {i}: {height:7.1f} سانتیمتر {status}")