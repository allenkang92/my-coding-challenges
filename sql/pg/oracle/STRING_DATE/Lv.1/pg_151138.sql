-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/151138?language=oracle
-- 간단한 문제 설명 : 
--   - CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 2022년 9월에 시작된 기록만 조회
--   - (END_DATE - START_DATE + 1)로 대여 일수 계산
--   - 대여 일수가 30일 이상이면 '장기 대여', 미만이면 '단기 대여'
--   - START_DATE와 END_DATE는 'YYYY-MM-DD' 형식으로 출력
--   - 결과는 HISTORY_ID 기준 내림차순 정렬

SELECT
    HISTORY_ID,                                         -- 대여 기록 ID
    CAR_ID,                                             -- 자동차 ID
    TO_CHAR(START_DATE, 'YYYY-MM-DD') AS START_DATE,    -- 시작일 (YYYY-MM-DD 포맷)
    TO_CHAR(END_DATE,   'YYYY-MM-DD') AS END_DATE,      -- 종료일 (YYYY-MM-DD 포맷)
    CASE 
        WHEN (END_DATE - START_DATE + 1) >= 30 THEN '장기 대여'  -- 30일 이상
        ELSE '단기 대여'                                        -- 30일 미만
    END AS RENT_TYPE
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    -- 2022-09-01 이상, 2022-10-01 미만 (즉, 2022년 9월 전체)
    START_DATE >= DATE '2022-09-01'
    AND START_DATE <  DATE '2022-10-01'
ORDER BY 
    HISTORY_ID DESC; -- HISTORY_ID 기준 내림차순 정렬