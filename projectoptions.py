def menu():
    
    print "*************************************************************"
    print "* MULTIPLE ALIGNMENT ANALYZER                               *"
    print "*************************************************************"
    print "* Select an option from below:                              *"
    print "*                                                           *"
    print "*    1) Open a Multiple Alignment File      (O)             *"
    print "*    2) Alignment Information               (A)             *"
    print "*    3) Alignment Explorer                  (E)             *"
    print "*    4) Information per Sequence            (I)             *"
    print "*    5) Analysis of Glycosylation Signatures(S)             *"
    print "*    6) Export to Fasta                     (X)             *"
    print "*    7) Exit                                (Q)             *"
    print "*                                                           *"
    print "*                                                File: None *"
    print "*************************************************************"
    print "Option:"
    

def openfile():
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        return "file not found"
    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            return "file not in clustal format"
        else:
            return "The file "+string+" has been successfully loaded."
def alignmentinfo():
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        print "file not found"
       
    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            print "file not in clustal format"
           
        else:
            print "The file "+string+" has been successfully loaded."
    alignments=[]
    
    for line in fat:
        if line!="\n":  
            alignments=alignments+[line]                      #creating a list of sequences and their sequenceIds
    alignments=[line[:-1] for line in alignments]     #removing the "|n" at the end of each line
    
    dictionery={}
    for k in alignments:
        a=k.index(" ")
        b=k.rindex(" ")               
        if k[:a] in dictionery.keys():  #creating a dictionery with sequenceIDs as keys and sequences as values 
            dictionery[k[:a]]=dictionery[k[:a]]+k[b+1:]  #concatenating sequences with the same id
        else:
            dictionery[k[:a]]=k[b+1:]
    sequenceIDs=[]
    sequences=[]
    
    for k in dictionery:
        sequenceIDs.append(k)         #creating a list of sequenceIDs only
        sequences.append(dictionery[k]) #creating a list of sequences only
        
    
    length=0 
    for k in sequences[1:]:
        length=length+len(k)
    countstars=0
    for k in sequences:
        for l in k:
            if l=="*":
                countstars=countstars+1
    averagelength=length/(len(sequences)-1) #because the other element of sequences is a sequence of stars only
    averagelength="%.3f"%averagelength
    percentagematches=(countstars*100)/length
    
    percentagematches="%.2f"%percentagematches
    print "File name:                "+c
    print "sequences:          "+", ".join(sequenceIDs)
    print "length:          ",length
    print "Average length:          ",averagelength
    print "% of X matches:          ",  percentagematches+"%"
    print "Number of X matches:"
    print "                  [03]="+str(countstars)
    

                                  

def alignmentexplorer():
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        print "file not found"

    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            print "file not in clustal format"
            
        else:
            "The file "+string+" has been successfully loaded."
    alignments=[]
    for line in fat:
        if line!="\n":  
            alignments=alignments+[line]                      #creating a list of sequences and their sequenceIds
    alignments=[line[:-1] for line in alignments]     #removing the "|n" at the end of each line
    dictionery={}
    for k in alignments:
        a=k.index(" ")
        b=k.rindex(" ")               
        if k[:a] in dictionery.keys():  #creating a dictionery with sequenceIDs as keys and sequences as values 
            dictionery[k[:a]]=dictionery[k[:a]]+k[b+1:]  #concatenating sequences with the same id
        else:
            dictionery[k[:a]]=k[b+1:]
    sequenceIDs=[]
    sequences=[]
    for k in dictionery:
        sequenceIDs.append(k)         #creating a list of sequenceIDs only
        sequences.append(dictionery[k]) #creating a list of sequences only
    d=input("enter the start of the sequence:")
    e=input("enter the end of the sequence:")
    print "CLUSTAL segment","["+str(d)+":"+str(e)+"]", "of the "+c,"alignment"
    for k in dictionery:
        if dictionery[k][0]!="*":
            if len(dictionery[k][d:e+1])<=60:
                print k+"          "+dictionery[k][d:e+1]
            else:
                t=""
                for i in range(len(dictionery[k][d:e+1])):
                    if i%60==0:
                        t=t+"\n"+dictionery[k][i] #splitting alignment into segments of 60 bases each
                    else:
                        t=t+dictionery[k][i]
                print k+"          "+t
    
