# Программа для написания алгоритма робота - PyRobot

Базовый функционал программы схож на функционал [КуМира](https://www.niisi.ru/kumir/) и [Среды "Исполнители"](https://kpolyakov.spb.ru/school/robots/robots.htm). Отличие заключается в том, что в этой программе необходимо писать алгоритм робота на языке `python` при помощи методов и функций.

## Инструкция по использованию

Для использования программы необходимо иметь установленную библиотеку `tkinter`.
Для запуска программы необходимо запустить файл под названием `main.py`. 
Алгоритм необходимо писать в файле `script.py`

## Методы и функции робота

+ robot.move() - передвинуть робота на одну клетку по направлению
+ robot.turn_left() - повернуть робота налево
+ robot.turn_right() - повернуть робота направо
+ robot.check_garden_under() - возвращает True, если под роботом находится невспашенная грядка
+ robot.check_wall_ahead() - возвращает True, если перед роботом находится стена
+ robot.plant() - вспахать грядку

## Настройка уровня
Уровень можно настроить в файле `level.txt`. Количество символов в каждой строке должно **совпадать**.

#### Обозначения символов
+ "\#" - стена
+ "r" - начальная позиция робота
+ "g" - невспашенная грядка
+ "p" - вспашенная грядка
+ "\*" - клетки, на которых был робот
+ " " - пустое пространство


#### Пример создания уровня
```
############
#g  #      #
#       #  #
#g g#   #pp#
#####   ####
#          #
#  #       #
#g #   #   #
#      # r #
###### #####
#g g     gg#
############
```

#### Отображение уровня в программе
![level](https://github.com/ionic101/pyrobot/assets/93050090/84f319c6-172e-46f1-bb5b-09fc36fa8d7a)

## Настройка программы
Настроить программу можно в файле `settings.py`

```python
import direction

WINDOW_TITLE = 'Robot'
LEVEL_FILE_NAME = 'level.txt'

CELL_SCALE = 150

ROBOT_SCALE = 0.6
ROBOT_START_DIRECTION = direction.Up
ROBOT_COLOR = 'red'
ARROW_COLOR = 'black'
ARROW_WIDTH = 3

DELAY = 50  #milliseconds

COLORS = {
    '#': 'black',
    'g': 'brown',
    'p': 'orange',
    '*': 'green',
    ' ': 'white'
}
```

## Пример написания алгоритма робота
Весь код необходимо писать в файле `script.py` в методе `robot_behavior_tree`
#### Код
```python
def robot_behavior_tree(robot: Robot) -> None:
    for _ in range(3):
        robot.move()

    robot.turn_left()

    while not robot.check_wall_ahead():
        robot.move()
    
    robot.turn_left()

    for _ in range(2):
        robot.move()
    
    if robot.check_garden_under():
        robot.plant()
    
    robot.move()

    robot.turn_left()

    for _ in range(4):
        robot.move()
```

#### Результат
![robot](https://github.com/ionic101/pyrobot/assets/93050090/391e2da2-8463-4eb5-bcae-89543210a339)
