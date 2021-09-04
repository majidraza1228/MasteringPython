# You are given two integer arrays, nums1 and nums2, and asked to sort them in a particular order. The elements in nums2 are distinct and all occur within nums1. Sort the elements of nums1such that the relative ordering of values are the same as nums2. All elements that don’t appear in nums2 should appear at the end of nums1 in ascending order. 
# Note: It is guaranteed that no value within nums1 and nums2 exceeds one thousand. 

# Ex: Given the following nums1 and nums2…

# nums1 = [3, 2, 5, 8, 2, 7], nums2 = [7, 8, 3], return [7, 8, 3, 2, 2, 5] (7, 8, and 3 appear first because of their ordering in nums2 followed by 2 and 5 sorted in ascending order since they don't exist in nums2).

class Solution(object):
    def order(self, nums1, nums2):
        dic = {}
        for i in nums2:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = []
        for i in nums1:
            if i in dic:
                res.append(i)
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
        for i in dic:
            res.append(i)
        return res

abc=Solution()
nums1 = [3, 2, 5, 8, 2, 7]
nums2 = [7, 8, 3]
print(abc.order(nums1, nums2))