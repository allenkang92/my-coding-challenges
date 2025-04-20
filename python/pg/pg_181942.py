# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181942
# 간단한 문제 설명 : 길이가 같은 두 문자열 str1과 str2의 각 문자가 번갈아 등장하는 문자열을 만들어 반환합니다.
# 해결 방법 설명 : for문을 사용해 두 문자열의 각 인덱스에 있는 문자를 번갈아 추가한 후, join() 메서드로 하나의 문자열로 합칩니다.
# 시간/공간 복잡도 : O(n) (두 문자열의 길이에 비례)

def solution(str1, str2):
    answer = []  # 결과 문자열의 각 문자들을 저장할 리스트입니다.
    for ch in range(len(str1)):  # 두 문자열의 길이는 같으므로, str1의 전체 인덱스를 순회합니다.
        answer.append(str1[ch])  # str1에 있는 현재 인덱스의 문자를 리스트에 추가합니다.
        answer.append(str2[ch])  # 이어서 str2에 있는 현재 인덱스의 문자를 리스트에 추가합니다.
    return "".join(answer)  # 리스트에 저장된 문자들을 하나의 문자열로 결합하여 반환합니다.