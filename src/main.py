import file_handler

import nltk

input=file_handler.load_file("tweets_es_second.txt");
for i in input:
	print(i, " : ", input[i], "\n");
