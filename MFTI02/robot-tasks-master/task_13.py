#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    for i in range (30):
        if wall_is_on_the_right() == False and (wall_is_above() == True and wall_is_beneath() == True):
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == False and wall_is_beneath() == True):
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == True and wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == False and wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_on_the_right() == True and (wall_is_above() == False and wall_is_beneath() == True):
            move_up()
            fill_cell()
            move_down()
        elif wall_is_on_the_right() == True and (wall_is_above() == True and wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
        elif wall_is_on_the_right() == True and (wall_is_above() == False and wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
            move_up()
            fill_cell()
            move_down() 
    i+=1
    pass


if __name__ == '__main__':
    run_tasks()
