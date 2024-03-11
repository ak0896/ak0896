a=int(input())
b=int(input())
print(a*(b%10))         # % 나머지
print(a*(b%100//10))    # // 몫
print(a*(b//100))
print(a*b)