def load_file(file_name):
	sample_folder	= "../samples";
	file_path	= sample_folder + "/" + file_name;
	text_file	= open(file_path, "r");
	lines_of_file	= text_file.read().split('\n');
	loaded_lines	= [];
	for i in range(0, len(lines_of_file)):
		loaded_lines.append(lines_of_file[i].split(":::"));
	return loaded_lines;
