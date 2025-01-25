-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59410?language=oracle
-- 간단한 문제 설명 :
--   - ANIMAL_INS 테이블에서 동물의 생물 종, 이름, 성별 및 중성화 여부를 조회
--   - 이름이 없는 동물의 경우, 이름을 'No name'으로 표시
--   - 결과는 ANIMAL_ID 기준 오름차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 (ANIMAL_INS):
--   - ANIMAL_ID         VARCHAR(N)    NOT NULL  -- 동물 아이디
--   - ANIMAL_TYPE       VARCHAR(N)    NOT NULL  -- 생물 종
--   - DATETIME          DATETIME      NOT NULL  -- 보호 시작일
--   - INTAKE_CONDITION  VARCHAR(N)    NOT NULL  -- 보호 시작 시 상태
--   - NAME              VARCHAR(N)         TRUE   -- 동물 이름 (NULL 가능)
--   - SEX_UPON_INTAKE   VARCHAR(N)    NOT NULL  -- 성별 및 중성화 여부
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. SELECT 절에서 필요한 컬럼(ANIMAL_TYPE, NAME, SEX_UPON_INTAKE)을 선택
--   2. CASE 문을 사용하여 NAME이 NULL인 경우 'No name'으로 대체
--   3. ORDER BY 절을 사용하여 ANIMAL_ID를 기준으로 오름차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼을 선택
--   - CASE WHEN ... THEN ... ELSE ... END: 조건에 따라 값을 변환
--   - IS NULL: 컬럼의 NULL 여부를 확인
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--
-- 쿼리 최적화 방법 :
--   - ANIMAL_ID 컬럼에 인덱스를 생성하면 ORDER BY 절의 성능을 향상시킬 수 있음
--   - NAME 컬럼에 인덱스를 생성하면 NULL 값을 빠르게 찾을 수 있음 (DBMS에 따라 다름)
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N) - ORDER BY 절로 인한 정렬 시간
--   - 공간복잡도 : O(N)       - 결과 집합 저장 공간

-- -------------------------------------------------------------------------------------------
-- 쿼리 작성
-- -------------------------------------------------------------------------------------------

SELECT 
    ANIMAL_TYPE,                                      -- 동물의 생물 종
    CASE
        WHEN NAME IS NULL THEN 'No name'              -- 이름이 NULL인 경우 'No name'으로 대체
        ELSE NAME                                     -- 그렇지 않은 경우 원래 이름 사용
    END AS NAME,                                       -- 결과 컬럼명: NAME
    SEX_UPON_INTAKE                                   -- 성별 및 중성화 여부
FROM 
    ANIMAL_INS                                        -- 데이터 소스 테이블
ORDER BY
    ANIMAL_ID ASC;                                    -- ANIMAL_ID 기준 오름차순 정렬