import sys

# 재귀 깊이 해제: 기본 재귀 제한을 10000으로 설정하여 깊은 재귀 호출 허용
sys.setrecursionlimit(10000)

# 입력부
n, m = map(int, sys.stdin.readline().split())  # n: 두부 판의 행 개수, m: 두부 판의 열 개수
tofu = [list(sys.stdin.readline().rstrip()) for _ in range(n)]  # 두부 판의 상태를 저장 (A, B, C, D, F 등급)

# cost: 두부 등급 간의 비용을 담는 2차원 딕셔너리 생성
cost = dict().fromkeys(['A', 'B', 'C', 'D', 'F'])
for i in cost:
    cost[i] = dict().fromkeys(['A', 'B', 'C', 'D', 'F'], 0)

# 두부 등급 간 비용을 정의한 표 temp를 이용해 cost 딕셔너리에 할당
temp = [[10, 8, 7, 5, 1], [8, 6, 4, 3, 1], [7, 4, 3, 2, 1], [5, 3, 2, 2, 1], [1, 1, 1, 1, 0]]
for idx_i, i in enumerate(['A', 'B', 'C', 'D', 'F']):
    for idx_j, j in enumerate(['A', 'B', 'C', 'D', 'F']):
        cost[i][j] = temp[idx_i][idx_j]

# dp: 현재 i번째 칸에서 j번째 비트일 때 얻을 수 있는 두부 가격의 최대값을 저장하는 2차원 리스트
dp = [[-1] * (1 << m) for _ in range(n * m)]

# go 함수: i번째 칸에서 j번째 비트를 기준으로 두부 가격의 최대값을 구함
def go(num, bit):
    # 두부 판의 범위를 벗어나는 경우 0 반환 (더 이상 자를 칸이 없음)
    if num >= n * m:
        return 0
        
    # Memoization: 이미 계산된 경우 저장된 값 반환
    if dp[num][bit] != -1:
        return dp[num][bit]
    dp[num][bit] = 0  # 초기화
    
    # d: 현재 칸을 그냥 지나치는 경우 얻을 수 있는 두부 가격
    d = go(num + 1, bit >> 1)  # bit를 오른쪽으로 한 칸 밀어서 다음 칸으로 이동
    
    # 현재 dp 값과 d를 비교하여 더 큰 값을 저장
    dp[num][bit] = max(dp[num][bit], d)
    
    # 현재 칸에 비트가 설정되어 있으면 (이미 채워져 있는 경우) 다음 칸으로 이동
    if bit & 1 == 1:
        # a: 현재 칸을 그대로 지나치는 경우
        a = go(num + 1, bit >> 1)
        dp[num][bit] = max(dp[num][bit], a)
        
    # 현재 칸에 비트가 설정되어 있지 않으면 (채워져 있지 않은 경우) 다음 칸을 채우는 방법 탐색
    else:
        # 밑 칸이 범위를 벗어나지 않는 경우 (밑으로 두부를 잘라 붙일 수 있는 경우)
        if num + m < n * m and bit & 1 == 0:
            # b: 현재 칸과 밑 칸을 한 덩어리로 자르는 경우
            b = go(num + 1, bit >> 1 | (1 << (m - 1)))
            dp[num][bit] = max(dp[num][bit], b + cost[tofu[num // m][num % m]][tofu[(num + m) // m][(num + m) % m]])
        
        # 옆 칸이 범위를 벗어나지 않는 경우 (옆으로 두부를 잘라 붙일 수 있는 경우)
        if num % m != (m - 1) and bit & 2 == 0:
            # c: 현재 칸과 옆 칸을 한 덩어리로 자르는 경우
            c = go(num + 2, bit >> 2)
            dp[num][bit] = max(dp[num][bit], c + cost[tofu[num // m][num % m]][tofu[(num + 1) // m][(num + 1) % m]])
    return dp[num][bit]

# 최종 결과 출력: 0번째 칸에서 비트 0인 상태에서 시작하여 최대 두부 가격을 구함
print(go(0, 0))
