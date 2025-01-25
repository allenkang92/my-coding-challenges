-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/151136?language=oracle
-- 간단한 문제 설명 : 
--   SUV 차량의 평균 일일 대여 요금을 계산하여 반올림한 값을 출력
--
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_CAR
--   - 컬럼정보:
--       CAR_ID INTEGER        NOT NULL  -- 자동차 ID
--       CAR_TYPE VARCHAR(255) NOT NULL  -- 자동차 종류
--       DAILY_FEE INTEGER     NOT NULL  -- 일일 대여 요금
--       OPTIONS VARCHAR(255)  NOT NULL  -- 자동차 옵션 리스트
--
-- 해결 방법 설명 :
--   1. WHERE 절로 SUV 차량만 필터링
--   2. AVG 함수로 DAILY_FEE의 평균 계산
--   3. ROUND 함수로 결과값 반올림
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N) - 전체 데이터 스캔
--   - 공간복잡도 : O(1) - 단일 결과값만 저장

SELECT 
    ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE  -- 평균값 계산 후 반올림
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    CAR_TYPE = 'SUV';  -- SUV 차량만 선택