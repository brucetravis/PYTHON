# An empty list of students
students = []


# Function to display_students
def display_students():
    # If the list is empty
    if not students:
        print("\nNo Students registered yet\n")
        return
    
    print(f"\nTotal number of students: {len(students)}")
    
    # Loop thorugh all the students in order to display them
    for student in students:
        print(f"Name: {student["name"]}\nMarks: {student["marks"]}\nGrade: {student["grade"]}\nStatus: {student["status"]}")    
    print()
    
# Function to determine the grades of a student
def student_grade(marks):
    # Conditions to deterrmine which grade the student gets
    if marks >= 95:
        return "A+"
    elif marks >= 90:
        return "A Plain"
    elif marks >= 85:
        return "B+"
    elif marks >= 80:
        return "B Plain"
    elif marks >= 75:
        return "C+"
    elif marks >= 70:
        return "C Plain"
    elif marks >= 65:
        return "D+"
    elif marks >= 60:
        return "D Plain"
    else:
        return "E"
    
# Function to determine a students status
def student_status(marks):
    # Conditions to determine the student status
    if marks >= 90:
        return "pass"
    elif marks >= 80:
        return "Potential"
    elif marks >= 70:
        return "Average"
    else:
        return "Fail"

# Function to add students to the list
def add_student():
    # Prompt the user to enter the students name
    name = input("Enter the students name: ").title()
    # Prompt the user to enter the students marks
    marks = int(input("Enter the students marks: "))
    
    
    # We can be more efficient and say
    if any(student["name"] == name for student in students):
        print("Student already exists!")
        return
    
    # Add the students name to list as a dictionary
    students.append({
        "name": name, 
        "marks": marks, 
        "grade": student_grade(marks), 
        "status": student_status(marks)
    })
    
    # Alert the user that the students jhave been added
    print(f"Student '{name}' added successfully! 'success'")
    
    # Display all the students
    display_students()
    

# Function to remove students
def remove_student():
    # Enter The name of teh student in order to remove by the name
    name = input("Enter a students name: ").title()
    
    # Loopt throught the list of dictionaries
    for student in students:
        # If the student name matches a name in the list, remove the student
        if student["name"] == name:
            students.remove(student)
            # Notify the user that the student has been removed
            print(f"{student["name"]} has been removed! success")
            # Display all the students remaining
            display_students()
            # Exit after removing to avoid unecessary Iterations
            return
    
    # If the student has not been found, notify the user
    print("Student not found!")
    

# Function to manage students
def manage_students():
    while True:
        # Options for the user
        print(f"""
            1. Add student
            2. Remove student
            3. Display students
            4. Exit the Management System
            """)
        
        try:
            # Prompt a user to choose
            user_choice = int(input("Choose an option: "))
        
            if user_choice == 1:
                add_student()
            elif user_choice == 2:
                remove_student()
                
            elif user_choice == 3:
                display_students()
            elif user_choice == 4:
                print("\nExiting the student management system.....\n")
                break
            else:
                print("\nInvalid choice! Please enter a valid choice\n")
        
        except Exception as e:
            print("Error: ", e)
        


# Run the program
manage_students()   
    
    