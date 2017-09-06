#!/bin/sh
. venv/bin/activate

START=$(date +%s)
while ! python3 main.py; do
	DIFF=$(( $(date +%s) - $START ))
	if [ $DIFF -ge 3600 ]
	then
		break
	fi
    sleep 15
done
deactivate
gedit menu.txt
