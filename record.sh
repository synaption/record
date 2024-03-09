#!/bin/bash

#started by gsdRecord.service
su pi
mkdir /home/pi/record
cd /home/pi/record
python3 -m venv env
source env/bin/activate
pip install pyalsaaudio
sudo apt install sox -y

touch /dev/shm/test.wav;
touch /dev/shm/test.raw;

while true
do
  python /home/pi/record/record.py -d null /dev/shm/test.raw
done
