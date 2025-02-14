from classes.school import School
from classes.student import Student
import random
import os

clear = lambda: os.system('clear')

school = School('Ridgemont High')


running = True


while running:
  try:
    (print("\nWhat would you like to do? Please input an int between 1-5\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")) 
    user_input = int(input("Input: "))

    match user_input:
      case 1:
        # clear()
        for student in school.students:
          print(student)
      case 2:
        # clear()
        print(f"What student would you like to print out?")
        choice = int(input("Input student ID: "))
        found = []
        for student in school.students:
          if int(student.school_id) == choice:
            found.append(student)
        if found:
          print(found)
        else:
          print(f"Student with ID: {choice} does not exist")
      case 3:

        student_name = input("Student Name: ")
        student_age = input("Student Age: ")
        student_password = input("Student Password: ")
        student_role = 'Student'
        student_school_id = random.randint(1, 10000)
        school.students.append(Student(student_name, student_age, student_password, student_role, student_school_id))
      case 4:
        print(f"What student would you like to REMOVE?")
        choice = int(input("Input student ID: "))
        for student in school.students:
          if int(student.school_id) == choice:
            print('CHOICE')
            print(f"Student: {student} succesfully removed!")
            school.students.remove(student)
        else:
          print(f"No student of ID: {choice} found")
      case 5:
        running = False
      case _:
        print("value not accepted, please try again")
  except:
    print('Terminal input error. Exiting...')
    running = False
