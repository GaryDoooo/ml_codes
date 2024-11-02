import pandas as pd
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
############# Own modules ############
from double_line_single import double_line, enhance


def split_Xs(img_filename, csv_filename,
             pdf_file="output23.pdf"):
    df = pd.read_csv(csv_filename)

    image = cv2.imread(img_filename, cv2.IMREAD_ANYDEPTH)
    image = image.astype('float32')

    a = image

    g_crosshairs = eval(df.loc[df['ParameterName'] == 'green_mtfgmp_Y_gmp12G_corners_M2']['TestValue'].values[0])

    pdf = PdfPages(pdf_file)
    for x, y in g_crosshairs:
        sub = a[y - 80:y + 80, x - 80:x + 80]
        sub = enhance(sub)
        plt.imshow(sub, cmap='gray')
        res = double_line(sub)
        if res is not None:
            plt.title("lvl=%d score=%.2f ad=%.2f sk=%.2f d1=%.2f d2=%.2f oc=%.2f" % (
                res['lvl'], res['score'], res['AD'], res['Skewness'],
                res['D1'], res['D2'], res['offCenter']))
        else:
            plt.title('Error.')
        pdf.savefig()  
        plt.close()

    pdf.close()

    return


if __name__ == "__main__":
    split_Xs("2Y0Y3B1XSDG8Q002H_G.tiff", "2Y0Y3B1XSDG8Q002H.csv")
