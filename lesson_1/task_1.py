"""Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком,
который формируется в цикле. После этого осуществляется вызов внешней lambda-функции,
которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией."""


def create_table(lines_num, rows_num):
    for i in range(1, lines_num + 1):
        line = []

        for k in range(1, rows_num + 1):
            item = i * k
            line.append(str(item))

        line_string = "    ".join(line)

        print(line_string)


def main():
    lines_num = int(input('First value: '))
    rows_num = int(input('Second value: '))
    create_table(lines_num, rows_num)


if __name__ == '__main__':
    main()


# line = lambda "\t".join(item): for item in line
# line = lambda item:
