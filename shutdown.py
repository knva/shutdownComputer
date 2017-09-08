#!/usr/bin/python
''' 注释
Filename: "shutdown.py"
author:   "knva"
date  :   "2017-03-16"
version:  "1.00"
'''
import os
import time,datetime
import psutil
dt = datetime.datetime.fromtimestamp(psutil.boot_time())
startHour = dt.strftime("%H")
startMin = dt.strftime("%M")
byebyetime = "18:00:00"
if(int(startHour)<9 and int(startMin)<40):
    byebyetime = "18:00:00"
else:
    byebyetime = "18:30:00"

if(datetime.datetime.now().weekday()==4):
    byebyetime = "16:30:00"
nowTime =  time.strftime('%H:%M:%S',time.localtime(time.time()))

hourcha = int(byebyetime.split(':')[0]) - int(nowTime.split(':')[0])
mincha = int(byebyetime.split(':')[1]) - int(nowTime.split(':')[1])
seccha = int(byebyetime.split(':')[2]) - int(nowTime.split(':')[2])
print("h%s , m:%s  , s:%s"%(hourcha,mincha,seccha))
shutdownsec = ((hourcha*60)+mincha)*60+seccha
cancelCmd = "shutdown -a"
str_cmd = "shutdown -s -t %s"%(shutdownsec)
print(str_cmd)
os.system(cancelCmd)
os.system(str_cmd)