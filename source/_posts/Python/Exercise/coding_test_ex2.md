---
title: "Coding Test Ex.2"
categories:
  - python
  - coding test
tag:
  - python
  - programmers
author: "Jiwon Kang"
date: 2022-11-15 16:45:15
---

# 성격유형검사

## 문제

나만의 카카오 성격 유형 검사지를 만들려고 합니다. 성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.

| 지표 번호 | 성격 유형 |
| --- | --- |
| 1번 지표 | 라이언형(R), 튜브형(T) |
| 2번 지표 | 콘형(C), 프로도형(F) |
| 3번 지표 | 제이지형(J), 무지형(M) |
| 4번 지표 | 어피치형(A), 네오형(N) |

4개의 지표가 있으므로 성격 유형은 총 16(=2 x 2 x 2 x 2)가지가 나올 수 있습니다. 예를 들어, "RFMN"이나 "TCMA"와 같은 성격 유형이 있습니다.

검사지에는 총 n개의 질문이 있고, 각 질문에는 아래와 같은 7개의 선택지가 있습니다.

- `매우 비동의`
- `비동의`
- `약간 비동의`
- `모르겠음`
- `약간 동의`
- `동의`
- `매우 동의`

각 질문은 1가지 지표로 성격 유형 점수를 판단합니다. 예를 들어, 어떤 한 질문에서 4번 지표로 아래 표처럼 점수를 매길 수 있습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 네오형 3점 |
| 비동의 | 네오형 2점 |
| 약간 비동의 | 네오형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 어피치형 1점 |
| 동의 | 어피치형 2점 |
| 매우 동의 | 어피치형 3점 |

검사자가 질문에서 `약간 동의` 를 선택할 경우 어피치형(A) 성격 유형 1점을 받게 됩니다. 만약 검사자가 `매우 비동의` 를 선택할 경우 네오형(N) 성격 유형 3점을 받게 됩니다.

위 예시처럼 네오형이 비동의, 어피치형이 동의인 경우만 주어지지 않고, 질문에 따라 네오형이 동의, 어피치형이 비동의인 경우도 주어질 수 있습니다. 하지만 각 선택지는 고정적인 크기의 점수를 가지고 있습니다.

- `매우 동의`나 `매우 비동의` 를 선택하면 3점을 얻습니다.
- `동의`나 `비동의` 를 선택하면 2점을 얻습니다.
- `약간 동의`나 `약간 비동의` 를 선택하면 1점을 얻습니다.
- `모르겠음` 를 선택하면 점수를 얻지 않습니다.

검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단합니다. 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.

질문마다 판단하는 지표를 담은 1차원 문자열 배열 `survey`와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 `choices`가 매개변수로 주어집니다. 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- 1 ≤ `survey`의 길이 ( = `n`) ≤ 1,000
    - `survey`의 원소는 `"RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"` 중 하나입니다.
    - `survey[i]`의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
    - `survey[i]`의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
- `choices`의 길이 = `survey`의 길이
    - `choices[i]`는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
    - 1 ≤ `choices`의 원소 ≤ 7
        
        
        | choices | 뜻 |
        | --- | --- |
        | 1 | 매우 비동의 |
        | 2 | 비동의 |
        | 3 | 약간 비동의 |
        | 4 | 모르겠음 |
        | 5 | 약간 동의 |
        | 6 | 동의 |
        | 7 | 매우 동의 |

### 입출력 예시

| survey | choices | result |
| --- | --- | --- |
| ["AN", "CF", "MJ", "RT", "NA"] | [5, 3, 2, 7, 5] | "TCMA" |
| ["TR", "RT", "TR"] | [7, 1, 3] | "RCJA" |

**입출력 예 #1**

1번 질문의 점수 배치는 아래 표와 같습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 어피치형 3점 |
| 비동의 | 어피치형 2점 |
| 약간 비동의 | 어피치형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 네오형 1점 |
| 동의 | 네오형 2점 |
| 매우 동의 | 네오형 3점 |

1번 질문에서는 지문의 예시와 다르게 비동의 관련 선택지를 선택하면 어피치형(A) 성격 유형의 점수를 얻고, 동의 관련 선택지를 선택하면 네오형(N) 성격 유형의 점수를 얻습니다. 1번 질문에서 검사자는 `약간 동의` 선택지를 선택했으므로 네오형(N) 성격 유형 점수 1점을 얻게 됩니다.

2번 질문의 점수 배치는 아래 표와 같습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 콘형 3점 |
| 비동의 | 콘형 2점 |
| 약간 비동의 | 콘형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 프로도형 1점 |
| 동의 | 프로도형 2점 |
| 매우 동의 | 프로도형 3점 |

2번 질문에서 검사자는 `약간 비동의` 선택지를 선택했으므로 콘형(C) 성격 유형 점수 1점을 얻게 됩니다.

