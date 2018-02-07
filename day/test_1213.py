import re

def get_math(path):
		sum_num = 0
		line_num =1
		txt = open(path,'r',encoding='utf-8').readlines()
		rule_list =re.findall(r"<!.*?->",str(txt))
		for i in txt:
			if i.strip() in rule_list:
				print("路径:",path)
				print("行数：",line_num,"\t","扫描内容：",'\t'*4,i)
			line_num +=1

# get_math(r'E:\new 2.xml')
a='c'
b ='e'
dic ={}
dic['a'] =(dict(a ,b))
