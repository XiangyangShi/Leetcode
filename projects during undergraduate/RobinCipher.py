import math
import random
import math

def st_module(a,b):
    flag=0
    if(a<b):
        key=a
        a=b
        b=key
        flag=1
    r2=a
    s1=1
    t1=0
    r1=b
    s=0
    t=1
    q=a/b
    r=a-b*q
    while(r!=0):
        s2=s1
        t2=t1
        r2=r1
        s1=s
        t1=t
        r1=r
        s=s2-q*s1
        t=t2-q*t1
        q=r2/r1
        r=r2-q*r1
    if(flag==0):
        return s,t
    else:
        return t,s
##  st(p,q)  ->  sp*tq=1
##  return (s,t)
    
def shengyu(b1,b2,p,q):
    a=st_module(p,q)
    s=a[0]%q
    t=a[1]%p
    n=p*q
    r1=(s*p*b2+t*q*b1)%n
    r2=(s*p*b2-t*q*b1)%n
    r3=(-s*p*b2+t*q*b1)%n
    r4=(-s*p*b2-t*q*b1)%n
    res=(r1,r2,r3,r4)
    return res
##  shengyu(b1,b2,p,q)  x=b1%p;x=b2%q
##  return(x1,x2,x3,x4)

def wordtonum():
    b=[]
    c=[]
    a='communicationskillmathematicalfundationofinformationsecurity2012010015130369064000001'
    length=len(a)
    residue=6-length%6
    a=a+residue*'0'
    block=len(a)/6
    for i in range(block):
        b.append(a[i*6:i*6+6])
    print b
    for j in b:
        res=0
        for k in j:
            res=res*36
            if('a'<=k and k<='z'):
                res=res+ord(k)-ord('a')+11
            if('0'<=k and k<='9'):
                res=res+ord(k)-ord('0')
        res=res*36+1
        res=res*36+1
        res=res*36+1
        c.append(res)
    print "the word is",c
    return c
##return (1234434545,423432432234,24343232432,4243324234)

def modsquare(a,b,c):
    aa=1
    bb=a
    while(b!=0):
        if(b%2==1):
            aa=aa*bb%c;
        bb=bb*bb%c
        b=b/2
    return aa
##a^b mod c=aa
##return aa

def test(p):
    for i in range(8):
        b=random.randint(2,200)
        a=modsquare(b,p-1,p)
        if(a!=1):
            return 0
    return 1
##test p
##return 1 0

def pq():
    flag=0
    while(flag!=1):
        res=random.randrange(268435457,536870911,2)
        if(test(res)==1 and res%4==3):
            flag=1
    ##print res
    return res
##create 2^28< p <2^29
##return p

def sqrtmod(c,p):
    res=modsquare(c,(p+1)/4,p)
    res=res%p
    return res
##calculate the square root, x^2=c mod p
##return abs x

def show(s):
    for i in s:
        res=''
        x1=i%36
        i=i/36
        x2=i%36
        i=i/36
        x3=i%36
        i=i/36
        if(x1==1 and x2==1 and x3==1):
            for j in range(6):
                char=i%36
                if(char<=10):
                    res=''+chr(char+ord('0'))+res
                else:
                    res=''+chr(char+ord('a')-11)+res
                i=i/36
            return res

def main():
    p=pq();
    q=pq();
    n=p*q
    print 'p:',p
    print 'q:',q
    print 'n:',n
    m=wordtonum()
    c=[]
    for i in m:
        c.append(i*i%n)
    print 'the code is:',c
    d=''
    for j in c:
        b1=sqrtmod(j,p)
        b2=sqrtmod(j,q)
        s=shengyu(b1,b2,p,q)
        ##print s
        d=d+show(s)
        #print j
        #print b1,b2,p,q
    while(d[-1]=='0'):
        d=d[0:-1]
    print 'after decode:',d
    
main()














