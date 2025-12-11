print("you can analyze your force value with this program 4 times (Your force shouble be bigger than 0)")

for item in range(1,5):
    force_value = float(input("please enter your force value in Newton : "))
    if force_value > 1000 :
        print("your force is high")
    elif 0 <= force_value < 1000 :
        print("your force is medium")
    else :
        print("your force is not bigger than 0")