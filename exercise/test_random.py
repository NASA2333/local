import random

##生成0-1之间随机浮点数
a = random.random()
print(a)

#生成指定数字范围内随机浮点数

b = random.uniform(5,6)
print(b)

#生成范围整数
c = random.randint(1,5)
print(c)

#从序列随机选取一个元素(字符串、列表、元组）
d = random.choice('abcdef')
print(d)

e = random.choice([1,2,3,4,5,6,7])
print(e)

f = random.choice(('a','b','c','d'))
print(f)

#将序列打乱(list)
g =[1,2,3,4,5,6,7]
random.shuffle(g)
print(g)

# h = 'abcdefgh'
# random.shuffle(h)
# print(h)

# i = (1,2,3,4,5,6,7,8)
# random.shuffle(i)
# print(i)

#指定序列中取一定长度
i= random.sample((1,2,3,4,5,6,7,8),2)
print(i)

j = random.sample('abcdefg',4)
print(j)

k = random.sample([1,2,3,4,5,6,7,8,9],3)
print(k)

# l = random.sample({'a':1,'b':2,'c':3,'d':4,'e':5,'f':6},2)
# print(l)
