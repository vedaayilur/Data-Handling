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
