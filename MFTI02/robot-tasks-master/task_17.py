# Практика: Робот
# Перейти на вторую закрашенную клетку. Клетка может быть как справа, так и слева.

#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_27():
    while cell_is_filled() == False:
        move_up()
    if cell_is_filled():
        move_left()
        if cell_is_filled() == False:
            move_right()
            move_right()
if __name__ == '__main__':
    run_tasks()
