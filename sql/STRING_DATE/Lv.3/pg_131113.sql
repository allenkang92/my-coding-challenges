-- 문제 링크 (예시) : https://school.programmers.co.kr/learn/courses/30/lessons/131113?language=oracle
-- 간단한 문제 설명 :
--   - FOOD_ORDER 테이블에서 ORDER_ID, PRODUCT_ID, OUT_DATE, 출고여부를 조회
--   - OUT_DATE를 기준으로 2022-05-01 이하 '출고완료', 초과 '출고대기', 값이 없으면 '출고미정'으로 분류
--   - 결과를 ORDER_ID 오름차순으로 정렬

-- 해결 방법 설명 :
--   1. TO_CHAR 함수로 OUT_DATE를 'YYYY-MM-DD' 문자열 형태로 변환
--   2. CASE WHEN ~ THEN 구문으로 날짜 문자열을 비교하여 상태를 결정
--   3. WHERE 절은 없으며, ORDER_ID 기준으로 오름차순 정렬

-- 사용한 SQL 문법 및 함수 설명 :
--   - TO_CHAR(OUT_DATE, 'YYYY-MM-DD'): 날짜 데이터를 문자열로 변환
--   - CASE WHEN: 조건에 따라 상황별 다른 내용을 반환
--   - ORDER BY ORDER_ID ASC: ORDER_ID 오름차순 정렬

-- 쿼리 최적화 방법 :
--   - ORDER_ID 컬럼에 인덱스를 생성하여 ORDER BY 절 성능 향상
--   - 필요한 컬럼만 SELECT하여 불필요한 I/O를 최소화

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N), 테이블 전체 스캔 후 CASE 문 수행
--   - 공간복잡도 : O(N), 조건에 따른 결과를 임시 저장 (N은 전체 레코드 수)

SELECT 
    ORDER_ID, 
    PRODUCT_ID, 
    TO_CHAR(OUT_DATE, 'YYYY-MM-DD') AS OUT_DATE, 
    CASE 
    WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') <= '2022-05-01' THEN '출고완료'
    WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') > '2022-05-01' THEN '출고대기'
    ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER
-- WHERE
ORDER BY ORDER_ID ASC;