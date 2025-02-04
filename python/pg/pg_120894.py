# 문제 설명:
#   영어로 표기된 숫자를 정수로 변환하는 문제입니다.
#   예: "onetwothree" -> 123
#
# 해결 방법 설명:
#   - 각 영어 숫자 단어를 해당하는 숫자로 치환합니다.
#   - 최종 문자열을 정수로 변환하여 반환합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n) (n은 문자열 길이)
#   - 공간 복잡도: O(1)

def solution(numbers):
    if "zero" in numbers:
        numbers = numbers.replace("zero", "0")
    if "one" in numbers:
        numbers = numbers.replace("one", "1")
    if "two" in numbers:
        numbers = numbers.replace("two", "2")
    if "three" in numbers:
        numbers = numbers.replace("three", "3")
    if "four" in numbers:
        numbers = numbers.replace("four", "4")
    if "five" in numbers:
        numbers = numbers.replace("five", "5")
    if "six" in numbers:
        numbers = numbers.replace("six", "6")
    if "seven" in numbers:
        numbers = numbers.replace("seven", "7")
    if "eight" in numbers:
        numbers = numbers.replace("eight", "8")
    if "nine" in numbers:
        numbers = numbers.replace("nine", "9")
    answer = int(numbers)
    return answer