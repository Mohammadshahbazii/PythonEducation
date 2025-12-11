print("Welcome to our program for analyzing your health based on age and body temperature !")
user_age = int(input("Please enter your age : "))
user_body_tempreture = int(input("Please enter your body tempreture : "))

if(user_body_tempreture > 37 and user_age > 40):
    print("There is a danger here please visit your doctor")
elif((user_body_tempreture > 37 and user_age <= 40) or (user_body_tempreture <=37 and user_age > 40)):
    print("You should take care")
else:
    print("Everything is alright")