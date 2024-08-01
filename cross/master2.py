import os
import glob
########### Own Module #########
from ghost_line import double_line


def get_png_files(directory):
    # Get a list of all PNG files in the specified directory
    png_files = glob.glob(os.path.join(directory, '*.png'))
    return png_files


def main3():

    directory_path = './png'
    png_files = get_png_files(directory_path)

    for file in png_files:
        try:
            #  print(file)
            res = double_line(file)
            print(file + "," + str(
                res['lvl']) + str(res['data']))
        except BaseException:
            pass


if __name__ == "__main__":
    main3()
