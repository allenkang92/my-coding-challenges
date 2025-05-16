-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59037?language=oracle
-- 간단한 문제 설명 : ANIMAL_INS 테이블에서 아픈 동물의 ANIMAL_ID와 NAME을 조회하고, ANIMAL_ID 순으로 오름차순 정렬하는 SQL 쿼리를 작성하세요.
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--   - 컬럼명 및 타입 :
--     - ANIMAL_ID VARCHAR(N) FALSE
--     - ANIMAL_TYPE VARCHAR(N) FALSE
--     - DATETIME DATETIME FALSE
--     - INTAKE_CONDITION VARCHAR(N) FALSE
--     - NAME VARCHAR(N) TRUE
--     - SEX_UPON_INTAKE VARCHAR(N) FALSE
-- 해결 방법 설명 :
--   1. ANIMAL_INS 테이블에서 INTAKE_CONDITION이 'Aged'가 아닌 행을 필터링합니다.
--   2. 필터링된 행들 중 ANIMAL_ID와 NAME 컬럼을 선택합니다.
--   3. ANIMAL_ID를 기준으로 오름차순으로 정렬합니다.
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(n log n) - ORDER BY 절로 인한 정렬 시간
--   - 공간복잡도 : O(n) - 정렬된 결과를 저장하기 위한 공간

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;