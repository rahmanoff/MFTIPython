# Практика: Робот
# Выйти из ловушки. Где находится выход, не известно.

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

    for i in range (10):
        if wall_is_on_the_left() and wall_is_above():
            move_right()
        if wall_is_on_the_right() and wall_is_above():
            while wall_is_above():
                move_left()
        elif (wall_is_on_the_left() == False and wall_is_above() and wall_is_on_the_right() == False):
            move_right()
        i+=1
    if wall_is_above() == False:
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()

    pass


if __name__ == '__main__':
    run_tasks()
