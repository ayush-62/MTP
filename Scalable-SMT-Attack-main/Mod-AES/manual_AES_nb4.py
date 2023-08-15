from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))
    
    
start_time = time.time()
#,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1,o17_1,o18_1,o19_1,o20_1,o21_1,o22_1,o23_1,o24_1,o25_1,o26_1,o27_1,o28_1,o29_1,o30_1,o31_1 
# ,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2,o17_2,o18_2,o19_2,o20_2,o21_2,o22_2,o23_2,o24_2,o25_2,o26_2,o27_2,o28_2,o29_2,o30_2,o31_2
#  o11_1 o12_1 o13_1 o14_1 o15_1 o16_1 o17_1 o18_1 o19_1 o20_1 o21_1 o22_1 o23_1 o24_1 o25_1 o26_1 o27_1 o28_1 o29_1 o30_1 o31_1'
#o11_2 o12_2 o13_2 o14_2 o15_2 o16_2 o17_2 o18_2 o19_2 o20_2 o21_2 o22_2 o23_2 o24_2 o25_2 o26_2 o27_2 o28_2 o29_2 o30_2 o31_2
# ,('11' , BitVecSort(32)),('12' , BitVecSort(32)),('13' , BitVecSort(32)),('14' , BitVecSort(32)),('15' , BitVecSort(32)),('16' , BitVecSort(32)),('17' , BitVecSort(32)),('18' , BitVecSort(32)),('19' , BitVecSort(32)),('20' , BitVecSort(32)),('21' , BitVecSort(32)),('22' , BitVecSort(32)),('23' , BitVecSort(32)),('24' , BitVecSort(32)),('25' , BitVecSort(32)),('26' , BitVecSort(32)),('27' , BitVecSort(32)),('28' , BitVecSort(32)),('29' , BitVecSort(32)),('30' , BitVecSort(32)),('31' , BitVecSort(32)),('32' , BitVecSort(32))
nb,n = BitVecs('nb n',32)
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1',32)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2',32)
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',32)
oo0_2,oo1_2,oo2_2,oo3_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2',32)
'''k1_1,k2_1,k3_1,k4_1,k5_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1')
k1_2,k2_2,k3_2,k4_2,k5_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2')'''
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 32)

tuple = Datatype('tuple')
tuple.declare('tuple1',('1' , BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)),('5' , BitVecSort(32)),('6' , BitVecSort(32)),('7' , BitVecSort(32)),('8' , BitVecSort(32)),('9' , BitVecSort(32)),('10' , BitVecSort(32)),('11' , BitVecSort(32)),('12' , BitVecSort(32)),('13' , BitVecSort(32)),('14' , BitVecSort(32)),('15' , BitVecSort(32)),('16' , BitVecSort(32)))
tuple.declare('tuple2',('1', BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 32

statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
Sbox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b,0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf,0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2,0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3,0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39,0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f,0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21,0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d,0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14,0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62,0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea,0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f,0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9,0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f,0xb0, 0x54, 0xbb, 0x16]]

#last element changed to 0x20 from 0x16

