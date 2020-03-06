'''
Print all pairs (sets) of prime numbers (p,q) such that p*q <= n, where n is given number.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow.
The first line of each test case is N.

Output:
For each testcase, in a new line, print the all pairs of prime numbers in increasing order.

Constraints:
1 ≤ T ≤ 50
4 ≤ N ≤ 400

Example:
Input:
2
4
8
Output:
2 2
2 2 2 3 3 2

Explanation:
Testcase 1: Pair (2, 2) which has both prime numbers as well as satisfying the condition 2*2 <= 4.
'''
t=int(input())
for _ in range(t):
    n=int(input())
    n += 1
    l=[]
    is_prime = [True for i in range(n)]
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i * i <= n:
        if is_prime[i]:
            # Start from i*i since i*2 would be marked already
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1

    numbers = [int(i) for i, p in enumerate(is_prime[2:], 2) if p]

    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if(numbers[i]*numbers[j]<n):
                l.append(str(numbers[i]))
                l.append(str(numbers[j]))
    print(' '.join(l))

