import collections, re

pats=[]
pats.append( re.compile(r"(\w+ ){0,100}((what)|(which)|(type of)|(conditions)) (\w* ){0,10}((drying)|(dry))\w*") )
#pats.append( re.compile(r"(\w+ ){0,30}((size)|(surface area)|) (\w* ){0,4}((material)|(materials)|(sample)|(samples)|(element)|(elements)|(cup)|(cups))\w*") )
#pats.append( re.compile(r"(\w+ ){0,30}((what)|(wat)|(which)|(wich)|(type of)|(kind of)|(name of)) (\w* ){0,4}((materia)?((l)|(s)))|((sampl)?((es)|(e)))(\w* ){0,4}(test)\w*") )
#pats.append( re.compile(r"(\w+ ){0,30}((type)|(kind)|(variety)|(brand)|(form)) (\w* ){0,4}((vinegar)|(vinigar)|(liquid))\w*") )
#pats.append( re.compile(r"(\w+ ){0,4}((how much)|(quantity)|(measur)?((ement)|(ing)|(e))|(amount)|(mass)) (\w* ){0,4}((vinegar)|(vinigar)|(liquid))\w*") )


#I'll tell you what each thing does in a regular expression
#(\w+) means there can be any number of words
#(\w*) there can be any no of words or spaces.
#{0,100} with (\w+) signifies there can be 0,100 words in between and words in brackets with or "|" symbol signify OR operation

text="Hi how are you the type of drying method used" #This regular expression will work.

text1 = "type of drying method used"# This regular expression will work 
text4=""
text2 = "Hey how are you. They type of drying method used" #This wouldnt work.
text5="the type of sample"
text6="the size of elements"


for reg in pats:

	if(re.match(reg,text)):
		print("matched text\n")

	if(re.match(reg,text1)):
		print("matched text1\n")
	if(re.match(reg,text2)):
		print("matched text2\n")
	if(re.match(reg,text4)):
		print("matched text4\n")
	if(re.match(reg,text5)):
		print("matched text5\n")
	if(re.match(reg,text6)):
		print("matched text6\n")
