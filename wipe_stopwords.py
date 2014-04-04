__author__ = 'dell'
def stop_list():
    stop_words=[]
    f_stopwords=open('stop_words.txt')
    for line in f_stopwords.readlines():
        line=line.replace('\n','')
        stop_words.append(line.decode('cp936'))
    f_stopwords.close()
    return stop_words