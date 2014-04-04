__author__ = 'dell'
#coding=utf-8
from logging import basicConfig, INFO
import gensim
from gensim import models, corpora
from gensim import similarities
import os
from math import log
import sys
import re
import aiml
import jieba
from wipe_stopwords import stop_list

# def cilin(word):
#     m = []
#     for ii in word:
#         for i in range(0, len(k)):
#             if ii in k[i]:
#                 for j in range(0, len(k[i])):
#                     if ii != k[i][j]:
#                         m.append(k[i][j])
#     return m


basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=INFO)
documents = []
users = {}#存储与机器人沟通过的用户
queries = []#存储每个用户的问题
choice = 0
stop_words=stop_list()#存储停用词

#以下是机器人资料初始化
# 姓名：诗诗
# 性别：女
# 职业：北邮在读大学生
# 籍贯：北京市
# 擅长语言：中文（不支持英文）
# 爱好：古诗词、古筝
resume = {}
resume['名字'] = '诗诗'
resume['性别'] = '女生'
resume['职业'] = '北邮的大学生'
resume['家乡'] = '北京'
resume['语言'] = '中文'
resume['爱好'] = '古诗词、古筝、舞蹈'
#以下是机器人资料初始化

# 以下原属于词林函数中部分，为了速度提出来了
f1 = open(r'hagongdatongyici.txt', 'r')
dd = f1.read()
dd = dd.split('\n')
k = []
for i in range(0, len(dd)):

    dd[i] = dd[i].split(' ')
    ee = []
    for j in range(1, len(dd[i])):
        ee.append(dd[i][j])
    k.append(ee)
# 以上原属于词林函数中部分，为了速度提出来了

#以下为手工建立的问答库模板
# QAtemplate = {}
# QAtemplate['你好'] = '你也好！'
# QAtemplate['你.*名字.*'] = '我的名字叫诗诗！很高兴认识你'
# QAtemplate['你.*性别.*'] = '我是一个' + resume['性别']
# QAtemplate['你.*职业.*'] = '我是一个' + resume['职业']
# QAtemplate['你.*[籍贯|家乡].*'] = '我是一个' + resume['家乡']
# QAtemplate['你.*[爱好|兴趣].*'] = '喜欢' + resume['爱好']
# QAtemplate['你.*叫[啥|什么].*'] = '我的名字叫诗诗！很高兴认识你'
k = aiml.Kernel()
k.learn("cn-startup.xml")
k.respond("load aiml cn")
#以上为手工建立的问答库模板

print 'step01'
#以下是处理水木数据模型
answers = []
f_text = open('reducecorpus/reduce20000.txt')
for line in f_text.readlines():
    line=line.decode('utf-8')
    line = line.split(u'\u0001')
    answers.append(line[1].encode('utf-8'))
    # document_list = jieba.cut(line[0].encode('utf-8'))
    # document_list=list(document_list)
    # document_sentence=' '.join(document_list)

    documents.append(line[0].encode('utf-8'))

print 'step02'
texts = [[word for word in document.lower().split()] for document in documents]
print len(texts)
print len(documents)
dictionary = gensim.corpora.Dictionary(texts)
dictionary.save('comment20000.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('comment20000.mm', corpus)
# corpus = corpora.MmCorpus('comment.mm')
# dictionary=corpora.Dictionary.load('comment.dict')



# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]#􀔕将上􀐺述用词频表示文档向量表示􀑪一个用tf-idf 值表示的文档向量
lda = models.LdaModel(corpus, id2word=dictionary, num_topics=50, update_every=0, passes=2)

# corpus_lsi = lsi[corpus_tfidf]
# for doc in corpus_lsi:
#     print 'doc:',
#     print doc
index = similarities.MatrixSimilarity(lda[corpus])
#以上是处理水木数据模型



# print 'robot说：',
# print '嗨，很高兴陪您聊天~你的名字是什么'
# query = raw_input("您说：")
# users[query] = []
# response=k.respond(query)
# if response:
#     print response
# else:
#     print query + '，很高兴陪您聊天~'
while (choice != '1'):
    match = None
    query = raw_input("您说：")
    choice = query
    queries.append(query)
    #以下为手工建立的问答库模板
    # for i in QAtemplate:
    #     pattern = re.compile(i)
    #     match = pattern.match(query)
    #     if match:
    #         print 'robot说：',
    #         print QAtemplate[i]
    #         break;
    #以上为手工建立的问答库模板
    # query=query.split()+cilin(query)
    # print len(cilin(query))
    # for i in cilin(query):
    #     print i
    response=k.respond(query)
    if response!='人家有点笨，不知道说什么了':
        print response
    else:
        seg_list = jieba.cut(query)
        query_list=list(seg_list)
        # print query


        #以下是去停用词
        for i in query_list:
            if i in stop_words:
                query_list.remove(i)
        #以上是去停用词


        query=' '.join(query_list)
        print query
        query_bow = dictionary.doc2bow(query.split())
        print 'query_bow' + str(query_bow)#将query映射到主题空间
        query_lda = lda[query_bow]
        sims = index[query_lda]

        sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
        print len(sort_sims)
        print "lsi结果："
        for i in range(3):#第一个最合适的回答
            print sort_sims[i][1],
            print 'robot说：',
            print documents[sort_sims[i][0]],
            print answers[sort_sims[i][0]]

users[query] = queries
print queries
print users

