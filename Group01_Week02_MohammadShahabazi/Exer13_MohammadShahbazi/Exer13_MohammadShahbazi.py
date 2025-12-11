print("Welcome to our program that if you relase the ball from each height you want how many times ball hit the ground until the height of ball is less than 0.1 meter when in each time the height will lose 20% of it !")

user_height = int(input("please enter your height : "))
hitting_counter = 0
while user_height >= 0.1 :
    hitting_counter += 1
    user_height = user_height * 0.8
print("the ball hit the ground ", hitting_counter, " times until the height is less than 0.1 meter")