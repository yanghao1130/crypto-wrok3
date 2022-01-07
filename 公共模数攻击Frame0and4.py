# 公共模数攻击 求解Frame0、Frame4
from gmpy2 import *
from Crypto.Util.number import *
import binascii


# 公共模数攻击
def same_modulus():
    # 寻找公共模数

    e1 = int(es[0], 16)
    e2 = int(es[4], 16)
    n = int(ns[0], 16)
    c1 = int(cs[0], 16)
    c2 = int(cs[4], 16)
    s = gcdext(e1, e2) # 欧几里得算法
    r = s[1]
    s = s[2]
    # 求模反元素
    if r<0:
        r = - r
        c1 = invert(c1, n)
    elif s<0:
        s = - s
        c2 = invert(c2, n)

    m = pow(c1,r,n)*pow(c2,s,n) % n
    result = binascii.a2b_hex(hex(m)[2:])
    print("解密密文为:",result)
    
    return result


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
        
    same_modulus()
