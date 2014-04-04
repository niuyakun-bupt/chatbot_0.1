#coding=utf-8
import jieba

__author__ = 'dell'
import re
p = re.compile(u'[^\u4e00-\u9fa5\t]+')
fpunctuation=open('comment936.txt')
# fpunctuation2=open('comment936_nopunction.txt','w')
for line in fpunctuation.readlines():
    line = line.decode('utf-8')
    line=line.split(u'\u0001')
    line[0]=p.sub(r'', line[0].strip())
    seg_list = jieba.cut(line[0])
    line[0]=' '.join(seg_list)
    fpunctuation2.write(line[0].encode('utf-8'))
    fpunctuation2.write(u'\u0001')
    fpunctuation2.write(line[1].encode('utf-8'))

fpunctuation2.close()
fpunctuation.close()