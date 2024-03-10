n=int(input())
n_list=list(map(int,input().split()))
max_n=max(n_list)
for x in range(len(n_list)):
  n_list[x]=n_list[x]/max_n*100
avg=sum(n_list)/n
print(round(avg,2))