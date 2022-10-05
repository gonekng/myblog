---
title : "R_basic_statistics"
categories:
  - r
tag:
  - r
  - statistic
author : "Jiwon Kang"
date : 2022-03-15 16:42:09
output : 
  html_document:
    keep_md : true
---

### 통계 분석 개요

1. 기술통계(discriptive Statistics) : 평균, 최솟값, 최댓값, 중앙값 등 데이터의 특징을 서술하는 것

2. 추론통계(inferential Statistics) : 변수 간의 관계를 파악하여 변수 간 인과관계나 새로운 사실을 밝혀내는 것

   1) 평균 차이 검정 : 집단별 평균의 차이가 실제로 있는가를 검정하는 것
   
   2) 교차분석 : 범주형 변수로 구성된 집단들의 관련성을 검정하는 것
   
   3) 상관관계분석 : 변수 간의 상관관계(correlation)를 알아보는 것
      - 상관관계는 한 변수가 변화하면 다른 변수도 변화하는 관계를 의미

      - 상관계수(r) : 변화의 강도와 방향을 나타내는 계수 (-1 <= r <= 1)

      - 수치가 클수록 영향을 주는 강도가 크며, '+'는 정의 관계, '-'는 역의 관계

   4) 회귀분석 : 독립변수와 종속변수 간의 인과관계를 분석하는 것
      - 독립변수 : 영향을 주는 변수 / 종속변수 : 영향을 받는 변수

      - 단순회귀분석 : 종속변수 1개, 독립변수 1개 (y = a + b*x)

      - 다중회귀분석 : 종속변수 1개, 독립변수 2개 이상 (y = a + b1*x1 + b2*x2 +...)

### 통계 검정

1. 가설(hypothesis)
   - 어떤 현상을 설명하기 위해서 가정하는 명제
   - 귀무가설(H0) : 처음부터 기각될 것으로 예상되는 가설 (영가설)

   - 대립가설(H1) : 귀무가설이 기각될 경우 받아들여지는 가설
   

2. 유의수준(significance level, p값)
   - 귀무가설이 맞는데도 대립가설을 채택할 확률 (제1종 오류의 최대 허용 범위)

   - 가설 검정에서 인정하는 유의수준 : 5%, 1%, 0.1%

   - 신뢰수준(confidence level) : 신뢰할 수 있는 범위 (1-유의수준)
   

3. 척도(scale)
   - 명목척도 : 측정대상의 특성이나 범주를 구분하는 척도
     - 등번호, 성별, 인종, 지역 등
     - 산술 연산을 할 수 없음

   - 서열척도 : 측정대상의 등급순위를 나타내는 척도
     - 계급, 사회계층, 자격등급 등
     - 산술 연산을 할 수 없음
     - 척도 간의 거리나 간격을 나타내지는 않음

   - 등간척도 : 측정대상을 일정한 간격으로 구분한 척도
     - 온도, 학력, 시험점수 등
     - 서열 뿐만 아니라 거리와 간격도 표현 가능
     - 덧셈, 뺄셈을 할 수 있음

   - 비율척도 : 측정대상을 비율로 나타낼 수 있는 척도
     - 연령, 키, 무게 등
     - 사칙연산을 모두 할 수 있음

### 통계 분석 사례

#### 1. 두 집단의 평균 차이 검정 - 독립표본 t검정(t.test())
   - 독립변수는 명목척도, 종속변수는 등간척도 또는 비율척도이어야 함
   - 귀무가설 : auto와 manual의 cty평균은 차이가 없다.

```r
mpg1 <- read.csv("mpg1.csv")
str(mpg1)
```

```
## 'data.frame':	234 obs. of  5 variables:
##  $ manufacturer : chr  "audi" "audi" "audi" "audi" ...
##  $ trans       : chr  "auto" "manual" "manual" "auto" ...
##  $ drv         : chr  "f" "f" "f" "f" ...
##  $ cty         : int  18 21 20 21 16 18 18 18 16 20 ...
##  $ hwy         : int  29 29 31 30 26 26 27 26 25 28 ...
```

```r
t.test(data=mpg1, cty~trans)
```

```
## 
## 	Welch Two Sample t-test
## 
## data :  cty by trans
## t = -4.5375, df = 132.32, p-value = 1.263e-05
## alternative hypothesis : true difference in means between group auto and group manual is not equal to 0
## 95 percent confidence interval:
##  -3.887311 -1.527033
## sample estimates:
##   mean in group auto mean in group manual 
##             15.96815             18.67532
```

###### >> p-value = 1.263e-05, 귀무가설 기각(유의수준 .05에서 유의미한 차이가 있음)

##
#### 2. 교차분석 - 카이제곱 검정(chisq.test())
   - 귀무가설 : trans에 따라 drv의 차이가 없다.
   
```r
mpg1 <- read.csv("mpg1.csv")
str(mpg1)
```

```
## 'data.frame':	234 obs. of  5 variables:
##  $ manufacturer : chr  "audi" "audi" "audi" "audi" ...
##  $ trans       : chr  "auto" "manual" "manual" "auto" ...
##  $ drv         : chr  "f" "f" "f" "f" ...
##  $ cty         : int  18 21 20 21 16 18 18 18 16 20 ...
##  $ hwy         : int  29 29 31 30 26 26 27 26 25 28 ...
```

