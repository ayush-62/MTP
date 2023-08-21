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
# ,('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)),('17' , BitVecSort(8)),('18' , BitVecSort(8)),('19' , BitVecSort(8)),('20' , BitVecSort(8)),('21' , BitVecSort(8)),('22' , BitVecSort(8)),('23' , BitVecSort(8)),('24' , BitVecSort(8)),('25' , BitVecSort(8)),('26' , BitVecSort(8)),('27' , BitVecSort(8)),('28' , BitVecSort(8)),('29' , BitVecSort(8)),('30' , BitVecSort(8)),('31' , BitVecSort(8)),('8' , BitVecSort(8))
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1',8)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2',8)
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16=BitVecs('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16',8)
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',8)
oo0_2,oo1_2,oo2_2,oo3_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2',8)
'''k1_1,k2_1,k3_1,k4_1,k5_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1')
k1_2,k2_2,k3_2,k4_2,k5_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2')'''
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 8)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 8)



tuple = Datatype('tuple')
tuple.declare('tuple',('1' , BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)),('5' , BitVecSort(8)),('6' , BitVecSort(8)),('7' , BitVecSort(8)),('8' , BitVecSort(8)),('9' , BitVecSort(8)),('10' , BitVecSort(8)),('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)))
tuple.declare('tuple2',('1' , BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)))#,('5' , BitVecSort(8)),('6' , BitVecSort(8)),('7' , BitVecSort(8)),('8' , BitVecSort(8)),('9' , BitVecSort(8)),('10' , BitVecSort(8)),('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)))
tuple = tuple.create()
out1 = tuple.tuple(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

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


def AddRoundKey(statemt , Sbox , word ,n):
    nb = 4
    for j in range(nb):
        statemt = Store(statemt,j*4, statemt[j * 4]^word[0][j + nb * n])
        statemt = Store(statemt,1 + j * 4, statemt[1 + j * 4]^word[1][j + nb * n])
        statemt = Store(statemt,2 + j * 4, statemt[2 + j * 4]^word[2][j + nb * n])
        statemt = Store(statemt,3 + j * 4,statemt[3 + j * 4]^word[3][j + nb * n])
    for i in range(16):
        statemt = Store(statemt,i,simplify(statemt[i]))
    statemt = simplify(statemt)
    return statemt
ret = Array('ret', BitVecSort(8), BitVecSort(8))

def ByteSub_ShiftRow(S, I , W , key1 , key2 , key3 , key4):
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

    s9_1 = S[key1] >> 4
    s9_1b = S[key1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[key2] >> 4
    s9_10b= S[key2] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[key3] >> 4
    s9_15b = S[key3] & 0xf
    s9_11 = S[11] >> 4
    s9_11b = S[11] & 0xf
    s9_7= S[7] >> 4
    s9_7b= S[7] & 0xf

    s9_0=S[0] >> 4
    s9_0b=S[0] & 0xf
    s9_4 = S[4] >> 4
    s9_4b = S[4] & 0xf
    s9_8 = S[8] >> 4
    s9_8b = S[8] & 0xf
    s9_12 = S[12] >> 4
    s9_12b = S[12] & 0xf

    temp = I[s9_1][s9_1b] 
    S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 8),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 8), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 8),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 8), temp)

    S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

    return S

