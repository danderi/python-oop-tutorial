# ¡Hagamos que diferentes formas hagan matemáticas a su manera! 📐

Vamos a crear diferentes formas que puedan calcular sus áreas y perímetros de maneras únicas y especiales. 

En este ejercicio, las formas (círculo, rectángulo, triángulo) comparten métodos comunes (area, perimetro y describir), pero cada una implementa estas acciones de manera única según sus propiedades.

## 📝 Instrucciones

1. Crea la clase Base `Forma`. La clase **Forma** actuará como una plantilla para otras formas. Contendrá métodos que serán sobrescritos por las formas específicas.

2. Incluye los métodos.
    - **area:** Devuelve 0 por defecto.
    - **perimeter:** Devuelve 0 por defecto.
    - **describe:** Retorna un mensaje genérico como: `Generic shape`

3. Crea la clases derivada `Circle`. Esta clase necesita un atributo `radius`. 
4. Crea la clases derivada `Rectangle`. Esta clase necesita los atributos `width` y `height`. 
5. Crea la clases derivada `Triangle`. Esta clase necesita los atributos `side1`, `side2`, `side3`, `height`. 
6. **Métodos sobrescritos.** Sobrescribe los métodos de `area, perimeter y describe` e implementa las fórmulas específicas para calcular area y perimeter, y ajusta el metodo describe para cada forma.
7. Crea instancias de cada forma y verifica que los métodos funcionen correctamente. Por ejemplo:

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



