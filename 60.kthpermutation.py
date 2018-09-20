class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def numsection():
            t = 1
            yield t
            for i in range(1,n):
                t*=i
                yield t
                
        numsec = list(numsection())[::-1]
        def func(k):
            for i in numsec:
                if k>=i:
                    this = k/i
                else:
                    this =0
                k-=i*this
                yield this
        print list(numsec)
        print list(func(k-1))
        res=""
        a = range(n)
        for i in func(k-1):
            res+=str(a[i]+1)
            del a[i]
        return res