from sql_connection import conn, cursor

while True:
    print("\n  Student result manager App.........")
    print("1 , for adding the student.")
    print("2 , for view the student. ")
    print("3 , for check the result. ")
    print("4 , for update the marks. ")
    print("5 , for deleting the student. ")
    print("6 , to exit.")

    choise = int(input("Enter your choise: "))
# add student 
    if choise == 1:
        name = input("Enter student name: ").lower()
        marks = int(input("Enter student marks: "))
        query = "INSERT INTO students(name, marks) VALUES(%s, %s)"

        cursor.execute(query, (name, marks))

        conn.commit()

        print(f"{name} student added successfully.")
        print("Student ID is:", cursor.lastrowid)

# # view student 
    elif choise == 2:
        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("There is no student found......")
        else:
            for student in students:
                print(student)

# # check result
    elif choise == 3:
        student_id = int(input("Enter student id: "))

        query = "SELECT marks FROM students WHERE id = %s"
        cursor.execute(query,(student_id,))

        result = cursor.fetchone()

        if result:
            marks = result[0]
            if marks >= 45:
                print("The Student is PASS")
            else:
                print("The Student is FAIL")    
        else:
            print("Student is not found..")


# # update marks
    elif choise == 4:

        student_id = int(input("Enter student id: "))

        newmarks = int(input("Enter new marks: "))

        query = "UPDATE students SET marks = %s WHERE id = %s"

        cursor.execute(query, (newmarks, student_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Marks updated successfully.")
        else:
            print("Student not found.")

# delete Student
    elif choise == 5:
        student_id = int(input("Enter student id: "))
        query = "DELETE  FROM students WHERE id = %s"
        cursor.execute(query,(student_id,))
        conn.commit()
        print(f"{student_id} is deleted from database.")


# to exitt
    elif choise == 6:
        break
    else:
        print("INVALID CHOISE OF THE OPTION ....")

            