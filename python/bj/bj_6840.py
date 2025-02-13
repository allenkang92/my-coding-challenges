# 문제 링크 (주석) : https://www.acmicpc.net/problem/6840
# 간단한 문제 설명 : 세 개의 무게를 입력받아 중간 무게를 출력하는 프로그램
# 해결 방법 설명 : 입력받은 무게를 리스트에 저장하고 정렬한 후, 중간값을 출력
# 시간/공간 복잡도 : O(1) (고정된 크기의 입력 및 정렬)

bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

bowl_list = []
bowl_list.append(bowl1)
bowl_list.append(bowl2)
bowl_list.append(bowl3)

bowl_list.sort()
print(bowl_list[int(len(bowl_list)/ 2)])