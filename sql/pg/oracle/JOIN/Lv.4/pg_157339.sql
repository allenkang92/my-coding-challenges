-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/157339
-- 간단한 문제 설명 : 
--   - 세단/SUV 중 11월 한달간 대여 가능한 차량 조회
--   - 30일 대여시 50-200만원 사이 요금
--   - 대여요금/차종/차ID 기준 정렬

-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_CAR
--     - CAR_ID INTEGER FALSE -- 자동차 ID
--     - CAR_TYPE VARCHAR(255) FALSE -- 자동차 종류
--     - DAILY_FEE INTEGER FALSE -- 일일 대여 요금
--     - OPTIONS VARCHAR(255) FALSE -- 옵션 리스트
--
--   - 테이블명 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
--     - HISTORY_ID INTEGER FALSE -- 대여 기록 ID
--     - CAR_ID INTEGER FALSE -- 자동차 ID
--     - START_DATE DATE FALSE -- 대여 시작일
--     - END_DATE DATE FALSE -- 대여 종료일
--
--   - 테이블명 : CAR_RENTAL_COMPANY_DISCOUNT_PLAN
--     - PLAN_ID INTEGER FALSE -- 할인 정책 ID
--     - CAR_TYPE VARCHAR(255) FALSE -- 자동차 종류
--     - DURATION_TYPE VARCHAR(255) FALSE -- 대여 기간 종류
--     - DISCOUNT_RATE INTEGER FALSE -- 할인율

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - 세단/SUV 필터링
--     - 30일 이상 할인율 적용
--     - 11월 대여 가능 여부 체크
--     - 요금 범위 필터링
--   2. 사용한 SQL 문법 및 함수 설명
--     - NOT EXISTS: 대여 불가능한 차량 제외
--     - TO_DATE: 날짜 형식 변환
--     - CASE: 할인율 계산
--   3. 쿼리 최적화 방법
--     - CAR_TYPE 인덱스 활용
--     - 날짜 인덱스 활용

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 차량 수
--   - 공간복잡도 : O(M), M은 결과 레코드 수

SELECT 
    DISTINCT C.CAR_ID AS CAR_ID, 
    C.CAR_TYPE AS CAR_TYPE, 
    ROUND(C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
    ON C.CAR_TYPE = P.CAR_TYPE
WHERE (C.CAR_TYPE = '세단' OR C.CAR_TYPE = 'SUV')
    AND C.DAILY_FEE * 30 >= 500000 
    AND C.DAILY_FEE * 30 < 2000000
    AND P.DURATION_TYPE = '30일 이상'
    AND NOT EXISTS (
        SELECT 1 
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H 
        WHERE H.CAR_ID = C.CAR_ID 
        AND H.END_DATE >= TO_DATE('2022-11-01', 'YYYY-MM-DD')
        AND H.START_DATE <= TO_DATE('2022-11-30', 'YYYY-MM-DD')
    )
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;