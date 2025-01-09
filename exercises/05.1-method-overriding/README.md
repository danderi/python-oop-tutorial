# Let's Make Different Shapes Do Math Their Own Way! 📐

Hey! Remember how different animals make different sounds? Well, now we're going to create different shapes that can calculate their own areas and perimeters in their own special ways!

## Why Are We Making This? 🤔

Think about it:
- A circle needs π×r² for its area
- A rectangle just multiplies width × height
- A triangle uses a different formula entirely
- But they're all finding areas - just in their own way!

This is perfect for learning method overriding because:
- All shapes need to calculate area and perimeter
- Each shape has its own special way of doing it
- We can use the same commands for any shape!

## What We'll Build 🛠️

1. First, we'll make a basic `Shape` class that:
   - Has a simple way to get area (returns 0)
   - Has a simple way to get perimeter (returns 0)
   - Can describe itself

2. Then we'll create three special shapes:
   - `Circle` with a radius
   - `Rectangle` with width and height
   - `Triangle` with three sides and height

3. Each shape will:
   - Calculate its own area using its special formula
   - Figure out its own perimeter
   - Tell us about itself in a nice way

## 💡 Need Help?

Here are the formulas you'll need:
- Circle area = πr² (π is about 3.14159)
- Circle perimeter = 2πr
- Rectangle area = width × height
- Rectangle perimeter = 2(width + height)
- Triangle area = ½ × base × height
- Triangle perimeter = add up all three sides

## What Should Happen? 🎯

When you run your code:
```python
# Create some shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 4)  # sides: 3,4,5, height: 4

# Check their areas
print(circle.area())      # Should show about 78.54
print(rectangle.area())   # Should show 24
print(triangle.area())    # Should show 6

# Get their descriptions
print(circle.describe())    # Shows "Circle with radius 5 - Area: 78.54, Perimeter: 31.42"
print(rectangle.describe()) # Shows "Rectangle 4x6 - Area: 24, Perimeter: 20"
print(triangle.describe())  # Shows "Triangle with sides 3,4,5 - Area: 6, Perimeter: 12"
```

## Why Is This Cool? 🌟

This exercise shows you:
1. How different shapes can share common actions (finding area and perimeter)
2. How each shape can do these actions in its own way
3. How we can treat all shapes the same way, even though they're different
4. How this works just like in the real world - different shapes, same idea!

Remember: Just like how different remote control buttons work for different devices, the same command (`area()` or `perimeter()`) works for all shapes - they just do it their own way! 🎨