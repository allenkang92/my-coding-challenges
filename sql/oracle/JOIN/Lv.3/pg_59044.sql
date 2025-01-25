-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59044
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블을 활용하여 입양되지 않은 동물 중 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
--   - 결과는 보호 시작일 순으로 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : 
--     - ANIMAL_INS
--       - ANIMAL_ID          VARCHAR(N)    NOT NULL  -- 동물의 아이디
--       - ANIMAL_TYPE        VARCHAR(N)    NOT NULL  -- 동물의 종류
--       - DATETIME           DATETIME      NOT NULL  -- 보호 시작일
--       - INTAKE_CONDITION   VARCHAR(N)    NOT NULL  -- 보호 시작 시 상태
--       - NAME               VARCHAR(N)               -- 동물의 이름
--       - SEX_UPON_INTAKE    VARCHAR(N)    NOT NULL  -- 성별 및 중성화 여부
--
--     - ANIMAL_OUTS
--       - ANIMAL_ID          VARCHAR(N)    NOT NULL  -- 동물의 아이디
--       - ANIMAL_TYPE        VARCHAR(N)    NOT NULL  -- 동물의 종류
--       - DATETIME           DATETIME      NOT NULL  -- 입양일
--       - NAME               VARCHAR(N)               -- 동물의 이름
--       - SEX_UPON_OUTCOME   VARCHAR(N)    NOT NULL  -- 성별 및 중성화 여부

-- 해결 방법 설명 :
--   1. ANIMAL_INS 테이블에서 ANIMAL_OUTS 테이블에 등록되지 않은 ANIMAL_ID를 필터링
--   2. 보호 시작일(DATETIME)을 기준으로 오름차순 정렬
--   3. 상위 3개의 동물을 조회

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT : 특정 컬럼을 선택하여 조회
--   - WHERE 절 : 조건에 맞는 레코드를 필터링
--   - NOT IN 절 : 특정 값들이 포함되지 않은 레코드를 선택
--   - ORDER BY : 특정 컬럼을 기준으로 정렬
--   - FETCH FIRST 3 ROWS ONLY : 상위 3개 행만 조회

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - ANIMAL_OUTS 테이블의 ANIMAL_ID 컬럼에 인덱스를 생성하여 WHERE 절의 서브쿼리 성능 향상
--     예시:
--       CREATE INDEX idx_animal_outs_animal_id ON ANIMAL_OUTS(ANIMAL_ID);
--   - ANIMAL_INS 테이블의 DATETIME 컬럼에 인덱스를 생성하여 ORDER BY 절의 정렬 성능 향상

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), ANIMAL_INS 테이블을 전체 스캔하여 필터링 및 정렬
--   - 공간복잡도 : O(1), 결과 집합의 크기가 고정되어 있음

SELECT 
    NAME, 
    DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID 
    FROM ANIMAL_OUTS
)
ORDER BY DATETIME ASC
FETCH FIRST 3 ROWS ONLY;