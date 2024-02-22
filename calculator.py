def add(a, b):
    """
    Функція для додавання двох чисел.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

def subtract(a, b):
    """
    Функція для віднімання одного числа від іншого.

    >>> subtract(5, 2)
    3
    >>> subtract(10, 5)
    5
    """
    return a - b

def multiply(a, b):
    """
    Функція для множення двох чисел.

    >>> multiply(3, 4)
    12
    >>> multiply(-2, 5)
    -10
    """
    return a * b

def divide(a, b):
    """
    Функція для ділення одного числа на інше.

    >>> divide(10, 2)
    5.0
    >>> divide(8, 4)
    2.0
    """
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
