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


class ClassificationPipeline:
	

	def setData(self, data):
		self.data = data	

	def setTokenizer(self, tokenizer):
		self.tokenizer = tokenizer

	def setCleaner(self, cleaner):
		self.cleaner = cleaner
	
	def setFeatureEx(self, featex):
		self.featex = featex

	def setClassifier(self, classifier):
		self.classifier = classifier

	#def loadClassifierFromFile

	#
