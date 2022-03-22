# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

m, n = map(int, input().split())

for i in range(m , n+1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) +1):
        if i % j == 0:      
            break
    print(i)
