# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/4/18, at 上午 10:09 by PyCharm '''
import requests
from bs4 import BeautifulSoup as bs


# web = 'http://127.0.0.1:5000/'
web = 'http://im.openmoa.cn:5000/'
# {'userID':'abcd','question':'你的童年经历怎么样？', #用户id、问题内容。
# 'answer':'','belief':1.0,'block':'','Q_choice':[]} # 答案、置信度、语义块、备选疑似问题

myform =  {'userID':'abcd','question':'高新技术企业的研发费用有怎样的考核标准？', #用户id、问题内容。
        'answer':'','belief':1.0,'block':'','Q_choice':[]} # 答案、置信度、语义块、备选疑似问题

r = requests.post(web,myform,timeout=3)

print(r.json())