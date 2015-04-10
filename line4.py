#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:55:43 2015

@author: tim
"""

from grs import RealtimeWeight #股票model
from line import  LineClient, LineGroup, LineContact # Line API model
from datetime import datetime
import time


from twseopen import TWSEOpen
from datetime import datetime
from tw_time import TWTime
import os



open_or_not = TWSEOpen()
open_or_not.d_day(datetime.today())        # 判斷今天是否開市
                                           # 回傳 True or False
open_or_not.d_day(datetime(2012, 12, 22))  # 判斷 2012/12/22 是否開市
csv_path = os.path.join(os.path.dirname(__file__), 'opendate.csv')


for i in open('authToken.txt'):
     ID = i
	
try:
     z = LineClient(authToken=ID)
        # 登入後的authToken
except:
     print "Login Failed"
     

friend_group = z.groups[6]  # group 的位置
print friend_group #friend = z.contacts[34]  # friend 的位置


i = 0 
while i < 2:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M")

    realtime_weight = RealtimeWeight()  # 擷取即時大盤資訊
    t00_tw = realtime_weight.data

    """
    print t00_tw['t00']['open'] #開盤價
    print t00_tw['t00']['price'] #目前大盤加權指數
    print t00_tw['t00']['volume_acc'] #目前大盤成交量
    print t00_tw['t00']['diff'][0] #漲跌
    print t00_tw['t00']['diff'][1] #幅度
    """

    price =  t00_tw['t00']['price'] #目前大盤加權指數
    price = str(price) #目前大盤加權指數

    volume_acc = t00_tw['t00']['volume_acc'] #目前大盤成交量
    volume_acc = volume_acc/100
    volume_acc = str(volume_acc) #目前大盤成交量

    diff_0 = t00_tw['t00']['diff'][0] #漲跌
    diff_0 = str(diff_0) #漲跌

    diff_1 = t00_tw['t00']['diff'][1] #幅度
    diff_1 = str(diff_1) #幅度

    msg1 = time_now+"\n"+"加權指數："+price+ "\n"  +\
    "       漲跌："+ diff_0+ "\n"  +"       幅度："+\
    diff_1+"%"+ "\n" +"    成交量："+ volume_acc+"億"
    
    friend_group.sendSticker("13")
    friend_group.sendMessage(msg1)
    
    '''
    friend.sendSticker("13")
    friend.sendMessage(msg1)
    '''
    
    time.sleep(10)
    print i
    i+=1
