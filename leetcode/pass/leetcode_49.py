'''
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''
'''
def groupAnagrams(strs):
	dicts ={}
	charlist = [''.join(sorted(x)) for x in strs]
	for i in range(len(charlist)):
		for j in charlist[i:]:
			if charlist[i] ==j:
				if charlist[i] in dicts:
					dicts[charlist[i]] =str(i)+dicts[charlist[i]]
				else:
					dicts[charlist[i]] =str(i)
	print(dicts)

	print(charlist)

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
'''
def groupAnagrams(strs):
	dicts = {}
	for s in strs:
		strs1 = ''.join(sorted(s))
		if strs1 not in dicts:
			dicts[strs1] =[s]
		else:
			dicts[strs1].append(s)
	result =[]
	for i in dicts.values():
		result.append(i)
	return result



print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for i, v in enumerate(strs):
            target = "".join(sorted(v))
            if target not in map:
                map[target]=[v]
            else:
                map[target].append(v)

        result = []
        for value in map.values():
            result += [sorted(value)]
        return result

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
'''