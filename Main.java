import java.util.Scanner;

public class Main {
    static String pattern = "youit"; // Паттерн для поиска последовательностей

    /**
     Главный метод программы.
     Обрабатывает ввод данных, проверяет ограничения и вычисляет максимальные последовательности.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // сканер для чтения данных с консоли

        // Проверка, что сначала вводится число тестов
        if (!scanner.hasNextInt()) {
            System.out.println("Ошибка: необходимо ввести число тестов");
            return;
        }

        int t = scanner.nextInt(); // считываем количество тестов
        scanner.nextLine(); // переходим на следующую строку после числа

        // Проверка диапазона количества тестов 1<=t<=10^5
        if (t < 1 || t > Math.pow(10, 5)) {
            System.out.println("Ошибка: количество тестов должно быть от 1 до 10^5");
            return;
        }

        String[] lines = new String[t]; // создаем массив строк, размером количества тестов
        int totalLength = 0; // переменная для проверки суммарной длины

        for (int i = 0; i < t; i++) { // создаем цикл для заполнения массива
            String line = scanner.nextLine(); // считываем текущую строку

            // Проверка длины строки 1<=s<=10^6
            if (line.isEmpty() || line.length() > Math.pow(10, 6)) {
                System.out.println("Ошибка: длина строки должна быть от 1 до 10^6 символов");
                return;
            }

            // Проверка суммарной длины строк (не должно превышать 10^6)
            totalLength += line.length();
            if (totalLength > Math.pow(10, 6)) {
                System.out.println("Ошибка: суммарная длина всех строк превышает 10^6 символов");
                return;
            }

            lines[i] = line; // если все проверки пройдены, сохраняем строку в массив
        }

        scanner.close(); // закрываем сканер

        for (String line : lines) { // цикл: перебираем каждую строку в массиве строк
            // для каждой строки вызываем функцию вычисления макс. последовательности
            int maxSequence = maxConsistency(line);
            System.out.println(maxSequence); // вывод результата
        }
    }

    /**
     Вспомогательная функция для поиска максимальной последовательности символов из паттерна.
     Символы должны идти в правильном порядке паттерна.

     @param line - на вход поступает строка для анализа
     @return maxSequence - на выход максимальная длина найденной последовательности
     */
    private static int maxConsistency(String line) {
        int maxSequence = 0; // Максимальная найденная длина последовательности в строке
        int currentSequence = 0; // Текущая длина последовательности
        int patternPosition = 0; // Текущая позиция в паттерне (0=y, 1=o, 2=u, 3=i, 4=t)

        for (int i = 0; i < line.length(); i++) { // цикл: перебираем строку по символьно
            char c = line.charAt(i); // присваиваем 'c' символ под индексом i (начиная от 0)

            // Если текущий символ совпадает с ожидаемым символом паттерна
            if (c == pattern.charAt(patternPosition)) {
                currentSequence++; // +1 к текущей длине
                patternPosition++; // +1 к позиции в паттерне (переход на следующий символ)

                // Если дошли до конца паттерна (5 символов), обнуляем позицию
                if (patternPosition == pattern.length()) {
                    patternPosition = 0;
                }

                // максимальной длине присваиваем максимально значение между макс.длиной и текущей длиной
                maxSequence = Math.max(maxSequence, currentSequence);
            } else { // если условие не выполнено
                currentSequence = 0; // обнуляем счетчик текущей последовательности
                patternPosition = 0; // обнуляем счетчик паттерна

                // Проверка, если символ начало новой последовательности (т.е. если старая последовательность оборвалась на новую)
                if (c == pattern.length()) {
                    currentSequence++;  // Начинаем новую последовательность, увеличиваем счетчик на 1
                    patternPosition++;  // Позицию в паттерне увеличиваем на 1 (переходим ко второму символу)
                }
                maxSequence = Math.max(maxSequence, currentSequence);
            }
        }

        return maxSequence; // возвращаем максимально найденную длину
    }
}