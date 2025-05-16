-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59041?language=oracle
-- 간단한 문제 설명 : 
--   - ANIMAL_INS 테이블에서 이름이 두 번 이상 사용된 동물의 이름과 그 횟수를 조회
--   - 이름이 없는 동물은 제외
--   - 결과는 이름을 기준으로 오름차순 정렬
    
-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_INS
--     - ANIMAL_ID			VARCHAR(N)	FALSE	-- 동물의 고유 ID
--     - ANIMAL_TYPE		VARCHAR(N)	FALSE	-- 동물의 종류 (예: Dog, Cat 등)
--     - DATETIME			DATETIME	FALSE	-- 동물이 보호소에 입소한 날짜 및 시간
--     - INTAKE_CONDITION	VARCHAR(N)	FALSE	-- 동물의 상태 (예: Normal, Injured 등)
--     - NAME				VARCHAR(N)	TRUE	-- 동물의 이름
--     - SEX_UPON_INTAKE	VARCHAR(N)	FALSE	-- 동물의 성별 및 중성화 여부 (예: Spayed Female, Neutered Male 등)
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명 :
--   1. ANIMAL_INS 테이블에서 이름이 있는 동물만을 선택하기 위해 WHERE 절에 NAME IS NOT NULL 조건을 추가
--   2. 이름별로 그룹화를 수행하여 각 이름의 사용 횟수를 COUNT 함수로 계산
--   3. HAVING 절을 사용하여 이름의 사용 횟수가 두 번 이상인 경우만 필터링
--   4. 결과를 이름 순으로 오름차순 정렬하기 위해 ORDER BY 절에 NAME ASC를 사용
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - COUNT(expression): 그룹별로 특정 표현식의 개수를 계산
--   - FROM: 데이터를 조회할 테이블을 지정
--   - WHERE: 특정 조건을 만족하는 행만 선택
--   - GROUP BY: 특정 컬럼을 기준으로 행을 그룹화
--   - HAVING: 그룹화된 데이터에 조건을 적용
--   - ORDER BY: 결과를 특정 컬럼을 기준으로 정렬
--   - ASC: 오름차순 정렬
--
-- 쿼리 최적화 방법 :
--   - NAME 컬럼에 인덱스를 생성하여 WHERE 절과 GROUP BY 절의 성능을 향상시킴
--     예시 인덱스 생성:
--       CREATE INDEX idx_animal_ins_name ON ANIMAL_INS(NAME);
--   - 필요 없는 컬럼은 SELECT 절에 포함하지 않음으로써 데이터 스캔을 최소화
--   - 단순한 그룹화 및 필터링 쿼리이므로 추가적인 최적화는 필요하지 않음
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하면서 이름을 그룹화하고 COUNT를 수행
--   - 공간복잡도 : O(K)
--     -- 그룹화된 이름과 그 횟수를 저장하는데 필요한 공간 (K는 고유한 이름의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------
    
SELECT 
    NAME, 
    COUNT(NAME) AS COUNT  -- 각 이름의 사용 횟수를 계산
FROM 
    ANIMAL_INS
WHERE 
    NAME IS NOT NULL  -- 이름이 있는 동물만 선택
GROUP BY 
    NAME  -- 이름별로 그룹화
HAVING 
    COUNT(NAME) >= 2  -- 이름의 사용 횟수가 두 번 이상인 경우만 필터링
ORDER BY 
    NAME ASC;  -- 이름을 기준으로 오름차순 정렬