def MixColumn_AddRoundKey(S, I , W, nb, n ,ret,key4,key5,key6,key7,key8,key9,key10):
    n = BitVecVal(1,32)
    ret = Store(ret, 0, S[0] << 1)
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = Store(ret, 1 , S[1] << 1)
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    ret = Store(ret, 2, S[2] << 1)
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ key4), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, key5, S[3] << 1) #key5 3
    ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][4*n]))

    ret = Store(ret, 4, S[4] << 1)
    ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
    x = S[5]
    x = x ^ (x << 1)
    ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][1+4*n]))

    ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[2 + 1 * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8 + 4] #key8 3 
    x = x ^ (x << 1)  
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
    ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][1+4*n]))

    ret = Store(ret, 8, S[8] << 1)
    ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
    x = S[9]
    x = x ^ (x << 1)
    ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
    ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][2+4*n]))

    ret = Store(ret, 9,  S[9] << 1)
    ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
    x = S[10]
    x = x ^ (x << 1)
    ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
    ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][2+4*n]))

    ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
    ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
    x = S[11]
    x = x ^ (x << 1)
    ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
    ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][2+4*n]))

    ret = Store(ret, 11,  S[11] << 1)
    ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
    x = S[8]
    x = x ^ (x << 1)
    ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
    ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][2+4*n]))
 
    ret = Store(ret, 12, S[12] << 1)
    ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
    x = S[13]
    x = x ^ (x << 1)
    ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
    ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][3+4*n]))

    ret = Store(ret, 13,  S[13] << 1)
    ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
    x = S[14]
    x = x ^ (x << 1)
    ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
    ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][3+4*n]))

    ret = Store(ret, 14, S[14] << 1)
    ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
    x = S[15]
    x = x ^ (x << 1)
    ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
    ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][3+4*n]))

    ret = Store(ret, 15, S[15] << 1)
    ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
    x = S[12]
    x = x ^ (x << 1)
    ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
    ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][3+4*n]))
    
    S = Store(S, BitVecVal(0,32), ret[0])
    S = Store(S, BitVecVal(1,32), ret[1])
    S = Store(S, BitVecVal(2,32), ret[2])
    S = Store(S, BitVecVal(3,32), ret[3])
    S = Store(S, BitVecVal(4,32), ret[4])
    S = Store(S, BitVecVal(5,32), ret[5])
    S = Store(S, BitVecVal(6,32), ret[6])
    S = Store(S, BitVecVal(7,32), ret[7])
    S = Store(S, BitVecVal(8,32), ret[8])
    S = Store(S, BitVecVal(9,32), ret[9])
    S = Store(S, BitVecVal(10,32), ret[10])
    S = Store(S, BitVecVal(11,32), ret[11])
    S = Store(S, BitVecVal(12,32), ret[12])
    S = Store(S, BitVecVal(13,32), ret[13])
    S = Store(S, BitVecVal(14,32), ret[14])
    S = Store(S, BitVecVal(15,32), ret[15])
    return [S, ret]


def AES_2_Round(S, I, W , ret ,in1 , in2 , in3 , in4 , in5 , in6 , in7 , in8 , in9 , in10 , in11 , in12 , in13 , in14 , in15 , in16 , key1 , key2 , key3 , key4 , key5 , key6, key7, key8 , key9, key10):
    
    S = Array('S', BitVecSort(8), BitVecSort(8))
    S2 = Array('S2', BitVecSort(8), BitVecSort(8))
    I = Array('A', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    W = Array('W', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    tm = Array('tm', BitVecSort(8), BitVecSort(8))
    tm2 = Array('tm2', BitVecSort(8), BitVecSort(8))
    ##initialzing the statemt array
    i = 0
    for
    ## Initializing the `Sbox` array ##
    i = 0
    for arr in Sbox:
        j = 0
        for elem in arr:
            tm = Store(tm, BitVecVal(j, 8), BitVecVal(elem, 8))
            j += 1
        I = Store(I, BitVecVal(i, 8), tm)
    i += 1

## Initilaizing the `word` array ##
    i = 0
    for arr in word:
        j = 0
        for elem in arr:
            tm2 = Store(tm2, BitVecVal(j, 8), BitVecVal(elem, 8))
            j += 1
        W = Store(W, BitVecVal(i, 8), tm2)
        i += 1
#print(S[0])
    
    

    S = AddRoundKey(S , I , W , 0)
    # for i in range(10):
    #     S =  ByteSub_ShiftRow(S, I , W , key1 , key2 , key3 , key4)
    #     rv =  MixColumn_AddRoundKey(S, I , W, 4, i+1 , ret , key4 , key5 , key6 , key7 , key8 , key9 ,key10)
    #     S = rv[0]
    #     ret = rv[1]   
    # S =  ByteSub_ShiftRow(S, I , W , key1 , key2 , key3 , key4) 

#-----------------------------------------------------------Iterration 1---------------------------------------------------------------------

#---------------------------------------------------------Byte shift-----------------------------------------------------------------------
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

    s9_1 = S[key1] >> 4
    s9_1b = S[key1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[key2] >> 4
    s9_10b= S[key2] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[key3] >> 4
    s9_15b = S[key3] & 0xf
    s9_11 = S[11] >> 4
    s9_11b = S[11] & 0xf
    s9_7= S[7] >> 4
    s9_7b= S[7] & 0xf

    s9_0=S[0] >> 4
    s9_0b=S[0] & 0xf
    s9_4 = S[4] >> 4
    s9_4b = S[4] & 0xf
    s9_8 = S[8] >> 4
    s9_8b = S[8] & 0xf
    s9_12 = S[12] >> 4
    s9_12b = S[12] & 0xf

    temp = I[s9_1][s9_1b] 
    S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 8),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 8), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 8),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 8), temp)

    S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

