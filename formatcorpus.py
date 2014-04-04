#!/usr/bin/python
#coding=utf-8
__author__ = 'dell'
import re
pattern=re.compile(u'【 在.*的大作中提到.*')
fin=open('niuyakun.txt')
fout=open('comment936.txt','w')
for line in fin.readlines():
    line=line.decode('utf-8')
    line=line.split(u'\u0001')
    resultq,number=pattern.subn('',line[0])
    resulta,number=pattern.subn('',line[1])
    if len(resultq)>1:
        fout.write(resultq.encode('utf-8')),
        fout.write(u'\u0001')
        fout.write(resulta.encode('utf-8'))
    else:
        continue


fin.close()
fout.close()