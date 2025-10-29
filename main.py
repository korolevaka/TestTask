def main():
    """
    Главная функция программы.
    Читает входные данные, проверяет ограничения и обрабатывает строки
    """
    pattern = "youit"  # Паттерн для поиска последовательностей

    try:
        t = int(input().strip()) # Чтение количества тестов
    except ValueError:
        # Ошибка если введено не числовое значение
        print("Ошибка: необходимо ввести число тестов")
        return

    # Проверка диапазона количества тестов 1<=t<=10^5
    if t < 1 or t > 10 ** 5:
        print("Ошибка: количество тестов должно быть от 1 до 10^5")
        return

    lines = []  # Список для хранения тестовых строк
    total_length = 0  # Переменная для проверки суммарной длины

    for i in range(t):
        line = input().strip()  # Считываем текущую строку

        # Проверка длины строки 1<=s<=10^6
        if not line or len(line) > 10 ** 6:
            print("Ошибка: длина строки должна быть от 1 до 10^6 символов")
            return

        # Проверка суммарной длины строк (не должно превышать 10^6)
        total_length += len(line)
        if total_length > 10 ** 6:
            print("Ошибка: суммарная длина всех строк превышает 10^6 символов")
            return

        lines.append(line)  # Сохраняем строку в список

    # Для каждой строки вызываем функцию вычисления макс. последовательности
    for line in lines:
        max_sequence = max_consistency(line, pattern)
        print(max_sequence)


def max_consistency(line, pattern):
    """
    Вспомогательная функция для поиска максимальной последовательности символов из паттерна.
    Символы должны идти в правильном порядке паттерна.

    Args:
        line (str): строка для анализа
        pattern (str): паттерн для поиска

    Returns:
        int: максимальная длина найденной последовательности
    """
    max_sequence = 0  # Максимальная найденная длина последовательности в строке
    current_sequence = 0  # Текущая длина последовательности
    pattern_position = 0  # Текущая позиция в паттерне (0=y, 1=o, 2=u, 3=i, 4=t)

    for char in line:
        # Если текущий символ совпадает с ожидаемым символом паттерна
        if char == pattern[pattern_position]:
            current_sequence += 1
            pattern_position += 1

            # Если дошли до конца паттерна (5 символов), обнуляем позицию
            if pattern_position == len(pattern):
                pattern_position = 0

            # Максимальной длине присваиваем максимальное значение между макс.длиной и текущей длиной
            max_sequence = max(max_sequence, current_sequence)
        else:  # Если условие не выполнено
            current_sequence = 0
            pattern_position = 0

            if char == pattern[pattern_position]:
                current_sequence += 1  # Начинаем новую последовательность, увеличиваем счетчик на 1
                pattern_position += 1  # Позицию в паттерне увеличиваем на 1 (переходим ко второму символу)

            max_sequence = max(max_sequence, current_sequence)

    return max_sequence  # Возвращаем максимально найденную длину


if __name__ == "__main__":
    main() # Запускаем функцию main, при запуске приложения
