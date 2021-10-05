
### <--  README.MD found at https://github.com/lin-at --> ###
### <--  with thanks to https://github.com/laduplessis --> ###



import sys,os

from fnmatch import fnmatch
from optparse import OptionParser
from Bio import SeqIO


# ./extract_partition_in_fasta.py -i /path/to/directory -o /path/to/outputfile.fasta -s patterntype (tRNA / CDS etc.)  ( -f "*.fa")
# -f if you only want specific sample IDs eg  those with prefix TXL   

# Input arguments
parser = OptionParser()

parser.add_option("-i", "--inputfile", dest="inputpath",
                  help="Directory with fasta files")

parser.add_option("-f", "--filepattern", dest="filepattern",
                  help="Pattern for sequences", default="*.fasta")

parser.add_option("-s", "--seqpattern", dest="seqpattern",
                  help="Pattern for sequences", default="tRNA")

parser.add_option("-o", "--outputfile", dest="outputfile",
                  help="Output file name", default="out.fasta")

(options, args) = parser.parse_args()


# Create output file
outfile = open(options.outputfile,"w")


print("Extracting "+options.filepattern+" from "+options.inputpath) 

# Iterate over files in input directory
f = 0
for file in sorted(os.listdir(options.inputpath)):
	if (fnmatch(file,options.filepattern)):	
		f += 1

		# Iterate over matching sequences in file	
		i = 0
		j = 0
		seqs = ""
		for seq in SeqIO.parse(options.inputpath+"/"+file,"fasta"):
			i += 1
			if (fnmatch(seq.description,"*"+options.seqpattern+"*")):
				# print(seq.description)
				seqs += seq.seq
				j += 1

		print("\t%3d) %20s: Extracted %d of %d sequences (%d bp)" % (f,file,j,i,len(seqs)))

		# Create sequence to save at the end
		seqid = file[:file.rfind(".")]
		#seqid = file[:file.rfind(".")]+"|"+options.seqpattern #if you want do obtain such names >ID.genes|tRNA
		outfile.write(">%s\n%s\n" % (seqid, seqs))

outfile.close()
		
print("Parsed %d matching files" % f)


