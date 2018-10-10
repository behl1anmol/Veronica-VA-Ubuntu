import wolframalpha
import wikipedia
import requests
from AudioIO import speak
from settings import LOGO_PATH,veronica_notify


#creating instance of wolfram alpha
appId='APER4E-58XJGHAVAK'
client=wolframalpha.Client(appId)



#RESOLVING LIST OR DICTIONARY FOR WOLFRAM
def resolveListOrDict(variable):
	if isinstance(variable,list):
		return variable[0]['plaintext']
	else:
		return variable['plaintext']

#REMOVING PARENTHESIS FOR WOLFRAM
def removeBrackets(variable):
	return variable.split('(')[0]

#ENHANCING SEARCH RESULT WITH IMAGE
def primaryImage(title=''):
    url = 'http://en.wikipedia.org/w/api.php'
    data = {'action':'query', 'prop':'pageimages','format':'json','piprop':'original','titles':title}
    try:
        res = requests.get(url, params=data)
        #print("key")
        key = res.json()['query']['pages'].keys()[0]
        #print("image url")
        imageUrl = res.json()['query']['pages'][key]['original']['source']
        print(imageUrl)
    except Exception as err:
        print('Exception while finding image:= '+str(err))

#METHOD TO SEARCH WIKIPEDIA
def search_wiki(keyword=''):
	print('V.E.R.O.N.I.C.A :Trying Wikipedia')
	#running the query
	searchResults=wikipedia.search(keyword)
	#if no result,print no result
	if not searchResults:
		print("NO results found")
		return
	#Search for page... try block
	try:
		page=wikipedia.page(searchResults[0])
	except wikipedia.DisambiguationError as err:
		#selecting first item in list
		page=wikipedia.page(err.option[0])
	#encoding the response to utf-8
	wikiTitle=str(page.title.encode('utf-8'))
	wikiSummary=str(page.summary.encode('utf-8'))
	#printing result
	print(wikiSummary)
	speak('Here is your result')
	veronica_notify(wikiSummary)
#search_wiki(input())

def search(text=''):
	ret_answer=''
	print("V.E.R.O.N.I.C.A:Trying Wolframalpha")
	res=client.query(text)
	#wolfram cannot resolve the question
	if res['@success']=='false':
		print('NO RESULTS FOUND')
	#wolfram was able to resolve
	else:
		result=''
		#pod[0] is question
		pod0=res['pod'][0]
		#pod[1] may contain the answer
		pod1=res['pod'][1]
		#checking if pod1 has primary=true or title=result|definition
		if(('definition' in pod1['@title'].lower()) or ('result' in
			pod1['@title'].lower()) or (pod1.get('@primary','false')=='true')):
		#extracting results from pod1
			result=resolveListOrDict(pod1['subpod'])
			print(result)
			#speak(result)
			#veronica_notify(result)
			return(result)
		else:
		#extracting wolfram questions interpretation from pod0
			question=resolveListOrDict(pod0['subpod'])
		#removing unnecessary parenthesis
			question=removeBrackets(question)
		#searching for response from wikipedia
			ret_answer=search_wiki(question)

'''while True:
	q=input('V.E.R.O.N.I.C.A :')
	search(q)
	primaryImage(q)
#search(input())'''