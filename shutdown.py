#!/usr/bin/python
''' 
Filename: "shutdown.py"
author:   "knva"
date  :   "2017-03-16"
version:  "1.00"
'''
import os
import sys
import time
from time import strftime, localtime

Closingtime = "18:00:00";
nowTime =  time.strftime('%H:%M:%S',time.localtime(time.time()));

hourcha = int(Closingtime.split(':')[0]) - int(nowTime.split(':')[0]);
mincha = int(Closingtime.split(':')[1]) - int(nowTime.split(':')[1]);
seccha = int(Closingtime.split(':')[2]) - int(nowTime.split(':')[2]);
print("h%s , m:%s  , s:%s"%(hourcha,mincha,seccha));
shutdownsec = ((hourcha*60)+mincha)*60+seccha;

str_cmd = "shutdown -s -t %s"%(shutdownsec);
print(str_cmd);
os.system(str_cmd);