__author__ = 'dell'
fin = open('comment936_nopunction&nostopwords.txt')
fou = open('reduce10000.txt','w')
fou2 = open('reduce20000.txt','w')
num=0

for line in fin.readlines():
    num+=1
    if num<10000:
        fou.write(line)
    if num<20000:
        fou2.write(line)

fin.close()
fou.close()
fou2.close()


