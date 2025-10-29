import re


def main():
    """
    Главная функция программы (без изменений)
    """
    pattern = "youit"

    try:
        t = int(input().strip())
    except ValueError:
        print("Ошибка: необходимо ввести число тестов")
        return

    if t < 1 or t > 10 ** 5:
        print("Ошибка: количество тестов должно быть от 1 до 10^5")
        return

    lines = []
    total_length = 0

    for i in range(t):
        line = input().strip()

        if not line or len(line) > 10 ** 6:
            print("Ошибка: длина строки должна быть от 1 до 10^6 символов")
            return

        total_length += len(line)
        if total_length > 10 ** 6:
            print("Ошибка: суммарная длина всех строк превышает 10^6 символов")
            return

        lines.append(line)

    for line in lines:
        max_sequence = max_consistency(line, pattern)
        print(max_sequence)


def max_consistency(line, pattern):
    """
    С использованием регулярных выражений
    """
    max_sequence = 0

    # Ищем полные повторения паттерна
    full_repeat_pattern = f"({pattern})+"
    for match in re.finditer(full_repeat_pattern, line):
        full_length = len(match.group())
        max_sequence = max(max_sequence, full_length)

    # Ищем частичные последовательности в конце
    for i in range(1, len(pattern)):
        partial_pattern = f"({pattern})*{re.escape(pattern[:i])}"
        for match in re.finditer(partial_pattern, line):
            partial_length = len(match.group())
            max_sequence = max(max_sequence, partial_length)

    return max_sequence


if __name__ == "__main__":
    main()
