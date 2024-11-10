import sys
n = int(sys.stdin.readline())  # n: 행렬의 개수

# matrix: 각 행렬의 행(row)과 열(column) 크기를 담는 리스트
matrix = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append((a, b))  # (행, 열) 크기로 튜플 저장

# d: DP를 위한 메모이제이션 배열로, d[x][y]는 x번째 행렬부터 y번째 행렬까지의 최소 곱셈 연산 수를 의미
d = [[-1] * n for _ in range(n)]  # 초기값 -1로 설정하여 아직 계산되지 않은 상태를 표시

# go: 점화식을 사용한 Top-Down 방식 DP 함수로, x번째 행렬부터 y번째 행렬까지의 최소 곱셈 횟수를 구함
def go(x, y):
    # 이미 d[x][y]가 계산된 경우, 메모이제이션을 통해 저장된 값 반환
    if d[x][y] != -1:
        return d[x][y]
    
    # 곱셈은 최소 두 개 이상의 행렬이 필요하므로, x와 y가 같으면 곱셈이 불가능하여 0 반환
    if x == y:
        return 0
    
    # x와 y가 연속된 두 행렬이라면, 단순히 두 행렬의 곱셈 연산 횟수를 반환
    if x + 1 == y:
        return matrix[x][0] * matrix[x][1] * matrix[y][1]
    
    # x번째 행렬부터 y번째 행렬까지의 최소 곱셈 횟수를 구하기 위해,
    # k를 x에서 y-1까지 이동하며 최소 곱셈 연산을 찾음
    for k in range(x, y):
        # x부터 k까지의 최소 곱셈 횟수(left)와 k+1부터 y까지의 최소 곱셈 횟수(right)를 재귀 호출로 구함
        left = go(x, k)
        right = go(k + 1, y)
        
        # x~k와 k+1~y의 두 부분 행렬을 곱하는 데 필요한 연산 횟수를 계산하여
        # d[x][y]에 최소 값을 저장 (현재 저장된 값보다 작으면 갱신)
        cost = left + right + matrix[x][0] * matrix[k][1] * matrix[y][1]
        if d[x][y] == -1 or d[x][y] > cost:
            d[x][y] = cost
    
    return d[x][y]

# 0번째 행렬부터 n-1번째 행렬까지의 최소 곱셈 연산 횟수를 구하여 출력
print(go(0, n - 1))
