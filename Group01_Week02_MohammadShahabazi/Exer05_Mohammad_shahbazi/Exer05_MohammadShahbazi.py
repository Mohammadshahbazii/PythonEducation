print("welcome to labratory ! ")

is_password_correct = False

while not is_password_correct :
    user_password = input("please enter your password : ")
    is_password_correct = (user_password == "1234")

print("Here you are !")