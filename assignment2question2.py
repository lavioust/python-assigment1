def reverse_complement(sequence):
    sequence=sequence.upper()
    complement=" "
    
    for i in range(len(sequence)):
        if sequence[i]=="A":
            complement=complement+"T"
        elif sequence[i]=="T":
            complement=complement+"A"
        elif sequence[i]=="G":
            complement=complement+"C"
        else:
            complement=complement+"G"
    return complement[::-1]

