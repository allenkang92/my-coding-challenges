-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59408?language=oracle
-- 간단한 문제 설명 :
--   - ANIMAL_INS 테이블에서 동물의 이름이 NULL이 아닌 경우 중복을 제거한 이름의 수를 조회
--   - 결과 컬럼명은 'count'로 지정

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
--   1. SELECT 절에서 NAME 컬럼의 중복을 제거한 개수를 COUNT(DISTINCT NAME)으로 조회
--   2. WHERE 절에서 NAME이 NULL이 아닌 경우만 필터링 (NAME IS NOT NULL)
--   3. 결과 컬럼명을 'count'로 지정

-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 원하는 컬럼을 선택
--   - COUNT(DISTINCT ...): 중복된 값을 제외하고 개수를 셈
--   - FROM: 데이터 소스 테이블 지정
--   - WHERE: 조건에 맞는 행을 필터링
--   - AS: 컬럼에 별칭(alias) 부여

-- 쿼리 최적화 방법 :
--   - NAME 컬럼에 인덱스를 생성하면 WHERE 절의 필터링과 DISTINCT 연산의 성능을 향상시킬 수 있음
--   - 인덱스는 데이터베이스의 조회 속도를 크게 향상시킬 수 있는 중요한 요소이지만, 너무 많은 인덱스는 쓰기 성능을 저하시킬 수 있으므로 주의가 필요함
--
--   예시 인덱스 생성:
--     CREATE INDEX idx_animal_name ON ANIMAL_INS(NAME);

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 테이블 전체 스캔 후 DISTINCT와 COUNT 연산
--   - 공간복잡도 : O(K) - 중복을 제거한 이름의 개수를 저장할 공간 (K는 고유 이름의 수)
    
-- -------------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    COUNT(DISTINCT NAME) AS count                        -- 중복을 제거한 이름의 총 개수를 'count'라는 별칭으로 조회
FROM 
    ANIMAL_INS                                           -- 데이터 소스 테이블
WHERE 
    NAME IS NOT NULL;                                    -- 이름이 NULL이 아닌 경우만 필터링

-- -------------------------------------------------------------------------------------------
-- 추가 최적화: 인덱스 생성 예시
-- -------------------------------------------------------------------------------------------

-- NAME 컬럼에 인덱스를 생성하여 WHERE 절과 DISTINCT 연산의 성능을 향상시킬 수 있습니다.
-- 단, 인덱스 생성 시 데이터베이스의 인덱스 관리 방식을 고려해야 합니다.

-- 인덱스 생성 명령어 예시:
-- CREATE INDEX idx_animal_name ON ANIMAL_INS(NAME);

-- -------------------------------------------------------------------------------------------
-- 쿼리 실행 예시
-- -------------------------------------------------------------------------------------------

-- 주어진 예시 데이터를 기준으로 쿼리를 실행하면 다음과 같이 결과가 출력됩니다:

-- | count |
-- |-------|
-- | 2     |

-- -------------------------------------------------------------------------------------------
-- 추가 설명:
--
-- 1. **COUNT(DISTINCT NAME)**:
--    - COUNT 함수는 행의 수를 세는 함수입니다.
--    - DISTINCT 키워드는 중복된 값을 제거합니다.
--    - 따라서, COUNT(DISTINCT NAME)은 중복된 이름을 하나로 간주하여 고유한 이름의 총 개수를 셉니다.
--
-- 2. **WHERE 절 (NAME IS NOT NULL)**:
--    - WHERE 절은 특정 조건을 만족하는 행만을 필터링합니다.
--    - NAME IS NOT NULL 조건은 이름이 없는 (NULL인) 동물들을 제외하고, 이름이 있는 동물들만을 대상으로 합니다.
--
-- 3. **AS 키워드**:
--    - AS 키워드는 컬럼에 별칭을 부여할 때 사용됩니다.
--    - 여기서는 COUNT(DISTINCT NAME)의 결과에 'count'라는 별칭을 부여하여 결과 컬럼명을 설정합니다.
--
-- 4. **쿼리 최적화**:
--    - NAME 컬럼에 인덱스를 생성하면, 데이터베이스는 WHERE 절과 COUNT(DISTINCT ...) 연산을 더 빠르게 수행할 수 있습니다.
--    - 인덱스는 특정 컬럼의 값을 빠르게 조회할 수 있게 해주지만, 인덱스를 너무 많이 생성하면 데이터 삽입, 수정, 삭제 시 오버헤드가 발생할 수 있습니다.
--
-- 5. **실제 데이터 적용**:
--    - 이름이 NULL인 경우는 집계에 포함되지 않기 때문에, 실제로 COUNT(DISTINCT NAME)은 고유한 비NULL 이름의 개수를 반환합니다.
--    - 예시 데이터에서는 이름이 NULL인 동물이 1마리이고, *Sam과 *Sweetie라는 두 개의 고유한 이름이 있으므로 결과는 2가 됩니다.
--
-- 6. **대체 방법**:
--    - NULL 값을 제외하고 고유한 이름의 개수를 세는 다른 방법으로는 GROUP BY를 사용하는 방법이 있습니다.
--    
--    ```sql
--    SELECT 
--        COUNT(*) AS count
--    FROM (
--        SELECT NAME
--        FROM ANIMAL_INS
--        WHERE NAME IS NOT NULL
--        GROUP BY NAME
--    ) AS unique_names;
--    ```
--
--    - 이 방법은 서브쿼리에서 이름을 그룹화한 후, 상위 쿼리에서 그 그룹의 개수를 세는 방식입니다.
--    - 그러나 COUNT(DISTINCT NAME)을 사용하는 것이 더 간결하고 효율적일 수 있습니다.
--
-- -------------------------------------------------------------------------------------------