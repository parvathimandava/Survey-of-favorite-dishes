'''
Given two numbers A and B. The task is to find the GCD of those 2 numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two space separated integers A and B.

Output:
For each testcase, in a new line, print the GCD of the two numbers.

Constraints:
1 <= T <= 100
1 <= A, B <= 103

Example:
Input:
98 56
48 18

Output:
14
6
'''
'''
a,b=map(int,input().split())
i=1
while (i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i+=1

print(gcd)
'''
def computeGCD(a,b):
    if b==0:
        return a
    else:
        return computeGCD(b,a%b)

T=int(input())

for i in range(T):
    a,b=input().split()
    gcd=computeGCD(int(a),int(b))
print(gcd)