#!/bin/sh
export DISPLAY=:0
cd /home/kuba/Documents/projects/checkMin8
echo 'Activating venv'
. venv/bin/activate

START=$(/bin/date +%s)
while ! python3 main.py; do
	DIFF=$(( $(date +%s) - $START ))
	echo 'In a loop for ', $DIFF, ' seconds'
	if [ $DIFF -ge 3600 ]
	then
		break
	fi
    sleep 15
done
echo 'got menu'
echo 'deactivating venv'
deactivate
echo 'running gedit'
gedit /tmp/menu.txt
