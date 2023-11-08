# Программа для написания алгоритма робота

Базовый функционал программы схож на [КуМир](https://www.niisi.ru/kumir/) и [Среду "Исполнители"](https://kpolyakov.spb.ru/school/robots/robots.htm). Отличие заключается в том, что в этой программе необходимо писать алгоритм робота на языке `python` при помощи методов и функций.

## Инструкция по использованию

Для запуска программы необходимо запустить файл под названием `main.py`. 
Алгоритм необходимо писать в файле `script.py`

## Методы и функции робота

+ robot.move() - передвинуть робота на одну клетку по направлению
+ robot.turn_left() - повернуть робота налево
+ robot.turn_right() - повернуть робота направо
+ robot.check_garden_under() - возвращает True, если под роботом находится невспашенная грядка
+ robot.check_wall_ahead() - возвращает True, если перед роботом находится стена
+ robot.plant() - засеять грядку

## Настройка уровня и программы
Уровень можно настроить в файле `level.txt`. Количество символов в каждой строке должно **совпадать**.
+ \# - стена
+ r - начальная позиция робота
+ g - незасеянная грядка
+ p - засеянная грядка
+ \* - клетки, на которых был робот