```r
table(mpg1$trans, mpg1$drv)
```

```
##         
##           4  f  r
##   auto   75 65 17
##   manual 28 41  8
```

```r
prop.table(table(mpg1$trans, mpg1$drv),1)
```

```
##         
##                  4         f         r
##   auto   0.4777070 0.4140127 0.1082803
##   manual 0.3636364 0.5324675 0.1038961
```

```r
chisq.test(mpg1$trans, mpg1$drv)
```

```
## 
## 	Pearson's Chi-squared test
## 
## data :  mpg1$trans and mpg1$drv
## X-squared = 3.1368, df = 2, p-value = 0.2084
```

###### >> p-value = 0.2084, 귀무가설 채택(유의수준 .05에서 유의미한 차이가 없음)
  
##
#### 3) 상관관계분석 - cor.test()
    - 귀무가설 : cty와 hwy는 상관관계가 없다.
    
```r
mpg1 <- read.csv("mpg1.csv")
str(mpg1)
```

```
## 'data.frame':	234 obs. of  5 variables:
##  $ manufacturer : chr  "audi" "audi" "audi" "audi" ...
##  $ trans       : chr  "auto" "manual" "manual" "auto" ...
##  $ drv         : chr  "f" "f" "f" "f" ...
##  $ cty         : int  18 21 20 21 16 18 18 18 16 20 ...
##  $ hwy         : int  29 29 31 30 26 26 27 26 25 28 ...
```

```r
cor.test(mpg1$cty, mpg1$hwy)
```

```
## 
## 	Pearson's product-moment correlation
## 
## data :  mpg1$cty and mpg1$hwy
## t = 49.585, df = 232, p-value < 2.2e-16
## alternative hypothesis : true correlation is not equal to 0
## 95 percent confidence interval:
##  0.9433129 0.9657663
## sample estimates:
##       cor 
## 0.9559159
```

###### >> p-value < 2.2e-16, 귀무가설 기각(유의수준 .05에서 상관관계가 있음)

###### >> 상관계수 r = 0.9559159 (매우 높은 상관관계)

##
#### 4. 단순회귀분석 - lm()
   - 독립변수와 종속변수가 모두 등간척도 또는 비율척도이어야 함
   - 귀무가설 : disp는 mpg에 영향을 주지 않는다.
   
```r
RA <- lm(data=mtcars, mpg~disp)
summary(RA)
```

```
## 
## Call:
## lm(formula = mpg ~ disp, data = mtcars)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -4.8922 -2.2022 -0.9631  1.6272  7.2305 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 29.599855   1.229720  24.070  < 2e-16 ***
## disp        -0.041215   0.004712  -8.747 9.38e-10 ***
## ---
## Signif. codes :  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error : 3.251 on 30 degrees of freedom
## Multiple R-squared :  0.7183,	Adjusted R-squared :  0.709 
## F-statistic : 76.51 on 1 and 30 DF,  p-value : 9.38e-10
```

```r
plot(data=mtcars, mpg~disp)
abline(RA, col="red")
```

![](images/chapter8_files/figure-html/unnamed-chunk-4-1.png)<!-- -->

###### >> p-value = 9.38e-10, 귀무가설 기각(유의수준 .05에서 회귀모형이 적합함)

###### >> 절편(Intercept) = 29.599855 (유의수준 .05에서 유의함)

###### >> 회귀계수(Estimate) = -0.041215 (유의수준 .05에서 유의함)

###### >> 회귀식 : mpg = 29.599855 - 0.041215 * disp

###### >> 수정된 결정계수(Adjusted R-Squared) = .709

##
#### 5. 다중회귀분석 - lm()

```r
RA <- lm(data=mtcars, mpg~disp+hp+wt)
summary(RA)
```

```
## 
## Call:
## lm(formula = mpg ~ disp + hp + wt, data = mtcars)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -3.891 -1.640 -0.172  1.061  5.861 
## 
## Coefficients:
##              Estimate Std. Error t value Pr(>|t|)    
## (Intercept) 37.105505   2.110815  17.579  < 2e-16 ***
## disp        -0.000937   0.010350  -0.091  0.92851    
## hp          -0.031157   0.011436  -2.724  0.01097 *  
## wt          -3.800891   1.066191  -3.565  0.00133 ** 
## ---
## Signif. codes :  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error : 2.639 on 28 degrees of freedom
## Multiple R-squared :  0.8268,	Adjusted R-squared :  0.8083 
## F-statistic : 44.57 on 3 and 28 DF,  p-value : 8.65e-11
```


###### >> p-value = 8.65e-11, 귀무가설 기각(유의수준 .05에서 회귀모형이 적합함)

###### >> 절편(Intercept) = 29.599855 (유의수준 .05에서 유의함)

###### >> dist의 계수 = -0.000937 (유의수준 .05에서 통계적으로 유의하지 않음)

###### >> hp의 계수 = -0.031157 (유의수준 .05에서 유의함)

###### >> wt의 계수 = -3.800891 (유의수준 .05에서 유의함)

###### >> 회귀식 : mpg = 29.599855 - 0.000937 * disp - 0.031157 * hp - 3.800891 * wt

###### >> 수정된 결정계수(Adjusted R-Squared) = .8083
