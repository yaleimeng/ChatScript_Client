# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/3/26, at 上午 08:47 by PyCharm '''

import requests as rq
from bs4 import BeautifulSoup as bs
import time, random


def get_CN(word):
    full = ' '
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


if __name__ == '__main__':
    my_dic = {}
    filename = 'D:/material40.tbl'  # 修改这里的文件名即可
    outfile = 'D:/yanse.txt'
    with open(filename, 'r')as fin:
        data = fin.readlines()

    with open(outfile, 'a', encoding='utf-8')as fout:
        for sen in data:
            sen = sen.strip()
            sen = sen.replace('[', '').replace(']', '').replace('"', '')
            if not sen :      continue
            exit_condition = sen.startswith('table:') or sen.startswith('^') or sen.startswith('DATA:') or sen.startswith('#')
            if exit_condition:
                fout.write( sen + '\n')
                continue
            else:
                fout.write('#'+sen + '\n')
            sen = sen.replace('[', '').replace(']', '').replace('"', '')
            word_li = sen.split()  # 切分为单词列表。
            print(word_li)
            for word in word_li:
                if word in my_dic.keys():
                    fout.write(word + my_dic.get(word))
                else:
                    fout.write(get_CN(word))  # 对每个单词作出翻译。
                    time.sleep(random.uniform(0.2, 0.6))
                fout.write(' ')
            fout.write('\n')
