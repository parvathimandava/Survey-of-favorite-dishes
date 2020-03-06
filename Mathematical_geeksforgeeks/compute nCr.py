'''
Find nCr for given n and r.

Input:
First line contains number of test cases T. T testcases follow. Each testcase contains 1 line of input containing 2 integers n and r separated by a space.

Output:
For each testcase, in a new line, find the nCr. Modulus your output to 109+7.

Constraints:
1 <= T <= 50
1 <= n <= 103
1 <= r <= 800

Example:
Input:
2
3 2
4 2
Output:
3
6
'''
'''
# program as per formula
import math
T=int(input())
for _ in range(T):
    n,r=map(int,input().split())
    result=math.factorial(n)//(math.factorial(r)*math.factorial(abs(n-r)))
    print(result)
'''
# program as per geeks for geeks logic
dp=[1]*1001
for i in range(1,1001):
    dp[i]=i*dp[i-1]
for _ in range(int(input())):
    n,r=map(int,input().split())
    print((dp[n]//(dp[r]*dp[n-r]))%1000000007)