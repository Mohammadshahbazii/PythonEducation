print("Welcome to our program for calculating maximum frequently G in your DNA input (Press 0 when your DNA is done)")

is_enough = False

g_counter = 0
maximum_g_count = 0

previous_sequence = ""

while not is_enough :
    user_answer = input("please enter your DNA sequence : ").strip().upper()
    if previous_sequence == "":
        previous_sequence = user_answer

    if user_answer == "0":
        is_enough = True
    else:
        if (user_answer != "A" and user_answer  != "T" and user_answer  != "C" and user_answer != "G"):
            print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, G.")
        else:
            if(user_answer == "G" and previous_sequence == "G"):
                g_counter += 1
            else:
                if(g_counter > maximum_g_count):
                    maximum_g_count = g_counter
            previous_sequence = user_answer

print("Maximum frequently G in your DNA input is : ", maximum_g_count - 1)  