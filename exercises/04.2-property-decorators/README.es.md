# ¡Creando un Convertidor de Temperatura Inteligente! 🌡️

Vamos a crear algo genial: un convertidor de temperatura lo suficientemente inteligente como para prevenir temperaturas imposibles. Usaremos algo llamado "propiedades" para que esto funcione sin problemas.

En la mayoría de los países usamos Celsius, pero a veces necesitamos Fahrenheit (como cuando leemos informes meteorológicos de Estados Unidos). No podemos tener temperaturas por debajo del cero absoluto (-273.15°C), por lo que queremos convertir entre ellas de manera fácil y segura.

Este ejercicio es perfecto para aprender sobre propiedades, ya que necesitamos verificar que las temperaturas sean posibles antes de usarlas. Queremos cambiar fácilmente entre Celsius y Fahrenheit, además de proteger nuestros datos de temperatura de errores.


## 📝 Instrucciones 

1. **Crea la clase `Temperature`**. La clase debe tener un atributo privado para almacenar la temperatura en grados Celsius.

2. **Uso de propiedades**. Crea la propiedad para Celsius dentro de la clase `Temperature` para poder leer y establecer la temperatura en Celsius de una manera segura. Para hacer esto, utilizamos el decorador **@property**. Esto convierte el método en un "getter", permitiendo que el valor se acceda como si fuera un atributo, sin necesidad de llamar al método directamente.

```python
    @property
    def celsius(self):
        return self.__celsius
```

3. **Crea el setter para Celsius.** Queremos asegurarnos de que el valor que establecemos para Celsius sea válido (mayor o igual a -273.15°C) para eso usaremos el decorador **@celsius.setter** para controlar cómo se establece el valor de Celsius.

```python
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Temperature too low. Cannot be set.")
```

4. **Crea la propiedad para Fahrenheit.** Para convertir entre Celsius y Fahrenheit, necesitamos una propiedad para Fahrenheit. Este es un **"getter"** que convierte la temperatura de Celsius a Fahrenheit.

```python
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
```

5. **Crea el setter para Fahrenheit.** También necesitamos un **"setter"** para Fahrenheit, para que podamos establecer la temperatura en grados Fahrenheit y luego convertirla automáticamente a grados Celsius. Recuerda que la fórmula para convertir de Fahrenheit a Celsius es: C = (F - 32) * 5/9.

6. **Prueba tu solución.** Crea una instancia de la clase `Temperature` llamada `temp` con:

```python
temp: 25
```
-

- Imprime la temperatura en celsius
- Imprime la temperatura en fahrenheit
- Usa el **setter fahrenheit** para cambiar la temperatura a 100°F. Luego, imprime la temperatura en Celsius para verificar que la conversión se realizó correctamente.

```python
temp.fahrenheit = 100
```
-

- Establece una temperatura imposible (por debajo del cero absoluto), por ejemplo, -300°C. Esto debería desencadenar un mensaje de error que indique que la temperatura no puede ser establecida.

Al seguir estos pasos, deberías ver algo similar a lo siguiente:

```python
25
77
37.77777777777778
Temperature too low. Cannot be set.
```


## ¿Por qué usar propiedades? 🎓

Las propiedades son muy útiles porque:
1. Verifican si los valores tienen sentido antes de usarlos
2. Calculan cosas automáticamente cuando es necesario
3. Facilitan cambiar cómo funcionan las cosas sin romper otro código
4. Mantienen nuestros datos seguros de accidentes

Piensa en las propiedades como tener un termostato inteligente: no te permitirá establecer temperaturas imposibles y puede mostrarte la temperatura en el formato que desees. 🌟