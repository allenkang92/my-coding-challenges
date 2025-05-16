-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/157342?language=oracle
-- 간단한 문제 설명 : 
--   - CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 자동차별 평균 대여 기간을 계산
--   - 평균 대여 기간이 7일 이상인 자동차의 CAR_ID와 AVERAGE_DURATION을 조회
--   - AVERAGE_DURATION은 소수점 두번째 자리에서 반올림
--   - 결과는 평균 대여 기간을 기준으로 내림차순 정렬, 동일 시 CAR_ID를 기준으로 내림차순 정렬

-- -----------------------------------------------------------------------------------------
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_RENTAL_HISTORY
--     - HISTORY_ID	INTEGER	FALSE	-- 대여 기록 ID
--     - CAR_ID		INTEGER	FALSE	-- 자동차 ID
--     - START_DATE	DATE	FALSE	-- 대여 시작일
--     - END_DATE		DATE	FALSE	-- 대여 종료일
-- -----------------------------------------------------------------------------------------
-- 해결 방법 설명 :
--   1. 대여 기간 계산: END_DATE와 START_DATE의 차이에 1을 더해 대여 기간을 일수로 계산
--   2. CAR_ID별로 평균 대여 기간을 계산
--   3. 평균 대여 기간을 소수점 두번째 자리에서 반올림
--   4. 평균 대여 기간이 7일 이상인 자동차만 필터링
--   5. AVERAGE_DURATION을 기준으로 내림차순 정렬, 동일 시 CAR_ID를 기준으로 내림차순 정렬
--
-- 사용한 SQL 문법 및 함수 설명 :
--   - SELECT: 조회할 컬럼을 선택
--   - ROUND(number, decimals): 숫자를 지정한 소수점 자리에서 반올림
--   - AVG(expression): 그룹별 평균값 계산
--   - TO_CHAR(number, format): 숫자를 지정한 형식의 문자열로 변환
--   - TO_NUMBER(string): 문자열을 숫자로 변환
--   - FROM: 데이터를 조회할 테이블 지정
--   - GROUP BY: 특정 컬럼을 기준으로 그룹화
--   - HAVING: 그룹화된 데이터에 조건 적용
--   - ORDER BY: 결과를 특정 컬럼 기준으로 정렬
--   - DESC: 내림차순 정렬 지정
--
-- 쿼리 최적화 방법 :
--   - CAR_ID 컬럼에 인덱스를 생성하여 GROUP BY 및 ORDER BY 절의 성능 향상
--     예시 인덱스 생성:
--       CREATE INDEX idx_car_id ON CAR_RENTAL_COMPANY_RENTAL_HISTORY(CAR_ID);
--   - START_DATE와 END_DATE에 인덱스를 생성하여 날짜 계산 성능 향상
--       CREATE INDEX idx_start_end_date ON CAR_RENTAL_COMPANY_RENTAL_HISTORY(START_DATE, END_DATE);
--   - 필요한 컬럼만 SELECT 절에 포함하여 불필요한 데이터 스캔을 줄임
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--     -- 테이블 전체를 스캔하며 대여 기간 계산과 평균을 구하므로 선형 시간 복잡도
--   - 공간복잡도 : O(K)
--     -- 그룹화된 결과를 저장하기 위한 공간 (K는 고유 CAR_ID의 수)
-- -----------------------------------------------------------------------------------------
-- 최종 쿼리
-- -------------------------------------------------------------------------------------------

SELECT 
    CAR_ID, 
    TO_CHAR(ROUND(AVG(END_DATE - START_DATE + 1), 2), 'FM9990.00') AS AVERAGE_DURATION  -- 자동차 별 평균 대여 기간을 소수점 두번째 자리에서 반올림하여 문자열로 변환
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    CAR_ID  -- 자동차 ID별로 그룹화
HAVING 
    AVG(END_DATE - START_DATE + 1) >= 7  -- 평균 대여 기간이 7일 이상인 자동차만 필터링
ORDER BY 
    TO_NUMBER(AVERAGE_DURATION) DESC,  -- 평균 대여 기간을 숫자로 변환하여 내림차순 정렬
    CAR_ID DESC;  -- 동일한 평균 대여 기간일 경우 자동차 ID를 기준으로 내림차순 정렬