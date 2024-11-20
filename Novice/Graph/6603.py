import sys
from itertools import combinations  # 조합을 생성하기 위한 모듈

input = sys.stdin.readline  # 빠른 입력을 위한 sys.stdin.readline 사용

while True:
    # 입력받은 한 줄을 공백 기준으로 나눠 정수 리스트로 변환
    nums = list(map(int, input().split()))
    
    # 입력값이 [0]인 경우 반복문 종료
    if len(nums) == 1 and nums[0] == 0:
        break

    # 첫 번째 숫자는 집합의 크기이므로 제거
    length = nums.pop(0)

    # nums에서 6개의 숫자를 조합으로 선택
    for comb in combinations(nums, 6):
        # 선택된 조합(comb)을 문자열로 변환하여 공백으로 연결
        temp = list(map(str, comb))
        print(" ".join(temp))
    
    # 각 테스트 케이스 출력 후 빈 줄 추가
    print()
