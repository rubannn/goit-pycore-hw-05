"""
Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл,
переданий як аргумент командного рядка,і виводити статистику за рівнями логування наприклад,
INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного
рядка, щоб отримати всі записи цього рівня.

Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному
забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи,
виявляти та діагностувати проблеми.
"""

import re
import sys
from collections import defaultdict
from colorama import init, Fore

init(autoreset=True)
COLOR = Fore.MAGENTA

log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)")


def parse_log_line(line: str) -> dict:
    """Розбирає один рядок логів у словник з полями:
    дата, час, рівень логування, повідомлення."""
    
    parse_log = dict()
    match = log_pattern.match(line)
    if match:
        date, time, code, text = match.groups()
        parse_log = {"date": date, "time": time, "code": code, "message": text}
    return parse_log


def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу та повертає список розібраних рядків."""

    logs = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            log = parse_log_line(line)
            if log:
                logs.append(log)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем логування."""
    return [item for item in logs if item["code"] == level]


def count_logs_by_level(logs: list) -> dict:
    """Рахує кількість логів для кожного рівня логування."""

    logs_by_level = defaultdict(int)
    for item in logs:
        logs_by_level[item["code"]] += 1
    return logs_by_level


def display_log_counts(counts: dict, level=""):
    """Виводить у консоль таблицю з підрахунком логів за рівнем."""

    title = ["Рівень логування", "Кількість"]
    a, b = [len(x) for x in title]
    separator = " | "

    print(f"{title[0]}{separator}{title[1]}")
    print(f"{'-' * a}{separator}{'-' * b}")
    for item in counts.items():
        code, k = item
        if code == level:
            print(COLOR + f"{code:<{a}}", end="")
            print(f"{separator}" + COLOR + f"{k}")
        else:
            print(f"{code:<{a}}{separator}{k}")


def display_log_details(logs: list, level: str):
    """Виводить детальні дані про логи певного рівня."""

    lvl = COLOR + f"{level}"
    print(f"\nДеталі логів для рівня {lvl}", ":", sep="")
    for log in filter_logs_by_level(logs, level):
        print(f"{log['date']} {log['time']} - {log['message']}.")


if __name__ == "__main__":
    # log_path = "./in/03.logs"
    arg_list = sys.argv
    if len(arg_list) < 2 or len(arg_list) > 3:
        print("Use: `python 03.py <log_path>` OR `python 03.py <log_path> <level>`")
        sys.exit(1)
    else:
        if len(arg_list) == 2:
            log_path, lvl = arg_list[1], ""
        else:
            log_path, lvl = arg_list[1:]
            lvl = lvl.upper()
        try:
            log_list = load_logs(log_path)
            display_log_counts(count_logs_by_level(log_list), lvl)
            if lvl:
                display_log_details(log_list, lvl)
        except FileNotFoundError:
            print(f"File '{log_path}' not found...")

# ---TESTS---
# python 03.py ./in/03.logs
# python 03.py ./in/03.logs error
# python 03.py ./in/03.logs info
