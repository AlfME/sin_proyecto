"""

Here the functions for the pipeline are defined.

"""

#define tokenizer
def tokenizer1():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1][0])]; #TODO change

		return res;

	return exToken;

def cleaner1():
	return lambda x : x;

def featureEx1():
	def featex(data):
		res = [];
		for d in data:
			for w in d[0]:
				res = res + [({w : 1}, d[1])]

		return res;

	return featex;

