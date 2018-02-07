'''
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


path = r"/a/./b/../../c/"
print(path.split('/')[1:])


def simplifypath(path):
	for i in path.split('/')[1:]:
		pass
