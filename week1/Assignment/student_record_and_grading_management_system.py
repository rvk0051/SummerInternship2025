'''

Student Record and Grading Management System

This system manages student records including their marks, calculates grades,
and provides functionality to store and retrieve data from files.

'''


def add_record(student_records):
    """
    Add a new student record to the system.
        
    The function:
    - Checks for duplicate roll numbers in existing records
    - Collects student name and marks for 3 subjects
    - Validates marks to be between 0-100
    - Stores the record in the student_records list

    """
    roll_no = int(input("Enter roll number: "))
    # Check if roll number already exists in file
    with open("student_records.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data and int(data[0]) == roll_no:
                print("Record already exists in file.")
                return

    name = input("Enter name: ")
    marks = []
    subject_no = 1

    # Collect marks for 3 subjects
    while subject_no <= 3:
        subject_marks = float(input(f"Enter marks of subject {subject_no}: "))

        if 100 < subject_marks < 0:  # Validate marks range
            print("Marks should be 0-100")
        else:
            marks.append(subject_marks)
            subject_no += 1

    # Storing a record in dictionary, as it's mutable.
    record = {"name": name, "roll_no": roll_no, "marks": marks}
    # and then storing each dictionary (each record) in the list 'student_records'
    student_records.append(record)


def display_records(student_records):
    """
    Display all student records in a formatted table.
    """
    # Print table header
    print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".
          format("Name", "Roll No.", "Subject1 Marks", "Subject2 Marks", "Subject3 Marks", "Average Marks", "Grade"))
    print("-" * 150)

    # Print each student's record
    for record in student_records:
        avg_marks, grade = calculate_avg_marks_and_grade(record)
        print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".
              format(record["name"], record["roll_no"], record["marks"][0], record["marks"][1], record["marks"][2],
                     avg_marks, grade))


def calculate_avg_marks_and_grade(record):
    """
    Calculate average marks and determine grade for a student.

    Returns:
        tuple: (average_marks, grade)
        
    Grade scale:
        A: >= 90
        B: >= 80
        C: >= 70
        D: >= 60
        E: < 60
    """
    marks = record["marks"]

    # calculating average marks of the student
    avg_marks = sum(marks) / len(marks)

    # rounding-off the avg_marks to 2 decimal points
    avg_marks = round(avg_marks, 2)
    # Determine grade based on average marks
    if avg_marks >= 90:
        grade = 'A'
    elif avg_marks >= 80:
        grade = 'B'
    elif avg_marks >= 70:
        grade = 'C'
    elif avg_marks >= 60:
        grade = 'D'
    else:
        grade = 'E'
    return avg_marks, grade


def display_avg_marks_and_grades(student_records):
    """
    Display average marks and grades for all students.
    """
    print("{:<21} {:<9}".format("Avg Marks", "Grade"))
    print("-" * 30)

    for record in student_records:
        avg_marks, grade = calculate_avg_marks_and_grade(record)
        print("{:<21} {:<9}".format(avg_marks, grade))


def search_by_roll_no(student_records, roll_no):
    """
    Search for a student record by roll number in the file.
    Displays the complete record of the matching student if found.
    """
    # Check if roll number already exists in file
    with open("student_records.txt", "r") as file:
        flag = 0
        for line in file:
            data = line.strip().split(",")
            if data and int(data[0]) == roll_no:
                flag = 1
                # Display table header
                print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".
                      format("Name", "Roll No.", "Subject1 Marks", "Subject2 Marks", "Subject3 Marks",
                             "Average Marks", "Grade"))
                print("-" * 150)

                # Display details of the searched student
                print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".format(
                    data[1].strip(),  # name
                    data[0].strip(),  # roll_no
                    data[2].strip(),  # subject1
                    data[3].strip(),  # subject2
                    data[4].strip(),  # subject3
                    data[5].strip(),  # average
                    data[6].strip()  # grade
                ))
                break
        if flag == 0:
                print("Record not found.")

def save_and_read_records_to_file(student_records):
    """
    Saves records to 'student_records.txt'
    Displays all records from the file after saving
    """
    with open("student_records.txt", "a+") as file:

        # Save records in our list 'student_records' to file
        for record in student_records:
            avg, grade = calculate_avg_marks_and_grade(record)
            line = f"{record['roll_no']}, {record['name']}, {', '.join(map(str, record['marks']))}, {avg}, {grade}\n"
            file.write(line)
        print("Records saved successfully.\n")

        # Display table header
        print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".
              format("Name", "Roll No.", "Subject1 Marks", "Subject2 Marks", "Subject3 Marks", "Average Marks", "Grade"))
        print("-" * 150)

        # Moving the file pointer to the beginning of the file before reading
        file.seek(0)

        # Read and display records from file
        for line in file:
            data = line.strip().split(",")
            print("{:<30} {:<10} {:<18} {:<18} {:<18} {:<21} {:<9}".format(
                data[1].strip(),  # name
                data[0].strip(),  # roll_no
                data[2].strip(),  # subject1
                data[3].strip(),  # subject2
                data[4].strip(),  # subject3
                data[5].strip(),  # average
                data[6].strip()  # grade
            ))


def main():
    """
    Main function to run the Student Record and Grading Management System.
    
    Provides a menu-driven interface with options to:
    1. Add student records
    2. Display all records
    3. Show average marks and grades
    4. Search for a student
    5. Save/read records to/from file
    6. Exit the program
    """
    print("--- Student Record and Grading Management System ---")

    # declaring list for storing records of multiple students in an ordered manner
    student_records = []

    while True:
        print("\n")
        print(" 1. Add student's record")
        print(" 2. Display all records")
        print(" 3. Calculate and display each student's average marks and grade")
        print(" 4. Search for a student")
        print(" 5. Save all records to a file and read from it")
        print(" 6. Exit")
        choice = int(input("Enter your choice: "))
        print("\n")
        # Handle user choice using match-case statement
        match choice:
            case 1:
                add_record(student_records)
            case 2:
                display_records(student_records)
            case 3:
                display_avg_marks_and_grades(student_records)
            case 4:
                roll_no = int(input("Enter roll number of the student: "))
                search_by_roll_no(student_records, roll_no)
            case 5:
                save_and_read_records_to_file(student_records)
            case 6:
                print("Thank you")
                break
            case _:
                print("Incorrect choice entered.")


if __name__ == "__main__":
    main()