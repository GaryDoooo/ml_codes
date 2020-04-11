import matplotlib.pyplot as plt
from pandas import read_excel
import numpy as np
import argparse


def insert_y(x, y1, y2, x1, x2):
    slope = (y2 - y1) / (x2 - x1)
    return y1 + slope * (x - x1)


def two_closest_x(x, input_x):
    length = len(input_x)
    if x <= input_x[0]:
        return 0, 1
    elif x >= input_x[length - 1]:
        return length - 1, length - 2
    else:
        abs_x = [abs(_ - x) for _ in input_x]
        i = np.argmin(abs_x)
        if input_x[i] < x:
            return i, i + 1
        else:
            return i - 1, i


def get_y_from_known_discrete_XY(
        x,  # any real number
        input_x,  # list of the known x
        input_y,  # list of the known y
):
    i1, i2 = two_closest_x(x, input_x)
    #  print(i1, i2)
    if x == input_x[i1]:
        return input_y[i1]
    y = insert_y(x, input_y[i1], input_y[i2], input_x[i1], input_x[i2])
    return y


def dispatch(input_xlsx,
             start,
             end,
             step,
             output_fig
             ):
    df = read_excel(input_xlsx)  # , sheet_name="Data")
    input_y = df["Y"]
    input_x = df["X"]
    x_result = []
    y_result = []
    print("X,Y,")
    for x in range(start, end + step, step):
        y = get_y_from_known_discrete_XY(
            x, input_x, input_y)
        #  i1, i2 = two_closest_x(x, input_x)
        #  y = insert_y(x, input_y[i1], input_y[i2], input_x[i1], input_x[i2])
        print("%f,%f," % (x, y))
        x_result.append(x)
        y_result.append(y)

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.plot(x_result, y_result, "r--")
    ax1.plot(input_x, input_y, 'go')
    plt.xlim([start, end])
    plt.savefig(output_fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_xlsx',
                        type=str,
                        help='Input xlsx filename.')
    parser.add_argument('--start',
                        default=400,
                        type=int,
                        help='Start of x in INT, default 400.')
    parser.add_argument('--end',
                        default=700,
                        type=int,
                        help='end of x in INT, default 700.')
    parser.add_argument('--step',
                        default=1,
                        type=int,
                        help='Step of x in INT, default 1.')
    parser.add_argument('--output_fig',
                        default='output.svg',
                        type=str,
                        help='Output figure filename, default output.svg.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
