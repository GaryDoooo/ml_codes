from urllib.parse import urlparse
import requests
import argparse


def iterate_url(link):
    if link.split(".")[-1] in ['ts']:
        print(link)
    else:
        o = urlparse(link)
        urlhead = o.scheme + "://" + o.netloc
        reading = requests.get(link)
        for each_line in reading.text.split("\n"):
            if len(each_line) > 0:
                if each_line[0] == "/":
                    iterate_url(urlhead+each_line)


def dispatch(link):
    try:
        iterate_url(link)
    except:
        print("An exception occurred")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--link',
                        default="no input",
                        type=str,
                        help='The Haiwai.tv MacPlayer.PlayUrl value.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
