class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        class t:
            able={}
            start=1
        
        def func(left,right,start):
            for i in range(left,right):
                t.able[(left,i)]=t.start
                t.start+=1
            for i in range(left,right):
                t.able[(i,right)]=t.start
                t.start+=1
            for i in range(left,right):
                t.able[(right,n-1-i)]=t.start
                t.start+=1
            for i in range(left,right):
                t.able[(n-1-i,left)]=t.start
                t.start+=1
            if left==right:
                t.able[(left,right)]=t.start
        for i in range(0,(n+1)/2):
            func(i,n-1-i,t.start)
        
        print t.able
        r=[]
        for i in range(n):
            res=[]
            for j in range(n):
                res.append(t.able[(i,j)])
            r.append(res)
        return r