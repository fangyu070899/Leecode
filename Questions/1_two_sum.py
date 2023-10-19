class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        r=[-1]*2
        if len(nums)==2:
            r[0]=0
            r[1]=1
        else :
            count=0
            for i in range(len(nums)):
                if target-nums[i] in nums:
                    r[0]=i
                    for j in range(i+1,len(nums)):
                        if nums[j]==target-nums[i]:
                            r[1]=j
                            break
                    if r[1]==-1:continue
                    else: break

        return r
