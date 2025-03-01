"""
Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого
лексичного контексту, тобто з області, де вона була оголошена.

Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання
і повторного використання вже обчислених значень чисел Фібоначчі.

- Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
- fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
- Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
- Використання рекурсії для обчислення чисел Фібоначчі.
"""

def caching_fibonacci():
    cache = dict()

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif cache.get(n, -1) > 0:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
