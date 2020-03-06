'''
Given two numbers A and B. The task is to find out their LCM and GCD.

Input:
The first line of input contains an integer T denoting the number of testcases. T testcases follow. In each test cases, there are two numbers A and B separated by space.

Output:
For each testcase in a new line, print LCM and GCD separated by space.

Constraints:
1 <= T <= 104
1 <= A <= 108
1 <= B <= 108

Example:
Input:
2
5 10
14 8

Output:
10 5
56 2

Explanation:
Testcase 1: LCM and GCD of given numbers 5 and 10 are: 10 and 5.
'''
import math
T=int(input())
for _ in range(T):
    a, b = map(int,input().split())
    i = 1
    while (i <= a and i <= b):
        if (a % i == 0 and b % i == 0):
            gcd = i
        i += 1
    #GCD = int(math.gcd(a, b))
    LCM = int((a * b) / gcd)

    print(LCM,gcd)
