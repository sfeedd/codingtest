import sys
input = sys.stdin.readline  # 빠른 입력을 위한 sys.stdin.readline 사용

T = int(input())  # 테스트 케이스의 개수 입력
for _ in range(T):
    N = int(input())  # 각 테스트 케이스에서 스티커 열의 개수 입력
    arr = [list(map(int, input().split())) for _ in range(2)]  # 2행 배열로 스티커 점수 입력

    # 2행 DP 배열 생성 (DP[i][j]는 i번째 행의 j번째 열을 선택했을 때 얻을 수 있는 최대 점수)
    DP = [[0] * N for _ in range(2)]

    # 스티커 열이 1개일 경우 (길이가 1)
    DP[0][0] = arr[0][0]  # 첫 번째 행의 첫 번째 열 선택
    DP[1][0] = arr[1][0]  # 두 번째 행의 첫 번째 열 선택
    if N == 1:
        # 스티커가 1개뿐이라면 두 값 중 최대값 출력 후 다음 테스트 케이스로 이동
        print(max(DP[0][0], DP[1][0]))
        continue

    # 스티커 열이 2개일 경우 (길이가 2)
    DP[0][1] = arr[1][0] + arr[0][1]  # 첫 번째 행 두 번째 열 선택 시 점수
    DP[1][1] = arr[0][0] + arr[1][1]  # 두 번째 행 두 번째 열 선택 시 점수
    if N == 2:
        # 스티커가 2개인 경우 두 DP 값 중 최대값 출력 후 다음 테스트 케이스로 이동
        print(max(DP[0][1], DP[1][1]))
        continue

    # 스티커 열이 3개 이상인 경우 (일반화)
    for i in range(2, N):
        # 첫 번째 행에서 i번째 열을 선택했을 때:
        # 1) 두 번째 행의 (i-2)번째 열을 선택한 경우
        # 2) 두 번째 행의 (i-1)번째 열을 선택한 경우
        # 중 더 큰 값에 현재 스티커 값을 더함
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i]
        
        # 두 번째 행에서 i번째 열을 선택했을 때:
        # 1) 첫 번째 행의 (i-2)번째 열을 선택한 경우
        # 2) 첫 번째 행의 (i-1)번째 열을 선택한 경우
        # 중 더 큰 값에 현재 스티커 값을 더함
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]

    # 마지막 열에서 첫 번째 행과 두 번째 행의 최대값 출력
    print(max(DP[0][-1], DP[1][-1]))
