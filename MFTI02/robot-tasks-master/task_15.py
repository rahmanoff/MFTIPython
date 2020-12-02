# Практика: Робот
# Перейти в противоположный угол. В начальный момент робот находится в углу, но не известно, в каком.

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
        if (wall_is_on_the_left() and wall_is_above()) and (wall_is_beneath() == False and wall_is_on_the_right() == False):
            for i in range (9):
                move_right()
                move_down()
        elif (wall_is_on_the_right() and wall_is_above()) and (wall_is_beneath() == False and wall_is_on_the_left() == False):
            for i in range (9):
                move_left()
                move_down()
        elif (wall_is_on_the_left() and wall_is_beneath()) and (wall_is_above() == False and wall_is_on_the_right() == False):
            for i in range (9):
                move_right()
                move_up()
        elif (wall_is_on_the_right() and wall_is_beneath()) and (wall_is_above() == False and wall_is_on_the_left() == False):
            for i in range (9):
                move_left()
                move_up()

if __name__ == '__main__':
    run_tasks()
