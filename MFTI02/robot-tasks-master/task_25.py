# Практика: Робот
# Закрасить клетки.

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
    move_up()
    move_up()

@task
def task_2_2():
    move_down()
    cross()
    for i in range (4):
        move_right(4)
        cross()
    
    pass


if __name__ == '__main__':
    run_tasks()
