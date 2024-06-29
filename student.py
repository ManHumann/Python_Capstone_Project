import json
class Student:

    def __init__ (self):
        self.name = None
        self.roll = None
        self.marks = {}
        self.email = None
        self.phone_number = None
        self.address = None 
        self.index = None


    def student_entry(self):
        """Function check for student name in the database and assign the indx so ,respective information can be fetched
        """

        self.name = input("Enter your name :")
        while True:
                try:
                    with open("data_files/student.json" , "r") as file1:
                        student_data = json.load(file1)
                    break
                except json.decoder.JSONDecodeError:
                    print("Oops!  The teacher has not defined any student\n\n")

                for idx , record in enumerate(student_data):                    #checks the name in every element in the list until it has found the index with the name in it
                    if record['name'] == self.name:
                        self.idx = idx
                        break
                        
                print(f"Welcome {record['name']}")


    
    
    def Pass_Fail_Determination(self):
        """_checks each marks obtained by a single student and returns false if any of them is less than 32

        Returns:
            bool: false if any marks obtained < 32 or data not present 
        """
        if self.idx != None:
            with open("data_files/student.json" , "r") as file1:
                try:
                    with open("data_files/student.json" , "r") as file1:
                        student_data = json.load(file1)
                except json.decoder.JSONDecodeError:
                    print("Oops!  The teacher has not defined any student\n\n")
                specific_student_list = student_data[self.idx]
                self.marks = specific_student_list['marks']
            mark_list = (self.marks)

            for key , value in mark_list.items():
                if value < 32 :
                    return False
            return True
        else:
            print("Student record not found")
            return False
    
            
    def Highest_and_Lowest_Scores(self):
        """returns the highest and the lowest marks obtained 
        """
        mark_list = self.marks
        highest_mark = 0
        lowest_mark = 100
        for key , value in mark_list.items():
                highest_mark = max(highest_mark , value)
                lowest_mark = min(lowest_mark , value)
        print(f"The highest score is {max(self.marks)} : {highest_mark} \n Lowest score is {min(self.marks)} : {lowest_mark}")



    def Percentage(self):
            mark_list = self.marks
            total_mark = 0
            for key , value in mark_list.items():
                total_mark = total_mark + value

            print("Your percentage is :" , total_mark/len(self.marks))
        

        
        
if __name__ == "__main__":
    student1 = Student()
    student1.student_entry()
    student1.Pass_Fail_Determination()
    student1.Highest_and_Lowest_Scores()
    student1.Percentage()