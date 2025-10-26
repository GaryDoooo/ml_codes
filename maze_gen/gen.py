from random import randint
from p44 import p44


def gen(width=8, height=8):
    vis = [0] * (width * height + 10)
    wall = [1] * (width * height * 2 + 10)
    ds = [-1, 1, width, -width]
    d_wall = [-1, 0, 0, -width]
    p0 = 0
    stack = [p44[randint(0, 23)]]
    vis[0] = 1
    while (len(stack) > 0):
        val = stack.pop()
        p = val // 1000
        dirs = val % 1000
        done = False
        for i in range(4):
            d_idx = dirs % 10
            dirs = dirs // 10
            if d_idx == 0:
                continue
            d = ds[d_idx - 1]
            if p % width == 0 and d == -1:
                continue
            if p < width and d == -width:
                continue
            if p >= width * (height - 1) and d == width:
                continue
            if p % width == (width - 1) and d == 1:
                continue
            new_p = p + d
            if vis[new_p] == 1:
                continue
            idx_wall = (p % width) + (p // width) * 2 + d_wall[d_idx - 1]
