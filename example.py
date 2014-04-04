__author__ = 'dell'
#coding=utf-8
import jieba
#encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
print "Full Mode:", "/ ".join(seg_list) #全模式

seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print "Default Mode:", "/ ".join(seg_list) #默认模式

seg_list = jieba.cut("他来到了网易杭研大厦")
print ", ".join(seg_list)

# import aiml
# import re
# k = aiml.Kernel()
# k.learn("cn-startup.xml")
# k.respond("load aiml cn")
# while True:
#     print k.respond(raw_input("> "))

# query=raw_input("您说：")
# #以下为手工建立的问答库模板
# pattern=re.compile("你.*叫[啥|什么].*")
# match=pattern.match(query)
# if match:
#     print 'robot说：',
#     print '我是牛亚坤！'
#     # query=query.split()+cilin(query)
#     # print len(cilin(query))
#     # for i in cilin(query):
#     #     print i