import sys

reader = open('train.tsv', 'r' )


SET = 1

for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	s1 = int(line[2])
	text = line[4]
	print('Id:\t%d' % Id)	
	print ("\n") 
	print ('Score:\t%d' % s1)
	print ("\n")
	print ('Text:\t%s' % text)
	print ("\n")
		


