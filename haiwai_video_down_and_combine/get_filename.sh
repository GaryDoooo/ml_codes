#!/bin/bash
IFS='/'
read -ra names <<< $1
echo "file "${names[-1]}
