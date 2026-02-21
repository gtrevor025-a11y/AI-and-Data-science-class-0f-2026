# ===== IMPORT STUDENT FUNCTIONS =====
from add_student import add_student
from view_students import view_students
from search_student import search_student
from remove_student import remove_student
from count_students import count_students
from edit_student import edit_student
from top_student import top_student

# ===== SHARED DATA =====
students = []

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
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            remove_student(students)
        elif choice == "5":
            count_students(students)
        elif choice == "6":
            edit_student(students)
        elif choice == "7":
            top_student(students)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()