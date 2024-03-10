x=int(input())
n=int(input())
result=0
for i in range(n):
  a,b=list(map(int,input().split()))
  result+=a*b

#n까지 반복한 값을 확인
if result==x:
    print("Yes")
else: print("No")