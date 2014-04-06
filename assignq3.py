dna=raw_input("put dna sequence in capital letters:")
counter=0
number=0
while counter<len(dna):
      if dna[counter]=="A" or dna[counter]=="G"or dna[counter]=="C" or dna[counter]=="T":
         counter=counter+1
         continue
      number=number+1
      counter=counter+1
print number   