word = [[43,40,171,9,160,136,35,42,242,122,89,115,61,71,30,109,239,168,182,219,212,124,202,17,109,17,219,202,78,95,132,78,234,181,49,127,172,25,40,87,208,201,225,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[126,174,247,207,250,84,163,108,194,150,53,89,128,22,35,122,68,82,113,11,209,131,242,249,136,11,249,0,84,95,166,166,210,141,43,141,119,250,209,92,20,238,63,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[21,210,21,79,254,44,57,118,149,185,128,246,71,254,126,136,165,91,37,173,198,157,184,21,163,62,134,147,247,201,79,220,115,186,245,41,102,220,41,0,249,37,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[22,166,136,60,23,177,57,5,242,67,122,127,125,62,68,59,65,127,59,0,248,135,188,188,122,253,65,253,14,243,178,79,33,210,96,47,243,33,65,110,168,137,200,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

S = Array('S', BitVecSort(32), BitVecSort(32))
I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
tm = Array('tm', BitVecSort(32), BitVecSort(32))


def findOutput(key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,nb,n):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))
    ## Initializing the `statemt` array ##
    i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
        i += 1

    ## Initializing the `Sbox` array ##
    i = 0
    for arr in Sbox:
        j = 0
        for elem in arr:
            tm = Store(tm, BitVecVal(j, 32), BitVecVal(elem, 32))
            j += 1
        I = Store(I, BitVecVal(i, 32), tm)
        i += 1

     ## Initilaizing the `word` array ##
    i = 0
    for arr in word:
        j = 0
        for elem in arr:
            tm2 = Store(tm2, BitVecVal(j, 32), BitVecVal(elem, 32))
            j += 1
        W = Store(W, BitVecVal(i, 32), tm2)
        i += 1
    #print(S[0])

# ------------------ Add Round Key ----------------
    x = BitVecVal(2, 32)
    j = BitVecVal(0, 32)

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

# --------------------------------Iteration 0 ----------------------------------------------------------------------------------
    # ---------------------- ByetSub ShiftRow ------------------

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3

#---------------------------------Iteration 1 ---------------------------------------------------------------------------------------


    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3

#---------------------------------Iteration 2------------------------------------------------------------------------------------------------------------

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3
    
#---------------------------------Iteration 3------------------------------------------------------------------------------------------------------------  
 
    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3

#---------------------------------Iteration 4------------------------------------------------------------------------------------------------------------  

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3   

#---------------------------------Iteration 5------------------------------------------------------------------------------------------------------------  

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3   

#---------------------------------Iteration 6------------------------------------------------------------------------------------------------------------   

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3   

#---------------------------------Iteration 7------------------------------------------------------------------------------------------------------------   

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3   

#---------------------------------Iteration 8------------------------------------------------------------------------------------------------------------   

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp) 
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11])) 
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8])) 
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    #ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[key3 + j * 4] << 1, ret[1 + j * 4])) #key3 1
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * key4] ^ (x ^ 283), ret[1 + j * 4])) #key4 4
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key5 + j * 4]  # key5 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> key6 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4])) #key6 8
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, key7 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4])) #key7 2
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    j = j + key8 #key8 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4])) #
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, key9 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4])) #key9 2

    ret = Store(ret, 3 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, key10 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4])) #key10 3   

#---------------------------------Iteration 9------------------------------------------------------------------------------------------------------------   

    o0 = ret[0]
    o1 = ret[1]
    o2 = ret[2]
    o3 = ret[3]
    o4 = ret[4]
    o5 = ret[5] 
    o6 = ret[6]
    o7 = ret[7]
    o8 = ret[8] 
    o9 = ret[9]
    o10 = ret[10]
    o11 = ret[11]
    o12 = ret[12]
    o13 = ret[13]
    o14 = ret[14]
    o15 = ret[15]
    o = tuple.tuple1(o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15)
    return o


