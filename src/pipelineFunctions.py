"""

Here the functions for the pipeline are defined.

"""
from nltk.tokenize.toktok import ToktokTokenizer
from nltk import FreqDist;


#define tokenizer
def tokenizer1():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1][0])]; #change here the second number for gender/stance

		return res;

	return exToken;

def cleaner1():
	return lambda x : x;

def featureEx1():
	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				feat_dict[w] = 1;

			res = res + [(feat_dict, d[1])];

		return res;

	return featex;



####################GENDER#######################

def tokenizer_gender():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1][1])];

		return res;

	return exToken;
def cleaner_gender():
	return lambda x : x;

def featureEx_gender():
	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				feat_dict[w] = 1;
			
			res = res + [(feat_dict, d[1])];

		return res;

	return featex;

def tokenizer_gender2():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1], d[2])]; 

		return res;

	return exToken;

def cleaner_gender2():
	return lambda x : x;

def featureEx_gender2():
	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				feat_dict[w] = 1;
			
			res = res + [(feat_dict, d[1], d[2])];

		return res;

	return featex;

def labelSelection_gender2():
	def labelsec(data):
		return [(d[0], d[1][1]) for d in data];

	return labelsec;

#####################STANCE########################
def tokenizer_stance():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1][0])]; 

		return res;

	return exToken;
def cleaner_stance():
	return lambda x : x;

def featureEx_stance():
	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				feat_dict[w] = 1;
			
			res = res + [(feat_dict, d[1])];

		return res;

	return featex;

"""
Vol. 2
"""

def tokenizer_stance2():
	toktok = ToktokTokenizer();

	def exToken(data):
		res = [];
		for d in data:
			res = res + [(toktok.tokenize(d[0]), d[1], d[2])]; 

		return res;

	return exToken;

def cleaner_stance2():
	return lambda x : x;

def featureEx_stance2():
	filer = open("../corpora/espanol_stopwords.txt");
	stopwords = set();
	for l in filer:
		stopwords.add(l);

	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				#if not w.lower() in stopwords:
				feat_dict[w.lower()] = 1;
			
			res = res + [(feat_dict, d[1], d[2])];

		return res;

	return featex;

def featureEx_stance2_vol2():
	def featex(data):
		res = [];
		
		for d in data:
			fdist = FreqDist(w.lower() for w in d[0]);
			words = fdist.most_common(100)[5:];

			feat_dict = {w : fdist[w] for w in words};
			
			res = res + [(feat_dict, d[1], d[2])];

		return res;

	return featex;

def labelSelection_stance2():
	def labelsec(data):
		return [(d[0], d[1][0]) for d in data];

	return labelsec;
	

