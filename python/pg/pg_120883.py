# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 간단한 문제 설명 : 
#   입력된 아이디/비밀번호와 데이터베이스를 비교하여 로그인 결과를 반환하는 문제입니다.
#   - 아이디/비밀번호 모두 일치: "login"
#   - 아이디만 일치: "wrong pw" 
#   - 아이디 불일치: "fail"
#
# 해결 방법 설명 : 
#   - 데이터베이스의 각 항목과 입력된 아이디/비밀번호를 비교합니다.
#   - 아이디가 일치하는 경우, 비밀번호를 확인합니다.
#   - 일치하는 아이디가 없으면 "fail"을 반환합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) (n은 db의 길이)
#   - 공간 복잡도: O(1)

def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:  # 아이디가 일치하는 경우
            if id_pw[1] == i[1]:  # 비밀번호도 일치
                return "login"
            else:  # 비밀번호가 불일치
                return "wrong pw"
    return "fail"  # 일치하는 아이디가 없음