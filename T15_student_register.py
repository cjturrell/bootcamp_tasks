"""
A program that allows a user to register students for an exam venue
"""

print("-" *40)
print("Welcome to Exam Register set up")
print("-" *40)

# User input for exam title and number of students
exam_name = (input("Exam name or subject:\t")).title()
student_count = int(input("Number of students:\t"))
print("-" *40)

# Open and create new txt file
with open('reg_form.txt', 'w') as file:
    
    # Title register and show section for students to sign
    file.write(f"{exam_name} Exam Register\n")
    file.write("\nStudent ID \tSign Here \n")

    # Loop to input student ID numbers and write to txt file
    for i in range(student_count):
        student_id = input(f"Student ID {i+1}:\t")
        file.write(student_id + "\t\t" + "."*20 + "\n")
        # sep="\t\t"

print("-" *40)
print("Register exported as reg_form.txt")
print("-" *40)

# with open('reg_form.txt', 'x') as file:  # For creating a new file each time.  good for this use