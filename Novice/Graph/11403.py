import sys

input = sys.stdin.readline()

from collections import deque

if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0]*N for _ in range(N)]     # 주어진 graph랑 똑같은 모양의 행렬, 정답
    
    for node in range(N):  # 0번 정점부터 N-1번 정점을 다 확인, 정점이 몇개인지 알기 때문에 정점을 기준으로 정보를 확인한다.
        Q = deque()
        Q.append(node)
        while Q:
            n = Q.popleft()               # 현재 노드 n
            for col in range(N):      # NxN, 열 정보를 확인 
                if graph[n][col] == 1 and ans[node][col] == 0 :  # 정점n과 열 정보 col 정점이 연결(1) 되어 있고 node에서 col을 처음 확인하는경우
                    Q.append(col)                         # 연결된 다음 정점으로 이동 
                    ans[node][col] = 1                         # 정점이 간선을 통해 연결되면 1 
        
        print(*ans[node])