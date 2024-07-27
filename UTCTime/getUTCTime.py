"""
This module at it's current version can generate log time at +0:00 UTC or GMT.
use the below import line to seamlessly used the two methods:
    # 1. getDate(): returns date DD-MM-YYYY
    # 2. getTime(): returns time HH:MM::SS\
    
use the below line to import the methods seamlessly:
    "from getUTCTime import getTime,getDate"

"""
import time as time_now

def getDate():
    time = time_now.gmtime()
    day = time.tm_mday
    month = time.tm_mon
    year = time.tm_year
    date = str(day)+"-"+str(month)+"-"+str(year)
    return date

def getTime():
    time = time_now.gmtime()
    hour = time.tm_hour 
    min = time.tm_min
    sec = time.tm_sec
    current_time = str(hour)+":"+str(min)+":"+str(sec)
    return current_time
