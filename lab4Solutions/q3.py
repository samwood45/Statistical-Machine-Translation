import sys 
'''

def CorpBigrams(input_file):
	f = open(input_file, "r")
	corpus = f.readlines()
	CBigrams = []
	for sentence in corpus:
		for i in range (len(sentence.split())-1):
			CBigrams.append(sentence.split()[i:i+2])
	return CBigrams

def SentBigrams(s):
	SBigrams = []
	for i in range (len(s.split())-1):
		SBigrams.append(s.split()[i:i+2])
	return SBigrams

def biGramProb(input_file, sentence):
	biGramCorps = CorpBigrams(input_file)
	biGramSent = SentBigrams(sentence)
	ProbAns = 1
	for word in biGramSent:
		biGramCount = biGramCorps.count(word)
		biGramMatch = 0
		for word1 in biGramCorps:
			if word[0] == word1[0]:
				biGramMatch += 1
		ProbAns *= (float(biGramCount))/(float(biGramMatch))
	return ProbAns



s = "the cat sat on the mat"
#print (CorpBigrams(sys.argv[1]))
#print (SentBigrams(s))

print(biGramProb(sys.argv[1], s))
'''

def SentBigrams(sentence):
	SentBigrams = []
	for i in range(len(sentence.split())-1):
		SentBigrams.append(sentence.split()[i:i+2])
	return SentBigrams

def CorpBigrams(input_file):
	f =  open(input_file, "r")
	corpus = f.readlines()
	CorpBigrams = []
	for sentence in corpus:
		for i in range(len(sentence.split())-1):
			CorpBigrams.append(sentence.split()[i:i+2])
	return CorpBigrams



def UnigramProb(input_file, sentence):
	CBigrams = CorpBigrams(input_file)
	SBigrams = SentBigrams(sentence)
	ans = 1
	for word in SBigrams:
		count = CBigrams.count(word)
		match = 0
		for word2 in CBigrams:
			if word[0] ==word2[0]:
				match += 1
		ans = ans * (float(count))/(float(match))
	return ans

def getVocab(input_file):
	f = open(input_file, "r")
	corpus = f.readlines()
	d = {}
	for sentence in corpus:
		for word in sentence.split():
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1

	print(d)

	

s = "the cat sat on the mat"

print (getVocab(sys.argv[1]))
