#!/bin/python3

#test file for the recursive-factorials assignment
import sys
import re
import argparse
from Bio import SeqIO
from Bio.Seq import translate


filename = sys.argv[1]

file_path = 'randomfile.txt'
sys.stdout = open(file_path, "w")
print("Results")
class attributes:

	def __init__(self,sample_id,date,color, sequence,count):
		self.id = sample_id
		self.date = date
		self.color = color
		self.seq = sequence
		self.count = headers

def ID(filename):
	"""
	Using SeqIO, the parse function takes in Fasta file, and can parse the file into different components.
	Seq variable created, called "record"

	Input
	______
	filename: .fasta file that comes from the command line

	Example output:
	_______________
	n (the number of sampled individuals = 100

	"""
	headers = []
	with open(filename,'r') as f:
    	 for record in SeqIO.parse(f, "fasta"):
    	 	headers.append(record.description)


    	 	#Seperating date and sample id to be cataloged to class attributes.
    	 	date= re.split(r'_(.+?$)', record.id)
    	 	sample_id = re.match(r'(^.+?)_', record.id).group(0)
  
  			#Getting sequences alone, to be cataloged to class attributes.
    	 	if filename != re.match('>',filename):
    	 		sequence = record.seq

    	 #Getting the number of samples "n" needed for the equation.
    	 n = len(headers)

    	 


	print("n (the number of sampled individuals) = " + str(n))

if __name__ == "__main__":
	ID(filename)
	#orange(filename)

