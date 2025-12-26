students_grades = {
    "Ali": [18, 19, 17, 18],
    "Sara": [20, 15, 12, 14],
    "Reza": [10, 9, 11, 12],
    "Mina": [18, 19, 20, 19]
}

grades_based_on_each_student = {}

for i in students_grades :
    avg = sum(students_grades[i]) / len(students_grades[i])
    if avg >= 17 :
            status = "Excellent"
    elif 12 <= avg < 17 :
            status = "Normal"
    else :
            status = "Conditional"
    print(f"{i} : {avg} that is {status}")

    grades_based_on_each_student[i] = {"average" : avg , "status" : status}

print("Final Result : " , grades_based_on_each_student)