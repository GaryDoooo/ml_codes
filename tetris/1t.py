import curses
from time import sleep

def gobal_init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    stdscr.nodelay(True)
    return stdscr

class board:
    def __init__(self
for y in range(5, 25):
    for x in (6, 27):
        stdscr.addstr(y, x, "#")
for x in range(6, 28):
    stdscr.addstr(y, x, "#")
stdscr.refresh()
i = 0
x, y = 0, 0
while True:
    c = ("-", "\\", "|", "/")
    i = (i + 1) % 4
    stdscr.addstr(5 + y, 7 + x, c[i])
    sleep(0.1)
    c = stdscr.getch()
    if c == curses.KEY_RIGHT and x < 19:
        x += 1
    elif c == curses.KEY_LEFT and x > 0:
        x -= 1
    elif c == curses.KEY_UP and y > 0:
        y -= 1
    elif c == curses.KEY_DOWN and y < 18:
        y += 1
    stdscr.refresh()
#  curses.nocbreak()
#  stdscr.keypad(False)
#  curses.echo()
#  curses.endwin()
