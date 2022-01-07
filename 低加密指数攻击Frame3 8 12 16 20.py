#低加密指数广播攻击e==5 Frame3,Frame8,Frame12,Frame16,Frame20
from gmpy2 import *
from Crypto.Util.number import *
import binascii

#中国剩余定理
def chinese_remainder_theorem(items):
    N = 1
    for a, n in items:
        N *= n
        result = 0
    for a, n in items:
        m = N//n
        d, r, s = gcdext(n, m)
        if d != 1:
            N = N//n
            continue
        result += a*s*m
    return result % N, N

#低加密指数e == 5
def low_e_5():
    sessions=[{"c": int(cs[3], 16),"n": int(ns[3], 16)},
    {"c":int(cs[8], 16) ,"n":int(ns[8], 16) },
    {"c":int(cs[12], 16),"n":int(ns[12], 16)},
    {"c":int(cs[16], 16),"n":int(ns[16], 16)},
    {"c":int(cs[20], 16),"n":int(ns[20], 16)}]
    data = []
    for session in sessions:
        data = data+[(session['c'], session['n'])]
    x, y = chinese_remainder_theorem(data)
    plaintext = iroot(mpz(x),5)
    finalplain=binascii.a2b_hex(hex(plaintext[0])[2:])
    print("解密结果为:",finalplain)
    
    return finalplain


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
        
    low_e_5()
