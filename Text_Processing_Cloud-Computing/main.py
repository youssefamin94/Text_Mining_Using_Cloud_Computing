import string,re

#reading books
b1=open('book1.txt','r',encoding='utf-8')
book1=b1.read()
b2=open('book2.txt','r',encoding='utf-8')
book2=b2.read()

#removing extra whitespaces
book1=re.sub(' +',' ',book1)
book2=re.sub(' +',' ',book2)

#lowercasing the two books
book1=book1.lower()
book2=book2.lower()

#removing punctuation marks by using translate function cause it customize the dictionary (the output of str.maketrans function) into STRING
book1=book1.translate(str.maketrans('','',string.punctuation))
book2=book2.translate(str.maketrans('','',string.punctuation))

#find the commen words 
book1=set(book1.split())
book2=set(book2.split())

commenwords=book1.intersection(book2)
print(commenwords)