3번 질문의 점수 배치는 아래 표와 같습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 무지형 3점 |
| 비동의 | 무지형 2점 |
| 약간 비동의 | 무지형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 제이지형 1점 |
| 동의 | 제이지형 2점 |
| 매우 동의 | 제이지형 3점 |

3번 질문에서 검사자는 `비동의` 선택지를 선택했으므로 무지형(M) 성격 유형 점수 2점을 얻게 됩니다.

4번 질문의 점수 배치는 아래 표와 같습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 라이언형 3점 |
| 비동의 | 라이언형 2점 |
| 약간 비동의 | 라이언형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 튜브형 1점 |
| 동의 | 튜브형 2점 |
| 매우 동의 | 튜브형 3점 |

4번 질문에서 검사자는 `매우 동의` 선택지를 선택했으므로 튜브형(T) 성격 유형 점수 3점을 얻게 됩니다.

5번 질문의 점수 배치는 아래 표와 같습니다.

| 선택지 | 성격 유형 점수 |
| --- | --- |
| 매우 비동의 | 네오형 3점 |
| 비동의 | 네오형 2점 |
| 약간 비동의 | 네오형 1점 |
| 모르겠음 | 어떤 성격 유형도 점수를 얻지 않습니다 |
| 약간 동의 | 어피치형 1점 |
| 동의 | 어피치형 2점 |
| 매우 동의 | 어피치형 3점 |

5번 질문에서 검사자는 `약간 동의` 선택지를 선택했으므로 어피치형(A) 성격 유형 점수 1점을 얻게 됩니다.

1번부터 5번까지 질문의 성격 유형 점수를 합치면 아래 표와 같습니다.

| 지표 번호 | 성격 유형 | 점수 | 성격 유형 | 점수 |
| --- | --- | --- | --- | --- |
| 1번 지표 | 라이언형(R) | 0 | 튜브형(T) | 3 |
| 2번 지표 | 콘형(C) | 1 | 프로도형(F) | 0 |
| 3번 지표 | 제이지형(J) | 0 | 무지형(M) | 2 |
| 4번 지표 | 어피치형(A) | 1 | 네오형(N) | 1 |

각 지표에서 더 점수가 높은 `T`,`C`,`M`이 성격 유형입니다.하지만, 4번 지표는 1점으로 동일한 점수입니다. 따라서, 4번 지표의 성격 유형은 사전순으로 빠른 `A`입니다.

따라서 `"TCMA"`를 return 해야 합니다.

**입출력 예 #2**

1번부터 3번까지 질문의 성격 유형 점수를 합치면 아래 표와 같습니다.

| 지표 번호 | 성격 유형 | 점수 | 성격 유형 | 점수 |
| --- | --- | --- | --- | --- |
| 1번 지표 | 라이언형(R) | 6 | 튜브형(T) | 1 |
| 2번 지표 | 콘형(C) | 0 | 프로도형(F) | 0 |
| 3번 지표 | 제이지형(J) | 0 | 무지형(M) | 0 |
| 4번 지표 | 어피치형(A) | 0 | 네오형(N) | 0 |

1번 지표는 튜브형(T)보다 라이언형(R)의 점수가 더 높습니다. 따라서 첫 번째 지표의 성격 유형은 `R`입니다.하지만, 2, 3, 4번 지표는 모두 0점으로 동일한 점수입니다. 따라서 2, 3, 4번 지표의 성격 유형은 사전순으로 빠른 `C`, `J`, `A`입니다.

따라서 `"RCJA"`를 return 해야 합니다.

<br>

## 풀이 1

