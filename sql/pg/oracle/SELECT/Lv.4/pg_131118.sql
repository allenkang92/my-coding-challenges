-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131118
-- 간단한 문제 설명 : 
--   - REST_INFO와 REST_REVIEW 테이블에서 서울 지역 식당의 정보와 평균 리뷰 점수 조회
--   - 평균 점수는 소수점 3자리에서 반올림
--   - 점수 내림차순, 동일 시 즐겨찾기 내림차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : REST_INFO
--     - REST_ID VARCHAR(5) FALSE -- 식당 ID
--     - REST_NAME VARCHAR(50) FALSE -- 식당 이름
--     - FOOD_TYPE VARCHAR(20) TRUE -- 음식 종류
--     - VIEWS NUMBER TRUE -- 조회수
--     - FAVORITES NUMBER TRUE -- 즐겨찾기수
--     - PARKING_LOT VARCHAR(1) TRUE -- 주차장 유무
--     - ADDRESS VARCHAR(100) TRUE -- 주소
--     - TEL VARCHAR(100) TRUE -- 전화번호
--
--   - 테이블명 : REST_REVIEW
--     - REVIEW_ID VARCHAR(10) FALSE -- 리뷰 ID
--     - REST_ID VARCHAR(10) TRUE -- 식당 ID
--     - MEMBER_ID VARCHAR(100) TRUE -- 회원 ID
--     - REVIEW_SCORE NUMBER TRUE -- 점수
--     - REVIEW_TEXT VARCHAR(1000) TRUE -- 리뷰 텍스트
--     - REVIEW_DATE DATE TRUE -- 리뷰 작성일

-- 해결 방법 설명 :
--   1. 서브쿼리에서 각 식당별 평균 리뷰 점수 계산
--   2. REST_INFO와 조인하여 서울 지역 식당만 필터링
--   3. 요구사항대로 정렬 수행

-- 사용한 SQL 문법 및 함수 설명 :
--   - SUBSTR: 문자열 자르기 (서울 지역 체크)
--   - ROUND: 소수점 반올림
--   - AVG: 평균값 계산
--   - JOIN: 테이블 결합
--   - GROUP BY: 식당별 집계
--   - ORDER BY: 정렬 조건 지정

-- 쿼리 최적화 방법 :
--   - 서브쿼리로 미리 평균 계산하여 데이터량 감소
--   - SUBSTR 사용하여 정확한 서울 지역 필터링
--   - REST_ID 인덱스 활용 조인

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 리뷰 수
--   - 공간복잡도 : O(M), M은 서울 지역 식당 수

SELECT 
    A.REST_ID, 
    A.REST_NAME, 
    A.FOOD_TYPE, 
    A.FAVORITES, 
    A.ADDRESS, 
    B.SCORE
FROM 
    REST_INFO A
JOIN (
    SELECT 
        REST_ID, 
        ROUND(AVG(REVIEW_SCORE), 2) SCORE
    FROM 
        REST_REVIEW
    GROUP BY 
        REST_ID
) B
ON 
    A.REST_ID = B.REST_ID
WHERE 
    SUBSTR(A.ADDRESS, 1, 2) = '서울'
ORDER BY 
    B.SCORE DESC, 
    A.FAVORITES DESC;