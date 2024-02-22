def add(x, y):
    """Функція додавання"""
    return x + y

def subtract(x, y):
    """Функція віднімання"""
    return x - y

def multiply(x, y):
    """Функція множення"""
    return x * y

def divide(x, y):
    """Функція ділення"""
    if y == 0:
        return "Ділення на нуль!"
    else:
        return x / y

print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = input("Введіть номер операції (1/2/3/4): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Некоректний вибір операції")
