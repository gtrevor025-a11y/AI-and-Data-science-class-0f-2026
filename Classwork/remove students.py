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