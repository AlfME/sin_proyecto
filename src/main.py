"""

The main class realizing training/classification/evaluation based on the command line inputs.

"""

import file_handler
from pipelineFunctions import *

import classifier
from classifier import ClassificationPipeline

import nltk.classify.util
from nltk.classify import MaxentClassifier
from nltk.tokenize.toktok import ToktokTokenizer

#load files
truth  = file_handler.load_file("truth_es_second.txt");
tweets = file_handler.load_file("tweets_es_second.txt");

formatted_input = [];
for i in truth:
	formatted_input.append((tweets[i], truth[i]));

print(tokenizer1()(formatted_input[:10]));
print(featureEx1()(tokenizer1()(formatted_input[:10])));

pipeline = ClassificationPipeline();

pipeline.setData(formatted_input);
pipeline.setTokenizer(tokenizer1());
pipeline.setCleaner(cleaner1());
pipeline.setFeatureEx(featureEx1());

pipeline.preprocess()
pipeline.train()
