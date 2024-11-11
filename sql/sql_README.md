# Jupyter Notebook에서 SQL 사용하기

## 1. ipython-sql 설치
```bash
pip install ipython-sql
```

## 2. 확장 기능 로드
Jupyter Notebook 셀에서 다음 명령어 실행:
```python
%load_ext sql
```

## 3. 데이터베이스 연결
```python
%sql mysql://username:password@localhost/database
```

연결 문자열 형식:
- username: 데이터베이스 사용자 이름
- password: 데이터베이스 비밀번호
- localhost: 데이터베이스 호스트
- database: 데이터베이스 이름

## 4. SQL 쿼리 실행
한 줄 쿼리:
```python
%sql SELECT * FROM table;
```

여러 줄 쿼리:
```sql
%%sql
SELECT column1, column2
FROM table
WHERE condition = 'value'
GROUP BY column1;
```

## 주의사항
- `%sql`은 한 줄 쿼리용
- `%%sql`은 여러 줄 쿼리용
- 쿼리 결과는 자동으로 pandas DataFrame으로 변환됨

## 활용 예시
```python
# 쿼리 결과를 변수에 저장
result = %sql SELECT * FROM table;

# pandas DataFrame으로 변환된 결과 확인
result.DataFrame()

# 결과 행 수 제한
%sql SELECT * FROM table LIMIT 5;
```