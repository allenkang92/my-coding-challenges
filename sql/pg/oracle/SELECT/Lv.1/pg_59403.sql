-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59403?language=oracle
-- 간단한 문제 설명 : 
--   ANIMAL_INS 테이블에서 모든 동물의 아이디와 이름을 ANIMAL_ID 순으로 조회해야 합니다.
--   결과는 ANIMAL_ID를 기준으로 오름차순 정렬합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--       ANIMAL_ID VARCHAR(N)   NOT NULL  -- 동물의 아이디
--       ANIMAL_TYPE VARCHAR(N) NOT NULL  -- 생물 종
--       DATETIME DATETIME     NOT NULL  -- 보호 시작일
--       INTAKE_CONDITION VARCHAR(N) NOT NULL  -- 보호 시작 시 상태
--       NAME VARCHAR(N)       NULL      -- 동물의 이름
--       SEX_UPON_INTAKE VARCHAR(N) NOT NULL  -- 성별 및 중성화 여부
--
-- 해결 방법 설명 :
--   1. ANIMAL_INS 테이블에서 ANIMAL_ID와 NAME 컬럼을 SELECT 합니다.
--   2. 모든 동물의 정보를 포함하기 위해 테이블 전체를 FROM 절에서 선택합니다.
--   3. ORDER BY 절을 사용하여 ANIMAL_ID를 오름차순(ASC)으로 정렬합니다.
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--       - N은 ANIMAL_INS 테이블의 총 행 수입니다. ORDER BY 절에 의해 N개의 행을 정렬하는 데 O(N log N)의 시간이 소요됩니다.
--   - 공간복잡도 : O(N)
--       - 정렬된 결과를 저장하는 데 O(N)의 추가 공간이 필요합니다.

SELECT 
    ANIMAL_ID, 
    NAME
FROM 
    ANIMAL_INS
ORDER BY 
    ANIMAL_ID ASC;