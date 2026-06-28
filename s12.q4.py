class Student:
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = [] #it is a list used to storing marks
    
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if 0 <= mark <= 80:
                self.marks_list.append(mark)
                print("Mark added successfully:", mark)
            else:
                print("Error: Mark should be between 0 and 80.")
        except ValueError:
            print("Error:Please enter a number only.")
    
    def get_average(self):
        if not self.marks_list:
            return 0 
        return sum(self.marks_list) / len(self.marks_list)
    
    def display_info(self):
        print("Name: ",self.name)
        print("Roll No: ",self.roll_no)
        print("Marks: ",self.marks_list)
        print("Average: {:2f}".format(self.get_average()))
        

student_name = input("Enter student name: ")
student_roll = input("Enter roll number: ")

# Creating object
stu= Student(student_name, student_roll)

num= 5
print("\nEnter marks for subjects:",num)
for i in range(num):
    var = input("Subject {}  marks: ".format(i+1))
    stu.add_mark(var)

stu.display_info()