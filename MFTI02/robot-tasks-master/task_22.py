# Практика: Робот
# Закрасить всё поле. Размеры поля неизвестны.

#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while (cell_is_filled() == False):
        while (wall_is_on_the_right() == False and cell_is_filled() == False):
            fill_cell()
            move_right()
        if wall_is_on_the_right():
            fill_cell()
            while wall_is_on_the_left() == False:
                move_left()
        if wall_is_beneath() == False:
             move_down()
if __name__ == '__main__':
    run_tasks()
