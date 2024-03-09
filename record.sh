#!/bin/bash

while true
do
  env/bin/python record.py -d null /dev/shm/test.raw
done