def infopersequence():
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        print "file not found"
        
    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            print "file not in clustal format"
            
        else:
            "The file "+string+" has been successfully loaded."
    alignments=[]
    for line in fat:
        if line!="\n":  
            alignments=alignments+[line]                      #creating a list of sequences and their sequenceIds
    alignments=[line[:-1] for line in alignments]     #removing the "|n" at the end of each line
    dictionery={}
    for k in alignments:
        a=k.index(" ")
        b=k.rindex(" ")               
        if k[:a] in dictionery.keys():  #creating a dictionery with sequenceIDs as keys and sequences as values 
            dictionery[k[:a]]=dictionery[k[:a]]+k[b+1:]  #concatenating sequences with the same id
        else:
            dictionery[k[:a]]=k[b+1:]
    sequenceIDs=[]
    sequences=[]
    for k in dictionery:
        sequenceIDs.append(k)         #creating a list of sequenceIDs only
        sequences.append(dictionery[k]) #creating a list of sequences only
    f=raw_input("enter the sequence Id:")
    v=0
    w=0
    x=0
    y=0
    z=0
    seq=""
    for k in dictionery:
        if k==f:
            v=len(dictionery[k])
            w=dictionery[k].count("A")
            x=dictionery[k].count("C")
            y=dictionery[k].count("G")
            z=dictionery[k].count("T")
            for i in range(v):
                if i%60!=0:
                    seq=seq+dictionery[k][i]
                else:
                    seq=seq+"\n"+dictionery[k][i]
    print "ID:   "+f
    print "Length:   ",v
    print "Frequency per base:"
    print "                   [A]:",w
    print "                   [G]:",x
    print "                   [C]:",y
    print "                   [T]:",z
    print "sequence:"
    print seq
    
def glycosylation():
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        print "file not found"
        
    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            print "file not in clustal format"
            
        else:
            "The file "+string+" has been successfully loaded."
    alignments=[]
    for line in fat:
        if line!="\n":  
            alignments=alignments+[line]                      #creating a list of sequences and their sequenceIds
    alignments=[line[:-1] for line in alignments]     #removing the "|n" at the end of each line
    dictionery={}
    for k in alignments:
        a=k.index(" ")
        b=k.rindex(" ")               
        if k[:a] in dictionery.keys():  #creating a dictionery with sequenceIDs as keys and sequences as values 
            dictionery[k[:a]]=dictionery[k[:a]]+k[b+1:]  #concatenating sequences with the same id
        else:
            dictionery[k[:a]]=k[b+1:]
    sequenceIDs=[]
    sequences=[]
    for k in dictionery:
        sequenceIDs.append(k)         #creating a list of sequenceIDs only
        sequences.append(dictionery[k]) #creating a list of sequences only    
    code={"ATC":"I","ATA":"I","ATT":"I","CTC":"L","CTA":"L","CTG":"L","TTA":"L","CTT":"L","GTC":"V","GTA":"V","GTG":"V","GTT":"V","TTC":"F","TTT":"F","ATG":"M","TGC":"C","TGT":"C","GCC":"A","GCA":"A","GCG":"A","GCT":"A","GGC":"G","GGA":"G","GGG":"G","GGT":"G","CCC":"P","CCA":"P","CCG":"P","CCT":"P","ACC":"T","ACA":"T","ACG":"T","ACT":"T","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S","TCT":"S","TAC":"Y","TAT":"Y","TGG":"W","CAG":"Q","CAA":"Q","AAC":"N","AAT":"N","CAC":"H","CAT":"H","GAG":"E","GAA":"E","GAC":"D","GAT":"D","AAG":"K","AAA":"K","TTG":"L","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","TAG":"stop","TAA":"stop","TGA":"stop"}
    import re
    protein=""
    for k in dictionery:
        for i in range(0,len(dictionery[k]),3):
            codon=dictionery[k][i:i+3]
            if codon in code:
                if codon=="TTG" or codon=="TGA" or codon=="TAG":
                    break
                protein=protein+code[codon]
                protein=protein.lower()
        glycosignatures=re.compile("n[^p][st]")
        match=glycosignatures.search(protein)
        if match:
            f=glycosignatures.findall(protein)
            for l in f:
                protein=protein.replace(l,l.upper())
            print "Glycosignatures found in:", k,"\n",protein
        else:
            print "There are no signatures in " + k 
        protein=""
        
