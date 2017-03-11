from dictionary_building import *

def cooccurrence_matrix(wordindex,wordcount):
    vector=([])
    matrix=([])
    for i in range(wordcount):
        vector=([])
        for j in range(wordcount):
            vector.append(float(0.0))
        matrix.append(vector)
        del(vector)
    for i in range(wordcount):
        for j in range(wordcount):
            coor=0
            for tuple_a in wordindex[i]:
                for tuple_b in wordindex[j]:
                    if tuple_a[0]==tuple_b[0]:
                        coor=coor+1
            matrix[i][j]=coor
            matrix[j][i]=coor
        print("Word "+str(i)+" parsed.")
    return matrix
    

if __name__=='__main__':
    parsetuple=document_parse()
    wordlist=parsetuple[0]
    wordindex=parsetuple[1]
    wordcount=parsetuple[2]
    pagelength=parsetuple[3]
    matrix=cooccurrence_matrix(wordindex,wordcount)
    f=open('co_occurrence_matrix.csv','w')
    s="word_list,"
    for word in wordlist:
        s=s+word+","
    s=s+"\r\n"
    for i in range(len(wordlist)):
        s=s+wordlist[i]+","
        for j in range(len(wordlist)):
            s=s+str(matrix[i][j])+","
        s=s+"\r\n"
        print("Column "+str(i)+" recorded.")
    f.write(s)
    f.close()
