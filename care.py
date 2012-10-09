#!/usr/bin/env python
#-*-coding:utf-8-*-
#=======================================
# Author: liuzhida - liuzhia@meituan.com
# Last modified: 2012-09-07 15:58
# Filename: ai.py
# Description: 
#=======================================
import urllib2
import redis
f = urllib2.urlopen(url = 'http://www.7timer.com/v4/bin/civillight.php?lon=116.407&lat=39.904&ac=0&unit=metric&output=json&tzshift=0',)
data =  f.read()
json = eval(data)
temp1 = json['dataseries'][0]['temp2m']['max']
temp2 = json['dataseries'][0]['temp2m']['min']
temp3 = json['dataseries'][1]['temp2m']['max']
temp4 = json['dataseries'][1]['temp2m']['min']
wind1 = json['dataseries'][0]['wind10m_max']
wind2 = json['dataseries'][1]['wind10m_max']
weather = json['dataseries'][1]['weather']
temp = temp1-temp3
wind = wind1 -wind2
string = "明天"
flag = 0
if temp >= 3:
    string = string + "降温%s度，添件衣服吧"%temp
    flag = 1
if wind1 > 5 and wind <= -3:
    string = string + "风力%s级，添件衣服吧"%wind2
    flag = 1
if "rain" in weather:
    string = string + "有雨，记得带伞哦"
    flag = 1
if "snow" in weather:
    string = string + "有雪，记得带伞哦"
    flag = 1
if "storm" in weather:
    string = string + "有暴风雨，记得带伞哦"
    flag = 1
if "shower" in weather:
    string = string + "局部地区有小雨，记得带伞哦"
    flag = 1

print string
#r=redis.Redis(host='127.0.0.1',port=6379,db=0)
#phone_li = r.keys("weather:*")
#if flag == 1:
#    for i in phone_li:
#        phone = i.split(':')[1]
#        sms = r.get(i)
#        sms = sms.replace("{weather}",string)
#else:
#    exit 
