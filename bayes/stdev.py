import mean
from math import sqrt

def stdev(numbers):
	avg = mean.mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)