-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/59042
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블을 활용하여 관리자의 실수로 일부 동물의 입양일이 보호 시작일보다 빠르게 입력된 동물의 정보를 조회
--   - 조회 항목: ANIMAL_ID, NAME
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
--   1. ANIMAL_OUTS 테이블에서 ANIMAL_INS 테이블에 존재하지 않는 ANIMAL_ID를 가진 동물을 필터링
--   2. 해당 동물들의 ANIMAL_ID와 NAME을 선택
--   3. 결과를 ANIMAL_ID 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT : 특정 컬럼을 선택하여 조회
--   - WHERE 절 : 조건에 맞는 레코드를 필터링
--   - NOT IN 절 : 서브쿼리의 결과에 포함되지 않는 값을 선택
--   - ORDER BY : 특정 컬럼을 기준으로 정렬

-- 쿼리 최적화 방법 :
--   - ANIMAL_INS 및 ANIMAL_OUTS 테이블의 ANIMAL_ID 컬럼에 인덱스를 생성하여 서브쿼리 및 필터링 성능 향상
--     예시:
--       CREATE INDEX idx_animal_ins_id ON ANIMAL_INS(ANIMAL_ID);
--       CREATE INDEX idx_animal_outs_id ON ANIMAL_OUTS(ANIMAL_ID);
--   - 필요한 컬럼만 SELECT 절에 포함시켜 불필요한 데이터 스캔 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), ANIMAL_OUTS 테이블을 전체 스캔하여 필터링 수행
--   - 공간복잡도 : O(K), K는 유실된 기록의 수

SELECT 
    ANIMAL_ID, 
    NAME
FROM 
    ANIMAL_OUTS 
WHERE 
    ANIMAL_ID NOT IN (
        SELECT ANIMAL_ID 
        FROM ANIMAL_INS
    )
ORDER BY 
    ANIMAL_ID ASC;