class Student:
    school_name = "Python Academy"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def student_info(self):
        return f"{self.name} is {self.age} years old in {self.grade} grade at {self.school_name}"

# Test code
if __name__ == "__main__":
    student = Student("Alice", 15, "10th")
    print(Student.school_name)
    print(student.student_info())
