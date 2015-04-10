# -*- coding: utf-8 -*-
"""
列出朋友與群組的ID List
注意有可能每次朋友的ID List都會變化, 例如可能新加好友就會發生變化.
"""

from line import  LineClient, LineGroup, LineContact # Line API model

for i in open('authToken.txt'):
     ID = i
	

try:
     z = LineClient(authToken=ID)
        # 登入後的authToken
except:
     print "Login Failed"
     

# users的list
print u"朋友的ID List"
i = 0
while i < len(z.contacts):
    print i, z.contacts[i]
    i+=1

print '\n'

# Groups的list
print u"群組的ID List"
i = 0
while i < len(z.groups):
    print i, z.groups[i]
    i+=1
    
    
"""
測試用
friend_group = z.contacts[20]  # group 的位置
print friend_group 

i = 1 
while i < 18:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    friend_group.sendMessage(str(i))
    friend_group.sendSticker(str(i))
    friend_group.sendMessage(time_now)
        
    time.sleep(5)
    print i
    i+=1
"""    
