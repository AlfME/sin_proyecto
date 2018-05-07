#!/bin/bash
if [ -z "$1" ]; then exit 1; fi
LINE_COUNT=$(cat $1 | wc -l)

echo $LINE_COUNT
HALF_FILE_COUNT=$(($LINE_COUNT / 2))
echo $HALF_FILE_COUNT

START_OF_FILE=$(head -n $HALF_FILE_COUNT $1)
END_OF_FILE=$(tail -n $HALF_FILE_COUNT $1)

BASE_FILE_NAME=${1%.txt}

echo "$START_OF_FILE"	>> "${BASE_FILE_NAME}_first.txt"
echo "$END_OF_FILE"	>> "${BASE_FILE_NAME}_second.txt"