def sub(key1,key2,nb,n):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))
    ## Initializing the `statemt` array ##
    i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
        i += 1

    ## Initializing the `Sbox` array ##
    i = 0
    for arr in Sbox:
        j = 0
        for elem in arr:
            tm = Store(tm, BitVecVal(j, 32), BitVecVal(elem, 32))
            j += 1
        I = Store(I, BitVecVal(i, 32), tm)
        i += 1

     ## Initilaizing the `word` array ##
    i = 0
    for arr in word:
        j = 0
        for elem in arr:
            tm2 = Store(tm2, BitVecVal(j, 32), BitVecVal(elem, 32))
            j += 1
        W = Store(W, BitVecVal(i, 32), tm2)
        i += 1
    

    # ------------------ Add Round Key ----------------
    x = BitVecVal(2, 32)
    j = BitVecVal(0, 32)

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])

    j = j + 1

    S = Store(S, j * 4 , S[j * 4]^W[0][j + nb * n])
    S = Store(S, 1 + j * 4 ,S[1 + j * 4]^W[1][j + nb * n])
    S = Store(S, 2 + j * 4 ,S[2 + j * 4]^W[2][j + nb * n])
    S = Store(S, 3 + j * 4 ,S[3 + j * 4]^W[3][j + nb * n])


    # ---------------------- ByetSub ShiftRow ------------------

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 32)) 
    S = Store(S, BitVecVal(1, 32), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 32), If(nb==4,  I[S[9] >> 4][S[9] & 0xf], S[5]))
    S = Store(S, BitVecVal(9, 32), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 32), If(nb==4, temp, S[13]))

    temp = If(nb==4,  I[S[2] >> 4][S[2] & 0xf], temp)
    S = Store(S, BitVecVal(2, 32), If(nb==4,  I[S[10] >> 4][S[10] & 0xf], S[2]))
    S = Store(S, BitVecVal(10, 32), If(nb==4, temp, S[10]))
    temp = If(nb==4,  I[S[6] >> 4][S[6] & 0xf], temp)
    S = Store(S, BitVecVal(6, 32), If(nb==4,  I[S[14] >> 4][S[14] & 0xf], S[6]))
    S = Store(S, BitVecVal(14, 32), If(nb==4, temp, S[14]))

    temp = If(nb==4,  I[S[3] >> 4][S[3] & 0xf], temp)
    S = Store(S, BitVecVal(3, 32), If(nb==4,  I[S[15] >> 4][S[15] & 0xf], S[3]))
    S = Store(S, BitVecVal(15, 32), If(nb==4,  I[S[11] >> 4][S[11] & 0xf], S[15]))
    S = Store(S, BitVecVal(11, 32), If(nb==4,  I[S[7] >> 4][S[7] & 0xf], S[11]))
    S = Store(S, BitVecVal(7, 32), If(nb==4, temp, S[7]))

    S = Store(S, BitVecVal(0, 32), If(nb==4,  I[S[0] >> 4][S[0] & 0xf], S[0]))
    S = Store(S, BitVecVal(4, 32), If(nb==4,  I[S[4] >> 4][S[4] & 0xf], S[4]))
    S = Store(S, BitVecVal(8, 32), If(nb==4,  I[S[8] >> 4][S[8] & 0xf], S[8]))
    S = Store(S, BitVecVal(12, 32), If(nb==4,  I[S[12] >> 4][S[12] & 0xf], S[12]))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, If(j < nb, S[j * 4] << 1, ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, ret[j * 4] >> 8 == 1), ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(And(j < nb, x >> 8 == 1), ret[j * 4] ^ (x ^ 283), ret[j * 4]))
    ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[j * 4] ^ x, ret[j * 4]))
    ret = Store(ret, j * 4, If(j < nb, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]), ret[j * 4]))

    ret = Store(ret, 1 + j * 4, If(j < nb, S[1 + j * 4] << 1, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, ret[1 + j * 4] >> 8 == 1), ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(And(j < nb, x >> 8 == 1), ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[1 + j * 4] ^ x, ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, If(j < nb, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]), ret[1 + j * 4]))

    ret = Store(ret, 2 + j * 4, If(j < nb, S[2 + j * 4] << 1, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(And(j < nb, ret[2 + j * 4] >> 8 == 1), ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If(And(j < nb, x >> 8 == 1), ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4])) 
    ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[2 + j * 4] ^ x, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, If(j < nb, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]), ret[2 + j * 4]))

    ret = Store(ret, key1 + j * 4, If(j < nb, S[3 + j * 4] << 1, ret[3 + j * 4])) #key1 3
    ret = Store(ret, 3 + j * 4, If(And(j < nb, ret[3 + j * 4] >> 8 == 1), ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(And(j < nb, x >> 8 == 1), ret[3 + j * 4] ^ (x ^ key2), ret[3 + j * 4])) #key2 283
    ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), ret[3 + j * 4] ^ x, ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, If(j < nb, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]), ret[3 + j * 4]))

    o0=ret[0]
    o1=ret[1]
    o2=ret[2]
    o3=ret[3]

    o=tuple.tuple2(o0,o1,o2,o3)
    return o


# gg = Tactic('smt').solver()
# ia = str(4) + " " + str(5)
# [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
# #,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
# oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))

# print(gg.check(findOutput(False,True,False,True,True,3,1,4,283,3,8,2,1,2,3,4,5)==oa))

'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))'''



j = 0


s = Tactic('smt').solver()

#s.add(simplify(findOutput(k1_1,k2_1,k3_1,k4_1,k5_1,key1_1,key2_1,key3_1,nb,n)) == out1)
#s.add(simplify(findOutput(k1_2,k2_2,k3_2,k4_2,k5_2,key1_2,key2_2,key3_2,nb,n)) == out2)

s.add(simplify(sub(key1_1,key2_1,nb,n)) == out3)
s.add(simplify(sub(key1_2,key2_2,nb,n)) == out4)
s.add(nb == 4)
s.add(n >= 0, n < 15)
s.add(key1_1>=0)
s.add(key1_2>=0)
s.add(key2_1>=0)
s.add(key2_2>=0)
s.add(key3_1>=0)
s.add(key3_2>=0)
s.add(key4_1>=0)
s.add(key4_2>=0)
s.add(key5_1>=0)
s.add(key5_2>=0)
s.add(key6_1>=0)
s.add(key6_2>=0)
s.add(key7_1>=0)
s.add(key7_2>=0)
s.add(key8_1>=0)
s.add(key8_2>=0)
s.add(key9_1>=0)
s.add(key9_2>=0)
s.add(key10_1>=0)
s.add(key10_2>=0)





pos_set = set()
print("loop1 enter")
# s.check()
# print(s.model())
#print(s.check(out1 != out2, Or(k1_1 != k1_2,k2_1 != k2_2 , k3_1 != k3_2 ,k4_1 != k4_2,k5_1 != k5_2 ,key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2)))

