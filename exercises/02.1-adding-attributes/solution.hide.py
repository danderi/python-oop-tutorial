class Student:
    school_name = "Python Academy"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def student_info(self):
        return f"{self.name} is {self.age} years old in {self.grade} grade at {self.school_name}"


student1 = Student("Alice", 15, "10th")
student2 = Student("Bob", 16, "11th")  
print(student1.student_info())
print(student2.student_info())
