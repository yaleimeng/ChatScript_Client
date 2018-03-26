# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2018
@desc: 
@DateTime: Created on 2018/3/19, at 下午 05:06 by PyCharm '''

with open('E:/cn_verb.txt', 'r', encoding='utf-8'
          )as fr, open('E:/chi_verb.top', 'a', encoding='utf-8')as fw:
    data = fr.readlines()  # 每一行是一条概念。有name和content两部分
    mid, end = ' (', ' ) ##>>\n'
    for sen in data:
        if not sen.split():  # 如果切分为空，找下一行
            continue
        head = '##<<ENGLISH concept: ~' + sen.split()[0]  # 概念话题头部。这里可以根据实际语言 修改。
        words = sen.split()[1:]  # 切分为单词列表。
        real = list(set(words))  # 注意要去除重复词条。
        real.sort(key=words.index)
        sentence = head + mid + ' '.join(real) + end
        print(sentence)
        fw.write(sentence)

    print('写入中文概念：',len(data),'条。')