```python
def solution(survey, choices):
    answer = ''
    score = [[0,0], # R, T
             [0,0], # C, F
             [0,0], # J, M
             [0,0]] # A, N
    
    for i, string in enumerate(survey):
        if string == "RT":
            if choices[i] == 1:
                score[0][0] += 3
            elif choices[i] == 2:
                score[0][0] += 2
            elif choices[i] == 3:
                score[0][0] += 1
            elif choices[i] == 5:
                score[0][1] += 1
            elif choices[i] == 6:
                score[0][1] += 2
            elif choices[i] == 7:
                score[0][1] += 3
            else:
                continue
        elif string == "TR":
            if choices[i] == 1:
                score[0][1] += 3
            elif choices[i] == 2:
                score[0][1] += 2
            elif choices[i] == 3:
                score[0][1] += 1
            elif choices[i] == 5:
                score[0][0] += 1
            elif choices[i] == 6:
                score[0][0] += 2
            elif choices[i] == 7:
                score[0][0] += 3
            else:
                continue
        elif string == "CF":
            if choices[i] == 1:
                score[1][0] += 3
            elif choices[i] == 2:
                score[1][0] += 2
            elif choices[i] == 3:
                score[1][0] += 1
            elif choices[i] == 5:
                score[1][1] += 1
            elif choices[i] == 6:
                score[1][1] += 2
            elif choices[i] == 7:
                score[1][1] += 3
            else:
                continue
        elif string == "FC":
            if choices[i] == 1:
                score[1][1] += 3
            elif choices[i] == 2:
                score[1][1] += 2
            elif choices[i] == 3:
                score[1][1] += 1
            elif choices[i] == 5:
                score[1][0] += 1
            elif choices[i] == 6:
                score[1][0] += 2
            elif choices[i] == 7:
                score[1][0] += 3
            else:
                continue
        elif string == "JM":
            if choices[i] == 1:
                score[2][0] += 3
            elif choices[i] == 2:
                score[2][0] += 2
            elif choices[i] == 3:
                score[2][0] += 1
            elif choices[i] == 5:
                score[2][1] += 1
            elif choices[i] == 6:
                score[2][1] += 2
            elif choices[i] == 7:
                score[2][1] += 3
            else:
                continue
        elif string == "MJ":
            if choices[i] == 1:
                score[2][1] += 3
            elif choices[i] == 2:
                score[2][1] += 2
            elif choices[i] == 3:
                score[2][1] += 1
            elif choices[i] == 5:
                score[2][0] += 1
            elif choices[i] == 6:
                score[2][0] += 2
            elif choices[i] == 7:
                score[2][0] += 3
            else:
                continue
        elif string == "AN":
            if choices[i] == 1:
                score[3][0] += 3
            elif choices[i] == 2:
                score[3][0] += 2
            elif choices[i] == 3:
                score[3][0] += 1
            elif choices[i] == 5:
                score[3][1] += 1
            elif choices[i] == 6:
                score[3][1] += 2
            elif choices[i] == 7:
                score[3][1] += 3
            else:
                continue
        elif string == "NA":
            if choices[i] == 1:
                score[3][1] += 3
            elif choices[i] == 2:
                score[3][1] += 2
            elif choices[i] == 3:
                score[3][1] += 1
            elif choices[i] == 5:
                score[3][0] += 1
            elif choices[i] == 6:
                score[3][0] += 2
            elif choices[i] == 7:
                score[3][0] += 3
            else:
                continue
    if score[0][0] >= score[0][1]:
        answer = answer + 'R'
    else:
        answer = answer + 'T'
    if score[1][0] >= score[1][1]:
        answer = answer + 'C'
    else:
        answer = answer + 'F'
    if score[2][0] >= score[2][1]:
        answer = answer + 'J'
    else:
        answer = answer + 'M'
    if score[3][0] >= score[3][1]:
        answer = answer + 'A'
    else:
        answer = answer + 'N'
    return answer
```

## 풀이 2

```python
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
```

## 풀이 3

```python
def solution(설문_조사_배열, 선택지_배열):
    지표 = {}
    지표['RT'] = 지표['TR'] = {'R': 0, 'T': 0,}
    지표['FC'] = 지표['CF'] = {'C': 0, 'F': 0,}
    지표['MJ'] = 지표['JM'] = {'J': 0, 'M': 0,}
    지표['AN'] = 지표['NA'] = {'A': 0, 'N': 0,}
    점수 = {
        '매우 비동의': 3,
        '비동의': 2,
        '약간 비동의': 1,
        '모르겠음': 0,
        '약간 동의': 1,
        '동의': 2,
        '매우 동의': 3,
    }
    비동의 = [1, 2, 3]
    동의 = [5, 6, 7]
    선택지 = {
        1: '매우 비동의',
        2: '비동의',
        3: '약간 비동의',
        4: '모르겠음',
        5: '약간 동의',
        6: '동의',
        7: '매우 동의',
    }
    answer = ''

    for 인덱스 in range(len(설문_조사_배열)):
        비동의_캐릭터, 동의_캐릭터 = 설문_조사_배열[인덱스]

        if 선택지_배열[인덱스] in 비동의:
            지표[설문_조사_배열[인덱스]][비동의_캐릭터] += 점수[선택지[선택지_배열[인덱스]]]
            continue

        if 선택지_배열[인덱스] in 동의:
            지표[설문_조사_배열[인덱스]][동의_캐릭터] += 점수[선택지[선택지_배열[인덱스]]]

    결과_배열 = [지표['RT'].items(), 지표['FC'].items(), 지표['MJ'].items(), 지표['AN'].items()]
    정렬된_배열 = []

    for 결과 in 결과_배열:
        정렬된_배열.append(sorted(결과, key=lambda x: -x[1]))

    return ''.join([캐릭터_점수_튜플[0] for [캐릭터_점수_튜플, _] in 정렬된_배열])
```

출처 : [Programmers](https://school.programmers.co.kr/learn/courses/30/lessons/118666)