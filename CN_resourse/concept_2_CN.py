# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 读取本体中的概念及元素，翻译为中文。
@DateTime: Created on 2018/3/12, at 下午 02:48 by PyCharm '''
import requests as rq
from bs4 import BeautifulSoup as bs
import time, random

concept_list = []
my_dic = {}
with open('D:/CS资料/ONTOLOGY/ENGLISH/adjectivehierarchy.top', 'r', encoding='utf-8')as fin:
    data = fin.readlines()
    full_line = ''
    for line in data:
        line = line.strip()
        if not line:
            continue
        if line.startswith('##<<'):
            if line.__contains__('##>>'):
                concept_list.append(line[22:-5])
                full_line = ''
            else:
                full_line += line[22:]
        else:
            if line.__contains__('##>>'):
                full_line += line[:-5]
                concept_list.append(full_line)
                full_line = ''
            else:
                full_line += line

print('动词概念数量：', len(concept_list))
sentences = [a.replace('(', ' ').replace(')', ' ') for a in concept_list]


def get_CN(word):
    full = ''
    try:
        url = 'http://www.iciba.com/' + word
        r = rq.get(url)
        soup = bs(r.text, 'lxml')
        tag = soup.find('li', class_='clearfix')
        meanings = tag.select('span')
        for mean in meanings[1:]:
            full += mean.getText().strip().replace(' ', '')
        my_dic[word] = full
    except:
        pass
    print(word + full)
    return word + full


with open('D:/cn_adj.txt', 'a', encoding='utf-8')as fo:
    for sen in sentences:
        word_li = sen.split()  # 切分为单词列表。
        print(word_li)
        for word in word_li:
            if word in my_dic.keys():
                fo.write(word+my_dic.get(word))
            else:
                fo.write(get_CN(word))  # 对每个单词作出翻译。
                time.sleep(random.uniform(0.2, 1.3))
            fo.write('\t')
        fo.write('\n')
