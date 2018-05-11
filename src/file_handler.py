"""

The module for loading a dataset from a given file and parsing it into a dictionary.
The offered functions allow to receive a list of pairs of samples with their labels

"""

def load_file(file_name):
	sample_folder	= "../samples";
	file_path	= sample_folder + "/" + file_name;
	text_file	= open(file_path, "r");
	lines_of_file	= text_file.read().split('\n');
	loaded_lines	= dict();
	for i in range(0, len(lines_of_file)):
		elements = lines_of_file[i].split(":::");
		if(elements[0] == ''):
			continue;
		if(len(elements) >= 3):
			elements_structured = (unicode(elements[1], 'utf8'), unicode(elements[2], 'utf8'))
		else:
			elements_structured = (unicode(elements[1], 'utf8'))
		loaded_lines[elements[0]] = elements_structured;
	return loaded_lines;
