-- 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/132204
-- 간단한 문제 설명 : 
--   - 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 조회
--   - 예약시간 기준 오름차순 정렬

-- 테이블 스키마 :
--   - 테이블명 : PATIENT
--     - PT_NO VARCHAR(N) FALSE -- 환자번호
--     - PT_NAME VARCHAR(N) FALSE -- 환자이름
--     - GEND_CD VARCHAR(N) FALSE -- 성별코드
--     - AGE INTEGER FALSE -- 나이
--     - TLNO VARCHAR(N) TRUE -- 전화번호
--
--   - 테이블명 : DOCTOR
--     - DR_NAME VARCHAR(N) FALSE -- 의사이름
--     - DR_ID VARCHAR(N) FALSE -- 의사ID
--     - LCNS_NO VARCHAR(N) FALSE -- 면허번호
--     - HIRE_YMD DATE FALSE -- 고용일자
--     - MCDP_CD VARCHAR(N) TRUE -- 진료과코드
--     - TLNO VARCHAR(N) TRUE -- 전화번호
--
--   - 테이블명 : APPOINTMENT
--     - APNT_YMD TIMESTAMP FALSE -- 진료예약일시
--     - APNT_NO INTEGER FALSE -- 진료예약번호
--     - PT_NO VARCHAR(N) FALSE -- 환자번호
--     - MCDP_CD VARCHAR(N) FALSE -- 진료과코드
--     - MDDR_ID VARCHAR(N) FALSE -- 의사ID
--     - APNT_CNCL_YN VARCHAR(N) TRUE -- 예약취소여부
--     - APNT_CNCL_YMD DATE TRUE -- 예약취소날짜

-- 해결 방법 설명 :
--   1. 쿼리 작성 단계
--     - 3개 테이블 INNER JOIN
--     - 날짜, 진료과, 취소여부 필터링
--     - 시간순 정렬
--
--   2. 사용한 SQL 문법 및 함수 설명
--     - INNER JOIN: 테이블 결합
--     - TO_CHAR: 날짜/시간 형식 변환
--     - WHERE: 조건 필터링
--     - ORDER BY: 정렬
--
--   3. 쿼리 최적화 방법
--     - 인덱스: APPOINTMENT.APNT_YMD, MCDP_CD에 인덱스 생성
--     - JOIN 순서: APPOINTMENT → PATIENT → DOCTOR

-- 시간/공간 복잡도 :
--   - 시간복잡도 : O(N log N), N은 예약 데이터 수
--   - 공간복잡도 : O(M), M은 결과 레코드 수

SELECT 
    A.APNT_NO,
    P.PT_NAME,
    P.PT_NO,
    D.MCDP_CD,
    D.DR_NAME,
    A.APNT_YMD
FROM 
    APPOINTMENT A
INNER JOIN 
    PATIENT P ON A.PT_NO = P.PT_NO
INNER JOIN 
    DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE 
    TO_CHAR(A.APNT_YMD, 'YYYY-MM-DD') = '2022-04-13'
    AND A.APNT_CNCL_YN = 'N'
    AND A.MCDP_CD = 'CS'
ORDER BY 
    A.APNT_YMD ASC;