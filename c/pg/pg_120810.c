// 문제 링크 : [https://school.programmers.co.kr/learn/courses/30/lessons/120810?language=c](https://school.programmers.co.kr/learn/courses/30/lessons/120810?language=c)
// 간단한 문제 설명 : 정수 num1과 num2가 주어질 때, num1을 num2로 나눈 나머지를 반환
// 해결 방법 설명 : % 연산자를 사용하여 나머지 계산
// 시간/공간 복잡도 : O(1)

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = num1 % num2;
    return answer;
}

// 로컬 실행용 main 함수
int main() {
    int num1, num2;
    // 두 정수 입력 받기
    if (scanf("%d %d", &num1, &num2) != 2) return 0;
    // solution 호출 및 결과 출력
    printf("%d", solution(num1, num2));
    return 0;
}