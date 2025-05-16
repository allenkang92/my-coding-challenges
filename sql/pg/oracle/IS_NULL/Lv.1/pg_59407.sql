-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59407?language=oracle
-- 간단한 문제 설명 : 
--   동물 보호소에 들어온 동물 중 이름이 있는 동물의 ID를 조회합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--   - 컬럼정보:
--       ANIMAL_ID VARCHAR(N)    NOT NULL  -- 동물 아이디
--       ANIMAL_TYPE VARCHAR(N)  NOT NULL  -- 생물 종
--       DATETIME DATETIME       NOT NULL  -- 보호 시작일
--       INTAKE_CONDITION VARCHAR(N) NOT NULL  -- 보호 시작시 상태
--       NAME VARCHAR(N)         TRUE      -- 이름
--       SEX_UPON_INTAKE VARCHAR(N) NOT NULL  -- 성별 및 중성화 여부
--
-- 해결 방법 설명 :
--   1. WHERE절에서 NAME IS NOT NULL 조건으로 이름이 있는 동물 필터링
--   2. ORDER BY로 ANIMAL_ID 오름차순 정렬
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - 정렬로 인해
--   - 공간복잡도 : O(N) - 결과 저장 공간

SELECT 
    ANIMAL_ID  -- 동물 아이디만 조회
FROM 
    ANIMAL_INS
WHERE 
    NAME IS NOT NULL  -- 이름이 NULL이 아닌 동물만 선택
ORDER BY 
    ANIMAL_ID ASC;  -- 동물 아이디 기준 오름차순 정렬