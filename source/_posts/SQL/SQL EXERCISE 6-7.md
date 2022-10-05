---
title: "SQL EXERCISE 6-7"
categories:
  - sql
  - Oracle
tag:
  - sql
  - Oracle
author: "Jiwon Kang"
date: 2022-05-02 09:32:11
---

# CHAPTER 06

### Q1.

101번 사원에 대해 아래의 결과를 산출하는 쿼리를 작성해 보자.

```sql
---------------------------------------------------------------------------------------
사번   사원명   job명칭 job시작일자  job종료일자   job수행부서명
---------------------------------------------------------------------------------------
```

### A1.

```sql
SELECT a.employee_id 사번
        , a.emp_name 사원명
        , b.job_title job 명칭
        , c.start_date job 시작일자
        , c.end_date job 종료일자
        , d.department_name
    FROM employees a
        , jobs b
        , job_history c
        , departments d
    WHERE a.employee_id = c.employee_id
        AND b.job_id = c.job_id
        AND c.department_id = d.department_id
        AND a.employee_id = 101;
```

필요한 컬럼 및 테이블

- 사번(`employee_id`), 사원명(`emp_name`) → `employees`
- job명칭(`job_title`) → `jobs`
- job시작일자(`start_date`), job종료일자(`end_date`) →  `job_history`
- job수행부서명(`department_name`) → `departments`

테이블 조인 조건

- `employees` & `job_history` → `employee_id`
- `jobs` & `job_history` → `job_id`
- `job_history` & `departments` → `department_id`

기타 조건

- 101번 사원에 대한 정보 : `a.employee_id = 101`

![](/images/sql/sql_ex/0.png)

---

### Q2.

아래의 쿼리를 수행하면 오류가 발생한다. 오류의 원인은 무엇인가?

```sql
select a.employee_id, a.emp_name, b.job_id, b.department_id
from employees a,
job_history b
where a.employee_id = b.employee_id(+)
and a.department_id(+) = b.department_id;
```

### A2.

(+) 연산자를 활용한 외부 조인의 경우 한쪽 방향으로만 가능하고, 이때 (+) 연산자는 데이터가 없는 테이블의 컬럼에만 붙여야 한다.

따라서, 위의 쿼리에서는 마지막 줄을 and `a.department_id = b.department_id(+)`로 수정해야 한다.

---

### Q3.

외부조인시 (+)연산자를 같이 사용할 수 없는데, IN절에 사용하는 값이 1개인 경우는 사용 가능하다. 그 이유는 무엇일까?

### A3.

IN절에 사용하는 값이 1개인 경우는 등호를 사용하는 것과 같은 의미이므로 사용 가능하다.

---

### Q4.

다음의 쿼리를 ANSI 문법으로 변경해 보자.

```sql
SELECT a.department_id
			, a.department_name
		FROM departments a
				, employees b
		WHERE a.department_id = b.department_id
				AND b.salary > 3000
		ORDER BY a.department_name;
```

### A4.

```sql
SELECT a.department_id, a.department_name
		FROM departments a
		INNER JOIN employees b
				On (a.department_id = b.department_id
						AND b.salary > 3000)
		ORDER BY a.department_name;
```

위의 쿼리는 `departments` 테이블과 `employees` 테이블의 내부 조인이다.

ANSI 문법에서 내부 조인은 `FROM`절에서 `INNER JOIN` 으로 수행하며,
조인 조건은 `ON` 절에 명시한다.

![](/images/sql/sql_ex/1.png)

---

### Q5.

다음은 연관성 있는 서브쿼리이다. 이를 연관성 없는 서브쿼리로 변환해 보자.

```sql
SELECT a.department_id
				, a.department_name
		FROM departments a
		WHERE EXISTS ( SELECT 1
											FROM job_history b
											WHERE a.department_id = b.department_id );
```

### A5.

```sql
SELECT a.department_id
				, a.department_name
		FROM departments a
		WHERE a.department_id
				IN (SELECT b.department_id
								FROM job_history b);
```

위의 쿼리는 `job_history` 테이블에 존재하는 `department_id`에 대해
`departments` 테이블의 `department_id`와 `department_name`을 출력한다.

이를 연관성 없는 서브쿼리로 변환하기 위해
조인 조건 대신 `IN` 연산자를 통해 메인 쿼리의 조건으로 활용했다. 

![](/images/sql/sql_ex/2.png)

