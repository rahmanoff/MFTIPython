#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_left()
    move_up(2)

@task(delay=0.02)
def task_2_4():
    for i in range (4):
        for i in range (9):
            cross()
            move_right(4)
        cross()
        move_left(36)
        move_down(4)
    for i in range (9):
        cross()
        move_right(4)
    cross()
    while wall_is_on_the_left() == False:
        move_left()

if __name__ == '__main__':
    run_tasks()
