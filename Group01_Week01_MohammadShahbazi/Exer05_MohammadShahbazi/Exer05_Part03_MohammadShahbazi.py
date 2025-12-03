number = abs(int(input("Please enter your number for calculating digits of the 2^n and 2^n it self :")))
power = 2 ** number
sum_of_digits = sum(int(digit) for digit in str(power))
print("2 to the power of", number, "=", power)
print("Sum of digits:", sum_of_digits)