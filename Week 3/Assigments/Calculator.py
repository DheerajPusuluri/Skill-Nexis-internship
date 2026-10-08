class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
calc = Calculator()
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", calc.add(a, b))
    print("Subtraction:", calc.subtract(a, b))
    print("Multiplication:", calc.multiply(a, b))
    print("Division:", calc.divide(a, b))
except ValueError:
    print("Error: Please enter valid numbers.")