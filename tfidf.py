from dictionary_building import *
from bs4 import BeautifulSoup
import math

def tfidf_build(wordlist,wordindex,wordcount,pagelength):
    vector=([])
    matrix=([])
    d=len(pagelength)
    for i in range(d):
        vector=([])
        for j in range(wordcount):
            vector.append(float(0.0))
        matrix.append(vector)
        del(vector)
    for i in range(wordcount):
        for pagetuple in wordindex[i]:
            doc=pagetuple[0]
            n=pagetuple[1]
            l=pagelength[doc]
            tf=float(n)/float(l)
            j=len(wordindex[i])
            idf=math.log(float(d)/float(j))
            tfidf=tf*idf
            matrix[doc][i]=tfidf
        #print("Word "+str(i)+"  "+wordlist[i]+" calculated.")
    return matrix

if __name__=='__main__':
    parsetuple=document_parse()
    wordlist=parsetuple[0]
    wordindex=parsetuple[1]
    wordcount=parsetuple[2]
    pagelength=parsetuple[3]
    matrix=tfidf_build(wordlist,wordindex,wordcount,pagelength)
    s=""
    f=open("tf_idf_matrix.txt","w")
    i=0
    for vector in matrix:
        s=s+"["
        for value in vector:
            s=s+str(value)+","
        print("Document "+str(i)+" data collected.")
        i=i+1
        s=s+"],"
    f.write(s)
    f.close()
