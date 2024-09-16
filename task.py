def task():

    # grade should be a tuple containing student name (str), subject (str) and score (int)
    name = input("Please enter the student name: ")
    subject = input("Please enter the student's subject: ")
    score = int(input("Please enter the student's score out of 100 (in integer form)): "))

    grade = (name, subject, score)
    return grade
