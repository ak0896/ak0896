import math
# math.row(2,4)   #2의4승=16   ->제곱함수
# math.sqrt(4)    #루트4=2     ->제곱근함수


m,n=map(int,input().split())

def is_prime(x):
  if x==1:             
    return False
  for i in range(2,int(math.sqrt(x))+1):     
    if x%i==0:                              ##반만 확인하면 나머지는 약수이므로
      return False
  else : return True


for x in range(m,n+1):
  if (is_prime(x)==True):
    print(x)
  
