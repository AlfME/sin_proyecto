"""

The main class realizing training/classification/evaluation based on the command line inputs.

"""

import file_handler
from pipelineFunctions import *

import classifier
from classifier import ClassificationPipeline

import evaluator

import nltk.classify.util
from nltk.classify import MaxentClassifier
from nltk.tokenize.toktok import ToktokTokenizer

import datetime
import time

import random
from random import shuffle

#load files
truth  = file_handler.load_file("truth_es_first.txt");
tweets = file_handler.load_file("tweets_es_first.txt");

formatted_input = [];
for i in truth:
	formatted_input.append((tweets[i], truth[i]));

shuffle(formatted_input);

print("Imported data");

#setup pipeline and run training
pipeline = ClassificationPipeline();

pipeline.setData(formatted_input);
pipeline.setTokenizer(tokenizer1());
pipeline.setCleaner(cleaner1());
pipeline.setFeatureEx(featureEx1());

pipeline.preprocess();
print("Preprocessed data");
pipeline.train();
print("Trained classifier");

#save classifier
ts = time.time();
pipeline.storeClassifierInFile("basic" +  datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'));
classifier = pipeline.getClassifier();
print("saved classifier");

#evaluate
truth  = file_handler.load_file("truth_es_second.txt");
tweets = file_handler.load_file("tweets_es_second.txt");

formatted_labels = [];
for i in truth:
	formatted_labels.append((tweets[i], truth[i]));

shuffle(formatted_labels);

evaluator.evaluate(classifier, formatted_labels);
print("Evalauted classifier");

