# mt_partition
individual scripts to partition mitochondrial genomes

If you have a reference mitogenome (with annotations), then you just need to align all of the other mitogenomes to the reference. Then you can use bedtools to extract all of the genes (http://bedtools.readthedocs.io/en/latest/). 

Here are the steps:
a. Align all of the mitogenomes (including the reference mitogenome - e.g. accession U96639.2) and save the alignment in FASTA format. 

b. Separate the sequences into individual files, so that each file has a single sequence name and sequence. 

c. For each mitogenome, prepare a “bed” file that contains the locations of all of the genes in the mitogenome. 

d. Run bedtools to extract all of the genes to a new file. The command is like this:
> fastaFromBed -fi xxx.fasta -bed xxx.bed -fo xxx.genes.fasta -s -name

where xxx is the name of the sequence in this particular example. In the bed file, there are six columns of data. The first column is the name of the sequence. The second and third columns are the start and end positions of each gene. The fourth column is the name of the gene. Ignore the fifth column (just leave it as “0”). The sixth column shows whether the gene runs in the forward direction (+) or the reverse direction (-). The sixth column is important because any genes that run in the reverse direction will automatically be reverse-complemented by bedtools. 

All the mitogenomes will need its own bed file. But if all the mitogenomes are aligned, then the gene positions should be the same – so you’ll only need to change the name in column 1. 

Once you have all of the separate fasta and corresponding bed files, you use this python script that can extract the partitions in the fasta files depending on the patterntype (tRNA, rRNA, CDS etc) you specify. The command is like this: 
> python extract_partition_in_fasta.py -i partitions -o partitions/out/tRNA.fasta -s tRNA

Once you have an alignment with all of the full CDS sequences only (shown in the bottom example as full_CDS.fasta), you use this python script that can extract the sequences based on 1st, 2nd, or 3rd codon position. The command is like this: 
> python codonextract.py full_CDS.fasta > codon_pos_1_2_or_3.fasta 
You need to edit the python file directly in a text editor to change the number in which_codon. which_codon = 0  is the 1st codon, which_codon = 2 is the 2nd codon, which_codon = 3 is the 3rd codon.

Should you have any questions, please contact Audrey T. Lin (linat@si.edu)
