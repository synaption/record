#!/bin/bash

sudo apt install sox -y

touch /dev/shm/test.wav
touch /dev/shm/test.raw

python3 -m venv env
source env/bin/activate
pip install pyalsaaudio
