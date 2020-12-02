# Практика: Робот
# Обойти стену. Размеры стены и расстояние до неё неизвестны. Стена одна.

#!/usr/bin/python3

from pyrob.api import *

@task
def task_5_4():
    while wall_is_beneath() == False:
        move_down()
    while wall_is_beneath():
        move_right()
    move_down()
    move_left()
    while wall_is_above() and wall_is_on_the_left() == False:
        move_left()
    pass


if __name__ == '__main__':
    run_tasks()
