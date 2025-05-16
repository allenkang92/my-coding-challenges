-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59414?language=oracle
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블에서 모든 동물의 ANIMAL_ID, NAME, 들어온 날짜를 조회
--   - DATETIME을 DATE 타입으로 변환
--   - 결과는 ANIMAL_ID 순으로 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - ANIMAL_INS 테이블:
--     - ANIMAL_ID         VARCHAR(N)    NOT NULL  -- 동물 아이디
--     - ANIMAL_TYPE       VARCHAR(N)    NOT NULL  -- 생물 종
--     - DATETIME          DATETIME      NOT NULL  -- 보호 시작일
--     - INTAKE_CONDITION  VARCHAR(N)    NOT NULL  -- 보호 시작 시 상태
--     - NAME              VARCHAR(N)         TRUE    -- 동물 이름 (NULL 가능)
--     - SEX_UPON_INTAKE   VARCHAR(N)    NOT NULL  -- 성별 및 중성화 여부
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. ANIMAL_INS 테이블에서 ANIMAL_ID, NAME, DATETIME을 선택
--   2. DATETIME을 TRUNC 함수를 사용하여 DATE 타입으로 변환
--   3. ANIMAL_ID를 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼 선택
--   - TRUNC: DATETIME의 시간 부분을 제거하여 DATE 타입으로 변환
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬

-- 쿼리 최적화 방법 :
--   - ANIMAL_ID 컬럼에 인덱스를 생성하여 정렬 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_animal_id ON ANIMAL_INS(ANIMAL_ID);
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 테이블 전체 스캔 후 정렬
--   - 공간복잡도 : O(K) - 결과 저장 공간 (K는 총 동물 수)
-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    ANIMAL_ID,                            -- 동물의 ID
    NAME,                                 -- 동물의 이름
    TRUNC(DATETIME) AS 날짜                -- DATETIME을 DATE 타입으로 변환
FROM 
    ANIMAL_INS
ORDER BY 
    ANIMAL_ID ASC;                        -- ANIMAL_ID를 기준으로 오름차순 정렬