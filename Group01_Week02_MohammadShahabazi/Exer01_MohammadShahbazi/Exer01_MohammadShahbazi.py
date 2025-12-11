user_input_number = int(input("Enter a number: "))

# Calculate remain to 6
remain_value_to_six = user_input_number % 6
print("Remain to 6: ", remain_value_to_six)

#calculate how many * should we print
if(remain_value_to_six > 0):
    stars_to_print = ""
    for i in range(remain_value_to_six):
        stars_to_print += "*"
    print("stars should be like this : " , stars_to_print)
else:
    print("THERE IS NOT ANY STAR HERE BECAUSE REMAIN VALUE IS 0")
