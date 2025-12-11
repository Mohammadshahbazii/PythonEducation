print("welcome to our program for analyzing for your product package (9 product for each) quality ")

is_enough = False

sum_of_good = 0
sum_of_damaged = 0

while not is_enough:
    for item in range(9):
        product_quality = input("please enter your product quality (good/damaged) : ").strip().lower()
        if product_quality == "good":
            sum_of_good += 1
        elif product_quality == "damaged":
            sum_of_damaged += 1
        else:
            print("Invalid input, please enter 'good' or 'damaged'.")
    print("you have entered ", sum_of_good, " good product and ", sum_of_damaged, " damaged product")
    continiue_input = input("do you want to continue ? (yes/no) : ").strip().lower()
    if continiue_input == "no":
        is_enough = True
    else:
        sum_of_good = 0
        sum_of_damaged = 0