import curses
from time import sleep
from copy import deepcopy
from blocks import data as d
from random import choice, randint


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
        self.banner.addstr(0, 0, "Score: %04d Speed: %02d \nPress Q to exit" %
                           (0, 1))
        self.old_b = deepcopy(self.b)

    def board_print(self, score=None, speed=1):
        c = ("  ", "[]")
        for y in range(self.h):
            for x in range(self.w):
                if self.old_b[y][x] != self.b[y][x]:
                    self.game_board_rows[y].addstr(0, x * 2, c[self.b[y][x]])
            self.game_board_rows[y].refresh()
        if score is not None:
            self.banner.addstr(
                0, 0, "Score: %04d Speed: %02d \nPress Q to exit" %
                (score, speed))
            self.banner.refresh()
        self.old_b = deepcopy(self.b)


def pos(b, x, y, r):
    return [(i + x, j + y) for j, i in b[r]]


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
    return over_all_changed


class player(object):
    def __init__(self, stdscr, keys, x0=6, speed=9):
        self.b = board(stdscr, x0=x0)
        self.b.board_print()
        self.score = 0
        self.speed_setting = speed
        self.keys = keys

    def new_block(self, add_lines=0):
        if add_lines > 0:
            for y in range(self.b.h - add_lines):
                for x in range(self.b.w):
                    self.b.b[y][x] = self.b.b[y + add_lines][x]
            for y in range(self.b.h - add_lines, self.b.h):
                res = [1] * self.b.w
                for _ in range(randint(1, 4)):
                    res[randint(0, self.b.w - 1)] = 0
                self.b.b[y] = res
        self.block = choice(d)
        self.timer, self.r, self.x, self.y = 0, 0, 5, 2
        self.pos_now = pos(self.block, self.x, self.y, self.r)
        if not valid(self.b.b, self.pos_now, [(0, 0)]):
            #  game_over(sc)
            return False
        update(self.b.b, ((0, 0),), self.pos_now)
        self.b.board_print()
        self.speed = self.speed_setting
        return True

    def key_handler(self, c):
        x1, y1, r1 = self.x, self.y, self.r
        if c == self.keys[1]:
            x1 += 1
        elif c == self.keys[0]:
            x1 -= 1
        elif c == self.keys[2]:
            r1 += 1
            r1 = r1 % len(self.block)
        elif c == self.keys[3]:  # :
            y1 += 1
            self.speed = 1
        newpos = pos(self.block, x1, y1, r1)
        if valid(self.b.b, newpos, self.pos_now):
            update(self.b.b, self.pos_now, newpos)
            self.b.board_print()
            self.y, self.x, self.r = y1, x1, r1
            self.pos_now = newpos

    def drop(self):
        self.timer += 1
        self.timer = self.timer % self.speed
        if self.timer == 0:
            y1 = self.y + 1
            newpos = pos(self.block, self.x, y1, self.r)
            if valid(self.b.b, newpos, self.pos_now):
                update(self.b.b, self.pos_now, newpos)
                self.b.board_print()
                self.y = y1
                self.pos_now = newpos
            else:
                s = check(self.b.b)
                if s > 0:
                    self.score += s
                    self.speed_setting = max(1, 9 - self.score // 10)
                    self.b.board_print(
                        score=self.score, speed=10 - self.speed_setting)
                #  break
                return max(0, s - 2)
        return -1


def main():
    sc = global_init()
    p1_keys = (
        curses.KEY_LEFT,
        curses.KEY_RIGHT,
        curses.KEY_UP,
        curses.KEY_DOWN)
    p1 = player(sc, p1_keys)
    p1.new_block()
    p1_add = 1
    while True:
        sleep(0.02)
        c = sc.getch()
        if c > 0:
            if c in p1_keys:
                p1.key_handler(c)
            elif c == ord('q') or c == ord('Q'):
                game_over(sc, "Bye")
        sleep(0.02)
        p1_drop = p1.drop()
        if p1_drop >= 0:
            if not p1.new_block(p1_add):
                game_over(sc, "P1 dead.")


def game_over(stdscr, msg=""):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("\n", msg, "\nGame Over")
    exit(0)


if __name__ == "__main__":
    main()
