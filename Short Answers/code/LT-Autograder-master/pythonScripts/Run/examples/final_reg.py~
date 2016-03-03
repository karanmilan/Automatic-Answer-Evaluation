import collections, re

import reg1,reg2
import sys

#To read all the inputs from the file
reader = open('train.tsv', 'r' )
SET = 1
count1= 0
count0=0
exp = []
exp=reg1.reg()
exp2 =[]
exp2=reg2.reg()
ans= [ ]
for row in reader:
	student = {}
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	s1 = int(line[2])
	s2 = int(line[3])
	text = line[4]	
	student["id"]  = Id
	student["score1"]= s1
	student["score2"]=s2
	student["text"]=text
	student["sen1"]=text	
	student["sen2"]=text
	student["sen3"]=text
	student["sen4"]=text
	ans.append(student)
	
	#if((s1>0)|(s2>0)):
	#	count0=count0+1
	#	for reg in exp:
	#		if(re.match(reg,text)):
	#			print(reg)
	#			print("\n")
	#			print(Id)
	#			print(text)
	#			count1=count1+1
	#			print('-----------------------------------------\n')

	'''for reg in exp:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count1=count1+1;
		
		for i in exp:					 
		if any(regex.match(text) for regex in exp):
			print('Id:\t%d' % Id)'''
		 
	#if any(regex.match(text) for regex in exp):
	#	print ('Some regex matched!')
	#	print('Id:\t%d' % Id)	
	#	print ("\n") 
	#	print ('Score:\t%d' % s1)
	#	print ("\n")
	#	print ('Text:\t%s' % text)
	#	print ("\n")'''

#if(regex.match(es) for regex in exp):
#	print("It has matched\n")
#	print(exp[regex])'''

print(ans)
print (count1)
print (count0)

'''SET=2
count2=0
for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	text = line[2]
	#print(Id)
	print("\n")
	for reg in exp2:
		if(re.match(reg,text)):
			#print("\n")
			#print(text)
			#print("-----------------\n")
			count2=count2+1;
print(count2)'''	
