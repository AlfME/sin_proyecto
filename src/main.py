"""

The main class realizing training/classification/evaluation based on the command line inputs.

"""

import file_handler
import classifier

truth  = file_handler.load_file("truth_es_second.txt");
tweets = file_handler.load_file("tweets_es_second.txt");

formatted_input = [];
for i in truth:
	formatted_input.append((tweets[i], truth[i]));

print(formatted_input);
