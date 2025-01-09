# Let's Build a Student Class! 📚

Hey! Remember how we talked about classes having attributes (like features or characteristics)? Now we're going to create a `Student` class that shows how to use both class attributes (things all students share) and instance attributes (things unique to each student).

## Why Are We Making This? 🤔

Think about your school - every student:
- Goes to the same school (that's a class attribute - everyone shares it!)
- Has their own name, age, and grade (these are instance attributes - they're different for each student!)

This exercise will help you understand how to:
- Create attributes that all instances share (like your school's name)
- Give each instance its own unique information (like each student's name)
- Make your class do useful things with this information

## 📝 Your Task

1. Create a class called `Student` in `app.py`
2. Add a class attribute `school_name` and set it to "Python Academy"
3. Add these personal details for each student:
   - name (like "Alice" or "Bob")
   - age (like 15)
   - grade (like "10th")
4. Create a method called `student_info` that tells us all about the student

## 💡 Need Help?

- Class attributes go outside `__init__` (they're for everyone!)
- Personal details go inside `__init__` (they're just for that student)
- Use f-strings to make your `student_info` method print nicely
- Remember to use `self` when working with instance attributes

## What Should Happen? 🎯

When someone uses your class like this:
```python
student = Student("Alice", 15, "10th")
print(Student.school_name)
print(student.student_info())
```

They should see:
```
Python Academy
Alice is 15 years old in 10th grade at Python Academy
```

Remember: This is just like filling out a form for each new student - the school name stays the same, but each student's information is different! 🌟