# ¡Construyamos una Cuenta Bancaria Segura! 🏦

Vamos a crear una clase `BankAccount` que mantenga tu dinero seguro, ¡como un banco real!

Este ejercicio es perfecto para aprender sobre atributos privados porque:
- Queremos mantener el saldo protegido
- Solo métodos especiales deben cambiar el dinero
- Necesitamos asegurarnos de que nadie pueda estropear las cosas accidentalmente

## 📝 Instrucciones

1. **Define una clase `BankAccount`** que debe:
    - Mantener el saldo de tu cuenta de forma privada `balance` (esto significa que el saldo no debe ser accesible directamente desde fuera de la clase).
    - Guardar un número de cuenta único, que también debe ser privado `account_number`.
    - Proporcionar un método `get_balance` que te permita verificar tu saldo de forma segura. Este método debe devolver el saldo de la cuenta.
    - Permitir hacer depósitos mediante un método `deposit`, que aumente el saldo cuando se deposite dinero.
    - Permitir hacer retiros mediante un método `withdraw`, pero solo si el saldo es suficiente. Si no tienes suficiente dinero, el retiro debe ser denegado.
    - Tener un método `display_info` que muestre la información de la cuenta, incluyendo el número de cuenta y el saldo actual de manera clara y legible. Ejemplo: `"Account {self.__account_number}: Balance = ${self.__balance}"`.

2. El sistema de retiros debe:
    - Verificar primero si tienes suficiente dinero para hacer el retiro.
    - Solo permitir el retiro si el monto es menor o igual al saldo actual.
    - Mantener un seguimiento adecuado del saldo después de cada operación de retiro.

3. **Prueba tu solución.** Crea una instancia de la clase `BankAccount` llamada `account` con:

```bash
initial_balance: 1000
account_number: "1234"
```

4. Realiza algunas operaciones como: obtener el balance, deposita 500, retira 2000, luego intenta retirar 800 y vuelve a obtener tu balance.

Piénsalo como usar un cajero automático: puedes verificar tu saldo, poner dinero y sacar dinero, pero solo si sigues los pasos correctos. ¡Igual que un banco real mantiene tu dinero seguro! 🏦

### 💡 Consejos:
- Los atributos como el saldo (`balance`) y el número de cuenta(`account_number`) deben ser privados, para que no puedan ser modificados directamente desde fuera de la clase. Esto se hace colocando dos guiones bajos `__` antes de sus nombres (por ejemplo: `__balance`).
- Asegúrate de que el método `deposit` solo acepte cantidades positivas.
- El método `withdraw` debe ser capaz de denegar retiros si el monto solicitado es mayor que el saldo disponible.
- Intenta acceder a `__balance` directamente - no funcionará (¡eso es bueno!) 



Así es como los programadores profesionales mantienen su código seguro y organizado. ¡Estás aprendiendo habilidades de programación del mundo real! 🌟