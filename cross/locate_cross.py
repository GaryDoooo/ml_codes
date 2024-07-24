from statistics import mean
import numpy as np


def rec_sum(x1, y1, x2, y2, s):
    return s[y2][x2] - s[y1 - 1][x2] - s[y2][x1 - 1] + s[y1 - 1][x1 - 1]


def locate_cross(data, c_size=15,
                 c_corner=5, cross_cnt=9):
    #  print(data)
    a = np.array(data)
    H, W = a.shape
    #  print(H, W)
    s = np.zeros((H + 1, W + 1))
    s1 = np.zeros((W + 1))
    for y in range(H):
        for x in range(W):
            s1[x + 1] = s1[x] + a[y][x]
            s[y + 1][x + 1] = s1[x + 1] + s[y][x + 1]

    rs = rec_sum
    ##### define the cross window #######
    c_size = c_size - 1
    c_corner = c_corner - 1

    sc = np.zeros(s.shape)
    for y in range(1, H - c_size):
        for x in range(1, W - c_size):
            x2 = x + c_size
            y2 = y + c_size
            res = rs(x, y, x2, y2, s)
            res -= rs(x, y, x + c_corner, y + c_corner, s)
            res -= rs(x2 - c_corner, y, x2, y + c_corner, s)
            res -= rs(x, y2 - c_corner, x + c_corner, y2, s)
            res -= rs(x2 - c_corner, y2 - c_corner, x2, y2, s)
            sc[y][x] = res
    thd = np.quantile(sc, 0.98)
    fsc = sorted([(sc[y][x], x, y) for y in range(1, H) for x in range(1, W)])
    vis = np.zeros(s.shape)
    idx = len(fsc) - 1
    cnt = 0
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    #  print(thd, fsc[-1])
    while cnt < cross_cnt:
        while True:
            _, x, y = fsc[idx]
            if vis[y][x] == 0:
                break
            idx -= 1
        stack = [(x, y)]
        cnt += 1
        while len(stack) > 0:
            x, y = stack.pop()
            vis[y][x] = cnt
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if vis[yy][xx] == 0 and sc[yy][xx] > thd:
                    stack.append((xx, yy))

    blks = [[] for i in range(cross_cnt)]
    for y in range(1, H):
        for x in range(1, W):
            if vis[y][x] > 0:
                blks[int(vis[y][x]) - 1].append((x, y))
    res = []
    for blk in blks:
        xs = [i[0] for i in blk]
        ys = [i[1] for i in blk]
        res.append((int(mean(xs)) - 1, int(mean(ys)) - 1))
    return res
