'''
17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
'''
import itertools

def letterCombinations(choice):
	numlist = [[''],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],
			   ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
	letter =[]
	for i in range(len(str(choice))):
		letter.append(numlist[int(str(choice)[i])])
	list1 = list(itertools.product(*letter))


	print(list1)
letterCombinations(2315)
