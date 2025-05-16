-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 간단한 문제 설명 : 
--   - 0-23시까지 시간대별 입양 건수 조회
--   - 입양 없는 시간대도 0으로 표시
--   - 시간 순서로 정렬

-- 테이블 스키마 :
--   - 테이블명 : ANIMAL_OUTS
--     - ANIMAL_ID VARCHAR(N) FALSE -- 동물ID
--     - ANIMAL_TYPE VARCHAR(N) FALSE -- 동물 종류
--     - DATETIME DATETIME FALSE -- 입양일시
--     - NAME VARCHAR(N) TRUE -- 이름
--     - SEX_UPON_OUTCOME VARCHAR(N) FALSE -- 성별/중성화

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - CONNECT BY로 0-23시 생성
--     - LEFT JOIN으로 입양데이터 연결
--     - GROUP BY로 시간대별 집계
--     - ORDER BY로 시간순 정렬
--
--   2. 사용한 SQL 문법 및 함수 설명
--     - CONNECT BY LEVEL: 연속된 숫자 생성
--     - LEVEL-1: 0부터 시작하는 시간대
--     - TO_CHAR/TO_NUMBER: 시간 추출/변환
--     - NVL: NULL을 0으로 변환
--
--   3. 쿼리 최적화 방법
--     - DATETIME 컬럼 인덱스 활용
--     - 시간 추출 함수 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 입양 데이터 수
--   - 공간복잡도 : O(24), 고정된 시간대 수

SELECT 
    L.HOUR,
    NVL(COUNT(A.ANIMAL_ID), 0) AS COUNT
FROM 
    (SELECT LEVEL-1 AS HOUR 
     FROM DUAL 
     CONNECT BY LEVEL <= 24) L
LEFT JOIN 
    ANIMAL_OUTS A ON L.HOUR = TO_NUMBER(TO_CHAR(A.DATETIME, 'HH24'))
GROUP BY 
    L.HOUR
ORDER BY 
    L.HOUR;