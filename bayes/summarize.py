import separate
import stdev
import mean

def resumirDataset(dataset):
	summaries = [(mean.mean(column), stdev.stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries

def resumirClasse(dataset):
	separated = separate.SepararPorClasse(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = resumirDataset(rows)
	return summaries
