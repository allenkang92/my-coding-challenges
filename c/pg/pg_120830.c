// 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120830
// 간단한 문제 설명 : 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return
// 해결 방법 설명 : 단순 뺄셈 수행
// 시간/공간 복잡도 : O(1)

#include <stdio.h>
// 표준 입출력: scanf, printf 함수를 사용하기 위한 헤더
#include <stdbool.h>
// bool 타입 사용을 위한 헤더 (true/false 값 지원)
#include <stdlib.h>
// 일반 유틸리티 함수 및 동적 메모리 관리를 위한 헤더

int solution(int num1, int num2) {
    // num1에서 num2를 뺀 결과를 계산하여 반환
    return num1 - num2;
}

int main() {
    // 프로그램의 시작점(main 함수)
    // 두 정수를 저장할 변수 선언
    int num1, num2;

    // 사용자로부터 두 정수를 입력 받음 (공백 구분)
    // scanf가 읽어들인 항목 수가 2가 아니면, 입력 오류로 판단하고 종료
    if (scanf("%d %d", &num1, &num2) != 2) return 0;

    // solution 함수를 호출하여 결과 계산 후 출력
    printf("%d", solution(num1, num2));

    // 0 반환으로 정상 종료를 운영체제에 알림
    return 0;
}