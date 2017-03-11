# Report on Assignment 1
######Niu Xingzhi, 2014011313
I. Type of Attributes
---
	-Military Rank: Ordinal (Discrete, Quantitative)
    -IP Address: Nominal (Discrete, Qualitative, Incomparable)
    -Duration of a program: Ratio (Continuous, Quantitative, Multipliable)
    -Birthday: Interval (Quantitative, Unmultipliable)
    -Programming Language: Nominal (Discrete, Quantitative, Incomparable)
    -Number of papers released: Ratio (Quantitative, Multipliable)

II. Data Representation
---
	i. Representation of Documents
    	To get the tf-idf vectors of each document, we should first construct a dictionary involving following information: the wordbank which contains each word, and where and how many times it occurs. I parse the documents first. Some simple techniques are applied in order to avoid special symbols like "/n" or "''". Regular expression is used to split the whole passage into a word list. I use a list "wordlist" to contain all words which exist in the corpus. Another list "wordindex" is a list of list like that:
~~~python
        	word = wordlist[i]
        	wordindex[i] = [(the first doc word exists , times it occurs in the doc), (the second doc word exists, times ...), ... ]
~~~
---
		After a document parsed, the total word count of the document is calculated for the usage in idf. That information is collected and output in files like "dictionary.xml" and "pagelength.txt".