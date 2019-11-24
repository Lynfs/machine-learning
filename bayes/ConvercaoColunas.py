def coluna_para_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

def coluna_para_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	print('\n')
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup