
#! /usr/bin/env python

"""
Problem Title: Introduction to the Bioinformatics Armory
Rosalind Armory ID: INI
Rosalind Armory #: 001
URL: http://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
"""


from Bio.Seq import Seq

def ini_armory():
    # Read the DNA sequence from the text file
    with open('rosalind_ini.txt', 'r') as file:
        dna_sequence = file.read().strip()
        
    # Create Seq object
    my_seq = Seq(dna_sequence)
    
    # Use dictioanry comprehension to count the occurences of each nucleotide
    symbol_count = {nucleotide:my_seq.count(nucleotide) for nucleotide in 'ACGT'}
    
    for nucleotide, count in symbol_count.items():
        print(count, end = " ")
        
    print() # Move to the next line after printing count
    

if __name__ == "__main__":
    ini_armory()
