
students=[]
def add_students():
    # Cleaning name: remove extra spaces between words and capitalize each word
    raw_name = input("What is the students name? ").strip()
    name = " ".join(raw_name.split()).title()

    age = input("How old is the student? ").strip()
    grade = input("What grade is the student in? ").strip()
    marks = input("What are the students marks? ").strip()
    student = {
        "name": name,
        "age": age,
        "grade": grade,
        "marks": marks
    }
    students.append(student)
    print(f"Student '{name}' added successfully!")
    return students

def view_students():
    if len(students) == 0:
        print("There are no students to view")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}")

def search_student():
    raw_name = input("What is the students name? ").strip()
    name = " ".join(raw_name.split()).title()
    for student in students:
        if student["name"] == name:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Marks: {student['marks']}")
            break
    else:
        print("Student not found")

def remove_student():
    raw_name = input("What is the students name to remove? ").strip()
    rem_student = " ".join(raw_name.split()).title()
    for student in students:
        if student["name"] == rem_student:
            students.remove(student)
            print("Student removed successfully!")
            break
    else:
        print("Student not found")

def count_students():
    print(f"There are {len(students)} students in this class")

def edit_student():
    raw_name = input("Enter the name of the student you want to edit: ").strip()
    name = " ".join(raw_name.split()).title()
    for student in students:
        if student["name"] == name:
            print(f"Editing details for {name}. (Leave blank to keep current value)")
            new_age = input(f"Current Age ({student['age']}): ").strip()
            if new_age: student['age'] = new_age
            new_grade = input(f"Current Grade ({student['grade']}): ").strip()
            if new_grade: student['grade'] = new_grade
            new_marks = input(f"Current Marks ({student['marks']}): ").strip()
            if new_marks: student['marks'] = new_marks
            print("Student details updated successfully!")
            return
    print("Student not found.")

def top_student():
    if not students:
        print("No students available.")
        return
    top = max(students, key=lambda s: float(s['marks']) if s['marks'].replace('.','',1).isdigit() else 0)
    print(f"Top Student: {top['name']} with {top['marks']} marks.")

# ===== MAIN PROGRAM =====
def main():
    while True:
        print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Count Students")
        print("6. Edit Student")
        print("7. Top Student")
        print("8. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            count_students()
        elif choice == "6":
            edit_student()
        elif choice == "7":
            top_student()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()