import sys

input = sys.stdin.readline

n = int(input())  # 수열의 길이 입력

num_list = list(map(int, input().split()))  # 수열 입력

# dp[i]: i번째 원소를 마지막으로 하는 최장 감소 부분 수열의 길이
dp = [1] * n  # 초기값은 모두 1로 설정 (각 숫자만 포함할 때의 길이)

# i번째 원소까지의 최장 감소 부분 수열 길이를 계산
for i in range(n):
    for j in range(0, i):  # i 이전의 모든 원소와 비교
        if num_list[i] < num_list[j]:  
            # i번째 원소가 j번째 원소보다 작다면 감소 조건을 만족
            # dp[i]를 dp[j] + 1과 비교하여 더 큰 값으로 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열 중 가장 큰 값이 최장 감소 부분 수열의 길이
print(max(dp))
