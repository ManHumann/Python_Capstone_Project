import json

class Student:
    def __init__(self):
        self.name = None
        self.roll = None
        self.marks = {}
        self.email = None
        self.phone_number = None
        self.address = None 
        self.idx = None

    def student_entry(self):
        """Function to check for student name in the database and assign the index."""
        self.name = input("Enter your name: ")
        while True:
            try:
                with open("data_files/student.json", "r") as file1:
                    student_data = json.load(file1)
                break
            except json.decoder.JSONDecodeError:
                print("teacher has not defined any student\n\n")
        
        for idx, record in enumerate(student_data):
            if record['name'] == self.name:
                self.idx = idx
                print(f"Welcome {record['name']}")
                break

    def Pass_Fail_Determination(self):
        """Checks each marks obtained by a single student and returns False if any of them is less than 32."""
        if self.idx is not None:
            with open("data_files/student.json", "r") as file1:
                student_data = json.load(file1)
                specific_student_list = student_data[self.idx]
                self.marks = specific_student_list.get('marks', {})

            for key, value in self.marks.items():
                if value < 32:
                    return False
            return True
        else:
            print("Student record not found")
            return False

    def Highest_and_Lowest_Scores(self):
        """Returns the highest and the lowest marks obtained."""
        if self.marks:
            highest_mark = max(self.marks.values())
            lowest_mark = min(self.marks.values())
            print(f"The highest score is {highest_mark}\nThe lowest score is {lowest_mark}")
        else:
            print("No marks found for this student.")

    def Percentage(self):
        """Calculates and prints the percentage of the student."""
        if self.idx is not None:
            with open("data_files/student.json", "r") as file1:
                student_data = json.load(file1)
                specific_student_list = student_data[self.idx]
                self.marks = specific_student_list.get('marks', {})

            total_marks = sum(self.marks.values())
            percentage = (total_marks / (len(self.marks) * 100)) * 100
            print(f"Your percentage is: {percentage:.2f}%")
        else:
            print("Student record not found")

    def rank(self):
        """Prints the rank of the student based on percentage."""
        score_card = []
        with open("data_files/student.json", "r") as file1:
            student_data = json.load(file1)

        for student in student_data:
            marks = student.get('marks', {})
            total_marks = sum(marks.values())
            percentage = (total_marks / (len(marks) * 100)) * 100
            score_card.append(percentage)

        score_card.sort(reverse=True)
        rank = score_card.index((total_marks / (len(marks) * 100)) * 100) + 1
        print(f"Your rank is: {rank}")


if __name__ == "__main__":
    student1 = Student()
    student1.student_entry()

    student1.Highest_and_Lowest_Scores()
    student1.Percentage()
    student1.rank()
