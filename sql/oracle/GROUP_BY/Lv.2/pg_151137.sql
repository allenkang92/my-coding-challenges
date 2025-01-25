-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/151137?language=oracle
-- 간단한 문제 설명 : 
--   - CAR_RENTAL_COMPANY_CAR 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 
--     자동차 종류 별로 몇 대인지 조회
--   - 결과는 자동차 종류를 기준으로 오름차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_CAR
--     - CAR_ID			INTEGER		FALSE	-- 자동차 ID
--     - CAR_TYPE		VARCHAR(255)	FALSE	-- 자동차 종류 (예: 세단, SUV, 승합차, 트럭, 리무진)
--     - DAILY_FEE		INTEGER		FALSE	-- 일일 대여 요금 (원)
--     - OPTIONS			VARCHAR(255)	FALSE	-- 자동차 옵션 리스트 (콤마로 구분된 키워드)
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명 :
--   1. OPTIONS 컬럼에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차를 필터링하기 위해 WHERE 절에 
--      OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%' 조건 추가
--   2. 자동차 종류(CAR_TYPE)별로 그룹화하여 COUNT 함수를 사용해 각 종류별 해당 옵션을 가진 자동차의 수를 계산
--   3. 결과를 자동차 종류 기준으로 오름차순 정렬을 수행
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - COUNT(*): 그룹별 행의 개수를 계산
--   - FROM: 데이터를 조회할 테이블을 지정
--   - WHERE: 특정 조건을 만족하는 행만 선택
--   - LIKE: 패턴 매칭을 위해 사용
--   - OR: 여러 조건 중 하나라도 만족하면 선택
--   - GROUP BY: 특정 컬럼을 기준으로 그룹화
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--   - ASC: 오름차순 정렬 지정
--
-- 쿼리 최적화 방법 :
--   - OPTIONS 컬럼에 대한 인덱스 생성:
--     CREATE INDEX idx_car_options ON CAR_RENTAL_COMPANY_CAR(OPTIONS);
--   - CAR_TYPE 컬럼에 대한 인덱스 생성:
--     CREATE INDEX idx_car_type ON CAR_RENTAL_COMPANY_CAR(CAR_TYPE);
--   - 가능하다면 OPTIONS 컬럼을 정규화하여 별도의 옵션 테이블을 만들고, 조인을 사용하는 방식으로 최적화
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 조건에 맞는 행을 필터링하고 그룹화를 수행하므로 선형 시간 복잡도
--   - 공간복잡도 : O(K)
--     -- 그룹화된 결과를 저장하기 위한 공간 (K는 고유 CAR_TYPE의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    CAR_TYPE, 
    COUNT(*) AS CARS  -- 각 자동차 종류별 특정 옵션을 가진 자동차의 수를 계산
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    OPTIONS LIKE '%가죽시트%' 
    OR OPTIONS LIKE '%열선시트%' 
    OR OPTIONS LIKE '%통풍시트%'  -- 특정 옵션 중 하나 이상을 포함하는 자동차 필터링
GROUP BY 
    CAR_TYPE  -- 자동차 종류별로 그룹화
ORDER BY 
    CAR_TYPE ASC;  -- 자동차 종류를 기준으로 오름차순 정렬
