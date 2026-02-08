"""
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
"""

score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:    print("F")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""
Create a dictionary where the keys are student names and the values are their grades. 
Allow the user to:
* Add a new student and grade.
* Update an existing students grade.
* Print all student grades.
"""
students = {}
while True:
    action = input("Choose an action: 1 = add, 2 = update, 3 = print, or 4 = quit: ")
    if action == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade (A-F): ")
        students[name] = grade
    elif action == "2":
        name = input("Enter student name: ")
        if name in students:
            grade = input("Enter new grade (A-F): ")
            students[name] = grade
        else:
            print("Student not found.")
    elif action == "3":
        for name, grade in students.items():
            print(f"{name}: {grade}")
    elif action == "4":
        break
    else:
        print("Invalid action. Please try again.")


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
Write to a File
Write a program to create a text file and write some content to it.
"""
filename = "example.txt"
content = "This is an example of writing to a file in Python."
with open(filename, "w") as file:
    file.write(content)
print(f"Content written to {filename}.")    


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""
Read from a File
"""
filename = "example.txt"
with open(filename, "r") as file:
    content = file.read()
print(f"Content read from {filename}:")
print(content)  

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
