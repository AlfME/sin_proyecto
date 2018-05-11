"""

The pipeline for realizing classification. Consists of a data pre-processing pipeline, a training
module for generating and storing classifiers and finally a procedure to load a defined classifer.

Generic pipeline structure:

1. Tokenization
2. Instance feature cleaning
3. Noise removal
4. Feature Extraction
5. Classification

"""

import nltk
import pickle

import nltk.classify.util
from nltk.classify import MaxentClassifier


class ClassificationPipeline:

	"""
	Sets the data of the pipeline. It should be given as a list of pairs of (instance, class_labels), where the instance is a text string and the class labels are a tupel of class labels.

	"""
	def setData(self, data):
		self.data = data	

	def getProcessedData(self):
		return self.dataProcessed

	def setTokenizer(self, tokenizer):
		self.tokenizer = tokenizer

	def setCleaner(self, cleaner):
		self.cleaner = cleaner
	
	def setFeatureEx(self, featex):
		self.featex = featex

	def resetClassifier(self, classifier):
		self.classifier = None

	def loadClassifierFromFile(self, name):
		f = open("../classifier/" + name + '.pickle', 'rb')
		classifier = pickle.load(f)
		f.close()

	def storeClassifierInFile(self, name):
		f = open("../classifier/"  + name + '.pickle', 'wb')
		pickle.dump(classifier, f)
		f.close()

	def getClassifier(self):
		return self.classifier

	def trainClassifier(self):
		self.preprocess()
		self.train
		
	def preprocess(self):
		dataTokenized = self.tokenizer(self.data)
		self.dataProcessed = self.cleaner(dataTokenized)

	def train(self):
		classifier = MaxentClassifier.train(self.featex(self.dataProcessed))
		

