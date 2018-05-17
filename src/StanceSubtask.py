"""

Module for realizing the stance subtask. With optional command line arguments, see below.

"""

#import own modules
import file_handler;
import pipelineFunctions;
import classifier;
import evaluator;

#other modules
import sys;

def load_data(tweet_files, truth_files):
	

















def main():
	print("###### STANCE SUBTASK ######");
	no_catalan = False;
	no_espanol = False;

	if len(sys.argv) > 1:
		print("Starting the task with the following configuration:");
		
		if sys.argv[1] = "-CA":
			no_espanol = True;
			print("ONLY CATALAN");
		elif sys.argv[1] = "-ES":
			no_catalan = True;
			print("ONLY ESPANOL");
		else
			print("INVALID CONFIG - default with ES and CA");

	tweet_files = []
	truth_files = []		

	if not no_catalan:
		tweet_files = tweet_files + ["tweets_ca.txt"];
		truth_files = truth_files + ["truth_ca.txt"];

	if not no_espanol:
		tweet_files = tweet_files + ["tweets_es.txt"];
		truth_files = truth_files + ["truth_es.txt"];
		
	load_data(tweet_files, truth_files);
	

#call main	
main();
