class Direction:
    x: int
    y: int

class Left(Direction):
    x = -1
    y = 0

class Right(Direction):
    x = 1
    y = 0

class Down(Direction):
    x = 0
    y = 1

class Up(Direction):
    x = 0
    y = -1
