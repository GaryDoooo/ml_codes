import pytesseract
from PIL import Image


def ocr(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def ocr_9zones(filename):
    im = Image.open(filename)
    x1, x2, x3, x4, x5, x6 = 1050, 1263, 1319, 1530, 1584, 1794
    y1, y2, y3, y4, y5, y6 = 173, 384, 501, 714, 824, 1038
    subs = [(x1, y1, x2, y2), (x3, y1, x4, y2), (x5, y1, x6, y2),
            (x1, y3, x2, y4), (x3, y3, x4, y4), (x5, y3, x6, y4),
            (x1, y5, x2, y6), (x3, y5, x4, y6), (x5, y5, x6, y6)]
    res = []
    for x1, y1, x2, y2 in subs:
        string = pytesseract.image_to_string(
            im.crop((x1, y1 - 100, x2, y2)))
        for s in string.replace(' ', '\n').split('\n'):
            try:
                res.append(float(s))
                break
            except BaseException:
                pass
    return res


if __name__ == "__main__":
    fn = input("")
    #  print(ocr(fn))
    print(fn, ocr_9zones(fn))
