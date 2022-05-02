#! /usr/local/bin/python3.6
"""
Correlation coefficient computaion
"""
import math
import sys
import traceback


class CorrelationCoefficient:
    def compute_r(self, x, y):
        """ R computation

        :param  list  x: 1st list of random variables
        :param  list  y: 2nd list of random variables
        :return float r: correlation coefficient of X and Y
        """
        if not isinstance(x, list):
            print("Argument(X) is not a list!")
            sys.exit()
        if not isinstance(y, list):
            print("Argument(Y) is not a list!")
            sys.exit()
        if len(x) == 0:
            print("List(X) is none!")
            sys.exit()
        if len(y) == 0:
            print("List(Y) is none!")
            sys.exit()
        if len(x) != len(y):
            print("Argument list size is invalid!")
            print(x, y)
            print(len(x), len(y))
            sys.exit()
        try:
            mean_x, mean_y = sum(x) / len(x), sum(y) / len(y)
            cov = sum([(a - mean_x) * (b - mean_y) for a, b in zip(x, y)])
            var_x = sum([(a - mean_x) ** 2 for a in x])
            var_y = sum([(b - mean_y) ** 2 for b in y])
            #  print(var_x, var_y, y)
            return (cov / math.sqrt(var_x)) / math.sqrt(var_y)
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        obj = CorrelationCoefficient()
        print(obj.compute_r(x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        print(obj.compute_r(x, [2, 3, 3, 4, 6, 7, 8, 9, 10, 11]))
        print(obj.compute_r(x, [15, 13, 12, 12, 10, 10, 8, 7, 4, 3]))
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
