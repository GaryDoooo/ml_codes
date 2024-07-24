import os
import glob


def get_png_files(directory):
    # Get a list of all PNG files in the specified directory
    png_files = glob.glob(os.path.join(directory, '*.png'))
    return png_files


def main():

    directory_path = './png'
    png_files = get_png_files(directory_path)
    # Create a presentation object

    cnt = 1
    while len(png_files) > 0:
        if cnt == 1:
            f = open('list' + str(cnt) + '.lst', 'w')
        elif cnt % 20 == 1:
            f.close()
            f = open('list' + str(cnt) + '.lst', 'w')
        cnt += 1
        filename = png_files.pop()
        f.write(f"{filename}\n")


if __name__ == "__main__":
    main()
