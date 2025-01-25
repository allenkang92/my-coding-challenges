-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59404?language=oracle
-- 간단한 문제 설명 : 
--   동물의 아이디, 이름, 보호 시작일을 이름 순으로 조회하되,
--   이름이 같은 동물은 보호 시작일 역순으로 정렬합니다.
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
--   1. SELECT 절에서 필요한 컬럼만 선택 (ANIMAL_ID, NAME, DATETIME)
--   2. ORDER BY 절에서 다중 정렬 조건 사용:
--      - NAME ASC: 이름 기준 오름차순 (1차 정렬)
--      - DATETIME DESC: 보호 시작일 기준 내림차순 (2차 정렬)
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - ORDER BY로 인한 정렬
--   - 공간복잡도 : O(N) - 결과 저장 공간

SELECT 
    ANIMAL_ID,   -- 동물 아이디
    NAME,        -- 이름 
    DATETIME     -- 보호 시작일
FROM 
    ANIMAL_INS
ORDER BY 
    NAME ASC,      -- 이름 기준 오름차순 (1차 정렬)
    DATETIME DESC;  -- 보호 시작일 기준 내림차순 (2차 정렬)