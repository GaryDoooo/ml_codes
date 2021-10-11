import csv


def read_400_700_sp(filename):
    res = []
    with open(filename, newline='') as csvfile:
        for r in csv.reader(csvfile, delimiter=' ', quotechar='|'):
            temp = []
            for col in r:
                try:
                    temp.append(float(col))
                except BaseException:
                    pass
            res.append(temp)
    return res


def main():
    raw = read_400_700_sp('2LED.res')
    white = list(filter(lambda x: abs(x[4] - .31)
                        < .02 and abs(x[5] - .33) < .02 and x[6] < 0.1, raw))
    white.sort(key=lambda x: x[6])
    print(white)


if __name__ == "__main__":
    main()