#-----------------------------------------MIXCloumn-------------------------------------------------------
    ret = Store(ret, 0, S[0] << 1)
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

    ret = Store(ret, 1 , S[1] << 1)
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

    ret = Store(ret, 2, S[2] << 1)
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

    ret = Store(ret, key5, S[3] << 1) #key5 3
    ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

    ret = Store(ret, 4, S[4] << 1)
    ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
    x = S[5]
    x = x ^ (x << 1)
    ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

    ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[2 + 1 * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8 + 4] #key8 3 
    x = x ^ (x << 1)  
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
    ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

    ret = Store(ret, 8, S[8] << 1)
    ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
    x = S[9]
    x = x ^ (x << 1)
    ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
    ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

    ret = Store(ret, 9,  S[9] << 1)
    ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
    x = S[10]
    x = x ^ (x << 1)
    ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
    ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

    ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
    ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
    x = S[11]
    x = x ^ (x << 1)
    ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
    ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

    ret = Store(ret, 11,  S[11] << 1)
    ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
    x = S[8]
    x = x ^ (x << 1)
    ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
    ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
    ret = Store(ret, 12, S[12] << 1)
    ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
    x = S[13]
    x = x ^ (x << 1)
    ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
    ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

    ret = Store(ret, 13,  S[13] << 1)
    ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
    x = S[14]
    x = x ^ (x << 1)
    ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
    ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

    ret = Store(ret, 14, S[14] << 1)
    ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
    x = S[15]
    x = x ^ (x << 1)
    ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
    ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

    ret = Store(ret, 15, S[15] << 1)
    ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
    x = S[12]
    x = x ^ (x << 1)
    ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
    ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

  

    S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
    S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
    S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
    S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
    S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
    S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
    S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
    S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
    S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
    S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
    S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
    S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
    S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
    S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
    S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
    S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

    s9_1 = S[key1] >> 4
    s9_1b = S[key1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[key2] >> 4
    s9_10b= S[key2] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[key3] >> 4
    s9_15b = S[key3] & 0xf
    s9_11 = S[11] >> 4
    s9_11b = S[11] & 0xf
    s9_7= S[7] >> 4
    s9_7b= S[7] & 0xf

    s9_0=S[0] >> 4
    s9_0b=S[0] & 0xf
    s9_4 = S[4] >> 4
    s9_4b = S[4] & 0xf
    s9_8 = S[8] >> 4
    s9_8b = S[8] & 0xf
    s9_12 = S[12] >> 4
    s9_12b = S[12] & 0xf

    temp = I[s9_1][s9_1b] 
    S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 8),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 8), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 8),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 8), temp)

    S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

#-----------------------------------------MIXCloumn-------------------------------------------------------
    ret = Store(ret, 0, S[0] << 1)
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

    ret = Store(ret, 1 , S[1] << 1)
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

    ret = Store(ret, 2, S[2] << 1)
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

    ret = Store(ret, key5, S[3] << 1) #key5 3
    ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

    ret = Store(ret, 4, S[4] << 1)
    ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
    x = S[5]
    x = x ^ (x << 1)
    ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

    ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[2 + 1 * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8 + 4] #key8 3 
    x = x ^ (x << 1)  
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
    ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

    ret = Store(ret, 8, S[8] << 1)
    ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
    x = S[9]
    x = x ^ (x << 1)
    ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
    ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

    ret = Store(ret, 9,  S[9] << 1)
    ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
    x = S[10]
    x = x ^ (x << 1)
    ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
    ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

    ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
    ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
    x = S[11]
    x = x ^ (x << 1)
    ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
    ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

    ret = Store(ret, 11,  S[11] << 1)
    ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
    x = S[8]
    x = x ^ (x << 1)
    ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
    ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
    ret = Store(ret, 12, S[12] << 1)
    ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
    x = S[13]
    x = x ^ (x << 1)
    ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
    ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

    ret = Store(ret, 13,  S[13] << 1)
    ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
    x = S[14]
    x = x ^ (x << 1)
    ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
    ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

    ret = Store(ret, 14, S[14] << 1)
    ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
    x = S[15]
    x = x ^ (x << 1)
    ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
    ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

    ret = Store(ret, 15, S[15] << 1)
    ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
    x = S[12]
    x = x ^ (x << 1)
    ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
    ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#-------------------------------------------------------iteration 3--------------------------------------------------------


