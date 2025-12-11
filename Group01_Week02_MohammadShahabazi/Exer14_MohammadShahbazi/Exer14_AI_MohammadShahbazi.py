# شبیه‌سازی دقیق‌تر
total_population = 1000
infected = 1.0  # استفاده از float برای دقت بیشتر
day = 0
quarantine_threshold = 500
quarantine_active = False
daily_log = []

print("شبیه‌سازی پیشرفت بیماری")
print("=" * 50)

while infected < total_population:
    day += 1
    
    # بررسی是否需要 شروع قرنطینه
    if infected > quarantine_threshold and not quarantine_active:
        quarantine_active = True
        print(f"\n🔴 روز {day}: قرنطینه اجباری اجرا شد!")
        print(f"   (تعداد بیماران: {infected:.0f} نفر)")
    
    # تعیین نرخ انتقال
    if quarantine_active:
        transmission_rate = 0.5
    else:
        transmission_rate = 2.0
    
    # محاسبه بیماران جدید
    healthy_people = total_population - infected
    potential_new_cases = infected * transmission_rate
    
    # بیماران جدید نمی‌توانند بیشتر از افراد سالم باشند
    new_cases = min(potential_new_cases, healthy_people)
    
    # به‌روزرسانی تعداد بیماران
    infected += new_cases
    
    # ذخیره‌سازی اطلاعات روز
    daily_log.append({
        'day': day,
        'new_cases': new_cases,
        'total_infected': infected,
        'transmission_rate': transmission_rate,
        'quarantine': quarantine_active
    })
    
    # نمایش وضعیت
    status = "قرنطینه فعال" if quarantine_active else "وضعیت عادی"
    print(f"روز {day:3d}: +{new_cases:6.1f} بیمار جدید | کل: {infected:6.1f} بیمار | وضعیت: {status}")

print("=" * 50)
print("\n📊 خلاصه نتایج:")
print(f"کل روزهای مورد نیاز: {day} روز")
print(f"تعداد روزهای قبل از قرنطینه: {len([d for d in daily_log if not d['quarantine']])} روز")
print(f"تعداد روزهای در قرنطینه: {len([d for d in daily_log if d['quarantine']])} روز")

# پیدا کردن دقیق روز شروع قرنطینه
quarantine_day = None
for log in daily_log:
    if log['quarantine']:
        quarantine_day = log['day']
        break

if quarantine_day:
    print(f"قرنطینه در روز {quarantine_day} شروع شد")
    infected_before_quarantine = daily_log[quarantine_day-2]['total_infected'] if quarantine_day > 1 else 1
    print(f"تعداد بیماران در شروع قرنطینه: {infected_before_quarantine:.0f} نفر")

print(f"\n✅ همه {total_population} نفر پس از {day} روز بیمار شدند.")