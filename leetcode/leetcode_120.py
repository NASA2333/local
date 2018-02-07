'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

def minimumTotal(s):
	a = 0
	b = []
	for i in s[1:]:
		a = i.index(min(i[a],i[a+1]))
		b.append(i[a])
	return sum(b)+s[0][0]

print(minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3],
 [1,2,3,4,5],
[4,6,8,1,2,3]
]))