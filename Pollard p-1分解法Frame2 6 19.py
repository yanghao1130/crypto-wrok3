# Pollard p-1分解法 求解Frame2 6 19
from gmpy2 import *
from Crypto.Util.number import *
import binascii

def Pollard(n,e,c):
    B=2**20
    a=2
    for k in range(2,B+1):
        a=powmod(a,k,n)
        d=GCD(a-1,n)
        if d==1 or d==n:
            continue
        else:
            q=n//d
            n=d*q
            break
    p=n//q
    phi=(p-1)*(q-1)
    d=invert(e,phi)
    m=powmod(c,d,n)
    plain=binascii.a2b_hex(hex(m)[2:])
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
        
    Pollard(int(ns[2],16),int(es[2],16),int(cs[2],16))
    Pollard(int(ns[6],16),int(es[6],16),int(cs[6],16))
    Pollard(int(ns[19],16),int(es[19],16),int(cs[19],16))
