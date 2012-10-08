#!/usr/bin/env python
#-*-coding:utf-8-*-
#=======================================
# Author: liuzhida - liuzhia@meituan.com
# Last modified: 2012-09-11 01:10
# Filename: op.py
# Description: 
#=======================================
with open("bak.sms","r") as f:
   li = f.readlines() 
   for i in li:
      print i.split()[0]
      print i.split()[1:-1][0]
      print "=========="
