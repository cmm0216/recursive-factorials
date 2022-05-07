#!/bin/python3

#test file for the recursive-factorials assignment
import sys
import re
import argparse
from Bio import SeqIO
from Bio.Seq import translate


filename = sys.argv[1]
p = float(sys.argv[2])
q = 1- p
file_path = 'results.txt'
sys.stdout = open(sys.argv[3], "w")
print("Results\n")
class attributes:

	def __init__(self,sample_id,date,color, sequence,count):
		self.id = sample_id
		self.date = date
		self.color = color
		self.seq = sequence
		self.count = n

def get_factorial_recur(n):


	""" 
	Using an easy if statement to create a factorial function

	Input
	_____
	n: any number, or equation that could give you a number

	Example output:
	______________

	>>>get_factorial_recur(2) 
	4
	>>> get_factorial_recur(4-2)
	4
	"""
	if n == 1:
		return 1
	else:
		return n * get_factorial_recur(n-1)

def weagle(filename):
	"""
	Using SeqIO, the parse function takes in Fasta file, and can parse the file into different components.
	Seq variable created, called "record"

	Input
	______
	filename: .fasta file that comes from the command line


	Example output:
	_______________
	n (the number of sampled individuals) =100
	k (the number of orange individuals in the sample set) = 26

	"""
	headers = []
	aa = []
	orange = []
	blue = []
	with open(filename,'r') as f:
    	 for record in SeqIO.parse(f, "fasta"):
    	 	headers.append(record.description)


    	 	#Seperating date and sample id to be cataloged to class attributes.
    	 	date= re.split(r'_(.+?$)', record.id)
    	 	sample_id = re.match(r'(^.+?)_', record.id).group(0)
  
  			#Getting sequences alone, to be cataloged to class attributes.
    	 	if filename != re.match('>',filename):
    	 		sequence = record.seq
    	 	aa = translate(sequence)
    	 	if aa[3] == 'R':
    	 		color = "orange"
    	 		orange.append(aa)
    	 	if aa[3] == 'S':
    	 		color = "blue"
    	 		blue.append(aa)
   		#Getting the number of samples "n" and "k" needed for the equation.
    	 k = len(orange)
    	 n = len(headers)
    	 eq  = ((get_factorial_recur(n))/(get_factorial_recur(n-k)*get_factorial_recur(k)))*(p**k)*(q**(n-k))

	print('p (the frequency of "orange" in the population) = ' + str(p))
	print('n (the number of sampled individuals) = ' + str(n))
	print('k (the number of "orange" individuals in the sample set) = ' + str(k))
	print('\nProbability of collecting 32 individuals with 5 being "orange" (given a population frequency of '+ str(p) + ") = " + str(eq))


if __name__ == "__main__":
	weagle(filename)

