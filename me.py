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
weather0 = json['dataseries'][0]['weather']
weather1 = json['dataseries'][1]['weather']
print weather0
print weather1
temp = temp1-temp3
wind = wind1 -wind2
string = "明天最高气温%s,风力%s"%(temp3,wind2)
flag = 0
if temp >= 3:
    string = string + "降温%s度，"%temp
    flag = 1
if wind1 > 5 and wind <= -3:
    string = string + "风力%s级，"%wind2
    flag = 1
if "rain" in weather1:
    string = string + "有雨，"
    flag = 1
if "snow" in weather1:
    string = string + "有雪，"
    flag = 1
if "storm" in weather1:
    string = string + "有暴风雨，"
    flag = 1
print string
#r=redis.Redis(host='127.0.0.1',port=6379,db=0)
#phone_li = r.keys("weather:*")
#print phone_li
#if flag == 1:
#    for i in phone_li:
#        print "============="
#        print i.split(':')[1]
#        phone = i.split(':')[1]
#        sms = r.get(i)
#        sms = sms.replace(u"{weather}",string)
#        #print sms
#        urllib2.urlopen(url = "http://cf.lmobile.cn/submitdata/service.asmx/g_Submit?sname=dlzhuoyc&spwd=bkuCMRZ8&scorpid=&sprdid=1012818&sdst=%s&smsg=%s"%(phone,sms), )
#else:
#    exit 
