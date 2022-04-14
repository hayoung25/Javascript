# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x = [a, c, e]
y = [b, d, f]

answer = []
for i in x:
    if x.count(i) == 2:
        continue
    if x.count(i) == 1:
        answer.append(i)

for i in y:
    if y.count(i) == 2:
        continue
    if y.count(i) == 1:
        answer.append(i)

print(str(answer[0]) + " " + str(answer[1]))         