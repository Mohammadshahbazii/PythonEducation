print("welcome to our program for find the hottest and coolest day between 10 days based on tempretures !")

maximum_tempreture = 0
minimum_tempreture = 0

for item in range(10):
    day_tempreture = int(input(f"Please enter the day {item+1} tempreture : "))
    if(item == 0):
        maximum_tempreture = day_tempreture
        minimum_tempreture = day_tempreture
    else:
        if(maximum_tempreture >= day_tempreture):
           maximum_tempreture = day_tempreture

        if(minimum_tempreture <= day_tempreture):
           minimum_tempreture = day_tempreture
    
print("The hottest day tempreture is: ", maximum_tempreture)
print("The coolest day tempreture is: ", minimum_tempreture)
