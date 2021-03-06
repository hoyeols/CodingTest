#1193.py
'''
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

예제 입력 1 
14
예제 출력 1 
2/4'''
import sys
input = sys.stdin.readline

X = int(input())

line = 0    #대각선
while (X > 0):  #몇번째 대각선까지 필요한지
    line += 1
    X -= line

denominator = line + X  #분모
molecules = line - denominator + 1  #분자는 최댓값에서 분모만큼 뺀것
if line % 2 == 0:
    denominator = -X + 1
    molecules = line - denominator + 1
print("{}/{}".format(molecules, denominator))

"""
stage	x
1		1     		1/1		  			2
2		2,3   		1/2 2/1     		3
3		4,5,6   	3/1,2/2,1/3			4
4		7,8,9,10	1/4,2/3,3/2,4/1 	5
"""

'''X = int(input())
#key_x : 첫번째 X
stage, key_X = 1, 1
#각 stage의 첫번째 X가됨.
while key_X + stage <= X:
    key_X += stage
    stage += 1
​
step = X - key_X
x, y = step + 1, stage - step
if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))'''