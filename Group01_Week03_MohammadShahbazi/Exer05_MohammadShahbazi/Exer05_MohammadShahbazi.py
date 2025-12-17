budget = 122

hardwares = [
    ["MotherBoard", 1,25],
    ["CPU", 1, 35],
    ["RAM", 4, 10],
    ["Hard", 2, 12],
    ["Case", 1, 8],
    ["Fan", 1, 18]
]

minimum_price = 0

for item in hardwares:
    if(item == hardwares[0]):
        minimum_price = item[2]
    elif(item[2] < minimum_price):
        minimum_price = item[2]

spent_money = 0
extra_needed_money = 0
bought_items = []
remaining_budget = budget
bought_count_each_item = 0
bought_count_sum = 0

while remaining_budget > minimum_price :
    for item_name , item_count , item_price in hardwares :
        while (item_count > 0 and remaining_budget > item_price):
            spent_money += item_price
            bought_count_each_item +=1
            item_count -=1
            remaining_budget -= item_price

        if(bought_count_each_item > 0):
            bought_items.append(f"{item_name} : {bought_count_each_item}")
            bought_count_sum += bought_count_each_item
            bought_count_each_item = 0

        if(item_count > 0):
             extra_needed_money += item_price



print("Bought List : ",bought_items)
print("Total Counts : ",bought_count_sum)
print(f"Spent Money : {spent_money}")
print(f"Extra Money : {extra_needed_money - remaining_budget}")
print(f"Remain Budget : {remaining_budget}")
