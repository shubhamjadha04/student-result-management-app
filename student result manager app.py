Student = { }

while True:
    print("\n  Student result manager App.........")
    print("1 , for adding the student.")
    print("2 , for view the student. ")
    print("3 , for check the result. ")
    print("4 , for update the marks. ")
    print("5 , to exit.")

    choise = int(input("Enter your choise: "))
# add student 
    if choise == 1:
        name = input("Enter student name: ").lower()
        marks = int(input("Enter student marks: "))
        Student[name] = marks
        print(f"{name} student is added successfully.. ")

# view student 
    elif choise == 2:
        if not Student:
            print("There is no student found......")
        else:
            print(Student)

# check result
    elif choise == 3:
        stu = input("Enter student name: ")
        if stu in Student:

            if Student[stu] > 45:
                print("PASS...")
            else:
                print("FAIL...")
        else:
            print("Student not found....")

# update marks
    elif choise == 4:
      stu = input("Enter student name: ").lower()
      newmarks = int(input("Enter new marks: "))

      if stu in Student:
        Student[stu] = newmarks
        print(f"{stu} new marks are {newmarks}.")
        print("updated successfully..")
      else:
          print("student not found ....")

# to exitt
    elif choise == 5:
        break
    else:
        print("INVALID CHOISE OF THE OPTION ....")

            