#---------------------------------------------------------Byte shift-----------------------------------------------------------------------
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

    s9_1 = S[key1] >> 4
    s9_1b = S[key1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[key2] >> 4
    s9_10b= S[key2] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[key3] >> 4
    s9_15b = S[key3] & 0xf
    s9_11 = S[11] >> 4
    s9_11b = S[11] & 0xf
    s9_7= S[7] >> 4
    s9_7b= S[7] & 0xf

    s9_0=S[0] >> 4
    s9_0b=S[0] & 0xf
    s9_4 = S[4] >> 4
    s9_4b = S[4] & 0xf
    s9_8 = S[8] >> 4
    s9_8b = S[8] & 0xf
    s9_12 = S[12] >> 4
    s9_12b = S[12] & 0xf

    temp = I[s9_1][s9_1b] 
    S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 8),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 8), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 8),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 8), temp)

    S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

#-----------------------------------------MIXCloumn-------------------------------------------------------
    ret = Store(ret, 0, S[0] << 1)
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

    ret = Store(ret, 1 , S[1] << 1)
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

    ret = Store(ret, 2, S[2] << 1)
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

    ret = Store(ret, key5, S[3] << 1) #key5 3
    ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

    ret = Store(ret, 4, S[4] << 1)
    ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
    x = S[5]
    x = x ^ (x << 1)
    ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

    ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[2 + 1 * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8 + 4] #key8 3 
    x = x ^ (x << 1)  
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
    ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

    ret = Store(ret, 8, S[8] << 1)
    ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
    x = S[9]
    x = x ^ (x << 1)
    ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
    ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

    ret = Store(ret, 9,  S[9] << 1)
    ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
    x = S[10]
    x = x ^ (x << 1)
    ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
    ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

    ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
    ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
    x = S[11]
    x = x ^ (x << 1)
    ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
    ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

    ret = Store(ret, 11,  S[11] << 1)
    ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
    x = S[8]
    x = x ^ (x << 1)
    ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
    ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
    ret = Store(ret, 12, S[12] << 1)
    ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
    x = S[13]
    x = x ^ (x << 1)
    ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
    ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

    ret = Store(ret, 13,  S[13] << 1)
    ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
    x = S[14]
    x = x ^ (x << 1)
    ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
    ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

    ret = Store(ret, 14, S[14] << 1)
    ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
    x = S[15]
    x = x ^ (x << 1)
    ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
    ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

    ret = Store(ret, 15, S[15] << 1)
    ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
    x = S[12]
    x = x ^ (x << 1)
    ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
    ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

   

    S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
    S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
    S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
    S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
    S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
    S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
    S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
    S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
    S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
    S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
    S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
    S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
    S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
    S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
    S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
    S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))


#     #------------------------------------------------------iteration 5--------------------------------------------------

# #-----------------------------------------------------------Iterration 1---------------------------------------------------------------------

# #---------------------------------------------------------Byte shift-----------------------------------------------------------------------
#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#----------------------------------------------------------iteration 7--------------------------------------

# #-----------------------------------------------------------Iterration 1---------------------------------------------------------------------

# #---------------------------------------------------------Byte shift-----------------------------------------------------------------------
#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#     #-------------------------------------iteration 9-----------------------------------------------------------

# #-----------------------------------------------------------Iterration 1---------------------------------------------------------------------

