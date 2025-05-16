-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131114?language=oracle
-- 간단한 문제 설명 :
--   - FOOD_WAREHOUSE 테이블에서 경기도에 위치한 창고만 조회
--   - FREEZER_YN 컬럼이 NULL이면 'N'으로 표시
--   - 결과는 WAREHOUSE_ID 기준 오름차순 정렬
--
-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 (FOOD_WAREHOUSE):
--   1) WAREHOUSE_ID  VARCHAR(10) NOT NULL  -- 창고 ID (기본 키)
--   2) WAREHOUSE_NAME VARCHAR(20) NOT NULL -- 창고 이름
--   3) ADDRESS        VARCHAR(100)         -- 창고 주소
--   4) TLNO           VARCHAR(20)          -- 전화번호
--   5) FREEZER_YN     VARCHAR(1)           -- 냉동시설 유무 (Y/N), NULL 가능
--
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명:
--   1. WHERE 절로 '경기도' 주소만 필터링
--   2. FREEZER_YN이 NULL인 경우에 'N'으로 처리
--   3. ORDER BY로 WAREHOUSE_ID ASC 정렬
--
-- 이때 '경기도' 필터링 방식은 두 가지가 가능:
--   (1) LIKE를 사용:    ADDRESS LIKE '%경기도%'
--   (2) SUBSTR를 사용:  SUBSTR(ADDRESS, 1, 3) = '경기도'
--
-- -----------------------------------------------------------------------------------------
-- 시간/공간 복잡도:
--   - 시간복잡도 : O(N log N) (정렬로 인해)
--   - 공간복잡도 : O(N)       (결과 저장 공간)

-------------------------------------------------------------------------------------------
-- 방법 1: LIKE 연산자 사용
-------------------------------------------------------------------------------------------
SELECT 
    WAREHOUSE_ID,                        -- 창고 ID
    WAREHOUSE_NAME,                      -- 창고 이름
    ADDRESS,                             -- 창고 주소
    CASE WHEN FREEZER_YN IS NULL THEN 'N'
         ELSE FREEZER_YN
    END AS FREEZER_YN                    -- 냉동시설 여부 (NULL => 'N')
FROM 
    FOOD_WAREHOUSE
WHERE 
    ADDRESS LIKE '%경기도%'             -- 주소에 '경기도' 문자열이 포함된 레코드
ORDER BY 
    WAREHOUSE_ID ASC;                   -- 창고 ID 기준 오름차순 정렬

-------------------------------------------------------------------------------------------
-- 방법 2: SUBSTR 함수 사용
--   - 주소의 앞 3자리가 '경기도'인지 판별
--   - '경기도'로 시작하는 주소를 필터링
-------------------------------------------------------------------------------------------
SELECT
    WAREHOUSE_ID,                        -- 창고 ID
    WAREHOUSE_NAME,                      -- 창고 이름
    ADDRESS,                             -- 창고 주소
    CASE WHEN FREEZER_YN IS NULL THEN 'N'
         ELSE FREEZER_YN
    END AS FREEZER_YN                    -- 냉동시설 여부 (NULL => 'N')
FROM
    FOOD_WAREHOUSE
WHERE
    SUBSTR(ADDRESS, 1, 3) = '경기도'     -- 주소의 시작 부분이 '경기도'
ORDER BY
    WAREHOUSE_ID ASC;                   -- 창고 ID 기준 오름차순 정렬