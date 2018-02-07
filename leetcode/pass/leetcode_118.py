'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

给定层数，返回对应层数的杨辉三角形
'''

def grtpascal(t):
    b =[1]
    a =(sum(i) for i in zip([0]+b,b+[0]))

    n = 0
    for i in a:
        print(i)
        n +=1
        if n ==t:
            break

grtpascal(10)











# def triangles():
#     a=[1]
#     while True:
#         yield a
#         a=[sum(i) for i in zip([0]+a,a+[0])]
#
# n=0
# for t in triangles():
#     print(t)
#     n=n+1
#     if n == 10:
#         break
#
#
# print([sum(i) for i in zip((1,2),(2,4))])
# # print(sum(zip((1,2),(2,4))))
