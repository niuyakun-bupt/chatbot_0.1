__author__ = 'dell'
stop_words={}
f_stopwords=open('stop_words.txt')
for line in f_stopwords.readlines():
    line=line.replace('\n','')
    stop_words[line.decode('cp936')]=1
f_stopwords.close()

fin=open('comment936_nopunction.txt')
fout=open('reducecorpus/comment936_nopunction&nostopwords.txt','w')

j=0
for line in fin.readlines():
    print j
    line=line.decode('utf-8')
    line = line.split(u'\u0001')
    sentence=line[0].split()
    for s in sentence:
        if s in stop_words:
            sentence.remove(s)
    sentence=' '.join(sentence)
    fout.write(sentence.encode('utf-8'))
    fout.write(u'\u0001')
    fout.write(line[1].encode('utf-8'))
    j+=1
fin.close()
fout.close()
