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
truth  = file_handler.load_file("test_samples/GenderEs", True);
tweets = file_handler.load_file("test_samples/GenderEs", True);

formatted_input = [];
for i in truth:
	formatted_input.append((tweets[i], truth[i]));

shuffle(formatted_input);

print("Imported data");

stance_pipeline = ClassificationPipeline();
gender_pipeline = ClassificationPipeline();
gender_classifier = None;
stance_classifier = None;



def train_stance():
	#setup pipeline and run training
	stance_pipeline.setClassifier(MaxentClassifier);
	stance_pipeline.setData(formatted_input);
	stance_pipeline.setTokenizer(tokenizer_stance());
	stance_pipeline.setCleaner(cleaner_stance());
	stance_pipeline.setFeatureEx(featureEx_stance());
	stance_pipeline.preprocess();
	print("Preprocessed data");
	stance_pipeline.train();
	print("Trained classifier");
	
	#save classifier
	ts = time.time();
	stance_pipeline.storeClassifierInFile("stance" +  datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'));
	stance_classifier = stance_pipeline.getClassifier();
	print("saved classifier");

def train_gender():
	#setup pipeline and run training
	gender_pipeline.setClassifier(MaxentClassifier);
	gender_pipeline.setData(formatted_input);
	gender_pipeline.setTokenizer(tokenizer_gender());
	gender_pipeline.setCleaner(cleaner_gender());
	gender_pipeline.setFeatureEx(featureEx_gender());
	
	gender_pipeline.preprocess();
	print("Preprocessed data");
	gender_pipeline.train();
	print("Trained classifier");
	
	#save classifier
	ts = time.time();
	gender_pipeline.storeClassifierInFile("gender" +  datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'));
	gender_classifier = gender_pipeline.getClassifier();
	print("saved classifier");




train_gender();
train_stance();

#evaluate
truth  = file_handler.load_file("truth_es_second.txt");
tweets = file_handler.load_file("tweets_es_second.txt");

formatted_labels= [];
for i in truth:
	formatted_labels.append((tweets[i], truth[i]));

shuffle(formatted_labels);

gender_result = [];
stance_result = [];
def evaluate_gender():
	gender_pipeline.setData(formatted_labels);
	gender_pipeline.preprocess();
	for i in gender_pipeline.getProcessedData():
		gender_result.append(gender_pipeline.getClassifier().classify(i[0]));
		print(gender_pipeline.getClassifier().classify(i[0]));


def evaluate_stance():
	stance_pipeline.setData(formatted_labels);
	stance_pipeline.preprocess();
	for i in stance_pipeline.getProcessedData():
		stance_result.append(stance_pipeline.getClassifier().classify(i[0]));
		print(stance_pipeline.getClassifier().classify(i[0]));


evaluate_gender();
evaluate_stance();
def print_result():
	print_str = [];
	count = 0;
	for i in tweets:
		count += 1;
		print_str.append(str(count) + "\t" + i + "\t");
	count = 0;
	for i in gender_result:
		print("[", i, "]\t");
		if(i == "Male"):
			print_str[count] += "Male\t";
		else:
			print_str[count] += "Female\t";
		count += 1;
#	for i in range(0, len(stance_result)):
#		print("{", i, "}\t");
#		if(i == "FAVOR"):
#			print_str[i] += "FAVOR\t";
#		elif(i == "AGAINST"):
#			print_str[i] += "AGAINST\t";
#		else:
#			print_str[i] += "NEUTRAL\t";

	write_file = open("guess_es.txt", "w");
	for s in print_str:
		write_file.write(s);

	write_file.close();

#print_result();

#get measures
print(">>> GENDER: ");
evaluator.evaluate(gender_result, gender_pipeline.getProcessedData());
print();
print(">>> STANCE: ");
evaluator.evaluate(stance_result, stance_pipeline.getProcessedData());


