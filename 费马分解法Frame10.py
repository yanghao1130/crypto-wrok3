# 费马分解法 求解Frame10
from gmpy2 import *
from Crypto.Util.number import *
import binascii
import math

def fermat():
    n = int(ns[10], 16)
    c = int(cs[10], 16)
    e = int(es[10], 16)
    B=math.factorial(2**14)
    u=0;v=0;i=0
    u0=iroot(n,2)[0]+1
    while(i<=(B-1)):
        u=(u0+i)*(u0+i)-n
        if is_square(u):
            v=isqrt(u)
            break
        i=i+1  
    p=u0+i+v
    q=n//p
    phi=(p-1)*(q-1)
    d=invert(e, phi)
    m = powmod(c, d, n)
    plain = binascii.a2b_hex(hex(m)[2:])
    print(plain)
    return plain


if __name__ == "__main__":
    ns=[]
    es=[]
    cs=[]
    for i in range(21):
        with open("RSA加密体制破译题目\密码挑战赛赛题三\附件3-2（发布截获数据）/Frame"+str(i), "r") as f:
            tmp = f.read()
            ns.append(tmp[0:256])
            es.append(tmp[256:512])
            cs.append(tmp[512:768])
        
    fermat()
