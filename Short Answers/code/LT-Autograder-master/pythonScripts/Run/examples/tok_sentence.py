import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


#f = open("test.txt")

def split(answer):
	text=answer
	sents =tokenizer.tokenize(text)
	return sents

data="The PunktSentenceTokenizer class learns from any string, which means you can open a text file and read its content. Here is an example of reading overheard.txt directly instead of using the raw() corpus method."
arr=split(data)
size=len(arr)
print(arr)
print("________________________\n")
print(text2)
print("________________________\n")
print(text3)
print("________________________\n")
#print '\n-----\n'.join(tokenizer.tokenize(data))



