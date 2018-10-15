class Solution:
    # 我的答案
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res

    # 优秀的答案
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = []
        for i in nums2:
            if i in dic:
                # 在a[0]处对数组2重复元素进行计数
                dic[i][0] += 1
            else:
                # 创建一个数据统计数组a[]
                dic[i] = [1, 0]
        for i in nums1:
            if i in dic:
                # 在a[1]处对数组1重复元素进行计数
                dic[i][1] += 1
        for i in dic:
            if dic[i][1] != 0:
                a = min(dic[i])
                for j in range(a):
                    ans.append(i)
        return ans

    # 排序后筛选
    def intersect3(self, nums1, nums2):
        """
        :type test1: List[int]
        :type test2: List[int]
        :rtype: List[int]
        """
        result = []
        test1 = nums1
        test2 = nums2
        test1.sort()
        test2.sort()
        i = 0
        j = 0
        while i < len(test1) and j < len(test2):
            if test1[i] == test2[j]:
                result.append(test1[i])
                i += 1
                j += 1
            elif test1[i] < test2[j]:
                i += 1
            elif test1[i] > test2[j]:
                j += 1
        return result
