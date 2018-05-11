#[(content, (gender, stance))]

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
			elements_structured = (elements[1], elements[2])
		else:
			elements_structured = (elements[1])
		loaded_lines[elements[0]] = elements_structured;
	return loaded_lines;
