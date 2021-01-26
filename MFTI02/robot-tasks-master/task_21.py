# Практика: Робот
# Закрасить отмеченные клетки.

#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.05)
def task_4_11():
    i=0
    move_down()
    while i < 13:
        for i in range(i+1):
            move_right()
            fill_cell()
            i+=1
        move_down()
        move_left(i)
    move_right()
    pass

if __name__ == '__main__':
    run_tasks()
