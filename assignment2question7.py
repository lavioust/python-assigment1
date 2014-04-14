import assignment2
import sys
sys.argv[1]="~/Documents/seq.fa.odt"
sys.argv[2]="~/Documents/translate.odt"
dnasequence=assignment2.read_fasta_file("~/Documents/seq.fa.odt")
reversecomp=assignment2.reverse_complement(dnasequence[1])
orf=assignment2.get_ORF(dnasequence)
gene=assignment2.get_gene_by_ORF(dnasequence,0)
protein=assignment2.translate(gene)
fastaformat=assignment2.get_fasta(protein,insulin)
h=open("/Documents/translate.odt","w")
h.write(fastaformat)
h.close