def translate(dna):
    code={"ATC":"I","ATA":"I","ATT":"I","CTC":"L","CTA":"L","CTG":"L","TTA":"L","CTT":"L","GTC":"V","GTA":"V","GTG":"V","GTT":"V","TTC":"F","TTT":"F","ATG":"M","TGC":"C","TGT":"C","GCC":"A","GCA":"A","GCG":"A","GCT":"A","GGC":"G","GGA":"G","GGG":"G","GGT":"G","CCC":"P","CCA":"P","CCG":"P","CCT":"P","ACC":"T","ACA":"T","ACG":"T","ACT":"T","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S","TCT":"S","TAC":"Y","TAT":"Y","TGG":"W","CAG":"Q","CAA":"Q","AAC":"N","AAT":"N","CAC":"H","CAT":"H","GAG":"E","GAA":"E","GAC":"D","GAT":"D","AAG":"K","AAA":"K","TTG":"L","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","TAG":"stop","TAA":"stop","TGA":"stop"}
    protein=""
    dna=dna.upper()
    for i in range(0,len(dna),3):
        codon=dna[i:i+3]
        
        if codon=="TTG" or codon=="TGA" or codon=="TAG":
            break
        protein=protein+code[codon]
    return protein