---

### Q6.

연도별 이태리 최대매출액과 사원을 작성하는 쿼리를 학습했다. 이를 기준으로 최대 매출액, 최소매출액, 해당 사원을 조회하는 쿼리를 작성해 보자.

### A6.

```sql
SELECT emp.sales_year
        , emp.employee_id
        , emp2.emp_name
        , emp.amount_sold
    FROM (SELECT SUBSTR(a.sales_month, 1, 4)
											AS sales_year
                , a.employee_id
                , SUM(a.amount_sold) as amount_sold
            FROM sales a
                , customers b
                , countries c
            WHERE a.cust_id = b.cust_id
                AND b.country_id = c.country_id
                AND c.country_name = 'Italy'
            GROUP BY SUBSTR(a.sales_month, 1, 4)
                    , a.employee_id) emp
        , (SELECT sales_year
                , MAX(amount_sold) AS max_sold
                , MIN(amount_sold) AS min_sold
            FROM (SELECT SUBSTR(a.sales_month, 1, 4)
															AS sales_year
                        , a.employee_id
                        , SUM(a.amount_sold) as amount_sold
                    FROM sales a
                        , customers b
                        , countries c
                    WHERE a.cust_id = b.cust_id
                        AND b.country_id = c.country_id
                        AND c.country_name = 'Italy'
                    GROUP BY SUBSTR(a.sales_month, 1, 4)
                            , a.employee_id) k
            GROUP BY sales_year) sale
        , employees emp2
    WHERE emp.sales_year = sale.sales_year
        AND (emp.amount_sold = sale.max_sold
			        OR emp.amount_sold = sale.min_sold)
        AND emp.employee_id = emp2.employee_id
    ORDER BY sales_year;
```

서브쿼리 1 : 연도, 사원별 이탈리아 매출액 (`emp`)

- `sales`, `customers`, `countries`를 조인하여 매출액 합계 계산

```sql
SELECT SUBSTR(a.sales_month, 1, 4)
											AS sales_year
                , a.employee_id
                , SUM(a.amount_sold) as amount_sold
            FROM sales a
                , customers b
                , countries c
            WHERE a.cust_id = b.cust_id
                AND b.country_id = c.country_id
                AND c.country_name = 'Italy'
            GROUP BY SUBSTR(a.sales_month, 1, 4)
                    , a.employee_id
```

서브쿼리 2: 연도별 최대, 최소 매출액 (`sale`)

- `emp` 서브쿼리에서 연도별 최대, 최소값 계산

```sql
SELECT sales_year
                , MAX(amount_sold) AS max_sold
                , MIN(amount_sold) AS min_sold
            FROM (SELECT SUBSTR(a.sales_month, 1, 4)
															AS sales_year
                        , a.employee_id
                        , SUM(a.amount_sold) as amount_sold
                    FROM sales a
                        , customers b
                        , countries c
                    WHERE a.cust_id = b.cust_id
                        AND b.country_id = c.country_id
                        AND c.country_name = 'Italy'
                    GROUP BY SUBSTR(a.sales_month, 1, 4)
                            , a.employee_id) k
            GROUP BY sales_year
```

![](/images/sql/sql_ex/3.png)

---

# CHAPTER 07

### Q1.

계층형 쿼리 응용편에서 `LISTAGG` 함수를 사용해 다음과 같이 로우를 컬럼으로 분리했었다.

```sql
SELECT department_id,
LISTAGG(emp_name, ',') WITHIN GROUP (ORDER BY emp_name) as empnames
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id;
```

`LISTAGG` 함수 대신 계층형 쿼리, 분석함수를 사용해서 위 쿼리와 동일한 결과를 산출하는 쿼리를 작성해 보자.

### A1.

```sql
SELECT department_id
      , SUBSTR(SYS_CONNECT_BY_PATH(emp_name, ','),2) empnames
    FROM (
          SELECT emp_name
              , department_id
              , COUNT(*) OVER (PARTITION BY department_id) cnt
              , ROW_NUMBER() OVER (PARTITION BY department_id
                                   ORDER BY emp_name) rowseq
            FROM employees
            WHERE department_id IS NOT NULL
         )
    WHERE rowseq = cnt
    START WITH rowseq = 1
    CONNECT BY PRIOR rowseq + 1 = rowseq
        AND PRIOR department_id = department_id;
```

서브쿼리 : 부서별 사원명, 사원 수, 행 번호 구하기