start=time.time()
while s.check(out3 != out4, Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1!=key4_2,key5_1!=key5_2,key6_1!=key6_2,key7_1!=key7_2,key8_1!=key8_2,key9_1!=key9_2,key10_1!=key10_2)) == sat:
    m = s.model()
    #print(m)
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2]))
    ia = str(m[nb]) + " " + str(m[n])
    [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    #,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
    oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
    s.add(simplify(findOutput(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,m[nb],m[n])) == oa)
    s.add(simplify(findOutput(key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,m[nb],m[n])) == oa)
    print("Iteration %d = %f second" %(j+1,time.time()-start))
    j = j + 1
print("unsat takes %d time" %(time.time()-start))
print("loop1 complete")


s.add(key1_1<=3)
s.add(key1_2<=3)
s.add(key3_1<=3)
s.add(key3_2<=3)
s.add(key4_1<=4)
s.add(key4_2<=4)
s.add(key5_1<=3)
s.add(key5_2<=3)
s.add(key6_1<=31)
s.add(key6_2<=31)
s.add(key7_1<=3)
s.add(key7_2<=3)
s.add(key8_1<=15)
s.add(key8_2<=15)
s.add(key9_1<=3)
s.add(key9_2<=3)
s.add(key10_1<=3)
s.add(key10_2<=3)

p=0
stat=time.time()
while s.check(key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1==key4_2,key5_1==key5_2,key6_1==key6_2,key7_1==key7_2,key8_1==key8_2,key9_1==key9_2,key10_1==key10_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    pos_set.add(m)
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1]))
    print("Iteration %d = %f second" %(p+1,time.time()-start))
    if len(pos_set) > rem_key_max:
        break
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1],key5_1!=m[key5_1],key6_1!=m[key6_1],key7_1!=m[key7_1],key8_1!=m[key8_1],key9_1!=m[key9_1],key10_1!=m[key10_1]))
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2],key5_2!=m[key5_2],key6_2!=m[key6_2],key7_2!=m[key7_2],key8_2!=m[key8_2],key9_2!=m[key9_2],key10_2!=m[key10_2]))
    p = p + 1


pos_l = list(pos_set)

g = Tactic('smt').solver()

g.add(simplify(findOutput(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,nb,n)) == out1)
g.add(simplify(findOutput(key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,nb,n)) == out2)
g.add(nb==4)
g.add(n>=0 ,n<15)

print("loop3 enter")

while len(pos_l) > 1:
    m1 = pos_l[0]
    m2 = pos_l[1]
    g.push()
    g.add(key1_1 == m1[key1_2],key2_1==m1[key2_2],key3_1==m1[key3_2],key4_1==m1[key4_2],key5_1==m1[key5_2],key6_1==m1[key6_2],key7_1==m1[key7_2],key8_1==m1[key8_2],key9_1==m1[key9_2],key10_1==m1[key10_2])
    g.add(key1_2 == m2[key1_2],key2_2==m2[key2_2],key3_2==m2[key3_2],key4_2==m2[key4_2],key5_2==m2[key5_2],key6_2==m2[key6_2],key7_2==m2[key7_2],key8_2==m2[key8_2],key9_2==m2[key9_2],key10_2==m2[key10_2])
    if g.check(out1 != out2) == sat:
        m = g.model()
        #print(str(m[nb])+"  "+str(m[n]))
        ia = str(m[nb]) + " " + str(m[n])
        [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16] = Cexec(ia)
        oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
        if g.check(simplify(findOutput(m1[key1_2],m1[key2_2],m1[key3_2],m1[key4_2],m1[key5_2],m1[key6_2],m1[key7_2],m1[key8_2],m1[key9_2],m1[key10_2],m[nb],m[n])) == oa) == unsat:
            pos_l.remove(m1)
        if g.check(simplify(findOutput(m2[key1_2],m2[key2_2],m2[key3_2],m2[key4_2],m2[key5_2],m2[key6_2],m2[key7_2],m2[key8_2],m2[key9_2],m2[key10_2],m[nb],m[n])) == oa) == unsat:
            pos_l.remove(m2)
    else:
        pos_l.remove(m1)
    g.pop()

print("The final key is:")
m = pos_l[0]
print(m[key1_1])
print(m[key2_1])
print(m[key3_1])
print(m[key4_1])
print(m[key5_1])
print(m[key6_1])
print(m[key7_1])
print(m[key8_1])
print(m[key9_1])
print(m[key10_1])
print()


end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (j, taken))      

