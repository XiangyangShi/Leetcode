class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def func(index):
            if index==0:
                yield (nums[0],)
            else:
                before = list( func(index-1) )
                for b in before:
                    for i in range(len(b)+1):
                        yield b[:i]+(nums[index],)+b[i:]
                    
        s = set( func( len(nums)-1 ) )
        return list(s)
                