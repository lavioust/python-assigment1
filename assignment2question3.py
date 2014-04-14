def get_ORF(sequence):
    for i in range(0,len(sequence),3):
        codon=sequence[i:i+3]
        a=-1
        b=-1
        c=-1
        d=-1
        if codon=="ATG":
            a=sequence.find(codon)
        if codon=="TGA":
            b=sequence.find(codon)
        if codon=="TAA":
            c=sequence.find(codon)
        if codon=="TAG":
            d=sequence.find(codon)
        if a!=-1 and b!=-1 or c!=-1 or d!=-1:
            if a<b or a<c or a<d:
                return 0
            else:
                for i in range(1,len(sequence),3):
                    codon=sequence[i:i+3]
                    a=-1
                    b=-1
                    c=-1
                    d=-1
                    if codon=="ATG":
                        a=sequence.find(codon)
                    if codon=="TGA":
                        b=sequence.find(codon)
                    if codon=="TAA":
                        c=sequence.find(codon)
                    if codon=="TAG":
                        d=sequence.find(codon)
                    if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                        if a<b or a<c or a<d:
                            return 1
                        else:
                            for i in range(2,len(sequence),3):
                                codon=sequence[i:i+3]
                                a=-1
                                b=-1
                                c=-1
                                d=-1                                
                                if codon=="ATG":
                                    a=sequence.find(codon)
                                if codon=="TGA":
                                    b=sequence.find(codon)
                                if codon=="TAA":
                                    c=sequence.find(codon)
                                if codon=="TAG":
                                    d=sequence.find(codon)
                                if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                                    if a<b or a<c or a<d:
                                        return 2
                else:
                    return -1
        if a==-1 and b!=-1 or c!=-1 or d!=-1:
            for i in range(1,len(sequence),3):
                codon=sequence[i:i+3]
                a=-1
                b=-1
                c=-1
                d=-1
                if codon=="ATG":
                    a=sequence.find(codon)
                if codon=="TGA":
                    b=sequence.find(codon)
                if codon=="TAA":
                    c=sequence.find(codon)
                if codon=="TAG":
                    d=sequence.find(codon)
                if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                    if a<b or a<c or a<d:
                        return 1 
                    else:
                        for i in range(2,len(sequence),3):
                            codon=sequence[i:i+3]
                            a=-1
                            b=-1
                            c=-1
                            d=-1
                            if codon=="ATG":
                                a=sequence.find(codon)
                            if codon=="TGA":
                                b=sequence.find(codon)
                            if codon=="TAA":
                                c=sequence.find(codon)
                            if codon=="TAG":
                                d=sequence.find(codon)
                            if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                                if a<b or a<c or a<d:
                                    return 2
                else:
                    return -1
        if a!=-1 and b==-1 and c==-1 and d==-1:
            for i in range(1,len(sequence),3):
                codon=sequence[i:i+3]
                a=-1
                b=-1
                c=-1
                d=-1
                if codon=="ATG":
                    a=sequence.find(codon)
                if codon=="TGA":
                    b=sequence.find(codon)
                if codon=="TAA":
                    c=sequence.find(codon)
                if codon=="TAG":
                    d=sequence.find(codon)
                if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                    if a<b or a<c or a<d:
                        return 1
                    else:
                        for i in range(2,len(sequence),3):
                            codon=sequence[i:i+3]
                            a=-1
                            b=-1
                            c=-1
                            d=-1
                            if codon=="ATG":
                                a=sequence.find(codon)
                            if codon=="TGA":
                                b=sequence.find(codon)
                            if codon=="TAA":
                                c=sequence.find(codon)
                            if codon=="TAG":
                                d=sequence.find(codon)
                            if a!=-1 and b!=-1 or c!=-1 or d!=-1:
                                if a<b or a<c or a<d:
                                    return 2                                
                else:
                    return -1

