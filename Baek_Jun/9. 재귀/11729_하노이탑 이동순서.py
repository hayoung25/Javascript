# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.

# 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# 예제 입력 1
# 3
# 예제 출력 1
# 7
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    # moving n-1 tiles from start to sub-poll
    hanoi_tower(n-1, start, 6-start-end)
    print(start, end)  # moving the biggest tile to the end-poll
    hanoi_tower(n-1, 6-start-end, end) # moving the remaining tiles on sub-poll to end-poll



n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
