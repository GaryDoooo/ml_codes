#!/bin/bash

function geturl {
	TESTARG=$1 python3 - <<END
from urllib.parse import urlparse
import requests
from os import environ

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

try:
    iterate_url(environ.get('TESTARG'))
except:
    print("An exception occurred")

END
}

function replace {
	TESTARG=$1 python3 - <<END
from os import environ
i=environ.get('TESTARG')
# print(i)
# print("replace to:")
print(i.replace(i[i.find(".ts")+3],"|"))

END
}

function filter {
# does not work with xargs, generates signal 13 error
read filelink
echo "read from xargs: "$filelink
filename=$(echo $filelink | xargs -n1 -d '/' | xargs -n1 | grep .ts)
if [ ! -f $filename ]; then
    #echo "File not found!"
    # axel -a - n 20 $1
    printf '%s\n' $filelink
fi
}

# get output from python extracting links from the input HTML codes

# linklist=$(python3 geturl.py --link=$1 | head)
linklist=$(geturl $1)

# get date and time into a string as the output filename
randstring=$(date '+%Y-%m-%d-%H_%M_%S')
# tmpfile=$(mktemp /tmp/downhaiwai-script_"$randstring".XXXXXX)
output=$randstring".ts"
echo "output to $output"

# filelist=$(printf '%s\n' "${linklist[@]}" | xargs -n1 getfilename)
# getfilename ${linklist[1]}
# echo "${filelist[@]}"
# echo "${linklist[0]}"
filelist=$(echo $linklist | xargs -n1 -d '/' | xargs -n1 | grep .ts)

for i in {1..100}
do
	missinglist=''
	while read -r line; do
		filename=$(echo $line | xargs -n1 -d '/' | xargs -n1 | grep .ts)
		if [ ! -f $filename ]; then
				missinglist=$missinglist$line" "
		fi
	done <<< "$linklist"
	if [ "$missinglist" == '' ]; then
		break
	fi
	echo $missinglist | xargs -n1 -P5 axel -a -n 20
done

filepath=$(pwd)"/"
# while read -r line; do
#		echo "file "$line >> $tmpfile
# done <<< "$filelist" 

cat <(while read -r line; do cat $filepath$line; done <<< "$filelist") \
	> $output

# fileString=$(replace "${filelist[@]}")
# ffmpeg -f concat -safe 0 -i <(for f in ./*.wav; do echo "file '$PWD/$f'"; done) -c copy output.wav
#ffmpeg -f concat -safe 0 \
#	   	-i <(while read -r line; do echo "file "$filepath$line; done <<< "$filelist") \
#		-threads 0 -c copy  $output \
#		&& echo "${filelist[@]}" | xargs -n1 | xargs -n1 rm 

# rm "$tmpfile"

# ffmpeg -f concat -i filelist -c copy $output \
#	&& cat filelist | xargs -n2 bash -c 'rm ${1}'
