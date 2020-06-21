#!/usr/bin/env python3
import urllib3
import subprocess
#host = subprocess.check_output('hostname', shell=True)
#http = urllib3.PoolManager()
from time import sleep
import os
os.chdir('/home/pi_weather/PIGPIO')
import pigpio
pi = pigpio.pi()
import DHT22
    

while True:
    s = DHT22.sensor(pi, 4)
    s.trigger()
    sleep(2)
    temp = '{:3.2f}'.format(s.temperature() / 1.)
    humi = '{:3.2f}'.format(s.humidity() / 1.)
    calibration = 0
    temp = str(float(temp) + calibration)
    print(f"Temp: {temp}C, Humidity: {humi}%")
    
 
#query = "http://192.168.1.5/push_temp.php?temp="+temp+"&humi="+humi+"&hostname="+host
#query = query.replace('\n', ' ').replace('\r', '').replace(' ', '')
#page = http.request('GET', query)
