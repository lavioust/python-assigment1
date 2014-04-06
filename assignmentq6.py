sequences=["TGAC","aattggcc","ccCCcc"]
a=len(sequences)
counter=0
for index in range(a):
    counter=counter+len(sequences[index])
print counter/a
