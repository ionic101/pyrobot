from robot import Robot

'''
robot.move() - передвинуть робота на одну клетку по направлению
robot.turn_left() - повернуть робота налево
robot.turn_right() - повернуть робота направо
robot.check_garden_under() - возвращает True, если под роботом находится невспашенная грядка
robot.check_wall_ahead() - возвращает True, если перед роботом находится стена
robot.plant() - вспахать грядку
'''

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
