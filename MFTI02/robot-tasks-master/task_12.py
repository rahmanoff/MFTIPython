# Практика: Робот
# Закрасить клетки. Расстояние до стены не известно.

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    for i in range (30):
        if wall_is_on_the_right() == False and (wall_is_above() and wall_is_beneath()):
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == False and wall_is_beneath() == False):
            move_right()
        elif wall_is_on_the_right() == False and (wall_is_above() == False and wall_is_beneath()):
            fill_cell()
            move_right()
        elif wall_is_on_the_right() == False and wall_is_above():
            move_right()
        elif wall_is_on_the_right() and  (wall_is_above() == False and wall_is_beneath()):
            fill_cell()
    i+=1
    pass


if __name__ == '__main__':
    run_tasks()
