-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59045
-- 간단한 문제 설명 : 
--   - ANIMAL_INS와 ANIMAL_OUTS 테이블을 이용하여 보호소에 들어올 당시 중성화되지 않았지만, 보호소를 나갈 때 중성화된 동물들의 정보를 조회.
--   - 보호소에 들어온 동물의 ANIMAL_ID, ANIMAL_TYPE, NAME을 출력.
--   - 결과는 ANIMAL_ID를 기준으로 오름차순 정렬.

-- 테이블 스키마 :
--   - ANIMAL_INS 테이블
--     - ANIMAL_ID VARCHAR(N) FALSE -- 동물의 아이디
--     - ANIMAL_TYPE VARCHAR(N) FALSE -- 생물 종
--     - DATETIME DATETIME FALSE -- 보호 시작일
--     - INTAKE_CONDITION VARCHAR(N) FALSE -- 보호 시작 시 상태
--     - NAME VARCHAR(N) TRUE -- 이름
--     - SEX_UPON_INTAKE VARCHAR(N) FALSE -- 성별 및 중성화 여부
--   
--   - ANIMAL_OUTS 테이블
--     - ANIMAL_ID VARCHAR(N) FALSE -- 동물의 아이디 (ANIMAL_INS의 외래 키)
--     - ANIMAL_TYPE VARCHAR(N) FALSE -- 생물 종
--     - DATETIME DATETIME FALSE -- 입양일
--     - NAME VARCHAR(N) TRUE -- 이름
--     - SEX_UPON_OUTCOME VARCHAR(N) FALSE -- 성별 및 중성화 여부

-- 해결 방법 설명 :
--   1. ANIMAL_INS와 ANIMAL_OUTS 테이블을 ANIMAL_ID를 기준으로 INNER JOIN.
--   2. 보호소에 들어올 당시 SEX_UPON_INTAKE가 'Intact'인 동물 필터링.
--   3. 보호소를 나갈 당시 SEX_UPON_OUTCOME이 'Neutered' 또는 'Spayed'인 동물 필터링.
--   4. 필요한 컬럼(ANIMAL_ID, ANIMAL_TYPE, NAME)을 선택.
--   5. ANIMAL_ID를 기준으로 오름차순 정렬.

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 특정 컬럼을 선택하여 조회.
--   - AS: 컬럼에 별칭을 부여하여 결과를 보기 쉽게 만듦.
--   - FROM: 데이터를 조회할 테이블을 지정.
--   - INNER JOIN: 두 테이블을 특정 조건에 맞춰 결합.
--   - ON: JOIN할 때 사용할 조건을 명시.
--   - WHERE: 조건에 맞는 데이터를 필터링.
--   - LIKE: 패턴 매칭을 위해 사용. '%Intact%'는 'Intact'를 포함하는 값을 검색.
--   - OR: 여러 조건 중 하나라도 만족하면 참으로 간주.
--   - ORDER BY: 결과를 정렬. 여기서는 ANIMAL_ID를 오름차순으로 정렬.

-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - 인덱스 생성:
--       * ANIMAL_INS 테이블의 ANIMAL_ID, SEX_UPON_INTAKE 컬럼에 인덱스를 생성하여 검색 속도를 향상시킴.
--       * ANIMAL_OUTS 테이블의 ANIMAL_ID, SEX_UPON_OUTCOME 컬럼에 인덱스를 생성함.
--       ```sql
--       CREATE INDEX idx_animal_ins_id_sex ON ANIMAL_INS (ANIMAL_ID, SEX_UPON_INTAKE);
--       CREATE INDEX idx_animal_outs_id_outcome ON ANIMAL_OUTS (ANIMAL_ID, SEX_UPON_OUTCOME);
--       ```
--   - 조인 방식 최적화:
--       * INNER JOIN을 사용하여 두 테이블 간의 일치하는 레코드만 결합함으로써 불필요한 데이터 로드를 줄임.
--       * 필요한 컬럼만 선택하여 데이터 처리량을 최소화함.
--   - WHERE 절 최적화:
--       * LIKE 연산자 대신 정확한 패턴 매칭이 가능할 경우 '=' 연산자를 사용하는 것이 성능에 유리할 수 있음.
--       * 불필요한 패턴 매칭을 피하고, 가능한 한 인덱스를 활용할 수 있는 조건을 사용함.

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블의 레코드 수. JOIN 연산과 WHERE 필터링이 포함됨.
--   - 공간복잡도 : O(K), K는 결과로 반환되는 레코드의 수. 인덱스는 데이터베이스 엔진에 의해 관리됨.

SELECT 
    A.ANIMAL_ID AS ANIMAL_ID, 
    A.ANIMAL_TYPE AS ANIMAL_TYPE,
    A.NAME AS NAME
FROM 
    ANIMAL_INS A
INNER JOIN 
    ANIMAL_OUTS B 
    ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE 
    A.SEX_UPON_INTAKE LIKE '%Intact%' AND
    (B.SEX_UPON_OUTCOME LIKE '%Neutered%' OR B.SEX_UPON_OUTCOME LIKE '%Spayed%')
ORDER BY 
    A.ANIMAL_ID ASC;