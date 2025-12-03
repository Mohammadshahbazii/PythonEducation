money_amount = int(input("Please enter the amount of money for calculating coins based on 1 toman , 5 toman and 10 toman : "))
coin_10 = money_amount // 10
remaining = money_amount % 10

coin_5 = remaining // 5
remaining = remaining % 5

coin_1 = remaining
print("For changing", money_amount, "toman you need :")
print(coin_10, "10 toman coin")
print(coin_5, "5 toman coin")
print(coin_1, "1 toman coin")