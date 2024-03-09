#!/usr/bin/env python
#python record21.py -d dmic_sv /home/pi/record/test.raw

from datetime import datetime
from datetime import timezone
from datetime import timedelta
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo
import os

import sys
import time
import getopt
import alsaaudio
import random
import subprocess
import shutil
import traceback
import glob


def usage():
    print('usage: recordtest.py [-d <device>] <file>', file=sys.stderr)
    sys.exit(2)

def read_data_from_device(inp, f):
    # Read data from device
    l, data = inp.read()
    if l:
        f.write(data)
    time.sleep(.001)
  

if __name__ == '__main__':
    os.chdir("/dev/shm")

    device = 'default'

    opts, args = getopt.getopt(sys.argv[1:], 'd:')
    for o, a in opts:
        if o == '-d':
            device = a

    if not args:
        usage()

    f = open(args[0], 'wb')
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, 
        channels=2, rate=32000, format=alsaaudio.PCM_FORMAT_S32_LE, 
        periodsize=640, device=device)


    subprocess.run(["sox", "-n", "-r", "32000", "frame.raw", "trim", "0.0", "0.0"])
    subprocess.run(["sox", "-r", "32000", "-e", "unsigned", "-b", "32", "frame.raw", "frame.wav"])
    subprocess.run(["cp", "frame.wav", "template.wav"])
    subprocess.run(["rm", "out.wav"])
    subprocess.run(["mkdir", "-p", "/dev/shm/detect"])
    subprocess.run(["mkdir", "-p", "/dev/shm/past"])
    subprocess.run(["sudo", "chmod", "777", "/dev/shm/detect"])
    subprocess.run(["sudo", "chmod", "777", "/dev/shm/past"])
    now = datetime.now()
    next_time = (now + timedelta(seconds=1)).strftime("%H_%M_%S")
    current_time = now.strftime("%H_%M_%S")
    detect_time=current_time 

    while True:
        try:
            now = datetime.now()
            if now.strftime("%H_%M_%S")>next_time:
                now = datetime.now()
                current_time = now.strftime("%H_%M_%S")
                next_time = (now + timedelta(seconds=1)).strftime("%H_%M_%S")
                current_second = now.strftime("%S")[1]
                #print("Current Time =", current_time)
                if os.path.getsize(args[0]) > 3000:
                    #print(os.path.getsize(args[0]))
                    shutil.move("test.raw", "test1.raw")
                    f = open(args[0], 'wb')
                    detect_time=current_time
            read_data_from_device(inp, f)
            
                
        except Exception as e:  # Catch the exception and print the traceback
            traceback.print_exc()
            
