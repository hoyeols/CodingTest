##### 학습에 참고한 사이트와 간단한 내용 
* https://www.fun-coding.org/Chapter19-greedy-live.html : 탐욕 알고리즘의 이해
* https://itholic.github.io/python-reverse-reversed/ : [python] reverse, reversed 차이
* https://dailyheumsi.tistory.com/67 : 파이썬 정렬, 다중조건으로 한번에 하기
* https://adrian0220.tistory.com/57#:~:text=Greedy%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98%20%EC%B5%9C%EB%8C%80%20%EC%9E%A5%EC%A0%90,%EC%9D%84%20%ED%95%98%EB%A9%B4%20%EB%90%A0%20%EA%B2%83%EC%9E%85%EB%8B%88%EB%8B%A4. : 탐욕 알고리즘(Greedy Algorithm)
* https://doorbw.tistory.com/75: 그리디 알고리즘

## 오늘 발견한 문제 
1. Greedy Algorithm이란 무엇이며 동적계획법과의 차이는
2. 이중리스트에서 a[i][1] 기준으로 정렬하기

## 해결 방안 
1.  Greedy Algorithm(탐욕 알고리즘)이란 최적의 해에 가까운 값을 구하기 위해 사용되는 방법으로 여러 경우 중 하나를 결정할때마다 최적이라고 생각되는 경우를 선택하는 방식을 말합니다. 최적화 문제의 대표적 알고리즘으로 미래를 예측하지 않고 매순간 최선의 선택을 합니다. 동적계획법은 데이터를 저장하고 문제를 풀어가며 지속적으로 데이터를 참조하므로 많은 동작이 발생됩니다.
-장점 : 빠르다, 매번 최선의 선택을 해나가기에 최소한의 노력을 하면 된다
-단점 : 항상 최적화가 되지 않는다. 미래에 대한 고려를 하지 않고 진행하므로 최적이 아닐 가능성이 존재한다.
-활용 : 다익스트라 알고리즘, 동전문제, 배낭문제
```
간단 슈도코드 예시
Greedy
N = s.length
A = {a_1}
K = 1
For m = 2 to n
	if s[m] >= f[K]
		A = A U {a_m}
		K = m
	return A 
```
시간복잡도 : O(n)
2. 회의시간 문제에서 회의 끝나는시간으로 정렬을 우선해야하는데 그러기 위해서는 이중리스트의 두번째값들을 기준으로 정렬을 해야했습니다. 그래서 sorted함수의 key인자를 이용해서 두번째 인자에 해당하는 값을 반환하게끔 lambda를 이용하여 해결했습니다.
```
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
```

#### 학습 내용에 대한 개인적인 총평 
- 파이썬에서 reverse와 reversed가 있어 두개의 차이점이 궁금했는데 며칠전에 학습하였던 sort와 sorted 함수의 차이점과 비슷해보였습니다. reverse는 sort처럼 리스트뒤에 .을붙여 사용하고 해당 리스트 자체를 변환해주며 reversed는 ()에 뒤집어줄 리스트나 객체를 넣어주고 값이 반환되는 sorted와 비슷한 타입이였습니다.

#### 다음 학습 계획 
1. Python으로 백준 단계별로 풀어보기
*      정수론 및 조합론
