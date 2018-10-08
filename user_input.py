def armstrong(n):
 sum=0
 t=n
 while(t>0):
  d=t%10
  sum=d**3
  d=t//10
 return sum
n=int(input())
y=armstrong (n)
print(y)
