from statistics import mean
import numpy as np


def rectangular_sum(x1, y1, x2, y2, s):
    """
    Using 2D prefix sum to calculate the sum of a rectangular area 
    s is the prefix sum array. x1,y1 is the top left corner, x2,y2 is the bottom right, both points included.
    """
    return s[y2][x2] - s[y1 - 1][x2] - s[y2][x1 - 1] + s[y1 - 1][x1 - 1]


def locate_cross(data, c_size=15,thd_quantile=0.98,
                 c_corner=5, cross_cnt=9):
    """
    This code detects white plus-sign shaped crosses on a black background. The algorithm employs a fixed-size plus-shaped mask. 
    
        ###...###
        ###...###
        .........
        ###...###
        ###...### 
        
        The mask is defined by the edge length of the outer square, and the size of four corner squares (the # part)
    
    Args:
        data: a 2D array of brightness level, RGB need be converted into grayscale
        c_size: the edge length of the outer square in pixel of the mask
        c_corner: the size of the four corner squares
        thd_quantile: a threshold to separate each cross area
        cross_cnt: how many crosses to look for in the image.        
        
    Returns:
        A list of (X, Y) coordinates tuples 

    """
    a = np.array(data)
    H, W = a.shape
    s = np.zeros((H + 1, W + 1))
    s1 = np.zeros((W + 1))
    
    # s is the 2D prefix sum of all pixel levels.
    for y in range(H):
        for x in range(W):
            s1[x + 1] = s1[x] + a[y][x]
            s[y + 1][x + 1] = s1[x + 1] + s[y][x + 1]

    rs = rectangular_sum
    c_size = c_size - 1
    c_corner = c_corner - 1
    # sc stores the sum of pixel levels with the cross shape mask 
    # the x,y coordinate is the top left corner of the outer square of the mask
    sc = np.zeros(s.shape)
    for y in range(1, H - c_size):
        for x in range(1, W - c_size):
            x2 = x + c_size
            y2 = y + c_size
            corners = [
                (x, y, x + c_corner, y + c_corner),
                (x2 - c_corner, y, x2, y + c_corner),
                (x, y2 - c_corner, x + c_corner, y2),
                (x2 - c_corner, y2 - c_corner, x2, y2)
            ]
            sc[y][x] = rs(x, y, x2, y2, s) - sum(rs(*corner, s) for corner in corners)
            
    # thd is the pixel level threshold to be counted into a detected cross area
    thd = np.quantile(sc, thd_quantile)
    # sort all the pixels with its sc value (the sum with the mask)
    fsc = sorted([(sc[y][x], x, y) for y in range(1, H) for x in range(1, W)])
    
    # Here we suppose all the cross area being separated into islands by the thd value 
    # Use DFS to mark the top cross_cnt numbers of the islands
    vis = np.zeros(s.shape)
    idx = len(fsc) - 1
    cnt = 0 # num of islands found
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    
    try:
        while cnt < cross_cnt:
            while True:
                _, x, y = fsc[idx]
                if vis[y][x] == 0:
                    break
                idx -= 1
            stack = [(x, y)]
            cnt += 1
            vis[y][x] = cnt
            while len(stack) > 0:
                x, y = stack.pop()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if vis[yy][xx] == 0 and sc[yy][xx] > thd:
                        stack.append((xx, yy))
                        vis[yy][xx] = cnt
    except:
        pass
        
    # Collect the coordinates of each marked islands
    # and get its averaged center XY as the detected cross center.
    blks = [[] for i in range(cnt)]
    for y in range(1, H):
        for x in range(1, W):
            if vis[y][x] > 0:
                blks[int(vis[y][x]) - 1].append((x, y))
    res = []
    for blk in blks:
        xs, ys = zip(*blk)  
        res.append((int(mean(xs)+c_size/2) -1, int(mean(ys)+c_size/2) - 1))
    
    return res
