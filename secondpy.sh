#!/bin/sh

if [ -z "$FIRST_NAME" ]; then 
	echo "FIRST_NAME enviroment value is missing, set it and try again"
fi 
if [ -z "$LAST_NAME" ]; then 
	echo "LAST_NAME enviroment value is missing, set it and try again"
fi 
if [ -z "$FIRST_NAME" ] || [ -z "$LAST_NAME" ]; then 
	exit 1
fi
python3 second.py

echo "The directories and txt files are successfully created" 

