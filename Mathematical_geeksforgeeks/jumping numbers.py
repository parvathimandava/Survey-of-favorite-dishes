'''
Given a positive number X. Find all Jumping Numbers smaller than or equal to X.
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input:
The first line of the input contains T denoting the number of testcases. Each testcase contain a positive number X.

Output:
Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.

Constraints:
1 <= T <= 100
1 <= N <= 109

Example:
Input:
2
10
50
Output:
0 1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45

Explanation:
Testcase 2: Here, the most significant digits of each jumping number is following increasing order, i.e., jumping numbers starting from 0, followed by 1, then 2 and so on, themselves being in increasing order 2, 21, 23.
'''
# Class queue for use later
class Queue:
	def __init__(self):
		self.lst = []

	def is_empty(self):
		return self.lst == []

	def enqueue(self, elem):
		self.lst.append(elem)

	def dequeue(self):
		return self.lst.pop(0)

# Prints all jumping numbers smaller than or equal to
# x starting with 'num'. It mainly does BFS starting
# from 'num'.
def bfs(x, num):

	# Create a queue and enqueue i to it
	q = Queue()
	q.enqueue(num)

	# Do BFS starting from 1
	while (not q.is_empty()):
		num = q.dequeue()

		if num<= x:
			print(str(num), end =' ')
			last_dig = num % 10

			# If last digit is 0, append next digit only
			if last_dig == 0:
				q.enqueue((num * 10) + (last_dig + 1))

			# If last digit is 9, append previous digit
			# only
			elif last_dig == 9:
				q.enqueue((num * 10) + (last_dig - 1))

			# If last digit is neighter 0 nor 9, append
			# both previous digit and next digit
			else:
				q.enqueue((num * 10) + (last_dig - 1))
				q.enqueue((num * 10) + (last_dig + 1))

# Prints all jumping numbers smaller than or equal to
# a positive number x
def printJumping(x):
	print (str(0), end =' ')
	for i in range(1, 10):
		bfs(x, i)

# Driver Program ( Change value of x as desired )
x = int(input())
printJumping(x)

# This code is contributed by Saket Modi
