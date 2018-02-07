'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

def trap(height):
	sum = 0

	for i in range(1,len(height)-1):
		# print(i+1)
		# print(height)
		if height[i] >height[i+1] and height[i] >height[i-1]:
			pass
		else:
			x  =height[:i][::-1]
			b = max(x)
			j = max(height[i+1:])
			sum +=min(b,j)-height[i]
			# print(x)
			# for z in x:
			# 	# x =height[:i+1]
			# 	# a = max(height[:i+1])
			# 	if z >height[i]:
			# 		b =z
			# 		break

			# for j in height[i+1:]:
			# 	if j >height[i]:
					# c = height[i:].index(j)+i	#最近大于最小的index

					# break


	print(sum)

trap([0, 1, 0, 3, 0, 0, 1, 3, 2, 1, 2, 1])

'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)
        maxh = [0 for __ in range(length)]
        h = height[length - 1]
        for i in range(length - 2, -1, -1):
            maxh[i] = h
            h = max(h, height[i])

        h = height[0]
        result = 0
        for i in range(1, length - 1):
            h = max(h, height[i])
            result += max(0, min(h, maxh[i]) - height[i])
        print(result)

Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
'''
# if __name__ == "__main__":
#     assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6