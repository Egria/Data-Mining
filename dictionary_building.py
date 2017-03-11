import re

def document_parse():
    wordlist=([])
    wordindex=([])
    wordcount=0
    pagelength=([])
    p=re.compile("[A-Za-z0-9\-\']+")
    for i in range(300):
        f=open('nyt_corp0//'+str(i),'r')
        s=f.read()
        s=s.replace("/n"," ")
        s=s.replace("''","")
        s=s.replace("--","")
        wordbox=p.findall(s)
        pagelength.append(len(wordbox))
        for word in wordbox:
            word=word.lower()
            if not word in wordlist:
                wordlist.append(word)
                wordindex.append([]) #empty list
                pagetuple=[i,1]
                wordindex[wordcount].append(pagetuple)
                wordcount=wordcount+1
            else:
                position=wordlist.index(word)
                page_noted=False
                for j in range(len(wordindex[position])):
                    if wordindex[position][j][0]==i:
                        wordindex[position][j][1]=wordindex[position][j][1]+1
                        page_noted=True
                        break
                if not page_noted:
                    wordindex[position].append([i,1])
        f.close()
        #print("Document "+str(i)+" parsed.")
    return (wordlist,wordindex,wordcount,pagelength)

if __name__=='__main__':
    parsetuple=document_parse()
    wordlist=parsetuple[0]
    wordindex=parsetuple[1]
    wordcount=parsetuple[2]
    pagelength=parsetuple[3]
    f=open('dictionary.xml','w')
    s="<dictionary>"
    for i in range(wordcount):
        s=s+"<word>"
        s=s+"<entry>"+wordlist[i]+"</entry>"
        s=s+"<reference>"
        for pagetuple in wordindex[i]:
            s=s+"<document times='"+str(pagetuple[1])+"'>"+str(pagetuple[0])+"</document>"
        s=s+"</reference></word>"
        #print("Word "+str(i)+"  "+wordlist[i]+" recorded.")
    s=s+"</dictionary>"
    f.write(s)
    f.close()
    print("Dictionary output.")
    s=""
    f=open('pagelength.txt','w')
    for length in pagelength:
        s=s+str(length)+","
    f.write(s)
    f.close()
