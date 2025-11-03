# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력
x = 50
y = 100
text = 208285344
n = 'Lee'

ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

ex2 = 'n = {}, s = {}, sum = {}'.format(n,text,x+y)
print(ex2)

ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)

ex4 = f'n = {n:@@^7}, s = {text}, sum = {x+y}'
print(ex4)

m = 100000000

print(f'm : {m:,}')