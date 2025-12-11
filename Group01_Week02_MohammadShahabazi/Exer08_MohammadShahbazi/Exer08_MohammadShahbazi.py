import random

print("Welcome to our game ! Guess the correct number between 1 and 100 ")

random_number = random.randint(1,100)
is_answer_true = False

while not is_answer_true:
    user_guess = int(input("enter your number : "))
    if(user_guess > random_number):
        print("your guess is too high ! try again ")
    elif(user_guess < random_number):
        print("your guess is too low ! try again ")
    else:
        is_answer_true = True
        print("congratulations ! you have guessed the correct number :", random_number)