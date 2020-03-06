def rev(n):
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev


for _ in range(int(input())):
    n = int(input())
    print(rev(n))



