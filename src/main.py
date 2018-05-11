import file_handler

import nltk

truth  = file_handler.load_file("truth_es_second.txt");
tweets = file_handler.load_file("tweets_es_second.txt");

formatted_input = [];
for i in truth:
	formatted_input.append((tweets[i], truth[i]));

print(formatted_input);
