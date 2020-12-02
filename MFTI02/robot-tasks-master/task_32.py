# Практика: Робот
# Закрасить отмеченные клетки. В регистр ax записать количество клеток, которые были закрашены ещё до того, 
# как робот начал двигаться. 
# Количество и размеры коридоров не известны.

#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.01)
def task_8_18():
    i = 0
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        move_right()
        if not wall_is_above() and wall_is_beneath():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    i+=1
                if not cell_is_filled():
                    fill_cell()
        if not wall_is_beneath() and wall_is_above():
            while not wall_is_beneath():
                move_down()
    mov ('ax',i)        

    pass

if __name__ == '__main__':
    run_tasks()
