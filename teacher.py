import json
import student
import sys


#initilizing the first teacher

# teacher_data = {
#     "name" : "Bijay" ,
#     "subject" : "DSA" ,
#     "ID" : int(1000),
#     "address" : "Dhapakhel" ,
#     "email" : 'bijay078@gmail.com',
#     "phone_number" : int(9865214755)

# }

# with open("data_files/teacher,json" , "w") as file1:
#     json.dump(teacher_data , file1)
#     file1.close()


def get_valid_phone_number():
    while True:
        try:
            phone_number = input("Enter your 10-digit phone number: ")
           
            phone_number = int(phone_number)      #converts input to integer
            if len(phone_number) == 10:           #checks for 10 digit
                return phone_number             # Return the valid phone number
            else:
                print("Please enter exactly 10 digits.")
        except ValueError:
            print("Please enter numeric digits only.")

class Teacher:

    def __init__(self):
        self.name = None
        self.id = None
        self.subject = None
        self.email = None
        self.phone_no = None

    def display_std_record(self):

        with open("data_files/student.json" , "r") as file1:
            try:
                student_data = json.load(file1)
            except json.decoder.JSONDecodeError:
                student_data = []

            for record in student_data:
                print(f"Name :{record['name']}")
                print(f"Email Address :{record['email']}")
                print(f"Phone Number :{record['phone_number']}\n")
            file1.close()

    def display_detail_record(self,specific_name):
         with open("data_files/student.json" , "r") as file2:
            student_data = json.load(file2)
            for record in student_data:
                if record['name'] == specific_name:
                    print(f"Name :{record['name']}")
                    print(f"Email Address :{record['email']}")
                    print(f"Phone Number :{record['phone_number']}")
                    print(f"Roll Number :{record['roll_number']}")
                    print(f"Marks :{record['marks']}")
                    print(f"Address :{record['address']}\n")
            file2.close()

    def new_student_entry(self):
        
        with open("data_files/student.json" , "r") as file3:
            try:
                content = json.load(file3)
            except json.decoder.JSONDecodeError:
                content = []
            file3.seek(0)                                           #points to the begining of the entity in the json file as "a+ mode defults to pointing at the end entity in json file which is empty and results an error"
            new_student_data = {}

            new_student_marks = {"D.S.A" : None , "T.O.C" : None , "Python" : None}
            
            new_student_data['name'] = input("Enter name of the Student :")
            new_student_data['email'] = input("Enter email of the student :")
            new_student_data['address'] = input("Enter address of the student :")
            new_number = input("Enter phone number of student :")
            new_student_data['phone_number'] = get_valid_phone_number()
            new_roll_number = input("Enter roll number of student :")
            new_student_data['roll_number']= int(new_roll_number)

            for i in new_student_marks.items():
                key , values = i
                print(f"Enter the marks obtained in {key}")
                mark = input(': ')
                new_student_marks[key] = int(mark)
                

            new_student_data["marks"] = new_student_marks 

            content.append(new_student_data)


        with open("data_files\student.json" , 'w') as file4:

            json.dump(content, file4 , indent=4)

    def delete_student_data(self,name_to_delete):
        with open("data_files/student.json" , "r") as file5:
            try:
                loaded_file = json.load(file5)
            except json.decoder.JSONDecodeError:
                loaded_file = []
            file5.seek(0)   
            for idx ,record in enumerate(loaded_file):
                if record['name'] == name_to_delete:
                    loaded_file.pop(idx)

        with open("data_files\student.json" , 'w') as file5:
            try:
                json.dump(loaded_file, file5 , indent=4)
            except SyntaxWarning:
                pass

    def teacher_verification(self):
         with open ('data_files/teacher.json' , 'r') as file:
            #file_content = json.load(file)
            try:
                file_content = json.load(file)
            except json.decoder.JSONDecodeError:
                file_content = []
                

            if file_content != []:
                teacher_name = input("Enter teacher name to validate:") 
                teacher_ID = input('Enter teacher ID to validate:')
                teacher_ID = int(teacher_ID)
                for file_data in file_content:
                    if file_data['name'] == teacher_name  and file_data['ID'] == teacher_ID:
                        print(file_data['name'])
                        print(file_data['ID'])
                        print('Log in passed')
                        return True
                print("Teacher not registered in database.")
                return False
            else:
                print("No teachers registered in database.")
                return False

    def add_new_teacher(self):


        new_teacher_data = {"name": None, "subject": None, "ID": int, "address": None, "email": None, "phone_number": int}
        for key in new_teacher_data:
            print(f"Enter teacher {key}")
            new_teacher_data[key] = input(": ")
        with open ('data_files/teacher.json' , 'r+') as file:

            try:
                file_content = json.load(file)
            except json.decoder.JSONDecodeError:
                file_content = []
            #file_content = json.load(file)
            if file_content == []:

                initial_entry = [new_teacher_data]
                json.dump(initial_entry , file)
                file.close()
                 
            
        with open("data_files/student.json" , "r") as file:
            try:
                file_content = json.load(file)
            except json.decoder.JSONDecodeError:
                file_content = []

            if self.teacher_verification():
                file_content.append(new_teacher_data)
                key = 1
            else:
                
                return("Teacher not registerd in database")
        if key == 1:    
            with open ('data_files/teacher.json' , 'w') as file:
                json.dump(file_content , file)
                return("Teacher added to the data base")
             
    def is_file_empty(self):
        with open ('data_files/teacher.json' , 'r') as file:

            try:
                record = json.load(file)
            except json.decoder.JSONDecodeError:
                return True










if __name__ == "__main__":
    
    teacher1 = Teacher()
    teacher1.display_std_record()
    
    #teacher1.display_detail_record('benit')

    #teacher1.delete_student_data('blade')
    print('\n')
    v = teacher1.teacher_verification()
    print(v)
    teacher1.add_new_teacher()
    #teacher1.display_std_record()
    print('\n')
    #teacher1.new_student_entry()