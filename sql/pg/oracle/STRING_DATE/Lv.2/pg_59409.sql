-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59409?language=oracle
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블에서 모든 동물의 ANIMAL_ID, NAME, 중성화 여부를 조회
--   - 중성화 여부는 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'가 포함되는지로 판단
--   - 중성화된 경우 'O', 아닌 경우 'X'로 표시
--   - 결과는 ANIMAL_ID 순으로 오름차순 정렬

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
--   2. CASE 문을 사용하여 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'가 포함되면 'O'로, 그렇지 않으면 'X'로 표시
--   3. 결과를 ANIMAL_ID 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - CASE WHEN ... THEN ... ELSE ... END: 조건에 따라 다른 값을 반환
--   - LIKE: 패턴 매칭을 위해 사용, 여기서는 특정 문자열이 포함되는지 확인
--   - OR: 여러 조건 중 하나라도 참이면 전체 조건을 참으로 만듦
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬

-- 쿼리 최적화 방법 :
--   - SEX_UPON_INTAKE 컬럼에 인덱스를 생성하여 LIKE 연산의 성능을 향상시킬 수 있음
--     예시 인덱스 생성:
--       CREATE INDEX idx_sex_upon_intake ON ANIMAL_INS(SEX_UPON_INTAKE);
--   - SELECT 절에서 필요한 컬럼만 선택하여 불필요한 데이터 스캔을 줄임

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 각 행에 대해 CASE 문을 적용
--   - 공간복잡도 : O(N)
--     -- 결과 집합을 저장하는 데 필요한 공간 (N은 전체 동물 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    ANIMAL_ID,                                     -- 동물의 고유 ID
    NAME,                                          -- 동물의 이름
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%'    -- 'Neutered'가 포함된 경우
             OR SEX_UPON_INTAKE LIKE '%Spayed%'   -- 'Spayed'가 포함된 경우
        THEN 'O'                                   -- 중성화 상태 표시
        ELSE 'X'                                   -- 중성화되지 않은 상태 표시
    END AS 중성화                                    -- 중성화 여부 컬럼 이름
FROM 
    ANIMAL_INS
ORDER BY 
    ANIMAL_ID ASC;                                 -- ANIMAL_ID를 기준으로 오름차순 정렬

-- -------------------------------------------------------------------------------------------
-- 쿼리 오류 수정:
-- 오류 메시지: 없음
-- 원인:
--   - 기존 쿼리는 논리적으로 정확하지만, 중성화 여부 판단에서 패턴 매칭이 정확히 이루어지지 않을 수 있음
-- 해결 방법:
--   1. LIKE 패턴에 와일드카드 '%'를 추가하여 단어의 어느 위치에 'Neutered' 또는 'Spayed'가 존재해도 매칭되도록 함
--      예: '%Neutered%', '%Spayed%'
--   2. 대소문자 구분 문제가 있을 경우 LOWER 함수를 사용하여 소문자로 통일 후 비교
--      예: LOWER(SEX_UPON_INTAKE) LIKE '%neutered%'
-- -------------------------------------------------------------------------------------------