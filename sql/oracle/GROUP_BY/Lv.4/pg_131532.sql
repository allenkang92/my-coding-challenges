-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131532
-- 간단한 문제 설명 : 
--   - 년, 월, 성별별 상품 구매 회원수 집계
--   - 성별 정보 없는 경우 제외
--   - 년, 월, 성별 기준 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : USER_INFO
--     - USER_ID INTEGER FALSE -- 회원 ID
--     - GENDER TINYINT(1) TRUE -- 성별 (0:남자, 1:여자)
--     - AGE INTEGER TRUE -- 나이
--     - JOINED DATE FALSE -- 가입일
--
--   - 테이블명 : ONLINE_SALE
--     - ONLINE_SALE_ID INTEGER FALSE -- 온라인 판매 ID
--     - USER_ID INTEGER FALSE -- 회원 ID
--     - PRODUCT_ID INTEGER FALSE -- 상품 ID
--     - SALES_AMOUNT INTEGER FALSE -- 판매량
--     - SALES_DATE DATE FALSE -- 판매일

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - USER_INFO와 ONLINE_SALE 테이블 JOIN
--     - 성별 NULL 제외
--     - 년/월/성별 그룹화
--     - 회원수 집계 (중복 제거)
--   2. 사용한 SQL 문법 및 함수 설명
--     - TO_NUMBER, TO_CHAR: 날짜 형식 변환
--     - COUNT(DISTINCT): 중복 회원 제거하여 카운트
--     - GROUP BY: 그룹화
--   3. 쿼리 최적화 방법
--     - GENDER 컬럼에 인덱스 생성
--     - USER_ID 조인 컬럼 인덱스 활용

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 판매 데이터 수
--   - 공간복잡도 : O(M), M은 년/월/성별 조합 수

SELECT 
    TO_NUMBER(TO_CHAR(SALES_DATE, 'YYYY')) AS YEAR,
    TO_NUMBER(TO_CHAR(SALES_DATE, 'MM')) AS MONTH,
    GENDER,
    COUNT(DISTINCT O.USER_ID) AS USERS
FROM USER_INFO I
INNER JOIN ONLINE_SALE O ON I.USER_ID = O.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY
    TO_NUMBER(TO_CHAR(SALES_DATE, 'YYYY')),
    TO_NUMBER(TO_CHAR(SALES_DATE, 'MM')),
    GENDER
ORDER BY YEAR ASC, MONTH ASC, GENDER ASC;