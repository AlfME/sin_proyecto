"""

Module for realizing the stance subtask. With optional command line arguments, see below.

"""

#import own modules
import file_handler;
import pipelineFunctions;
import classifier;
import evaluator;

from classifier import ClassificationPipeline;

#other modules
import sys;

import nltk
from nltk.classify import MaxentClassifier


def load_data(tweet_files, truth_files):
	print("> Loading data..." +  str(tweet_files) + " and " + str(truth_files));
	
	if not no_training:
		data = file_handler.load_files_formatted_split(truth_files, tweet_files, 0.9, 0.1);
	else:
		data = file_handler.load_files_formatted_split(truth_files, tweet_files, 1- test_prop, test_prop); #all data test
	
	print("< Loaded data successfully");

	return data;


def setup_pipeline(data):
	print("> Instantiating pipeline...");
	pipeline = ClassificationPipeline();

	pipeline.setTokenizer(pipelineFunctions.tokenizer_stance2());
	pipeline.setCleaner(pipelineFunctions.cleaner_stance2());
	pipeline.setFeatureEx(pipelineFunctions.featureEx_stance2());

	if not no_training:
		pipeline.setClassifier(MaxentClassifier);
		pipeline.setLabelSelection(pipelineFunctions.labelSelection_stance2());
	else:
		pipeline.loadClassifierFromFile(classifierFile);	

	pipeline.setData(data);

	print("< Instantiated pipeline successfully")
	return pipeline;

def apply(data, classifier):
	#we assume that the labels are still given in the data, so (feat, (labels)) structure
	print("> Classifying data using classifier");	
	result = [];
	indexkeymap = dict();	

	i = 0;
	for (inst, labels, key) in data:
		result = result + [classifier.classify(inst)];
		indexkeymap[i] = key;
		i = i + 1;
	
	print("> Successfully classified instances.");
	return (result, indexkeymap);


def print_result(data, result, indexkeymap, labelindex):
	print("> Printing result to file");
	
	print_str = "";
	gold_str = "";
	for i in range(len(result)):
		print_str += indexkeymap[i] + "\t" + result[i].decode('utf8') + "\t" + data[i][0].decode('utf8') + "\n";
		#gold_str += indexkeymap[i] + "\t" + data[i][1][labelindex].decode('utf8') + "\t" + data[i][0].decode('utf8')  + "\n";
		#print_str += indexkeymap[i] + "\ttarget\t" + data[i][0].decode('utf8') + "\t" + result[i].decode('utf8') + "\n";
		#gold_str += indexkeymap[i]  + "\ttarget\t" + data[i][0].decode('utf8') + "\t" + data[i][1][labelindex].decode('utf8') + "\n";

	open_name = "result_stance_" + classifierFile;
	if not no_catalan:
		open_name += "CA";

	if not no_espanol:
		open_name += "ES";

	wfile = open(open_name, "w");
	wfile.write(str(print_str));

	wfile.close();

	wfile = open(open_name + "_GOLD", "w");
	wfile.write(str(gold_str));
	wfile.close();


def main():
	print("###### STANCE SUBTASK ######");
	global no_espanol;
	global no_catalan;
	global no_training;
	global classifierFile;
	global test_prop;

	if len(sys.argv) > 1:
		print("Starting the task with the following configuration:");
		
		if sys.argv[1] == "-CA":
			no_espanol = True;
			print("ONLY CATALAN");
		elif sys.argv[1] == "-ES":
			no_catalan = True;
			print("ONLY ESPANOL");
		elif sys.argv[1] == "-ALL":
			print("BOTH LANGUAGES");
		else:
			print("INVALID LANUGAGE CONFIG - default with ES and CA");

	if len(sys.argv) > 2:
		classifierFile = sys.argv[2];
		no_training = True;
		print("LOADING CLASSIFIER " + classifierFile + " - RUN AS TEST EVAL");

	if len(sys.argv) > 3:
		test_prop = float(sys.argv[3]);
		print("WITH TEST SPLIT " +  str(test_prop));

	tweet_files = [];
	truth_files = [];		

	if not no_catalan:
		tweet_files = tweet_files + ["tweets_ca.txt"];
		truth_files = truth_files + ["truth_ca.txt"];

	if not no_espanol:
		tweet_files = tweet_files + ["tweets_es.txt"];
		truth_files = truth_files + ["truth_es.txt"];
		
	data = load_data(tweet_files, truth_files);

	if not no_training:
		pipeline = setup_pipeline(data[0]);
	else:
		pipeline = setup_pipeline(data[1]);

	pipeline.preprocess();

	if not no_training:
		pipeline.train();
		pipeline.storeClassifierInFile(classifierFile);
		print("### TRAINED AND STORED CLASSIFIER (in " +  classifierFile + ")");
	else:
		res = apply(pipeline.getProcessedData(), pipeline.getClassifier());
		print_result(data[1], res[0], res[1], 0);
		
		evaluator.evaluateMultilabel(res[0], pipeline.getProcessedData(), 0);

#call main
no_catalan = False;
no_espanol = False;

test_prop = 0.1;

no_training = False;
classifierFile = "basic1_es";
	
main();
