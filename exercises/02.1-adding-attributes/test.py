import unittest
from app import Student

class TestStudent(unittest.TestCase):
    def test_student_info(self):
        estudiante1 = Student("Alice", 15, "10th")
        estudiante2 = Student("Bob", 16, "11th")
        
        self.assertEqual(estudiante1.student_info(), "Alice is 15 years old, in 10th grade, and studies at Python Academy.")
        self.assertEqual(estudiante2.student_info(), "Bob is 16 years old, in 11th grade, and studies at Python Academy.")

if __name__ == "__main__":
    unittest.main()