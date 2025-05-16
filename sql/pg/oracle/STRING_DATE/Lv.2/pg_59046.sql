-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59046?language=oracle
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블에서 이름이 'Lucy' 또는 'Ella'인 동물의 ANIMAL_ID, NAME, SEX_UPON_INTAKE를 조회
--   - 결과는 ANIMAL_ID를 기준으로 오름차순 정렬

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
--   1. ANIMAL_INS 테이블에서 ANIMAL_ID, NAME, SEX_UPON_INTAKE 컬럼을 선택
--   2. WHERE 절을 사용하여 NAME이 'Lucy' 또는 'Ella'인 행을 필터링
--   3. ORDER BY 절을 사용하여 ANIMAL_ID를 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - FROM: 데이터를 조회할 테이블을 지정
--   - WHERE: 조건에 맞는 행을 필터링
--   - IN: 여러 값 중 하나와 일치하는지 확인
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬

-- 쿼리 최적화 방법 :
--   - NAME 컬럼에 인덱스를 생성하여 WHERE 절의 필터링 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_animal_name ON ANIMAL_INS(NAME);
--   - 필요한 컬럼만 SELECT 절에 포함하여 불필요한 데이터 스캔을 줄임

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 필터링과 정렬을 수행
--   - 공간복잡도 : O(K)
--     -- 결과 집합을 저장하는 데 필요한 공간 (K는 조건에 맞는 동물의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    ANIMAL_ID,                             -- 동물의 고유 ID
    NAME,                                  -- 동물의 이름
    SEX_UPON_INTAKE                        -- 성별 및 중성화 여부
FROM 
    ANIMAL_INS
WHERE 
    NAME IN ('Lucy', 'Ella')                -- 이름이 'Lucy' 또는 'Ella'인 동물 필터링
ORDER BY 
    ANIMAL_ID ASC;                         -- ANIMAL_ID를 기준으로 오름차순 정렬

-- -------------------------------------------------------------------------------------------
-- 쿼리 오류 수정:
-- 오류 메시지: 없음
-- 원인:
--   - 기존 쿼리는 모든 지정된 이름을 포함하지만, 문제의 의도는 'Lucy'와 'Ella'만 포함하는 것일 수 있음
-- 해결 방법:
--   - WHERE 절에서 IN 리스트를 'Lucy'와 'Ella'로 제한
-- -------------------------------------------------------------------------------------------