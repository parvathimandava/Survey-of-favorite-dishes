'''
Given a number N, calculate the prime numbers upto N using Sieve of Eratosthenes.

Input:
The first line of the input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing N.

Output:
For all testcases, in a new line, print all the prime numbers upto or equal to N.

Constraints:
1 <= T<= 100
1 <= N <= 104

Example:
Input:
2
10
35
Output:
2 3 5 7
2 3 5 7 11 13 17 19 23 29 31
'''

'''
Sieve Algorithm:

Sieve of Eratosthenes is used to get all prime number in a given range and is a very efficient algorithm. You can check more about sieve of Eratosthenes on Wikipedia. It follows the following steps to get all the prime numbers from up to n:

Make a list of all numbers from 2 to n.
 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ……., n]
Starting from 2, delete all of its multiples in the list, except itself.
 [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,……., n]
Repeat the step 2 till square root of n.
For 3 –  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
For 5 – [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20……., n]
Till sqrt(n)
The remaining list only contains prime numbers.
'''

#code with more execution time
import math
T=int(input())
for _ in range(T):
    n=int(input())
    sqroot=int(math.sqrt(n))
    l=[]
    notprime=[]
    for i in range(2,n+1):
        l.append(i)
    for i in range(len(l)):
        for j in range(2,sqroot+1):
            if(l[i]%j==0):
                notprime.append(l[i])

    list3=[item for item in l if item not in notprime]
    list3.append((2))
    list3.append((sqroot))
    list3= sorted(list3)
    print(' '.join([str(elem) for elem in list3]))

#code with less execution time
t = int(input())
for test in range(t):
    n = int(input())
    n += 1
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

    numbers = [str(i) for i, p in enumerate(is_prime[2:], 2) if p]
    print(' '.join(numbers))







