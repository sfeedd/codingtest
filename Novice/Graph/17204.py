import sys

input = sys.stdin.readline

# 첫 번째 줄에서 두 개의 정수 N과 M을 입력받습니다.
# N은 게임 리스트의 요소 개수이고, M은 찾고자 하는 특정 숫자입니다.      
N, M = map(int,input().split())

# 게임 리스트를 구성하는 숫자들을 입력받아 리스트에 저장합니다.
# 게임 리스트는 N개의 정수로 이루어져 있으며, 각 줄에 하나씩 입력됩니다.
gameList = [int(input()) for _ in range(N)]

# 변수 a에 게임 리스트의 첫 번째 요소를 저장합니다.
# 이는 탐색을 시작할 첫 번째 요소입니다.
a = gameList[0]

# 탐색 경로를 저장할 리스트 mylist를 초기화합니다.
mylist = []

# gameList의 길이만큼 반복하면서 다음 요소로 이동합니다.
for _ in range(len(gameList)):
    # 현재 위치의 요소 a를 mylist에 추가합니다.
    mylist.append(a)
    
    # 현재 요소 a가 가리키는 요소를 변수 b에 저장하고, 이를 다시 mylist에 추가합니다.
    b = gameList[a]
    mylist.append(b)
    
    # 다음 반복에서는 b를 기준으로 탐색을 계속합니다.
    a = gameList[b]

# mylist에 M이 있으면 그 위치의 인덱스를 찾아 1을 더한 값을 출력합니다.
# (1을 더하는 이유는 1부터 시작하는 위치를 출력하기 위함입니다.)
if M in mylist:
    print(mylist.index(M) + 1)
# mylist에 M이 없으면 -1을 출력합니다.
else:
    print('-1')
