def read_fasta_file(fastafile):
    f=open(fastafile,"r")
    f.seek(0,0)
    x=f.readlines()
    t=" "
    for line in f:
        t=t+line
    return (x[0],t)