"""
created by Nagaj at 08/05/2021
"""


class Direction:
    TEXT = ""

    @classmethod
    def help_text(cls):
        print("You Are Moving to {}".format(cls.TEXT))

    @classmethod
    def __repr__(cls):
        return cls.TEXT


class Up(Direction):
    TEXT = "UP"


class Right(Direction):
    TEXT = "RIGHT"


class Down(Direction):
    TEXT = "DOWN"


class Left(Direction):
    TEXT = "LEFT"


directions = [Up, Right, Down, Left]
for direction in directions:
    direction().help_text()


print(directions.pop())
print([obj() for obj in directions])