#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:55:43 2015

@author: tim
"""

from line import  LineClient, LineGroup, LineContact # Line API model
from datetime import datetime
from random import randint
import time

for i in open('authToken.txt'):
     ID = i
	

try:
     z = LineClient(authToken=ID)
        # 登入後的authToken
except:
     print "Login Failed"
     

friend_group = z.groups[6]  # group 的位置
print friend_group #friend = z.contacts[34]  # friend 的位置

#i = randint(1,9)
# 表情符號ID為1~17

i = 1 
while i < 2:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    k = randint(1,9)

    
    friend_group.sendMessage(str(k))
    friend_group.sendSticker(str(k))
    friend_group.sendMessage(time_now)
        
    time.sleep(5)
    print i
    i+=1
