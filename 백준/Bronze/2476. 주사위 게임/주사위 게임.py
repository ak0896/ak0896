n=int(input())
max_money=0
for i in range(1,n+1):
  tmp=input().split()     #숫자를 문자화
  tmp.sort()              #오름차순으로 정렬
  a,b,c=map(int,tmp)        #list문자열이 숫자화되서 출력

  if a==b and b==c :      #같은눈3개
    money = 10000+(a*1000)
  elif a==b or a==c:      #같은눈2개 중에서 우선순위높으걸 먼저 작성
    money = 1000+(a*100)
  elif b==c:              #같은눈2개
    money = 1000+(b*100)
  else :                  #모두 다른눈일 경우 가장 큰수(위에서 정렬했음) 
    money = c*100

  if max_money<money:
    max_money=money
print(max_money)