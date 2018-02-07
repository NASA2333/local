import  requests,urllib3,re,xlrd
#
# r = requests.get(r"http://www.qiushibaike.com/hot/page/1")
# a =r.text
# print(a)
# print(re.search(r"[\u4e00-\u9fa5]+[。，：…]+",a))
# print(re.findall(r'href=".*(?=\d+)',a))


a = 'abcdeft cgdfCcdss'
re.IGNORECASE()
print(re.findall(re.IGNORECASE('c'),a))
print(re.split('c',a,1))
print()
# print(re.findall('\W+',a))
# print(re.subn('c','zz',a,flags=1))
# print(re.escape(a))
# print(re.match('c',a))
#
# a= xlrd.open_workbook(r"D:\11.xlsx").sheet_by_index(0)
#
# b = a.col_values(3)
# print(b)


