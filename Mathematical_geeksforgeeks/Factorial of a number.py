'''
Given a positive integer N. The task is to calculate the factorial of N.

Input:
The first line contains an integer 'T' denoting the total number of test cases. T testcases follow. In each test cases, it contains an integer 'N'.

Output:
For each testcase in a new line, print the factorial of N.

Constraints:
1 <= T <= 19
0 <= N <= 18

Example:
Input:
2
1
4

Output:
1
24

Explanation:
Testcase 2: Factorial of 4 is 4 * 3 * 2 * 1 = 24.
'''
#program using loops
'''
T=int(input())

for _ in range(T):
    n = int(input())
    result=1
    for i in range(n,0,-1):

        result=result*i
    print(result)
'''
# program using inbuilt function
'''
import math
T=int(input())
for _ in range(T):
    n=int(input())
    result=math.factorial(n)
    print(result)
'''
#Program using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input())
result=fact(n)
print(result)