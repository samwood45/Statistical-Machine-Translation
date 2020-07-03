import sys
'''
def frequency(inp_file):
	corpus = open(inp_file, "r")
	corpus = corpus.readlines()
	
	#print(corpus)
	for word in corpus:
		corpus =word.lower().split()
	NOM = len(corpus)
	#print(corpus)
	d = {}
	for word in corpus:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	for word in d:
		d[word] = d[word]/NOM
	return d


def uniProb(sentence, inp_file):
	d = frequency(inp_file)
	ans = 1
	for word in d:
		if word in sentence:
			ans *= d[word]
	return ans

s = "a cat sat on the mat"
print (uniProb(s, sys.argv[1]))

'''
def frequency(inp_file):
	f = open(inp_file, "r")
	corpus = f.readlines()
	li = []
	d = {}
	for word in corpus:
		li.append(word.split())
	for sentence in li:
		for word in sentence:
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1
	print (d)
	NOM = 0
	for sentence in li:
		for word in sentence:
			NOM += 1
	print(NOM)

	print(corpus)

print(frequency(sys.argv[1]))