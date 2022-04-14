# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.


n = int(input())

if n == 1:
    print('')
for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n / i
