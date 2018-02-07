

#无限迭代器
		#count()  接收两个参数，第一个参数指定开始值，默认为 0，第二个参数指定步长，默认为 1：
'''
import itertools
nums = itertools.count()
for i in nums:
	if i >6:
		break
	print(i)

nums1 = itertools.count(6,2)
for i in nums1:
	if i >14:
		break
	print(i)
'''
		#cycle()  用于对iterable 中的元素反复执行循环
'''
import itertools
cycle_strings = itertools.cycle("ABC")
i = 1
for string in cycle_strings:
	if i ==10:
		break
	print(i,string)
	i +=1
'''

	#repeat()  用于反复生成一个object
'''
import itertools
for item in itertools.repeat("Hello word",3):
	print(item)
'''


####有限迭代器
		#chain()    接受多个可迭代对象作为参数，将它们连接起来，作为一个新的迭代器返回
'''
from itertools import  chain
string = chain.from_iterable('ABCDEF')			#传入参数，产生迭代器		https://codeday.me/bug/20170919/75581.html
a = chain('123')					#需要本身可以迭代
# print(next(string))
print(string)

for item in chain([1,2,3],['a','b','c']):
	print(item)
'''
			#compress(data,selectors)    用于删选，当selectors 的某个元素为True时，则保留data对应位置的元素，否则去除
'''
from itertools import  compress

lsit_1 = list(compress('abcedf',[1,1,0,1,0,1,1]))
lsit_2 = list(compress('abcdef',[1,1,0,1]))
lsit_3 = list(compress('abcdef','1232'))							#元组，字符都行，可迭代对象（循环）

print(lsit_1)
print(lsit_2)
print(lsit_3)
'''

		#dropwhile（predficate,iterable)   predicate 是函数，iterable 是可迭代对象。
											# 对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项。
						#备注（符合条件的删除，当出现第一个不符合条件时，保留下来，并直接保留未执行的部分（和filter有区别）
'''
from itertools import  dropwhile
print(list(dropwhile(lambda x:x <5,[1,3,6,2,1])))
print(list(dropwhile(lambda  x:x>3,[2,1,6,5,4])))
print(list(dropwhile(lambda x:x <5,(1,3,6,2,1))))
print(list(dropwhile(lambda x:int(x) <5,'13621')))
###内置函数
print(list(filter(lambda  x:x<5 ,[1,3,6,2,1])))
print (list(map(lambda x:x+1,[1,2,3]))) #all
print (list(filter(lambda x: x==1,[1,23,4]))) #True序列
'''

		#gropby(iterable[, keyfunc])
'''
		其中，iterable 是一个可迭代对象，keyfunc 是分组函数，用于对 iterable 的连续项进行分组，
		如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 (key, sub-iterator) 的迭代器
'''
'''
from itertools import  groupby

for key,value in groupby('aaabbbaaccdddd'):
	print(key,':',list(value))

data = ['a','bb','ccc','dd','eee','f']
for  key,value in groupby(data,len):
	print(key,':',list(value))

data1 = ['a','bb','cc','dd','eee','f']
for  key,value in groupby(data1,len):
	print(key,':',list(value))
'''

		#ifilter(function or None ,sequence)  将 iterable 中 function(item) 为 True 的元素组成一个迭代器返回，
									# 如果 function 是 None，则返回 iterable 中所有计算为 True 的项。
'''
from itertools import ifilter
python3.x中该方法被一出了，功能和filter一致
ifilterfalse    与其相反，得出不符合条件的
 '''

		#islice(iterable,[start],stop,[step])	切片操作  iterable是可迭代对象，start 是开始索引，stop是结束索引，step是步长，start和step可选填
'''
from itertools import count,islice
print(list(islice([10,6,2,8,1,3,9],5)))
print(list(islice(count(),6)))
print(list(islice(count(),2,10)))
print(list(islice(count(),3,10,2)))
'''
	#imap  与map类似   imap(func,iter1,iter2.。。。)
'''
python 3.x中已经取消了imap，要使用同样功能可以用map（）
print(list(map(pow,[2,3,10],[4,2,3])))
'''
		########组合生成器

	#product(iter1,iter2.....[repeat =1])   用于求多个可迭代对象的笛卡尔积，与嵌套的for循环等价

'''
from itertools import product
			#每个元素中取一个值，列出所有组合可能
for i in product('abcd',[1,2]):
	print(i)

		#repeat 是一个关键字参数，用于指定重复生成序列的次数，
for i in product('abcd',repeat=2):
	print(i)
'''

		#permutations（iterable,[r])    用于生产一个排列,r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度。

from itertools import permutations,combinations_with_replacement,combinations
#将元素按照按照指定长度重新排列
print(list(permutations('abc',2)))							#包含重复的比如顺序不一致的
print(list(combinations_with_replacement('abc',2)))			#包含本身
print(list(combinations('abc',2)))							#去重
# print(list(permutations('abc')))


##combinations(iterable,r)   用于求序列的组合，其中R表示生生成组合元素的长度
