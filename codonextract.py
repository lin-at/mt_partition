#!/usr/bin/env python

### <--  contact Audrey T. Lin (linat@si.edu) --> ###
### <--  README.MD found at https://github.com/lin-at --> ###

import sys
from Bio import SeqIO

# ./codonextract.py full_CDS.fasta > codon_pos_1_2_or_3.fasta #
def codonextract(file1):
	source=open(file1)

	for i in range(3):
		codon=str(i+1)
		Filename="CDS_"+codon+".fasta"
		dest=open(Filename,"w")
		source.seek(0)
		which_codon = i ## 0 for first codon, 1 for second codon, 2 for third codon.
		for record in SeqIO.parse(source, "fasta"):
			dest.write('>'+record.id)
			dest.write("\n")
			dest.write(str(record.seq[which_codon::3])) ### 3 is codon length. This extract every third character, starting at which_codon. 
			dest.write("\n")
		dest.close()

inp=sys.argv[1]
codonextract(inp)