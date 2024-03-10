a,b=map(int,input().split())
k=list(map(int,input().split()))
n=a*b
for x in k:
  print(x-n, end=' ')