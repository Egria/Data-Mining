from cooccurrence import *
from dictionary_building import *
from euclid_dist import *


if __name__=='__main__':
    parsetuple=document_parse()
    wordlist=parsetuple[0]
    wordindex=parsetuple[1]
    wordcount=parsetuple[2]
    pagelength=parsetuple[3]
    matrix=cooccurrence_matrix(wordindex,wordcount)
    root=0
    result_vector=calc_euclid_dist(root,matrix)
    for i in range(6):
        mindist=float(9999998.0)
        minpos=-1
        for j in range(len(result_vector)):
            if result_vector[j]<mindist:
                minpos=j
                mindist=result_vector[j]
        print("The nearest "+str(i)+" document is No."+str(minpos)+" with distance of "+str(mindist))
        result_vector[minpos]=float(9999999.0)
