import student as st
import teacher as th
import json

teacher_object = th.Teacher()
student_object = st.Student()

print("Select role:")
key = input("Enter 1 for teacher, 2 for student, 0 to exit: ")

def role_selector(role_key):
    while True:
        if role_key == '1':
            if teacher_object.is_file_empty():
                print("Enter data for the first teacher")
                teacher_object.add_new_teacher()

            return_key = '100'
            while return_key != '10':
                teacher_roles()
                teacher_key = input("Enter the operation number you want to perform: ")
                return_key = teacher_task(teacher_key)

            # Exit teacher role loop, return to main role selection
            role_key = input("Enter 1 for teacher, 2 for student, 0 to exit: ")

        elif role_key == '2':
            student_object.student_entry()
            return_key = '200'
            while return_key != '20':
                student_roles()
                student_key = input("Enter the operation number you want to perform: ")
                return_key = student_task(student_key)

            # Exit student role loop, return to main role selection
            role_key = input("Enter 1 for teacher, 2 for student, 0 to exit: ")

        elif role_key == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid number selected, please select again.")
            role_key = input("Enter 1 for teacher, 2 for student, 0 to exit: ")

def student_task(task_key):
    if task_key == '1':
        result = student_object.Pass_Fail_Determination()
        if result:
            print("Congratulations, you Passed!")
        else:
            print("Sorry, you have failed.")
        return '200'

    elif task_key == '2':
        student_object.Highest_and_Lowest_Scores()
        return '200'

    elif task_key == '3':
        student_object.Percentage()
        return '200'

    elif task_key == '0':
        return '210'

    else:
        print("Invalid number selected, please select again.")
        return '100'

def teacher_task(task_key):
    if task_key == '1':
        teacher_object.add_new_teacher()
        return '100'

    elif task_key == '2':
        teacher_object.new_student_entry()
        return '100'

    elif task_key == '3':
        teacher_object.display_std_record()
        return '100'

    elif task_key == '4':
        name_to_lookup = input("Enter the name of the student: ")
        teacher_object.display_detail_record(name_to_lookup)
        return '100'

    elif task_key == '5':
        name_to_delete = input("Enter the name of the student: ")
        teacher_object.delete_student_data(name_to_delete)
        return '100'

    elif task_key == '0':
        return '10'

    else:
        print("Invalid number selected, please select again.")
        return '100'

def teacher_roles():
    print("1. Add new teacher")
    print("2. Add new student")
    print("3. See student reports")
    print("4. See detailed student report")
    print("5. Delete student record")
    print("0. To exit")

def student_roles():
    print("1. Pass-Fail determination")
    print("2. Highest and Lowest Scores")
    print("3. Percentage")
    print("0. To exit")

if __name__ == "__main__":
    role_selector(key)
