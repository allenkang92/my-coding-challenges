-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131124
-- 간단한 문제 설명 : 
-- 테이블 스키마 :
--   - 테이블명 : 
--   - 컬럼명 및 타입 : 
-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--   2. 사용한 SQL 문법 및 함수 설명
--   3. 쿼리 최적화 방법 (인덱스 사용, 조인 방식 등)
-- 시간/공간 복잡도 :
--   - 시간복잡도 : 
--   - 공간복잡도 : 


SELECT A.MEMBER_NAME, B.REVIEW_TEXT, TO_CHAR(B.REVIEW_DATE, 'YYYY-MM-DD')
FROM MEMBER_PROFILE A
JOIN 
(SELECT REVIEW_TEXT, REVIEW_DATE, COUNT(MEMBER_ID) FROM REST_REVIEW GROUP BY MEMBER_ID) AS B ON A.MEMBER_ID = B.MEMBER_ID
ORDER BY B.REVIEW_DATE ASC, B.REVIEW_TEXT ASC
;