-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131534
-- 간단한 문제 설명 : 
--   - 2021년에 가입한 전체 회원 중 상품을 구매한 회원 비율
--   - 년, 월별로 구매한 회원 수와 비율 조회
--   - 소수점 두번째 자리 반올림

-- 테이블명 및 컬럼 :
--   1) USER_INFO(USER_ID, GENDER, AGE, JOINED)
--   2) ONLINE_SALE(ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE)

-- 해결 방법 설명 :
--   1. EXTRACT(YEAR/MONTH)로 연월 추출
--   2. 2021년 가입자 수 카운트
--   3. 구매한 회원 COUNT(DISTINCT ...)
--   4. 비율 계산 및 반올림

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N)
--   - 공간복잡도 : O(M)

SELECT 
    EXTRACT(YEAR FROM O.SALES_DATE) AS YEAR,
    EXTRACT(MONTH FROM O.SALES_DATE) AS MONTH,
    COUNT(DISTINCT O.USER_ID) AS PURCHASED_USERS,
    ROUND(
        COUNT(DISTINCT O.USER_ID) * 1.0
        / (SELECT COUNT(*) FROM USER_INFO WHERE EXTRACT(YEAR FROM JOINED) = 2021),
        2
    ) AS PURCHASED_RATIO
FROM USER_INFO U
JOIN ONLINE_SALE O 
    ON U.USER_ID = O.USER_ID
WHERE EXTRACT(YEAR FROM U.JOINED) = 2021
GROUP BY 
    EXTRACT(YEAR FROM O.SALES_DATE),
    EXTRACT(MONTH FROM O.SALES_DATE)
ORDER BY 
    YEAR ASC,
    MONTH ASC;