# #---------------------------------------------------------Byte shift-----------------------------------------------------------------------
#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     S = Store(S, BitVecVal(0,8), simplify(Select(ret,0)))
#     S = Store(S, BitVecVal(1,8), simplify(Select(ret,1)))
#     S = Store(S, BitVecVal(2,8), simplify(Select(ret,2)))
#     S = Store(S, BitVecVal(3,8), simplify(Select(ret,3)))
#     S = Store(S, BitVecVal(4,8), simplify(Select(ret,4)))
#     S = Store(S, BitVecVal(5,8), simplify(Select(ret,5)))
#     S = Store(S, BitVecVal(6,8), simplify(Select(ret,6)))
#     S = Store(S, BitVecVal(7,8), simplify(Select(ret,7)))
#     S = Store(S, BitVecVal(8,8), simplify(Select(ret,8)))
#     S = Store(S, BitVecVal(9,8), simplify(Select(ret,9)))
#     S = Store(S, BitVecVal(10,8), simplify(Select(ret,10)))
#     S = Store(S, BitVecVal(11,8), simplify(Select(ret,11)))
#     S = Store(S, BitVecVal(12,8), simplify(Select(ret,12)))
#     S = Store(S, BitVecVal(13,8), simplify(Select(ret,13)))
#     S = Store(S, BitVecVal(14,8), simplify(Select(ret,14)))
#     S = Store(S, BitVecVal(15,8), simplify(Select(ret,15)))

#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[key1] >> 4
#     s9_1b = S[key1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[key2] >> 4
#     s9_10b= S[key2] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[key3] >> 4
#     s9_15b = S[key3] & 0xf
#     s9_11 = S[11] >> 4
#     s9_11b = S[11] & 0xf
#     s9_7= S[7] >> 4
#     s9_7b= S[7] & 0xf

#     s9_0=S[0] >> 4
#     s9_0b=S[0] & 0xf
#     s9_4 = S[4] >> 4
#     s9_4b = S[4] & 0xf
#     s9_8 = S[8] >> 4
#     s9_8b = S[8] & 0xf
#     s9_12 = S[12] >> 4
#     s9_12b = S[12] & 0xf

#     temp = I[s9_1][s9_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s9_5][s9_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s9_9][s9_9b])
#     S = Store(S, BitVecVal(9, 8),I[s9_13][s9_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s9_2][s9_2b]
#     S = Store(S, BitVecVal(2, 8), I[s9_10][s9_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s9_6][s9_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s9_14][s9_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s9_3][s9_3b]
#     S = Store(S, BitVecVal(3, 8), I[s9_15][s9_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s9_11][s9_11b])
#     S = Store(S, BitVecVal(11, 8), I[s9_7][s9_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s9_0][s9_0b])
#     S = Store(S, BitVecVal(4, 8), I[s9_4][s9_4b])
#     S = Store(S, BitVecVal(8, 8), I[s9_8][s9_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s9_12][s9_12b])

# #-----------------------------------------MIXCloumn-------------------------------------------------------
#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][36]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][36]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][36]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][36]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][37]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][37]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][37]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][37]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][38]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][38]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][38]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][38]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][39]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][39]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][39]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][39]))
    
    S =  AddRoundKey(S , I , W , 10)
    o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16 = BitVecs('o1 o2 o3 o4 o5 o6 o7 o8 o9 o10 o11 o12 o13 o14 o15 o16', 32)
    o1 = simplify(Select(S,0))
    o2 = simplify(Select(S,1))
    o3 = simplify(Select(S,2))
    o4 = simplify(Select(S,3))
    o5 = simplify(Select(S,4))
    o6 = simplify(Select(S,5))
    o7 = simplify(Select(S,6))
    o8 = simplify(Select(S,7))
    o9 = simplify(Select(S,8))
    o10 = simplify(Select(S,9))
    o11 = simplify(Select(S,10))
    o12 = simplify(Select(S,11))
    o13 = simplify(Select(S,12))
    o14 = simplify(Select(S,13))
    o15 = simplify(Select(S,14))
    o16 = simplify(Select(S,15))
    out = tuple.tuple(o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16)
    return S
x = Int('x')

s = Tactic('smt').solver()
out = AES_2_Round(S , I , W , ret ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,10,15,0,3,1,4,3,8,2)
for i in range(1):
    s.add(simplify(Select(out,0)) == 2)
print(s.check())

exit()