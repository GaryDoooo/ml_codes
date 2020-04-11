from urllib.parse import urlparse
import requests
from os import environ

file_index=0

def iterate_url(link):

    global file_index

    o = urlparse(link)
    filename = o.path.split("/")[-1].split("?")[0]
    file_index = file_index +1
    filename = str(file_index)+"____"+filename
    if filename.split(".")[-1] in ['ts']:
        print(link+" "+filename)
    else:
        urlhead = o.scheme + "://" + o.netloc
        in_server_path = o.path[:o.path.rfind("/")+1]
        reading = requests.get(link)
        for each_line in reading.text.split("\n"):
            if len(each_line) > 0:
                if each_line[0] != "#":
                    if each_line[0] == "/":
                        iterate_url(urlhead+each_line)
                    elif each_line.split(":")[0].lower() in ['http','https']:
                        iterate_url(each_line)
                    else:
                        iterate_url(urlhead+in_server_path+each_line)

try:
    iterate_url(environ.get('TESTARG'))
except:
    print("An exception occurred")
