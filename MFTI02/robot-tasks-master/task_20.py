# Практика: Робот
# Закрасить отмеченные клетки.

#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.05)
def task_4_3():
    for i in range(12):
        for i in range (27):
            move_right()
            fill_cell()
        move_down()
        move_left(27)
    move_right()

    pass
if __name__ == '__main__':
    run_tasks()
