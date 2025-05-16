-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59035?language=oracle
-- 간단한 문제 설명 : 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하고, ANIMAL_ID의 역순으로 정렬하는 SQL 쿼리를 작성하세요.
-- 해결 방법 설명 :
--   1. ANIMAL_INS 테이블에서 NAME과 DATETIME 컬럼을 선택합니다.
--   2. ANIMAL_ID를 기준으로 내림차순 정렬하여 결과를 역순으로 표시합니다.
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(n log n) - ORDER BY 절로 인한 정렬 시간
--   - 공간복잡도 : O(n) - 결과 집합 저장 공간

-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;