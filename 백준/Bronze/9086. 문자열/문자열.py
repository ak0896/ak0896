t=int(input())
t_list=[input() for _ in range(t)]
for x in t_list:
  print(x[0]+x[-1])
print()