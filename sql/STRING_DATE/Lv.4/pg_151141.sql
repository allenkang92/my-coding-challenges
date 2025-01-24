-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/151141
-- 간단한 문제 설명 : 
--   - 트럭 대여 기록별 대여 금액 계산
--   - 대여 기간에 따른 할인율 적용
--   - 대여금액/기록ID 내림차순 정렬

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
--     - 트럭 데이터 필터링
--     - 대여 기간 계산
--     - 기간별 할인율 적용
--     - 최종 금액 계산
--   2. 사용한 SQL 문법 및 함수 설명
--     - CASE: 기간별 할인율 적용
--     - ROUND: 정수 부분만 출력
--     - DATE 연산: 대여 기간 계산
--   3. 쿼리 최적화 방법
--     - CAR_TYPE 인덱스 활용
--     - JOIN 순서 최적화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 대여 기록 수
--   - 공간복잡도 : O(M), M은 트럭 대여 기록 수

SELECT 
    H.HISTORY_ID,
    ROUND(
        DAILY_FEE * (END_DATE - START_DATE + 1) * 
        CASE 
            WHEN (END_DATE - START_DATE + 1) >= 90 THEN (100 - 10) / 100
            WHEN (END_DATE - START_DATE + 1) >= 30 THEN (100 - 7) / 100
            WHEN (END_DATE - START_DATE + 1) >= 7 THEN (100 - 5) / 100
            ELSE 1
        END
    ) AS FEE
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY H
JOIN 
    CAR_RENTAL_COMPANY_CAR C ON H.CAR_ID = C.CAR_ID
WHERE 
    C.CAR_TYPE = '트럭'
ORDER BY 
    FEE DESC, 
    HISTORY_ID DESC;