#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    for i in range (30):
        if wall_is_on_the_right() == False and wall_is_above() == False:
            fill_cell()
            move_right()
        elif wall_is_on_the_right() == False and wall_is_above() == True:
            move_right()
        elif wall_is_on_the_right() == True and wall_is_above() == False:
            fill_cell()
    i+=1

if __name__ == '__main__':
    run_tasks()
