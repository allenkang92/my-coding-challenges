-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131535?language=oracle
-- 간단한 문제 설명 :
--   USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20~29세인 회원 수를 조회해야 합니다.
--
-- 테이블 스키마 :
--   - USER_ID INTEGER NOT NULL
--   - GENDER TINYINT(1)
--   - AGE INTEGER
--   - JOINED DATE NOT NULL
--
-- 해결 방법 설명 :
--   1. 2021년 1월 1일부터 2022년 1월 1일까지 가입일이 포함된 회원 필터링
--   2. 나이(AGE)가 BETWEEN 20 AND 29인 조건 추가
--   3. COUNT(*) AS USERS 로 회원 수만 조회
--
-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N)
--   - 공간복잡도 : O(1)

SELECT 
    COUNT(*) AS USERS
FROM 
    USER_INFO
WHERE 
    -- 나이 20세 이상, 29세 이하만
    AGE BETWEEN 20 AND 29
    -- 가입일이 2021-01-01 ~ 2021-12-31까지 (오전 0시부터 다음 해 1월 1일 0시 전까지)
    AND JOINED >= TO_DATE('2021-01-01', 'YYYY-MM-DD') 
    AND JOINED <  TO_DATE('2022-01-01', 'YYYY-MM-DD');