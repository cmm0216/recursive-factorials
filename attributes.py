#!/bin/python3

#test file for the recursive-factorials assignment
import sys
import re
import argparse
from Bio import SeqIO

filename = sys.argv[-1]

def ID(filename):
	"""
	Using SeqIO, the parse function takes in Fasta file, and can parse the file into different components.
	Seq variable created, called "record"

	Input
	______

	"""
	headers = []
	with open(filename,'r') as f:
    	 for record in SeqIO.parse(f, "fasta"):
        	headers.append(record.description)
	print(headers)
	n = len(headers)
	print("n (the number of sampled individuals = " + str(n)) 





#class attributes():
#	def ID():
#		for line in SeqIO.parse("Aubie.fasta", "fasta"):
#			start = line(r'^>')
#			return wc -l
#
#	def date():
#		for seq in SeqIO.parse("Aubie.fasta", "fasta"):
#			str = seq.findall
#			print(str)
#

if __name__ == "__main__":
	ID(filename)
