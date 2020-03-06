'''
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case should contain a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a prime number else print "No".

Constraints:
1 <= T <= 100
1 <= N <= 109

Example:
Input:
1
5
Output:
Yes

Explanation:
Testcase 1: 5 is the prime number as it is divisible only by 1 and 5.
'''
T=int(input())
for _ in range(T):
    n=int(input())
    count=0

    for i in range(1,n):
        if(n%i==0):
            count+=1
    if(count==1):
        print("Yes")
    else:
        print("No")