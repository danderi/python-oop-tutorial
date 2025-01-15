# Let's Build a Student Class! 📚

Do you remember how we talked about classes having attributes (like characteristics)? Now we are going to create a `Student` class that shows how to use both class attributes (things all students share) and instance attributes (things unique to each student).

## 📝 Instructions

1. Define a class called `Student` in `app.py`

2. **Add a class attribute.** Declare a class attribute called `school_name` and set it to "Python Academy". Note: This attribute will be shared by all students.

3. **Define three attributes.** Inside the `__init__` method, set up the following attributes: name, age, grade

4. **Define a method called `student_info`.** This method should return a description that includes the student's name, age, grade, and the school name.
Example:

```python
"Alice is 15 years old, in 10th grade, and studies at Python Academy."
```

5. Instantiate the `Student` class with 2 new objects with the following values:

```python
student1 = Student("Alice", 15, "10th")
student2 = Student("Bob", 16, "11th")
```

6. Print the information of each student by calling the `student_info` method.


## 💡 Need Help?

- Class attributes go outside `__init__` (they're for everyone!)
- Personal details go inside `__init__` (they're just for that student)
- Use f-strings to make your `student_info` method print nicely
- Remember to use `self` when working with instance attributes




