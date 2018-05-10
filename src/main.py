"""

The main class realizing training/classification/evaluation based on the command line inputs.

"""

import file_handler
import classifier

input=file_handler.load_file("tweets_es_second.txt");
for i in input:
	print(i, " : ", input[i], "\n");