- 부서별 파티션 : `PARTITION BY department_id` `ORDER BY emp_name`

```sql
SELECT emp_name
              , department_id
              , COUNT(*) OVER (PARTITION BY department_id) cnt
              , ROW_NUMBER() OVER (PARTITION BY department_id
                                   ORDER BY emp_name) rowseq
            FROM employees
            WHERE department_id IS NOT NULL
```

각 파티션의 마지막 행에 대하여(`WHERE rowseq = cnt`)
파티션의 첫 행부터(`START WITH rowseq = 1`)
부서번호가 같은 직전 행까지(`CONNECT BY PRIOR rowseq + 1 = rowseq
 AND PRIOR department_id = department_id`)의 `emp_name`을
연결하여 나타낸다.(`SUBSTR(SYS_CONNECT_BY_PATH(emp_name, ','),2)`)

![](/images/sql/sql_ex/4.png)

---

### Q2.

아래의 쿼리는 사원테이블에서 `JOB_ID`가 '`SH_CLERK`'인 사원을 조회하는 쿼리이다.

```sql
SELECT employee_id, emp_name, hire_date
FROM employees
WHERE job_id = 'SH_CLERK'
ORDER By hire_date;

EMPLOYEE_ID EMP_NAME             HIRE_DATE         
----------- -------------------- -------------------
        184 Nandita Sarchand     2004/01/27 00:00:00 
        192 Sarah Bell           2004/02/04 00:00:00 
        185 Alexis Bull          2005/02/20 00:00:00 
        193 Britney Everett      2005/03/03 00:00:00 
        188 Kelly Chung          2005/06/14 00:00:00
....        
....
        199 Douglas Grant        2008/01/13 00:00:00
        183 Girard Geoni         2008/02/03 00:00:00
```

사원테이블에서 퇴사일자(`retire_date`)는 모두 비어있는데,
위 결과에서 사원번호가 184인 사원의 퇴사일자는 다음으로 입사일자가 빠른 192번 사원의 입사일자라고 가정해서
다음과 같은 형태로 결과를 추출해낼 수 있도록 쿼리를 작성해 보자. (입사일자가 가장 최근인 183번 사원의 퇴사일자는 `NULL`이다)

```sql
EMPLOYEE_ID EMP_NAME             HIRE_DATE             RETIRE_DATE
----------- -------------------- -------------------  ---------------------------
        184 Nandita Sarchand     2004/01/27 00:00:00  2004/02/04 00:00:00
        192 Sarah Bell           2004/02/04 00:00:00  2005/02/20 00:00:00
        185 Alexis Bull          2005/02/20 00:00:00  2005/03/03 00:00:00
        193 Britney Everett      2005/03/03 00:00:00  2005/06/14 00:00:00
        188 Kelly Chung          2005/06/14 00:00:00  2005/08/13 00:00:00
....        
....
        199 Douglas Grant        2008/01/13 00:00:00  2008/02/03 00:00:00
        183 Girard Geoni         2008/02/03 00:00:00
```

### A2.

```sql
SELECT employee_id
        , emp_name
        , hire_date
        , LEAD(hire_date)
						OVER (PARTITION BY job_id ORDER BY hire_date)
						AS retire_date
    FROM employees
    WHERE job_id = 'SH_CLERK'
    ORDER BY hire_date;
```

문제에서 요구하는 퇴사일자(`retire_date`)는
입사일자로 정렬했을 때 다음 사원의 입사일자(`hire_date`)와 같다.

따라서, 다음 행의 데이터를 가져오는 `LEAD(hire_date)` 함수를 통해
각 사원의 퇴사일자(`retire_date`)를 산출할 수 있다.

![](/images/sql/sql_ex/5.png)

---

### Q3.

`sales` 테이블에는 판매데이터, `customers` 테이블에는 고객정보가 있다.
2001년 12월 판매데이터 중 현재일자를 기준으로 고객의 나이를 계산해서 다음과 같이 연령대별 매출금액을 보여주는 쿼리를 작성해 보자.

```sql
-------------------------   
연령대    매출금액
-------------------------
10대      xxxxxx
20대      ....
30대      .... 
40대      ....
-------------------------
```

### A3.

