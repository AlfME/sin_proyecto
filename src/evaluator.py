"""

"""

import nltk

def evaluate(result, data):
	data = [x[1] for x in data]
	
	res = nltk.ConfusionMatrix(result, data);	

 	print(res.pretty_format(sort_by_count=True, show_percents=True, truncate=9))
