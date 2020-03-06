'''
Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = N.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains integer N.

Output:
For each testcase, in a new line, print count of all 'a' and 'b' that satisfy the above equation.

Constraints:
1 <= T <= 100
a>=1, b>=0
1 <= N <= 105

Example:
Input:
2
9
28

Output:
2
2
'''
import math
T=int(input())
for i in range(T):
    n=int(input())
    a=1
    b=0
    count=0
    cbrt=math.ceil(math.pow(n,1/3))
    for a in range(1,(cbrt+1)):

        for b in range(0,(cbrt+1)):
            if((pow(a,3)+pow(b,3))==n):
                count+=1
    print(count)