```sql
WITH age_amt
		AS (
		    SELECT TRUNC((TO_CHAR(SYSDATE, 'yyyy')
														 - b.cust_year_of_birth), -1)
										AS age_seg
			        , SUM(a.amount_sold)
										AS amount
		        FROM sales a
                 , customers b
            WHERE a.sales_month = '200112'
		            AND a.cust_id = b.cust_id
            GROUP BY TRUNC((TO_CHAR(SYSDATE, 'yyyy')
														 - b.cust_year_of_birth), -1)
       )
SELECT * FROM age_amt
    ORDER BY age_seg;
```

서브쿼리 : 현재일자 기준 고객 연령대별 매출액 구하기 (`age_amt`)

- 현재일자를 기준으로 고객의 나이를 계산한 다음
(`TO_CHAR(SYSDATE, 'yyyy') - b.cust_year_of_birth`)
각 연령대별 `amount_sold`의 합계를 계산하였음

```sql
SELECT TRUNC((TO_CHAR(SYSDATE, 'yyyy')
														 - b.cust_year_of_birth), -1)
										AS age_seg
			        , SUM(a.amount_sold)
										AS amount
		        FROM sales a
                 , customers b
            WHERE a.sales_month = '200112'
		            AND a.cust_id = b.cust_id
            GROUP BY TRUNC((TO_CHAR(SYSDATE, 'yyyy')
														 - b.cust_year_of_birth), -1)
```

![](/images/sql/sql_ex/6.png)

---

### Q4.

월별로 판매금액이 가장 하위에 속하는 대륙 목록을 뽑아보자.
(대륙목록은 `countries` 테이블의 `country_region`에 있으며, `country_id` 컬럼으로 `customers` 테이블과 조인을 해서 구한다.)

```sql
---------------------------------   
매출월    지역(대륙)  매출금액 
---------------------------------
199801    Oceania      xxxxxx
199803    Oceania      xxxxxx
...
---------------------------------
```

### A4.

```sql
WITH basis
			AS (
		      SELECT a.sales_month
			          , c.country_region
                , SUM(a.amount_sold) as amt
	          FROM sales a
		            , customers b
                , countries c
            WHERE a.cust_id = b.cust_id
	            AND b.country_id = c.country_id
            GROUP BY a.sales_month, c.country_region
         )
	 , month_amt
			AS (
          SELECT sales_month AS "매출월"
                , country_region AS "지역(대륙)"
                , amt AS "매출금액"
                , RANK()
										OVER (PARTITION BY sales_month
													ORDER BY amt) AS ranks
	          FROM basis
         )
SELECT "매출월", "지역(대륙)", "매출금액"
    FROM month_amt
    WHERE ranks = 1;
```

서브쿼리 1 : 월별, 지역별 판매금액 합계 구하기 (`basis`)

- `sales`, `customers`, `countries` 조인
- 월별, 지역별 합계 : `SUM(a.amount_sold) as amt`

```sql
SELECT a.sales_month
			 , c.country_region
       , SUM(a.amount_sold) as amt
	  FROM sales a
		   , customers b
       , countries c
    WHERE a.cust_id = b.cust_id
	     AND b.country_id = c.country_id
    GROUP BY a.sales_month, c.country_region
```

서브쿼리 2 : 월별로 각 대륙의 판매금액 합계 순위 구하기 (`month_amt`)

- basis 서브쿼리에서 `sales_month` 파티션별 `amt` 순위값 계산

```sql
SELECT sales_month AS "매출월"
       , country_region AS "지역(대륙)"
       , amt AS "매출금액"
       , RANK()
						OVER (PARTITION BY sales_month
									ORDER BY amt) AS ranks
	          FROM basis
```

![](/images/sql/sql_ex/7.png)

---

### Q5.

5장 연습문제 5번의 정답 결과를 이용해 다음과 같이 지역별, 대출종류별, 월별 대출잔액과 지역별 파티션을 만들어
대출종류별 대출잔액의 %를 구하는 쿼리를 작성해보자.

```sql
------------------------------------------------------------------------------------------------
지역    대출종류        201111         201112    201210    201211   201212   203110    201311
------------------------------------------------------------------------------------------------
서울    기타대출       73996.9( 36% )
서울    주택담보대출   130105.9( 64% ) 
부산
...
...
-------------------------------------------------------------------------------------------------
```

### A5.

