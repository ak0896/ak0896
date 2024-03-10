n=int(input())
result=""
for a in range(1,n+1):
  if a<n:
    result=(" "*(n-a)+"*"*a)
  else:
    result="*"*a
  print(result)