# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:32:53 2015

@author: tim
"""



from twseopen import TWSEOpen
from datetime import datetime
from tw_time import TWTime
import os


open_or_not = TWSEOpen()

open_or_not.d_day(datetime.today())        # 判斷今天是否開市
                                           # 回傳 True or False
open_or_not.d_day(datetime(2012, 12, 22))  # 判斷 2012/12/22 是否開市

csv_path = os.path.join(os.path.dirname(__file__), 'opendate.csv')

if open_or_not.d_day(datetime.today()):
    print u"今天開市"
else:
    print u"今天休市"