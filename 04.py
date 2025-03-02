"""
Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

Вимоги до завдання:

- Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор
відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
- Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це
винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну
відповідь користувачеві. Виконання програми при цьому не припиняється.
"""

from colorama import init, Fore

init(autoreset=True)
RED = Fore.RED


def input_error(func):
    """Декоратор для обробки помилок введення користувача."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return RED + f"\tGive me name and phone please. Format: <name> <phone>"
        except KeyError:
            return RED + f"\tContact not found."
        except IndexError:
            return RED + f"\tNot enough arguments provided."

    return inner


@input_error
def parse_input(user_input):
    """Розбирає введений користувачем рядок на команду та аргументи."""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """Додає новий контакт."""

    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Змінює телефон існуючого контакту."""

    name, phone = args
    contacts[name] = phone
    return "Contact changed."


@input_error
def show_phone(args, contacts):
    """Показує телефон контакту."""

    name = args[0]
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    """Виводить усі контакти."""

    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