```sql
WITH basis AS (
						SELECT region, gubun
									, CASE WHEN period = '201111'
											THEN loan_jan_amt ELSE 0 END amt1
									, CASE WHEN period = '201112'
											THEN loan_jan_amt ELSE 0 END amt2
									, CASE WHEN period = '201210'
											THEN loan_jan_amt ELSE 0 END amt3
									, CASE WHEN period = '201211'
											THEN loan_jan_amt ELSE 0 END amt4
									, CASE WHEN period = '201212'
											THEN loan_jan_amt ELSE 0 END amt5
									, CASE WHEN period = '201310'
											THEN loan_jan_amt ELSE 0 END amt6
									, CASE WHEN period = '201311'
											THEN loan_jan_amt ELSE 0 END amt7
								FROM kor_loan_status
							)
	, sum_amt AS (
						 SELECT region, gubun
										, SUM(amt1) AS amt1
										, SUM(amt2) AS amt2
										, SUM(amt3) AS amt3
										, SUM(amt4) AS amt4
										, SUM(amt5) AS amt5
										, SUM(amt6) AS amt6
										, SUM(amt7) AS amt7
								FROM basis
								GROUP BY region, gubun
					     )
SELECT region AS "지역", gubun AS "대출종류"
			, amt1 || '(' || ROUND(RATIO_TO_REPORT(amt1)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201111"
			, amt2 || '(' || ROUND(RATIO_TO_REPORT(amt2)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201112"
			, amt3 || '(' || ROUND(RATIO_TO_REPORT(amt3)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201210"
			, amt4 || '(' || ROUND(RATIO_TO_REPORT(amt4)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201211"
			, amt5 || '(' || ROUND(RATIO_TO_REPORT(amt5)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201212"
			, amt6 || '(' || ROUND(RATIO_TO_REPORT(amt6)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201311"
			, amt7 || '(' || ROUND(RATIO_TO_REPORT(amt7)
					OVER (PARTITION BY region), 3) *100 || '%)'
					AS "201311"
		FROM sum_amt
		ORDER BY region;
```

서브쿼리 1 :  월별 대출잔액 변수 만들기 (`basis`)

- `CASE WHEN ~ THEN ~ ELSE` 구문으로 월별 대출잔액 변수 생성

```sql
SELECT region, gubun
		, CASE WHEN period = '201111'
					THEN loan_jan_amt ELSE 0 END amt1
		, CASE WHEN period = '201112'
					THEN loan_jan_amt ELSE 0 END amt2
		, CASE WHEN period = '201210'
					THEN loan_jan_amt ELSE 0 END amt3
		, CASE WHEN period = '201211'
					THEN loan_jan_amt ELSE 0 END amt4
		, CASE WHEN period = '201212'
					THEN loan_jan_amt ELSE 0 END amt5
		, CASE WHEN period = '201310'
					THEN loan_jan_amt ELSE 0 END amt6
		, CASE WHEN period = '201311'
					THEN loan_jan_amt ELSE 0 END amt7
	FROM kor_loan_status
```

서브쿼리 2 : 지역, 구분으로 그룹화하여 월별 합계 산출 (`sum_amt`)

```sql
SELECT region, gubun
			, SUM(amt1) AS amt1, SUM(amt2) AS amt2
			, SUM(amt3) AS amt3, SUM(amt4) AS amt4
			, SUM(amt5) AS amt5, SUM(amt6) AS amt6
			, SUM(amt7) AS amt7
	FROM basis
	GROUP BY region, gubun
```

메인 쿼리 : 지역 내 대출종류별 대출잔액의 비율 산출

```sql
SELECT region AS "지역", gubun AS "대출종류"
		, amt1 || '(' || ROUND(RATIO_TO_REPORT(amt1)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201111"
		, amt2 || '(' || ROUND(RATIO_TO_REPORT(amt2)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201112"
		, amt3 || '(' || ROUND(RATIO_TO_REPORT(amt3)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201210"
		, amt4 || '(' || ROUND(RATIO_TO_REPORT(amt4)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201211"
		, amt5 || '(' || ROUND(RATIO_TO_REPORT(amt5)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201212"
		, amt6 || '(' || ROUND(RATIO_TO_REPORT(amt6)
			OVER (PARTITION BY region), 3) *100 || '%)' AS "201311"
		, amt7 || '(' || ROUND(RATIO_TO_REPORT(amt7)
			OVER (PARTITION BY region), 3) *100 || '%)'	AS "201311"
	FROM sum_amt
	ORDER BY region
```

![](/images/sql/sql_ex/8.png)