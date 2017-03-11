from dictionary_building import *
from tfidf import *
import math

def calc_euclid_dist(root,matrix):
    result=([])
    for vector in matrix:
        dist=float(0.0)
        for i in range(len(vector)):
            dist=dist+(vector[i]-matrix[root][i])*(vector[i]-matrix[root][i])
        dist=math.sqrt(dist)
        result.append(dist)
    return result

if __name__=='__main__':
    parsetuple=document_parse()
    wordlist=parsetuple[0]
    wordindex=parsetuple[1]
    wordcount=parsetuple[2]
    pagelength=parsetuple[3]
    matrix=tfidf_build(wordlist,wordindex,wordcount,pagelength)
    root=0
    result_vector=calc_euclid_dist(root,matrix)
    for i in range(len(result_vector)):
        mindist=float(9999998.0)
        minpos=-1
        for j in range(len(result_vector)):
            if result_vector[j]<mindist:
                minpos=j
                mindist=result_vector[j]
        print("The nearest "+str(i)+" document is No."+str(minpos)+" with distance of "+str(mindist))
        result_vector[minpos]=float(9999999.0)
