import sys
input = sys.stdin.readline  # 표준 입력을 사용하기 위해 sys 모듈에서 stdin을 가져옴

# 첫 번째 줄에서 두 개의 정수 n, m을 입력받아 각각 n과 m에 저장
n, m = map(int, input().split())

# 두 번째 줄에서 집합 a의 원소들을 입력받아 정수형으로 변환 후 집합 a에 저장
a = set(map(int, input().split()))

# 세 번째 줄에서 집합 b의 원소들을 입력받아 정수형으로 변환 후 집합 b에 저장
b = set(map(int, input().split()))

# 집합 a에서 집합 b를 뺀 차집합을 구하여 res에 저장
res = a - b

# 차집합이 존재하면, 원소의 개수와 오름차순 정렬된 결과를 출력
if res:
    print(len(res))  # 차집합의 원소 개수를 출력
    print(*sorted(list(res)))  # 차집합의 원소들을 정렬하여 출력
else:
    # 차집합이 비어 있으면 0을 출력
    print(0)
