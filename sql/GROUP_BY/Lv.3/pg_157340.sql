-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/157340
-- 간단한 문제 설명 : 
--   - CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블을 이용하여 특정 날짜(2022-10-16)에 대여 중인 자동차는 '대여중', 그렇지 않은 자동차는 '대여 가능'으로 표시.
--   - 자동차 ID와 AVAILABILITY를 출력하며, 자동차 ID를 기준으로 내림차순 정렬.
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
--   - 컬럼명 및 타입 : 
--     - HISTORY_ID INTEGER NOT NULL -- 자동차 대여 기록 ID
--     - CAR_ID INTEGER NOT NULL -- 자동차 ID
--     - START_DATE DATE NOT NULL -- 대여 시작일
--     - END_DATE DATE NOT NULL -- 대여 종료일
-- 해결 방법 설명 :
--   1. 각 자동차(CAR_ID)별로 2022-10-16일에 대여 중인지 확인.
--   2. 상관 서브쿼리를 사용하여 날짜가 대여 기간 내에 있는지 판단.
--   3. CASE 문을 사용하여 '대여중' 또는 '대여 가능'을 표시.
--   4. GROUP BY 및 집계 함수를 활용.
--   5. 결과를 CAR_ID 기준으로 내림차순 정렬.
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT, CASE WHEN, MAX, MIN, GROUP BY, ORDER BY
--   - BETWEEN 연산자를 사용한 날짜 비교
-- 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등) :
--   - CAR_ID, START_DATE, END_DATE에 인덱스 생성
--   - 효율적인 범위 검색을 위해 인덱스 활용
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), N은 테이블의 행 수
--   - 공간복잡도 : O(K), K는 자동차의 수

SELECT 
    CAR_ID, 
    CASE 
        WHEN MAX(CASE WHEN DATE '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1 ELSE 0 END) = 1 
            THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    CAR_ID
ORDER BY 
    CAR_ID DESC;