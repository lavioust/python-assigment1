dna=raw_input("put dna sequence:")
if len(dna)<6:
      print "sequence is too short"
else:
      print dna[:3], dna[-3:]
