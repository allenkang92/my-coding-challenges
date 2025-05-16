-- 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/157343?language=oracle
-- 간단한 문제 설명 : 
--   자동차 대여 회사의 자동차 중 네비게이션 옵션이 포함된 차량을 조회합니다.
--
-- 테이블 스키마 :
--   - 테이블명 : CAR_RENTAL_COMPANY_CAR
--   - 컬럼정보:
--       CAR_ID INTEGER        NOT NULL  -- 자동차 ID
--       CAR_TYPE VARCHAR(255) NOT NULL  -- 자동차 종류
--       DAILY_FEE INTEGER     NOT NULL  -- 일일 대여 요금
--       OPTIONS VARCHAR(255)  NOT NULL  -- 옵션 리스트 (콤마로 구분)

-- 방법 1: LIKE 연산자 사용
-- 장점: 직관적이고 가독성이 좋음
-- 단점: 와일드카드(%) 사용으로 인덱스 활용이 제한적
SELECT 
    CAR_ID, 
    CAR_TYPE, 
    DAILY_FEE, 
    OPTIONS
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    OPTIONS LIKE '%네비게이션%'
ORDER BY 
    CAR_ID DESC;

-- 방법 2: INSTR 함수 사용
-- 장점: 성능상 더 효율적일 수 있음
-- 단점: 가독성이 LIKE에 비해 떨어질 수 있음
SELECT 
    CAR_ID, 
    CAR_TYPE, 
    DAILY_FEE, 
    OPTIONS
FROM 
    CAR_RENTAL_COMPANY_CAR
WHERE 
    INSTR(OPTIONS, '네비게이션') > 0
ORDER BY 
    CAR_ID DESC;