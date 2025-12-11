def sqrt_newton(n, precision=1e-10, max_iterations=1000):
    """
    محاسبه جذر با روش نیوتن-رافسون
    فرمول: x_{n+1} = 0.5 * (x_n + n / x_n)
    """
    if n < 0:
        raise ValueError("جذر اعداد منفی تعریف نشده است!")
    
    if n == 0:
        return 0
    
    # حدس اولیه (می‌توانیم از n/2 شروع کنیم)
    x = n / 2.0
    
    print(f"محاسبه √{n} با روش نیوتن-رافسون")
    print("=" * 60)
    print(f"حدس اولیه: {x}")
    
    for i in range(max_iterations):
        x_next = 0.5 * (x + n / x)
        
        # محاسبه خطا
        error = abs(x_next - x)
        
        print(f"تکرار {i+1:3d}: {x_next:.15f} | خطا: {error:.2e}")
        
        if error < precision:
            print(f"\n✅ همگرایی در تکرار {i+1}")
            break
        
        x = x_next
    
    return x

# تست تابع
number = float(input("عدد مورد نظر برای محاسبه جذر را وارد کنید: "))
result = sqrt_newton(number)
print(f"\n🎯 نتیجه نهایی: √{number} ≈ {result}")
print(f"بررسی: {result} × {result} = {result*result}")