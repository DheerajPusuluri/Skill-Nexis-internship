import csv
import os
FILE_NAME = "students.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")

def search_student():
    roll = input("Enter roll number to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return
    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    students = []
    found = False
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student["Roll Number"] == roll:
                found = True
            else:
                students.append(student)
    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n--- Student Records ---")
        for student in reader:
            print(
                "Roll Number:", student["Roll Number"],
                "| Name:", student["Name"],
                "| Marks:", student["Marks"]
            )

create_file()
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")