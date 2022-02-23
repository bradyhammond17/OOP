import studentClass as s


def main():
    stuID = "1"
    name = "John"
    dob = input("Enter the year you were born: ")
    classification = "F"
    student = s.Student(stuID, name, dob, classification)
    print(student.get_class())


main()
