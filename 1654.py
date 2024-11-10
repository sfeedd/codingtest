import sys

# 입력받은 두 수 n, k를 변수로 저장 (n은 랜선의 개수, k는 필요한 랜선의 개수)
n, k = map(int, sys.stdin.readline().split())

# 다음 줄들에 입력된 랜선의 길이를 리스트에 저장
lans = list(map(int, sys.stdin.readlines()))    

# 이분 탐색을 위한 초기값 설정
# pl은 최소 길이 1, pr은 현재 랜선 중 가장 긴 길이로 설정
pl, pr = 1, max(lans)
ans = 0  # 최종 답을 저장할 변수 초기화

# 이분 탐색 시작
while pl <= pr:
    # 중간값(mid)을 계산하여 현재 시도하는 랜선의 길이로 설정
    mid = (pl + pr) // 2
    tmp = 0  # 현재 길이로 랜선을 잘랐을 때 나오는 개수 합계를 저장할 변수 초기화

    # 모든 랜선에 대해 현재 길이로 나눈 몫을 tmp에 더함
    # (즉, 각 랜선이 현재 길이로 몇 개의 랜선으로 잘릴 수 있는지를 계산)
    for lan in lans:
        tmp += lan // mid

    # 잘린 랜선의 총 개수가 필요한 랜선 개수 k보다 작으면, 길이를 줄여야 하므로 범위를 왼쪽으로 줄임
    if tmp < k:
        pr = mid - 1
    # 잘린 랜선의 총 개수가 k보다 크거나 같으면, 길이를 늘려도 되므로 범위를 오른쪽으로 줄임
    # 동시에 현재 mid 값을 정답 후보로 저장
    else:
        pl = mid + 1
        ans = mid  # 현재 mid 값을 최종 답에 저장 (최대 길이를 찾기 위함)

# 최종적으로 ans 출력 (가능한 랜선의 최대 길이)
print(ans)
