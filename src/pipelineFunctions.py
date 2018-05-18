"""

Here the functions for the pipeline are defined.

"""
from nltk.tokenize.toktok import ToktokTokenizer


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
	def featex(data):
		res = [];
		for d in data:
			feat_dict = {};

			for w in d[0]:
				feat_dict[w] = 1;
			
			res = res + [(feat_dict, d[1], d[2])];

		return res;

	return featex;

def labelSelection_stance2():
	def labelsec(data):
		return [(d[0], d[1][0]) for d in data];

	return labelsec;
	

