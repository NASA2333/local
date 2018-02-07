from bs4 import BeautifulSoup
import  requests,re

html_doc = """
<b><!--Hey, buddy. Want to buy a used parser?--></b>"
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title"><b>The Dormouse's story</b></p>
		<p class="story">Once upon a time there were three little sisters; and their names were
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
			<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.</p>

		<p class="story">...</p>
"""

# soup = BeautifulSoup(html_doc,"html.parser")
# print(soup.b.string)
# # print(soup.prettify())
# print(soup.prettify())
# print(soup.title.string)
# # soup.find_all()
# print(soup.attrs)
# a = requests.get(url='https://www.qiushibaike.com/text/')
# b = a.text
# soup = BeautifulSoup(b,"html.parser")
# print(soup.prettify())
# print(re.findall(r"(?<=span>\s*).*?(?=\s+)",b))
# d =soup.find_all(class_="content")
# for i in d:
# 	x = i.contents[1].text
# 	print(x)


# d = soup.find_all(class_='number')
# print(d)

# z = re.findall(r'(?<=number">).*(?=</i>)',b)
# print(len(z))													#点赞、留言
# print(type(d))
# zz = BeautifulSoup(d[0],"html.parser")
# print(zz.i)
# for j in d:
# 	# if soup.j['class'] =='number':
# 	# 	print(j.text)
# 	zz = BeautifulSoup(j,"html.parser")
# 	if zz.j['class']=='number':
# 		print(zz.j.text)