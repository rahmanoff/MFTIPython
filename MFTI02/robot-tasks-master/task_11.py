#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    for i in range (30):
        if wall_is_on_the_right() == False and (wall_is_above() == True and wall_is_beneath() == True):
            fill_cell()
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == False or wall_is_beneath() == False):
            move_right()
        elif wall_is_on_the_right() == True and (wall_is_above() == True and wall_is_beneath() == True):
            fill_cell()
    i+=1
    pass


if __name__ == '__main__':
    run_tasks()
