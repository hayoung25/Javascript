# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.

num = int(input())
prime_numbers = list(map(int, input().split()))

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

count = 0
for i in prime_numbers:
    if prime(i):
        count += 1
print(count)

