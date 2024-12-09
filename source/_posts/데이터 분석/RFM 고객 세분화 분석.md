---
title: "RFM 고객 세분화 분석"
categories:
  - 데이터 분석
tag:
  - 데이터 분석
  - 비즈니스 분석
  - sql
author: "Jiwon Kang"
date: 2024-12-09 22:07:15
---

## RFM 분석이란?

고객 관계 관리(CRM)를 위해 고객의 구매 행동 데이터를 기반으로 고객을 세분화하는 분석 기법으로, 다음의 3가지 지표를 기반으로 한다.

- **R**ecency : 얼마나 **최근에** 구매하였는가
    
    > 마지막으로 구매한 시점이 가까울수록 브랜드에 대한 관심도가 높다
    > 
- **F**requency : 얼마나 **자주** 구매하였는가
    
    > 방문한 빈도가 높을수록 브랜드에 대한 충성도 및 재구매 확률이 높다
    > 
- **M**onetary : 얼마나 **많은 금액**을 지출하였는가
    
    > 지출한 금액이 많을수록 브랜드에 더 큰 가치를 부여할 확률이 높다
    > 

![https://velog.io/@vive0508/rfm]('/images/데이터 분석/rfm.png')

---

## RFM 고객 세분화 예시

다음은 고객들의 최근 구매일, 총 구매 횟수, 총 구매 금액을 기준으로 RFM 값을 부여한 예시이다.

- Recency : 2024-12-09 기준으로 한 달 이내에 구매한 고객은 ‘recent’, 그 외에는 ‘past’로 구분
- Frequency : 총 5회 이상 구매한 고객은 ‘high’, 그 외에는 ‘low’로 구분
- Monetary : 총 10만원 이상 구매한 고객은 ‘high’, 그 외에는 ‘low’로 구분

| **고객번호** | **최근 구매일** | **총 구매 횟수(회)** | **총 구매 금액(천원)** | **Recency** | **Frequency** | **Monetary** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2024-11-28 | 15 | 125.5 | recent | high | high |
| 2 | 2024-12-01 | 9 | 21.8 | recent | high | low |
| 3 | 2024-11-25 | 2 | 3.5 | recent | low | low |
| 4 | 2024-12-02 | 1 | 210.0 | recent | low | high |
| 5 | 2024-09-11 | 7 | 315.3 | past | high | high |
| 6 | 2024-10-31 | 10 | 85.9 | past | high | low |
| 7 | 2024-11-05 | 3 | 151.2 | past | low | high |
| 8 | 2024-10-12 | 1 | 12.5 | past | low | low |

각 고객의 RFM 값을 기준으로 그룹을 나누어 볼 때, 그룹별 특징을 다음과 같이 추정할 수 있다.

| **고객번호** | **Recency** | **Frequency** | **Monetary** | **특징** |
| --- | --- | --- | --- | --- |
| 1 | recent | high | high | 가장 브랜드 충성도가 높은 고객군 |
| 2 | recent | high | low | 브랜드 관심도에 비해 매출 기여도는 낮은 고객군 |
| 3 | recent | low | low | 최근에 구매는 했으나 브랜드 충성도는 낮은 고객군 |
| 4 | recent | low | high | 최근까지 고가의 제품에 관심이 많은 고객군 |
| 5 | past | high | high | 브랜드 충성도가 높았으나 최근 구매가 없는 고객군 |
| 6 | past | high | low | 최근 구매가 없고 매출 기여도도 낮은 고객군 |
| 7 | past | low | high | 고가의 제품에 관심 있으나 최근 구매가 없는 고객군 |
| 8 | past | low | low | 이탈 가능성이 가장 높은 고객군 |

그렇다면 각 그룹에 대하여 어떠한 마케팅이 효과적일지도 다음과 같이 적용해볼 수 있다.

| **고객번호** | **Recency** | **Frequency** | **Monetary** | **마케팅 전략** |
| --- | --- | --- | --- | --- |
| 1 | recent | high | high | 개인 맞춤형 추천, 초대 이벤트, 멤버십 혜택 등 |
| 2 | recent | high | low | 기간 한정 세일, 묶음 판매, 할인 쿠폰 등 |
| 3 | recent | low | low | 재구매 유도 이벤트, 사용자 리뷰 공유 등 |
| 4 | recent | low | high | VIP 전용 제품 소개, 고급 제품 대상 특별 할인  등 |
| 5 | past | high | high | 개인 맞춤형 리마인드, 과거 구매 기반 제품 추천 등 |
| 6 | past | high | low | 가격 비교 정보 제공, 재구매 할인 쿠폰 등 |
| 7 | past | low | high | 고급 제품 위주의 카탈로그 홍보 등 |
| 8 | past | low | low | 고객 리뷰 요청, 브랜드 이미지 홍보 등 |

---

## SQL 쿼리 예시

- `With`문에서 recency, frequency, monetary 컬럼을 각각 생성한 다음 window 함수 `NTILE()`을 사용하여 각각 5단계로 구분하는 예제

```sql
-- RFM 점수 계산을 위한 기본 쿼리
WITH rfm_calc AS (
  SELECT 
    customer_id,
    DATEDIFF(day, MAX(purchase_date), CURRENT_DATE) as recency,
    COUNT(order_id) as frequency,
    SUM(amount) as monetary
  FROM orders
  GROUP BY customer_id
),
rfm_scores AS (
  SELECT *,
    NTILE(5) OVER (ORDER BY recency DESC) as R, # Recency 5단계 구분
    NTILE(5) OVER (ORDER BY frequency ASC) as F, # Frequency 5단계 구분
    NTILE(5) OVER (ORDER BY monetary ASC) as M # Monetary 5단계 구분
  FROM rfm_calc
)
SELECT * FROM rfm_scores;
```

---

## RFM 적용 시 고려사항

비즈니스의 성격, 산업군의 특성에 따라 다음의 고객 세분화 기준 등을 다르게 적용할 필요가 있다.

- Recency, Frequency, Monetary 지표의 분류 기준 및 단계 설정
    - 쿠팡, 배달의민족 등 자주 이용하는 플랫폼의 경우 한 달 이내 구매하지 않은 고객의 Recency 단계가 낮아질 수 있으나, 여행상품을 판매하는 항공사, 숙박업체 등은 최소 3개월에서 6개월 정도 구매이력이 없더라도 Recency가 떨어진다고 보기 어렵다.
    - 웨딩 서비스 등은 재구매가 거의 이루어지지 않으므로 Frequency는 사실상 의미가 없다.
- Frequency, Monetary 지표의 집계 기간 설정
    - Frequency와 Monetary 집계 기간을 서비스 출시 이후로 설정할 경우 오랜 기간 구매하지 않아 사실상 이탈한 고객의 Frequency, Monetary가 필요 이상으로 집계될 수 있으므로 적절한 집계 기간을 설정할 필요가 있다.

---

## Reference

[RFM 고객 세분화 분석이란 무엇일까요](https://datarian.io/blog/what-is-rfm)

[RFM 고객 세분화 (Segmentation)](https://velog.io/@vive0508/rfm)