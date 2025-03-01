"""
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати
всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні
числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також
потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для
підсумовування цих чисел і обчислення загального прибутку.

- Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати
генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються
записаними без помилок і чітко відокремлені пробілами з обох боків.
- Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers
для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.
"""

from typing import Callable
import re


def generator_numbers(text: str):
    for match in re.finditer(r"\b\d+\.\d+\b", text):  # find all float in format "X.Y"
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    return sum(generator_numbers(text)) # calc sum of generator items


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
