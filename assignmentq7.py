a=1
b=2
total=0
for i in range(17):
      if a%5==0:
         total=total+a
      a,b=b,a+b
print total
