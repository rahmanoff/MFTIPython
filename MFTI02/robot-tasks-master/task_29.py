#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    a=0
    b=0
    while not wall_is_on_the_right() and b<3: 
        move_right()
        if cell_is_filled():
            a+=1
            b+=1
        if not cell_is_filled():
            b=0



    pass


if __name__ == '__main__':
    run_tasks()
