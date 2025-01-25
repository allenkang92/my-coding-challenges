-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/131124
-- 간단한 문제 설명 : 
--   - 리뷰를 가장 많이 작성한 회원의 리뷰 조회
--   - 회원이름, 리뷰텍스트, 작성일 출력
--   - 작성일/텍스트 기준 정렬

-- 테이블 스키마 :
--   - 테이블명 : MEMBER_PROFILE
--     - MEMBER_ID VARCHAR(100) FALSE -- 회원 ID
--     - MEMBER_NAME VARCHAR(50) FALSE -- 회원 이름
--     - TLNO VARCHAR(50) TRUE -- 연락처
--     - GENDER VARCHAR(1) TRUE -- 성별
--     - DATE_OF_BIRTH DATE TRUE -- 생년월일
--
--   - 테이블명 : REST_REVIEW
--     - REVIEW_ID VARCHAR(10) FALSE -- 리뷰 ID
--     - REST_ID VARCHAR(10) TRUE -- 식당 ID
--     - MEMBER_ID VARCHAR(100) TRUE -- 회원 ID
--     - REVIEW_SCORE NUMBER TRUE -- 점수
--     - REVIEW_TEXT VARCHAR(1000) TRUE -- 리뷰 텍스트
--     - REVIEW_DATE DATE TRUE -- 리뷰 작성일

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - 회원별 리뷰 수 집계
--     - 최다 리뷰 회원 필터링
--     - 리뷰 정보 조회 및 정렬
--   2. 사용한 SQL 문법 및 함수 설명
--     - WITH: 서브쿼리 결과 재사용
--     - COUNT: 리뷰 수 집계
--     - TO_CHAR: 날짜 형식 변환
--   3. 쿼리 최적화 방법
--     - MEMBER_ID 인덱스 활용
--     - 리뷰 수 계산 결과 재사용

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 리뷰 수
--   - 공간복잡도 : O(M), M은 최다 리뷰 회원의 리뷰 수

WITH MAX_REVIEWER AS (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(*) = (
        SELECT COUNT(*)
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(*) DESC
        FETCH FIRST 1 ROW ONLY
    )
)
SELECT 
    M.MEMBER_NAME,
    R.REVIEW_TEXT,
    TO_CHAR(R.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM 
    REST_REVIEW R
JOIN 
    MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
WHERE 
    R.MEMBER_ID IN (SELECT MEMBER_ID FROM MAX_REVIEWER)
ORDER BY 
    R.REVIEW_DATE ASC,
    R.REVIEW_TEXT ASC;