# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:26:46 2015

@author: tim
"""

from line import LineClient, LineGroup, LineContact
f = open('../ID_PW.txt','r') #於前一個相對目錄中放置登入LINE帳號密碼,目的為了不再GitHub顯示出來.
ID = f.readline().strip('\n') #不包含換行符號\n
PW = f.readline().strip('\n')

client = LineClient(ID, PW)          

print client.authToken
authToken = client.authToken

fileopen = open('authToken.txt','w') #開啟檔案,w沒有該檔案就新增
fileopen.write(authToken)               #寫入 p的內容
fileopen.close()                #關閉檔案
"""
fileopen = open('ppp3.txt')
while True:             
    line = fileopen.readline()  #讀寫一行
    if len(line) == 0:           #檢視是否有字串
        break
    print (line)
fileopen.close()
"""
