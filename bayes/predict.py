import calcProb

def predict(summaries, row):
	probabilidade = calcProb.probClasse(summaries, row)
	lbl, best_prob = None, -1
	for class_value, prob in probabilidade.items():
		if lbl is None or prob > best_prob:
			best_prob = prob
			lbl = class_value
	return lbl

