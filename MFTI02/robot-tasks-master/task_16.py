#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_22():
    while (wall_is_above() == False and wall_is_on_the_left() and wall_is_on_the_right()):
        move_up()
    if wall_is_above() and wall_is_on_the_left():
        while wall_is_on_the_right() == False:
            move_right()
    elif wall_is_above() and wall_is_on_the_right():
        while wall_is_on_the_left() == False:
            move_left()
    pass
if __name__ == '__main__':
    run_tasks()
