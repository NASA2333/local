'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' '
when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more
spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''
def fulljustify(words,l):
	lens = [len(i) for i in words]
	len_sum =sum(lens)
	row = int(len_sum/l)+1			#行数
	list1 =[]
	sums = 0
	r = 0
	while r<row:
		for i in range(len(lens)):
			sums +=(lens[i]+1)
			# sums +=1
			if sums >16:
				list1.append(words[:i])
				sums =0
				lens =lens[i:]
				words =words[i:]
				break
		r+=1
		if r ==row:
			list1.append(words)
	c =[len("".join(i)) for i in list1]
	print(c)
	# print(len(list1[2]))
	list2 = []
	for i in range(len(c)):
		if len(list1[i]) ==1:
			z3 =l-c[i]
			print(z3)
			z2 =" "*(l-c[i])
			print(list1[i])
			z = list1[i][0].append(" "*(l-c[i]))
			list2.append(z)
			print(z2)
			# list2.append(str(list1[i].append((l-len(list1[i]))*' ')))
		else:
			a =(l-c[i])/(len(list1[i])-1)
			# print(a)
			list2.append(str(list1[i]).replace(","," "*int(a)))

	print(list2)
	# print(sum([len(j) for i in list1 for j in i]))
	# print(len(list1[0]))
	# print(list1)

fulljustify(["This", "is", "an", "example", "of", "text", "justification."],16)

# a = ["This", "is", "an", "example", "of", "text", "justification."]
# c =[len(i) for i in a]
# print(c)
# print(sum(c))
# print(round(2.5))


# print(str(['1','2']).replace(',',' '*1.5))