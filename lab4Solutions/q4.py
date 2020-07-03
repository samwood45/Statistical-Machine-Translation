import sys

s = "<s> a cat sat on the car </s>"

def getBigramsSent(sentence):
	bigramSent = []
	for i in range(len(sentence.split())-1):
		bigramSent.append(sentence.split()[i:i+2])
	return (bigramSent)

def getBigramsCorpus(input_file):
	corpus = readFile(input_file)
	bigramsCorp = []
	for sentence in corpus:
		for i in range(len(sentence.split())-1):
			bigramsCorp.append(sentence.split()[i:i+2])
	return (bigramsCorp)

def readFile(input_file):
	f = open(sys.argv[1], "r")
	corpus = f.readlines()
	return corpus
	
#this funtion gets the frequency of each word in the corpus	

def getVocab(input_file):
	wordDict={}
	corpus=readFile(input_file)
	#print(corpus)
	for sentence in corpus:
		for i in range (len(sentence.split())):
			if sentence.split()[i] not in wordDict:
				wordDict[sentence.split()[i]] = 1
			else:
				wordDict[sentence.split()[i]] += 1
	print (wordDict)
	'''
	for sentence in corpus:
		for i in range(len(sentence.split())):
			if sentence.split()[i] in wordDict:
				wordDict[sentence.split()[i]]+=1
			else:
				wordDict[sentence.split()[i]]=1
	return wordDict
'''
def bigramPSmoothing(sent, input_file):
 
	bigramsSentence=getBigramsSent(sent)
	bigramsCorpus=getBigramsCorpus(input_file)
	vocabDict=getVocab(input_file) #returns a dictionary of your corpus
	print (vocabDict)
	print (len(vocabDict))
	vocabCount=len(vocabDict) #take length of this vocabDict in
								#order to find the unique words
	totalBigramProb=1
	for bigramS in bigramsSentence:
		bigramCount=bigramsCorpus.count(bigramS)
		totalCount=0
		for bigramC in bigramsCorpus:
			if bigramS[0] == bigramC[0]:
				totalCount+=1
		totalBigramProb*=float(bigramCount+1)/float(totalCount+vocabCount)
	print(totalBigramProb)

#print (bigramPSmoothing(s, sys.argv[1]))
print(getVocab(sys.argv[1]))
