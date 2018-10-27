from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
from autocorrect import spell


tagged=[]
sentence=[]

def content(ct):
	try:
		ct1=''
		tagged=[]
		sentence=[]
		ct2=''
		ct1=word_tokenize(ct)
		print(ct1)
		tagged=nltk.pos_tag(ct1)
		print(tagged)
		#print(tagged[1])
		for i in range(len(tagged)):
			if tagged[i][1]!='NNP':
				sentence.append(spell(ct1[i]))
			else:
				sentence.append(ct1[i])	
		ct2=' '.join(map(str,sentence))
		ct2=ct.lower()
		print(ct2)	
	except Exception as e:
		print(str(e))
	return ct2		

#content('i am Anmol please open terminul')				