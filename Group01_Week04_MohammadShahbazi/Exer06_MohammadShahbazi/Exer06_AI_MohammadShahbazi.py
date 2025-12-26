# داده‌های ورودی
cities = {
    "Karaj": "Alborz",
    "Tehran": "Tehran", 
    "Fardis": "Alborz",
    "Damavand": "Tehran"
}

print("📌 دیکشنری اصلی (شهر → استان):")
print("="*50)
for city, province in cities.items():
    print(f"{city:20} → {province}")
print(f"\nتعداد شهرها: {len(cities)}")

print("\n" + "="*50 + "\n")

# 1. معکوس کردن دیکشنری (استان → لیست شهرها)
provinces_cities = {}

for city, province in cities.items():
    if province in provinces_cities:
        provinces_cities[province].append(city)
    else:
        provinces_cities[province] = [city]

# 2. نمایش نتایج
print("🗺️ دیکشنری معکوس (استان → شهرها):")
print("="*50)

for province in sorted(provinces_cities.keys()):
    city_list = provinces_cities[province]
    print(f"\n🏙️ {province} ({len(city_list)} شهر):")
    for city in sorted(city_list):
        print(f"   • {city}")

# 3. آمار کلی
print("\n" + "="*50)
print("📊 آمار:")
print("="*50)

print(f"تعداد استان‌ها: {len(provinces_cities)}")
print(f"تعداد شهرها: {len(cities)}")

# محاسبه میانگین شهرها در هر استان
avg_cities = len(cities) / len(provinces_cities)
print(f"میانگین شهر در هر استان: {avg_cities:.1f}")

# استان با بیشترین شهر
max_province = max(provinces_cities.items(), key=lambda x: len(x[1]))
min_province = min(provinces_cities.items(), key=lambda x: len(x[1]))

print(f"\n🏆 استان با بیشترین شهر: {max_province[0]} ({len(max_province[1])} شهر)")
print(f"📉 استان با کمترین شهر: {min_province[0]} ({len(min_province[1])} شهر)")

# نمایش لیست شهرها برای استان‌های با بیش از یک شهر
print(f"\n📈 استان‌های با بیش از یک شهر:")
for province, city_list in sorted(provinces_cities.items()):
    if len(city_list) > 1:
        print(f"  {province:25}: {', '.join(sorted(city_list))}")