import sys

input = sys.stdin.readline

N = int(input()) # 재료의 개수를 입력 받음
materials = list(map(int, input().split(" "))) # 각 재료의 맛 정도을 리스트로 입력 받음

def solution(N, materials):
    answer = 0 # 결과값을 저장할 변수
    pre_material = 987654321 # 이전 재료의 맛 정도을 저장할 변수, 큰 값을 초기값으로 설정
    max_material = 0 # 지금까지 나온 재료 맛 정도중 최대 값을 저장할 변수
    up_flag = True # 재료의 맛 정도가 증가하고 있는지 확인하는 플래그
   
    for material in materials: # 모든 재료를 순회
        max_material = max(max_material, material) # 현재 재료의 맛 정도와 최대 재료 맛 정도을 비교하여 업데이트

        if up_flag: # 증가하는 구간일 경우
            pre_material = material
            answer += material # 현재 재료 정도를 결과에 더함

            if max_material > material: # 최대 재료 맛 정도가 현재 재료 맛 정도보다 크면 감소 구간으로 진입
                up_flag = False

        else: # 감소하는 구간일 경우
            if pre_material < material: # 이전 재료 맛 정도가 현재 재료 맛 정도보다 작으면 문제가 되므로 0 출력
                print(0)
                return

            pre_material = material
            answer += material # 현재 재료의 맛 정도를 결과에 더함

    print(answer) # 최종 결과 출력
    return

solution(N, materials) # 함수 호출