-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/151139
-- 간단한 문제 설명 : 
--   - CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블을 이용하여 2022년 8월부터 10월까지 대여 횟수가 5회 이상인 자동차들의 월별 대여 횟수를 조회.
--   - 월별 자동차 ID별 총 대여 횟수(RECORDS)를 출력.
--   - 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬.
--   - 특정 월의 대여 횟수가 0인 경우 결과에서 제외.
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
--   - 컬럼명 및 타입 : 
--     - HISTORY_ID INTEGER NOT NULL -- 자동차 대여 기록 ID
--     - CAR_ID INTEGER NOT NULL -- 자동차 ID
--     - START_DATE DATE NOT NULL -- 대여 시작일
--     - END_DATE DATE NOT NULL -- 대여 종료일
-- 해결 방법 설명 :
--   1. 대여 시작일을 기준으로 2022년 8월부터 10월까지의 대여 기록을 필터링.
--   2. 각 자동차(CAR_ID)에 대해 총 대여 횟수가 5회 이상인 자동차를 선정.
--   3. 선정된 자동차들에 대해 월별 대여 횟수를 집계.
--   4. 결과를 월을 기준으로 오름차순, 월이 동일할 경우 자동차 ID를 기준으로 내림차순 정렬.
--   5. 특정 월의 대여 횟수가 0인 경우 제외.
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY
--   - TO_CHAR, TO_NUMBER 함수 사용
-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - START_DATE, CAR_ID에 인덱스 생성
--   - 효율적인 범위 검색을 위해 인덱스 활용
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 테이블의 행 수
--   - 공간복잡도 : O(K * M), K는 자동차의 수, M은 월의 수

SELECT 
    TO_NUMBER(TO_CHAR(START_DATE, 'MM')) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    TO_CHAR(START_DATE, 'YYYY-MM') IN ('2022-08', '2022-09', '2022-10')
    AND CAR_ID IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE TO_CHAR(START_DATE, 'YYYY-MM') IN ('2022-08', '2022-09', '2022-10')
        GROUP BY CAR_ID
        HAVING COUNT(*) >= 5
    )
GROUP BY 
    TO_NUMBER(TO_CHAR(START_DATE, 'MM')),
    CAR_ID
ORDER BY 
    MONTH ASC,
    CAR_ID DESC;