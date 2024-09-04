# Initial greeting.
print("Greetings!")

# Asking for and collecting the student's name.
name = input("Please enter the student's name.\n")

# Asking for and collecting the student's age.
age = input("Please enter the student's age.\n")
age = int(age)  # Convert the age to an integer

# Asking for and collecting the student's grade.
grade = input("Please enter the student's grade.\n")
grade = float(grade.replace(',', '.'))  # Convert the grade to a float and replace comma with dot if necessary

# Displaying the collected information, one per line
print(f"Student: {name}\nAge: {age}\nGrade: {grade}")
