import math

m,n=map(int,input().split())

def is_prime(x):
  if x==1:
    return False
  for i in range(2,int(math.sqrt(x))+1):
    if x%i==0:
      return False
  else : return True

for x in range(m,n+1):
  if (is_prime(x)==True):
    print(x)
  