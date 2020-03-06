'''
Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

Input:
First line consists of T test cases. Then T test cases follow .Each test case consists of a number N.

Output:
For each testcase, in a new line, output in a single line 1 if a number is a perfect number else print 0.

Constraints:
1 <= T <= 300
1 <= N <= 1018

Example:
Input:
2
6
21
Output:
1
0
'''
T=int(input())
for _ in range(T):
    n=int(input())
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum=sum+i
    if(sum==n):
        print (1)
    else:
        print(0)

#program for less execution time:

import math

num = eval(input())
input_number = []
for i in range(num):
    input_number.append(eval(input()))

for i in input_number:
    sum1=0
    number = i
    while(number > 1):
        number = number/2
        sum1 += math.ceil(number)
        number = math.ceil(number)

    if sum1 == i:
        print(1)
    else:
        print(0)
