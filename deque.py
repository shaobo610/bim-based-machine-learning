# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:03:53 2020

@author: striver
"""

from collections import deque
d=deque()
d=deque(['a','b','c'])
#d.appendleft
#d.extendleft
#d.insert()
#d.popleft()
d.clear()

#限制最大长度
d=deque([],maxlen=4)
for i in range(10):
    d.append(i)