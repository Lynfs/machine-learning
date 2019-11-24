import calcProb, PegarArquivo, mean, predict, stdev, summarize, separate, ConvercaoColunas

def main():
	dataset = PegarArquivo.PegarArquivo('iris.csv')
	for i in range(len(dataset[0])-1):
		ConvercaoColunas.coluna_para_float(dataset, i)
	ConvercaoColunas.coluna_para_int(dataset, len(dataset[0])-1)
	model = summarize.resumirClasse(dataset)
	row = [5.7,2.9,4.2,1.3]
	label = predict.predict(model, row)
	print("""
		Iris-setosa: 0
		Iris-versicolor: 1
		Iris-virginica: 2
		\n
		""")
	print(f"""
		Data={row}
	 	Predicted: {float(label)}
	 """)
main()