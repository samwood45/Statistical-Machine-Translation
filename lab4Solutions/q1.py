import sys
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

print (frequency(sys.argv[1]))

