-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59043
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
--   1. ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블을 ANIMAL_ID로 INNER JOIN하여 입양된 동물과 보호 정보를 결합
--   2. WHERE 절에서 입양일(DATETIME)이 보호 시작일보다 빠른 동물들을 필터링 (B.DATETIME - A.DATETIME < 0)
--   3. 보호 시작일(DATETIME)을 기준으로 오름차순 정렬
--   4. 필요한 컬럼(ANIMAL_ID, NAME)을 선택하여 결과를 제한 없이 조회

-- 사용한 SQL 문법 및 함수 설명 :
--   - INNER JOIN : 두 테이블을 ANIMAL_ID 기준으로 결합하여 관련된 레코드를 가져옴
--   - WHERE 절 : 조건에 맞는 레코드를 필터링
--   - 날짜 연산 : 입양일과 보호 시작일을 비교하여 잘못 입력된 데이터를 식별
--   - ORDER BY : 보호 시작일을 기준으로 결과를 정렬

-- 쿼리 최적화 방법 :
--   - ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블의 ANIMAL_ID 컬럼에 인덱스를 생성하여 JOIN 성능 향상
--     예시:
--       CREATE INDEX idx_animal_ins_id ON ANIMAL_INS(ANIMAL_ID);
--       CREATE INDEX idx_animal_outs_id ON ANIMAL_OUTS(ANIMAL_ID);
--   - 필요한 컬럼만 SELECT 절에 포함시켜 불필요한 데이터 스캔 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 ANIMAL_INS 테이블의 총 행 수
--     -- 모든 행을 스캔하여 JOIN 및 필터링 수행
--   - 공간복잡도 : O(1), 결과 집합의 크기가 고정되어 있음

SELECT 
    A.ANIMAL_ID AS ANIMAL_ID, 
    A.NAME AS NAME
FROM 
    ANIMAL_INS A
INNER JOIN 
    ANIMAL_OUTS B 
    ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE 
    B.DATETIME - A.DATETIME < 0
ORDER BY 
    A.DATETIME ASC;