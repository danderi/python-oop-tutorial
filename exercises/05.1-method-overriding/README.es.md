# ¡Hagamos que diferentes formas hagan matemáticas a su manera! 📐

Vamos a crear diferentes formas que puedan calcular sus áreas y perímetros de maneras únicas y especiales. 

En este ejercicio, las formas (círculo, rectángulo, triángulo) comparten métodos comunes (area, perimetro y describir), pero cada una implementa estas acciones de manera única según sus propiedades.

## 📝 Instrucciones

1. Crea la clase Base `Shape`. Esta clase actuará como una molde para otras formas, no tiene detalles específicos solo métodos básicos que puedes usar o reemplazar más adelante.

2. Agrega estos métodos a `Shape`:
    - **area:** Este método devolverá siempre 0. Por ahora, no calcula nada.
    - **perimeter:** Igual que area, este método devolverá 0.
    - **describe:** Este método simplemente retornará el texto `Generic shape`

3. Crea la clase llamada `Circle`. Esta clase necesita un atributo `radius`, el cual será el tamaño del círculo. Ejemplo:

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
     def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def describe(self):
        return "Generic shape"
```

4. Tal y como hicimos en el paso anterior crea la clase `Rectangle`. Esta clase necesita los atributos `width` y `height`, estos serán las dimensiones del rectángulo. 

5. Crea la clase `Triangle`. Esta clase necesita los atributos `side1`, `side2`, `side3` (los tres lados del triángulo) y `height` (la altura para calcular el área). 

6. **Métodos sobrescritos.** Sobrescribe los métodos de `area, perimeter y describe` e implementa las fórmulas específicas para calcular area y perimeter, y ajusta el metodo describe para cada forma.

- `area`: Calcula el área según las fórmulas específicas de la forma (por ejemplo, para un círculo es π*r² que traducido a lenguaje de programación seria `pi * self.radius ** 2`).
- `perimeter`: Calcula el perímetro según la forma.
- `describe`: Devuelve una descripción personalizada para cada forma.

7. **Prueba tu codigo**. Crea un círculo, un rectángulo y un triángulo usando las clases que acabas de hacer.
Verifica que los métodos funcionen correctamente llamándolos. Por ejemplo:

```python
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 4)

print(circle.area())  # Approximately 78.54
print(rectangle.area())  # 24
print(triangle.area())  # 6

print(circle.describe())    # Shows "Circle with radius 5 - Area: 78.54, Perimeter: 31.42"
print(rectangle.describe()) # Shows "Rectangle 4x6 - Area: 24, Perimeter: 20"
print(triangle.describe())  # Shows "Triangle with sides 3,4,5 - Area: 6, Perimeter: 12"
```


## 💡 Pista

Aquí tienes las fórmulas que necesitarás:
- Área del círculo = πr² (π ≈ 3.14159)
- Perímetro del círculo = 2πr
- Área del rectángulo = ancho × alto
- Perímetro del rectángulo = 2(ancho + alto)
- Área del triángulo = ½ × base × altura
- Perímetro del triángulo = suma de los tres lados



