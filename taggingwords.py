from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
from autocorrect import spell

#
tagged=[]
sentence=[]

def content(ct):
	try:
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
		ct=' '.join(map(str,sentence))
		ct=ct.lower()
		print(ct)	
	except Exception as e:
		print(str(e))
	return ct		

#content('i am Anmol please open terminul')				