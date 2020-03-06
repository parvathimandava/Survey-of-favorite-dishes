'''
Given a number N, the task is to find the largest prime factor of that number.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case, in a new line, print the largest prime factor of N.

Constraints:
1 <= T <= 100
2 <= N <= 1010

Example:
Input:
2
6
15
Output:
3
5
'''

def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return prime_factor


T=int(input())
for _ in range(T):
    n=int(input())
    print(Largest_Prime_Factor(n))
