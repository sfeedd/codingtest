import sys

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수 입력

for i in range(T):
    stack = []  # 여는 괄호를 저장할 스택
    a = input()  # 괄호 문자열 입력
    
    for j in a:
        if j == '(':  
            # 여는 괄호 '('일 경우 스택에 추가
            stack.append(j)
        elif j == ')':
            if stack:  
                # 닫는 괄호 ')'일 경우 스택에 여는 괄호가 있다면 하나 제거
                stack.pop()
            else:  
                # 스택이 비어있는데 닫는 괄호가 나온 경우는 올바르지 않은 괄호 문자열
                print("NO")
                break  # 더 이상 확인할 필요가 없으므로 루프 종료
    else:  
        # break문으로 루프가 중단되지 않은 경우에만 실행 (모든 문자를 확인한 경우)
        if not stack:  
            # 스택이 비어있다면 모든 괄호가 짝을 이루는 경우
            print("YES")
        else:  
            # 스택에 여는 괄호가 남아 있다면 짝이 맞지 않는 경우
            print("NO")
