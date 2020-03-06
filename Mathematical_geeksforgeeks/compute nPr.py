'''
Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

Input:
The first line of the input contains T denoting the number of testcases. T testcases follow. First line of the test case will be the value of n and r respectively.

Output:
For each test case, in a new line, output will be the value of nPr.

Constraints:
1 <= T <= 100
1 <= n,r <= 20
n >= r

Example:
Input:
2
2 1
10 4
Output:
2
5040
'''
T= int(input())
for _ in range(T):
    n,r=map(int,input().split())
    result=1
    result1=1
    for i in range(n,0,-1):
        result=result*i
    for i in range((n-r),0,-1):
        result1=result1*i
    fact=result//result1
    print(fact)