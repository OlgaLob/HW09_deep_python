# Напишите следующие функции: ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import random
import csv
import json
from typing import Callable


def csv_file():
    with open('num.csv', 'a', newline='') as f_csv:
        writer_csv = csv.writer(f_csv, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(100, 1000):
            list_for_csv = [i for i in range(1, 100)]
            # random.shuffle(list_for_csv)
            csv_list = random.sample(list_for_csv, k=3)
            writer_csv.writerow(csv_list)
    with open('num.csv', 'r', newline='') as f_csv:
        reader_csv = csv.reader(f_csv, delimiter=' ', quotechar='|')
        rnd_row = random.randint(1, 900)
        count = 0
        for row in reader_csv:
            count += 1
            if count == rnd_row:
                return row


def json_file(func: Callable):
    def wrapper(*args, **kwargs):
        csv_file()
        a = int(csv_file()[0])
        b = int(csv_file()[1])
        c = int(csv_file()[2])
        result = func(a, b, c)
        print(f'Результат функции {func.__name__}, где {a = }, {b = }, {c = }: {result}')
        json_file = {f"{a}, {b}, {c}": result}
        with open('json_file.json', 'a', encoding='utf-8') as f:
            json.dump(json_file, f, sort_keys=True, indent=2, ensure_ascii=False)

        return result

    return wrapper


@json_file
def roots_equation(a: int = None, b: int = None, c: int = None):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение имеет бесконечное число корней")
            else:
                print("ошибка записи уравнения")
        else:
            x1 = -c / b
            print("x=", x1)
    else:
        discr = b ** 2 - 4 * a * c
        if discr < 0:
            return f'Нет корней'
        elif discr == 0:
            x1 = -b / (2 * a)
            return x1
        else:
            x1 = (-b + discr ** 0.5) / (2 * a)
            x2 = (-b - discr ** 0.5) / (2 * a)
            return x1, x2


roots_equation()
