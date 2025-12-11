citizens_count = 1000

illness_counter = 1
illness_range = 2

days_counter = 0

is_full = False

while not is_full:
    illness_counter += (illness_counter * illness_range)
    days_counter+=1
    print(f"sick people count is {illness_counter} in {days_counter} day")

    if(illness_counter > 500 and illness_range == 2):
        illness_range = 0.5
        print("quarantine performed")

    if(illness_counter >= citizens_count):
        is_full = True

print(f"All citizens are sick in {days_counter} days")
