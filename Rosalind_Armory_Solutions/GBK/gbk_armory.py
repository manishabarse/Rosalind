
#! /usr/bin/env python

"""
Problem Title: GenBank Introduction
Rosalind Armory ID: GBK
URL: http://rosalind.info/problems/gbk/

Given: A genus name, followed by two dates in YYYY/M/D format.
Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
"""

from Bio import Entrez

def count_genbank_entries(genus, start_date, end_date, output_file):
    # Set your email for Entrez
    Entrez.email = 'manishabarse93@gmail.com'  # Replace with your email

    # Construct the query and search Nucleotide database
    query = f"{genus}[ORGN] AND {start_date}:{end_date}[pdat]"
    handle = Entrez.esearch(db='nucleotide', term=query)
    record = Entrez.read(handle)

    # Extract the count of matching entries
    count = record['Count']

    # Print the count
    print(count)

    # Write the count to output file
    with open(output_file, 'w') as output_data:
        output_data.write(count)

if __name__ == "__main__":
    # Read input data from file
    with open('rosalind_gbk.txt') as input_data:
        genus, start_date, end_date = [line.strip() for line in input_data]

    # Define the output file path
    output_file = 'gbk_output.txt'

    # Call the function to count entries and write output
    count_genbank_entries(genus, start_date, end_date, output_file)
