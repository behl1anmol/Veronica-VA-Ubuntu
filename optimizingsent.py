from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from maps import mapopen

st=StanfordNERTagger('/home/anmol/VA/Documents/VLOG/std/classifiers/english.all.3class.distsim.crf.ser.gz',
						'/home/anmol/VA/Documents/VLOG/std/stanford-ner.jar',encoding='utf-8')

def fetch(text):
	temp=''
	words=word_tokenize(text)
	classified_text=st.tag(words)
	print(classified_text)
	for i in range(len(classified_text)):
		if(classified_text[i][1]=='LOCATION' or classified_text[i][1]=='ORGANIZATION'):
			temp=temp + classified_text[i][0] + ' '
	print(temp)
	return temp

#fetch('i live in Krishna Institute Of Engineering And Technology')	

