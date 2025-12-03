n = int(input("لطفاً یک عدد مثبت وارد کنید: "))

power = 2 ** n

sum_of_digits = sum(int(digit) for digit in str(power))

print("2 به توان", n, "=", power)
print("مجموع ارقام:", sum_of_digits)
