# 因数碰撞法 破解frame1、frame18
from gmpy2 import *
from Crypto.Util.number import *
import binascii

def same_factor():
    prime = GCD(int(ns[1], 16), int(ns[18], 16))
    if prime != 1:
        print((ns[1], ns[18]))
        print((1, 18))
        p=prime
    q1 = int(ns[1], 16) // prime
    q18 = int(ns[18], 16) // prime
    print("p=",prime)
    print("q1=",q1)
    print("p1=,p1")

    phi1 = (p-1)*(q1-1)
    phi18 = (p-1)*(q18-1)

    d1 = invert(int(es[1],16) ,phi1)
    d18 = invert(int(es[18], 16), phi18)

    plaintext1 = powmod(int(cs[1], 16), d1, int(ns[1], 16))
    plaintext18 = powmod(int(cs[18], 16), d18, int(ns[18], 16))

    final_plain1 = binascii.a2b_hex(hex(plaintext1)[2:])
    final_plain18 = binascii.a2b_hex(hex(plaintext18)[2:])


    print("Frame1解密结果:",final_plain1)
    print("Frame18揭秘结果:",final_plain18)

    return 1

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
        
    same_factor()
