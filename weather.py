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
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
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
print weather
weather = "lightrain"
string = u"今天的最高温度是%s，"%temp1
if temp >= 3:
    string = string + u"明天降温%s度，"%temp
if wind1 > 5 and wind <= -3:
    string = string + u"明天风力%s级，"%wind2
if "rain" in weather:
    string = string + u"明天有雨，"
if "snow" in weather:
    string = string + u"明天有雪，"
if "storm" in weather:
    string = string + u"明天有暴风雨，"

string = string + u"注意天气，关心亲人"
phone = 18626891201
print string
#urllib2.urlopen(url = "http://cf.lmobile.cn/submitdata/service.asmx/g_Submit?sname=dlzhuoyc&spwd=bkuCMRZ8&scorpid=&sprdid=1012818&sdst=%s&smsg=%s"%(phone,string), )
