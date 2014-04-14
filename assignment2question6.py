def get_fasta(sequence,identity):
    identity=">"+identity
    lines=" "
    for i in range(len(sequence)):
        if i%60!=0:
            lines=lines+sequence[i]
        else:
            lines=lines+"\n"+sequence[i]
    print identity
    return lines



