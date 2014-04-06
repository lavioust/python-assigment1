sequence=raw_input("write your sequence:")
a=sequence[::-1]
s=len(a)
t=" "
for counter in range(s):
     if   a[counter]=="T" or a[counter]=="t":
          t=t+"U"
     else:
          t=t+a[counter]
print t
        
