def get_gene_by_ORF(seq,j):
     a=seq[j:].find("ATG")
     b=seq[j:].rfind("TGA")
     c=seq[j:].rfind("TAA")
     d=seq[j:].rfind("TAG")
     sequence1=" "
     sequence2=" "
     sequence3=" "
     
     largest=len(sequence1)
     if a!=-1 and b!=-1:
          if a<b:
                    for i in range (a+1,b+4):
                         sequence1=sequence1+seq[i]
     if a!=-1 and c!=-1:
          if a<c:
                    for i in range(a+1,c+4):
                         sequence2=sequence2+seq[i]
     if a!=-1 and d!=-1:
          if a<d:
                    for i in range(a+1,d+4):
                         sequence3=sequence3+seq[i]
     if len(sequence2)>largest:
                                   largest=len(sequence2)
     if len(sequence3)>largest:
                                   largest=len(sequence3)
     
     if largest==len(sequence1):
                                   return sequence1 
     elif largest==len(sequence2):
                                   return sequence2 
     else:
                                   return sequence3
                              

