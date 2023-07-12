class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        originalsFound = {}
        for number in nums:
            if number in originalsFound:
                return True
            else:
                originalsFound[number]=True
        return False