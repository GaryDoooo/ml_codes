import curses
from time import sleep
from copy import deepcopy
from blocks import data as d
from random import choice


def global_init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(0)
    stdscr.nodelay(True)
    return stdscr


class board:
    def __init__(self, stdscr, x0=6, y0=3, w=10, h=25):
        self.b = [[0] * w for _ in range(h)]
        self.w = w
        self.h = h
        self.game_board = stdscr.subpad(h + 1, w * 2 + 2, y0, x0)
        self.banner = stdscr.subwin(y0 + h + 2, x0)
        self.game_board.border()
        self.game_board_rows = []
        for y in range(h):
            self.game_board_rows.append(
                stdscr.subwin(1, w * 2 + 2, y0 + y, x0 + 1))
            #  for x in range(w):
            #      try:
            #          self.game_matrix[y][x] = stdscr.subpad(
            #              1, 2, y0 + y, x0 + x * 2)
            #      except BaseException:
            #          print(x, y)
            #          exit(1)
        self.banner.addstr(0, 0, "Score: %04d Speed: %02d \nPress Q to exit" %
                           (0, 1))
        self.old_b = deepcopy(self.b)

    def board_print(self, score=None, speed=1):
        c = ("  ", "[]")
        #  try:
        for y in range(self.h):
            for x in range(self.w):
                if self.old_b[y][x] != self.b[y][x]:
                    self.game_board_rows[y].addstr(0, x * 2, c[self.b[y][x]])
                    #  self.game_board.addstr(y, x * 2 + 1, c[self.b[y][x]])
                    #  self.game_matrix[y][x].addstr(c[self.b[y][x]])
                    #  if self.b[y][x]:
                    #      self.game_matrix[y][x].border()
                    #  else:
                    #      self.game_matrix[y][x].border(
                    #          " ", " ", " ", " ", " ", " ", " ", " ")
            self.game_board_rows[y].refresh()
        #  self.game_board.refresh()
        if score is not None:
            self.banner.addstr(
                0, 0, "Score: %04d Speed: %02d \nPress Q to exit" %
                (score, speed))
            self.banner.refresh()
        #  stdscr.refresh()
        self.old_b = deepcopy(self.b)
        #  except BaseException:
        #  for y in range(y0, y0 + self.h):
        #      for x in (x0, x0 + self.w * 2 + 1):
        #          stdscr.addstr(y, x, "#")
        #  for x in range(x0, x0 + self.w * 2 + 2):
        #      stdscr.addstr(y0 + self.h, x, "#")
        #  stdscr.border()  # x0, x0 + self.w * 2 + 1, y0, y0 + self.h)
        #  stdscr.addstr(
        #  y0 - 2, x0,             #  stdscr.refresh()
        #  self.ol"Score: %04d Speed: %d \t press Q to exit" %
        #  (0, 1))
#  d_b = deepcopy(self.b)


def pos(b, x, y, r):
    return [(i + x, j + y) for j, i in b[r]]
    #  key=lambda x: x[1], reverse=True)


def valid(b, l, old_l):
    try:
        for x, y in l:
            if (x, y) in old_l:
                continue
            if x < 0 or y < 0:
                return False
            if b[y][x] == 1:
                return False
    except BaseException:
        return False
    return True


def update(b, old_l, new_l):
    for x, y in old_l:
        b[y][x] = 0
    for x, y in new_l:
        b[y][x] = 1


def check(b):
    changed = True
    over_all_changed = 0
    while changed:
        changed = False
        for y0 in range(len(b) - 1, 0, -1):
            row = b[y0]
            if 0 not in row:
                changed = True
                over_all_changed += 1
                for y in range(y0, 0, -1):
                    for x in range(len(row)):
                        b[y][x] = b[y - 1][x]
        #  over_all_changed |= changed
    return over_all_changed


def main():
    sc = global_init()
    b = board(sc)
    b.board_print()
    score = 0
    speed_setting = 9
    while True:
        block = choice(d)
        timer, r, x, y = 0, 0, 5, 2
        pos_now = pos(block, x, y, r)
        if not valid(b.b, pos_now, [(0, 0)]):
            game_over(sc)
        update(b.b, ((0, 0),), pos_now)
        b.board_print()
        speed = speed_setting
        #  print(len(block))
        while True:
            sleep(0.02)
            c = sc.getch()
            if c > 0:
                x1, y1, r1 = x, y, r
                if c == curses.KEY_RIGHT:
                    x1 += 1
                elif c == ord('q') or c == ord('Q'):
                    game_over(sc)
                elif c == curses.KEY_LEFT:
                    x1 -= 1
                elif c == curses.KEY_UP:
                    r1 += 1
                    r1 = r1 % len(block)
                elif c == curses.KEY_DOWN:
                    y1 += 1
                    speed = 1
                newpos = pos(block, x1, y1, r1)
                if valid(b.b, newpos, pos_now):
                    update(b.b, pos_now, newpos)
                    b.board_print()
                    y, x, r = y1, x1, r1
                    pos_now = newpos
            sleep(0.02)
            timer = timer + 1
            timer = timer % speed
            if timer == 0:
                y1 = y + 1
                newpos = pos(block, x, y1, r)
                if valid(b.b, newpos, pos_now):
                    update(b.b, pos_now, newpos)
                    b.board_print()
                    y = y1
                    pos_now = newpos
                else:
                    s = check(b.b)
                    if s > 0:
                        score += s
                        speed_setting = max(1, 9 - score // 10)
                        b.board_print(score=score, speed=10 - speed_setting)
                    break
#	b.board_print(sc)
    # game_over(sc)

# for y in range(5, 25):
#	for x in (6, 27):
#		stdscr.addstr(y, x, "#")
# for x in range(6, 28):
#	stdscr.addstr(y, x, "#")
# stdscr.refresh()
#i = 0
#x, y = 0, 0
# while True:
#	c = ("-", "\\", "|", "/")
#	i = (i + 1) % 4
#	stdscr.addstr(5 + y, 7 + x, c[i])
#	sleep(0.1)
#	stdscr.refresh()


def game_over(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("\nGame Over")
    exit(0)


if __name__ == "__main__":
    main()
