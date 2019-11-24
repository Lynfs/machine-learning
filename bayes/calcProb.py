from math import pi
from math import exp
from math import sqrt

def probabilidade(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent

def probClasse(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	prob = dict()
	for class_value, resumo_classe in summaries.items():
		prob[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(resumo_classe)):
			mean, stdev, _ = resumo_classe[i]
			prob[class_value] *= probabilidade(row[i], mean, stdev)
	return prob