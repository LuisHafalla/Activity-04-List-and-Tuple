import csv

filename = "students.csv"

def load_records():
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return [tuple(row) for row in reader]
    except FileNotFoundError:
        return []

def save_records(records):
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(records)
    print("Records saved successfully.")

def show_all(records):
    print("\nStudent Records:")
    for rec in records:
        print(rec)
    print()

def order_by_last_name(records):
    return sorted(records, key=lambda r: r[1].split()[1])  

def order_by_grade(records):
    return sorted(records, key=lambda r: 0.6 * float(r[2]) + 0.4 * float(r[3]), reverse=True)

def add_record(records):
    student_id = input("Enter 6-digit Student ID: ")
    fullname = input("Enter Full Name (First Last): ")
    class_standing = input("Enter Class Standing Grade: ")
    major_exam = input("Enter Major Exam Grade: ")
    
    new_record = (student_id, fullname, class_standing, major_exam)
    records.append(new_record)
    print("Record added successfully.\n")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, rec in enumerate(records):
        if rec[0] == student_id:
            print("Current Record:", rec)
            fullname = input("Enter New Full Name: ")
            class_standing = input("Enter New Class Standing Grade: ")
            major_exam = input("Enter New Major Exam Grade: ")
            records[i] = (student_id, fullname, class_standing, major_exam)
            print("Record updated successfully.\n")
            return
    print("Student ID not found.\n")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for rec in records:
        if rec[0] == student_id:
            records.remove(rec)
            print("Record deleted successfully.\n")
            return
    print("Student ID not found.\n")

def show_student(records):
    student_id = input("Enter Student ID to search: ")
    for rec in records:
        if rec[0] == student_id:
            print("Student Record:", rec, "\n")
            return
    print("Student ID not found.\n")

def main():
    records = load_records()
    
    while True:
        print("\nStudent Record Management")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Save File")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_all(records)
        elif choice == "2":
            records = order_by_last_name(records)
            print("Records sorted by last name.\n")
        elif choice == "3":
            records = order_by_grade(records)
            print("Records sorted by grade.\n")
        elif choice == "4":
            show_student(records)
        elif choice == "5":
            add_record(records)
        elif choice == "6":
            edit_record(records)
        elif choice == "7":
            delete_record(records)
        elif choice == "8":
            save_records(records)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
