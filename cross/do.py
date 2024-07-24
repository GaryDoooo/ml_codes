from PIL import Image
import numpy as np
from locate_cross import locate_cross
from statistics import mean
############# Own modules ############
from utilities import norm_test
from describe import describe


def make_list(data, u=0):
    return np.repeat(
        [float(i) - u for i in range(len(data))],
        data)


def derivative_forward(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]


def compress_list(lst):
    return [x for i, x in enumerate(lst) if i == 0 or x != lst[i - 1]]


def check_2d2p(d):
    d2 = derivative_forward(derivative_forward(
        [float(i) for i in d]))
    thd = min(d2) * .5
    l = [0 if i >= thd else 1 for i in d2
         if i > 0 or i < thd]
    #  print(thd, compress_list(l))
    return len(compress_list(l)) > 3


filename = input("")
# Open the PNG image
image = Image.open(filename)

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Convert the grayscale image to a 2D NumPy array
a = array_2d = np.array(grayscale_image)

# Print the shape of the 2D array
print("image size", array_2d.shape)

x1, x2, x3, x4, x5, x6 = 1050, 1263, 1319, 1530, 1584, 1794
y1, y2, y3, y4, y5, y6 = 173, 384, 501, 714, 824, 1038
subs = [(x1, y1, x2, y2), (x3, y1, x4, y2), (x5, y1, x6, y2),
        (x1, y3, x2, y4), (x3, y3, x4, y4), (x5, y3, x6, y4),
        (x1, y5, x2, y6), (x3, y5, x4, y6), (x5, y5, x6, y6)]

#  sub = a[y1:y2, x1:x2]
#  print(sub.shape)
cnt = 0
for x1, y1, x2, y2 in subs:
    sub = a[y1:y2, x1:x2]
    r = locate_cross(sub, cross_cnt=1)
    x, y = r[0]
    cnt += 1
    #  print(x, y)
    ad, sk, d2 = [], [], []
    for dy in [-40, -20, 20, 40]:
        l = [sub[y + dy][_] for _ in range(x - 20, x + 21)]
        x0 = x - 20 + l.index(max(l))
        l = [sub[y + dy][_] for _ in range(x0 - 20, x0 + 20)]
        ll = make_list(l)
        r = norm_test(ll, print_out=False)
        r2 = describe(ll, print_out=False)
        ad.append(r['AD s'])
        sk.append(abs(r2['skew']))
        d2.append(check_2d2p(l))
        #  print(cnt, r['shapiro s'], r["AD s"], r2["skew"],
    print("Zone %d ctr(%d, %d) AD=%.2f skew=%.2f D2:%.2f" % (
        cnt, x, y, mean(ad), mean(sk), mean(d2)))
