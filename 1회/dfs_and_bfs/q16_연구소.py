# 나의 풀이
from collections import deque
import itertools
import copy

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph_ori = []
for i in range(n):
    graph_ori.append(list(map(int, input().split())))
graph_test = copy.deepcopy(graph_ori)

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 리스트에서 값이 0인 요소들의 위치 찾기
list_0 = [[i, j] for i in range(n) for j in range(m) if graph_ori[i][j] == 0]

# 2차원 리스트에서 값이 2인 요소들의 위치 찾기
list_2 = [[i, j] for i in range(n) for j in range(m) if graph_ori[i][j] == 2]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 연구소를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph_test[nx][ny] == 1:
                continue
            # 바이러스가 퍼진 영역으로 기록
            if graph_test[nx][ny] == 0:
                graph_test[nx][ny] = 2
                queue.append((nx, ny))
    return


# 벽 3개를 세울 수 있는 조합
answer = 0
for x in itertools.combinations(list_0, 3):

    graph_test[x[0][0]][x[0][1]] = 1  # 벽 세우기1
    graph_test[x[1][0]][x[1][1]] = 1  # 벽 세우기2
    graph_test[x[2][0]][x[2][1]] = 1  # 벽 세우기3

    # 바이러스 퍼트리기(BFS)
    for y in list_2:
        bfs(y[0], y[1])

    # 안전 영역의 크기 구하기
    size = 0
    for i in range(n):
        for j in range(m):
            if graph_test[i][j] == 0:
                size += 1

    if answer < size:
        answer = size

    graph_test = copy.deepcopy(graph_ori)

print(answer)

# 책의 풀이
n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 해당 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계싼
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result,get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)