def export2fasta():
    import re
    code={"ATC":"I","ATA":"I","ATT":"I","CTC":"L","CTA":"L","CTG":"L","TTA":"L","CTT":"L","GTC":"V","GTA":"V","GTG":"V","GTT":"V","TTC":"F","TTT":"F","ATG":"M","TGC":"C","TGT":"C","GCC":"A","GCA":"A","GCG":"A","GCT":"A","GGC":"G","GGA":"G","GGG":"G","GGT":"G","CCC":"P","CCA":"P","CCG":"P","CCT":"P","ACC":"T","ACA":"T","ACG":"T","ACT":"T","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S","TCT":"S","TAC":"Y","TAT":"Y","TGG":"W","CAG":"Q","CAA":"Q","AAC":"N","AAT":"N","CAC":"H","CAT":"H","GAG":"E","GAA":"E","GAC":"D","GAT":"D","AAG":"K","AAA":"K","TTG":"L","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","TAG":"stop","TAA":"stop","TGA":"stop"}
    string=raw_input("Enter a valid path for a Multiple Alignment File:")
    fat=open(string,"r")
    if not fat:
        print "file not found"
        
    else:
        fat.seek(0,0)
        c=fat.readline()
        if c[:7]!="CLUSTAL":
            print "file not in clustal format"
            
        else:
            "The file "+string+" has been successfully loaded."
    alignments=[]
    for line in fat:
        if line!="\n":  
            alignments=alignments+[line]                      #creating a list of sequences and their sequenceIds
    alignments=[line[:-1] for line in alignments]     #removing the "|n" at the end of each line
    dictionery={}
    for k in alignments:
        a=k.index(" ")
        b=k.rindex(" ")               
        if k[:a] in dictionery.keys():  #creating a dictionery with sequenceIDs as keys and sequences as values 
            dictionery[k[:a]]=dictionery[k[:a]]+k[b+1:]  #concatenating sequences with the same id
        else:
            dictionery[k[:a]]=k[b+1:]
    sequenceIDs=[]
    sequences=[]
    for k in dictionery:
        sequenceIDs.append(k)         #creating a list of sequenceIDs only
        sequences.append(dictionery[k]) #creating a list of sequences only    
    m=raw_input("If you want to create Multiple files(one per sequence) press M or or press S for a single file that includes all the sequences:")
    if m=="M":
        
        n=raw_input("Do you want to save the DNA sequences(input D) or the proteins (input P):")
        if n=="D":
                for k in dictionery:
                    o=raw_input("Please input the name of the file to save:")
                    p=open(o,"w")
                    p.seek(0,0)
                    p.write(dictionery[k])
                    p.close()
                    print "File "+o+" saved."
        if n=="P":
                for k in dictionery:
                    protein=""
                    for i in range(0,len(dictionery[k]),3):
                        codon=dictionery[k][i:i+3]
                        if codon in code:
                            if codon=="TTG" or codon=="TGA" or codon=="TAG":
                                break
                            protein=protein+code[codon]  
                            protein=protein.lower()
                    q=raw_input("Do you want to mark by case the bases involve in a Glycosylation Signature (Y/N):")
                    if q=="Y":
                        global protein
                        glycosignatures=re.compile("n[^p][st]")
                        match=glycosignatures.search(protein)
                        f=[]
                        if match:
                            f=glycosignatures.findall(protein)
                            for l in f:
                                protein=protein.replace(l,l.upper())
                        o=raw_input("Please input the name of the file to save:")
                        p=open(o,"w")
                        p.write(protein)
                        p.close()
                        print "File "+o+" saved."
                        protein=""
                    if q=="N":
                        global protein
                        o=raw_input("Please input the name of the file to save:")
                        p=open(o,"w")
                        p.write(protein)
                        p.close()
                        print "File "+o+" saved."
                        protein=""
    if m=="S":
        n=raw_input("Do you want to save the DNA sequences(input D) or the proteins (input P):")
        if n=="D":
            o=raw_input("Please input the name of the file to save:")
            p=open(o,"w")
            p.seek(0,0)
            for k in dictionery:
                p.write(dictionery[k])
            p.close()
            print "File "+o+" saved."
        if n=="P":
            o=raw_input("Please input the name of the file to save:")
            p=open(o,"w")
            for k in dictionery:
                protein=""
                for i in range(0,len(dictionery[k]),3):
                    codon=dictionery[k][i:i+3]
                    if codon in code:
                        if codon=="TTG" or codon=="TGA" or codon=="TAG":
                            break
                        protein=protein+code[codon]
                        protein=protein.lower()
            q=raw_input("Do you want to mark by case the bases involve in a Glycosylation Signature (Y/N):")
            if q=="Y":
                global protein
                glycosignatures=re.compile("n[^p][st]")
                match=glycosignatures.search(protein)
                f=[]
                if match:
                    f=glycosignatures.findall(protein)
                    for l in f:
                        protein=protein.replace(l,l.upper())
                p.write("protein")
                p.close()
            else:
                global protein
                p.write(protein)
                p.close()
            print "File "+o+" saved."   
                
                
                        
                        
                        
                  
                        
            
            
        
