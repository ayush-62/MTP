
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
tuple.declare('tuple1',('1' , BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)),('5' , BitVecSort(8)),('6' , BitVecSort(8)),('7' , BitVecSort(8)),('8' , BitVecSort(8)),('9' , BitVecSort(8)),('10' , BitVecSort(8)),('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)))
tuple.declare('tuple2',('1' , BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)))#,('5' , BitVecSort(8)),('6' , BitVecSort(8)),('7' , BitVecSort(8)),('8' , BitVecSort(8)),('9' , BitVecSort(8)),('10' , BitVecSort(8)),('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 32

statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
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


#,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10
def findOutput1(key1,key2,key3,key4,key5,key6,key7,key8,key9,key10):
    S = Array('S', BitVecSort(8), BitVecSort(8))
    S2 = Array('S2', BitVecSort(8), BitVecSort(8))
    I = Array('A', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    W = Array('W', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    tm = Array('tm', BitVecSort(8), BitVecSort(8))
    tm2 = Array('tm2', BitVecSort(8), BitVecSort(8))
    ret = Array('ret', BitVecSort(8), BitVecSort(8))

    statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]

    S = Store(S,BitVecVal(0,8),BitVecVal(statemt[0],8))
    S = Store(S,BitVecVal(1,8),BitVecVal(statemt[1],8))
    S = Store(S,BitVecVal(2,8),BitVecVal(statemt[2],8))
    S = Store(S,BitVecVal(3,8),BitVecVal(statemt[3],8))
    S = Store(S,BitVecVal(4,8),BitVecVal(statemt[4],8))
    S = Store(S,BitVecVal(5,8),BitVecVal(statemt[5],8))
    S = Store(S,BitVecVal(6,8),BitVecVal(statemt[6],8))
    S = Store(S,BitVecVal(7,8),BitVecVal(statemt[7],8))
    S = Store(S,BitVecVal(8,8),BitVecVal(statemt[8],8))
    S = Store(S,BitVecVal(9,8),BitVecVal(statemt[9],8))
    S = Store(S,BitVecVal(10,8),BitVecVal(statemt[10],8))
    S = Store(S,BitVecVal(11,8),BitVecVal(statemt[11],8))
    S = Store(S,BitVecVal(12,8),BitVecVal(statemt[12],8))
    S = Store(S,BitVecVal(13,8),BitVecVal(statemt[13],8))
    S = Store(S,BitVecVal(14,8),BitVecVal(statemt[14],8))
    S = Store(S,BitVecVal(15,8),BitVecVal(statemt[15],8))

    i = 0
    for arr in Sbox:
        j = 0
        tm = Array('tm', BitVecSort(8), BitVecSort(8))
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

# ------------------ Add Round Key ----------------

    # S = Store(S,BitVecVal(0,8),BitVecVal(155,8))
    # S = Store(S,BitVecVal(1,8),BitVecVal(202,8))
    # S = Store(S,BitVecVal(2,8),BitVecVal(23,8))
    # S = Store(S,BitVecVal(3,8),BitVecVal(230,8))
    # S = Store(S,BitVecVal(4,8),BitVecVal(58,8))
    # S = Store(S,BitVecVal(5,8),BitVecVal(172,8))
    # S = Store(S,BitVecVal(6,8),BitVecVal(192,8))
    # S = Store(S,BitVecVal(7,8),BitVecVal(159,8))
    # S = Store(S,BitVecVal(8,8),BitVecVal(170,8))
    # S = Store(S,BitVecVal(9,8),BitVecVal(242,8))
    # S = Store(S,BitVecVal(10,8),BitVecVal(48,8))
    # S = Store(S,BitVecVal(11,8),BitVecVal(141,8))
    # S = Store(S,BitVecVal(12,8),BitVecVal(133,8))
    # S = Store(S,BitVecVal(13,8),BitVecVal(83,8))
    # S = Store(S,BitVecVal(14,8),BitVecVal(211,8))
    # S = Store(S,BitVecVal(15,8),BitVecVal(238,8))

    # --------------------------------Iteration 1 ----------------------------------------------------------------------------------
    s3_0,s3_1,s3_2,s3_3,s3_4,s3_5,s3_6,s3_7,s3_8,s3_9,s3_10,s3_11,s3_12,s3_13,s3_14,s3_15=BitVecs('s3_0 s3_1 s3_2 s3_3 s3_4 s3_5 s3_6 s3_7 s3_8 s3_9 s3_10 s3_11 s3_12 s3_13 s3_14 s3_15',8)
    s3_0b,s3_1b,s3_2b,s3_3b,s3_4b,s3_5b,s3_6b,s3_7b,s3_8b,s3_9b,s3_10b,s3_11b,s3_12b,s3_13b,s3_14b,s3_15b=BitVecs('s3_0b s3_1b s3_2b s3_3b s3_4b s3_5b s3_6b s3_7b s3_8b s3_9b s3_10b s3_11b s3_12b s3_13b s3_14b s3_15b',8)

    s3_1 = S[1] >> 4
    s3_1b = S[1] & 0xf
    s3_5 = S[5] >> 4
    s3_5b = S[5] & 0xf
    s3_9 = S[9] >> 4
    s3_9b = S[9] & 0xf
    s3_13= S[13] >> 4
    s3_13b= S[13] & 0xf


    s3_2 = S[2] >> 4
    s3_2b = S[2] & 0xf
    s3_10= S[10] >> 4
    s3_10b= S[10] & 0xf
    s3_6 = S[6] >> 4
    s3_6b = S[6] & 0xf
    s3_14 = S[14] >> 4
    s3_14b = S[14] & 0xf

    s3_3 = S[3] >> 4
    s3_3b = S[3] & 0xf
    s3_15 = S[15] >> 4
    s3_15b = S[15] & 0xf
    s3_11 = S[11] >> 4
    s3_11b = S[11] & 0xf
    s3_7= S[7] >> 4
    s3_7b= S[7] & 0xf

    s3_0=S[0] >> 4
    s3_0b=S[0] & 0xf
    s3_4 = S[4] >> 4
    s3_4b = S[4] & 0xf
    s3_8 = S[8] >> 4
    s3_8b = S[8] & 0xf
    s3_12 = S[12] >> 4
    s3_12b = S[12] & 0xf

    temp = I[s3_1][s3_1b] 
    S = Store(S, BitVecVal(1, 8),I[s3_5][s3_5b]) #key1=5
    S = Store(S, BitVecVal(5, 8),I[s3_9][s3_9b])
    S = Store(S, BitVecVal(9, 8),I[s3_13][s3_13b])
    S = Store(S, BitVecVal(13, 8),temp)

    temp = I[s3_2][s3_2b]
    print( simplify((BitVecVal(152,32))/16)," ", simplify(s3_10)," ",simplify(s3_10b))
    S = Store(S, BitVecVal(2, 8), I[s3_10][s3_10b]) #key2=10
    S = Store(S, BitVecVal(10, 8), temp)
    temp = I[s3_6][s3_6b] 
    S = Store(S, BitVecVal(6, 8), I[s3_14][s3_14b])
    S = Store(S, BitVecVal(14, 8),temp)

    temp = I[s3_3][s3_3b]
    S = Store(S, BitVecVal(3, 8), I[s3_15][s3_15b]) #key3=15
    S = Store(S, BitVecVal(15, 8), I[s3_11][s3_11b])
    S = Store(S, BitVecVal(11, 8), I[s3_7][s3_7b]) 
    S = Store(S, BitVecVal(7, 8), temp)

    S = Store(S, BitVecVal(0, 8), I[s3_0][s3_0b])
    S = Store(S, BitVecVal(4, 8), I[s3_4][s3_4b])
    S = Store(S, BitVecVal(8, 8), I[s3_8][s3_8b]) 
    S = Store(S, BitVecVal(12, 8),I[s3_12][s3_12b])
    simplify(S)

    # ------------------------ MixColumn AddRoundKey ---------------------------------


    # j = BitVecVal(0,8)

    # ret = Store(ret, 0, S[0] << 1)
    # ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    # x = S[1]
    # x = x ^ (x << 1)
    # ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    # ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][12]))

    # ret = Store(ret, 1, S[1] << 1)
    # ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    # x = S[2]
    # x = x ^ (x << 1)
    # ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    # ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][12]))

    # ret = Store(ret, 2, S[2] << 1)
    # ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    # x = S[3]
    # x = x ^ (x << 1)
    # ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    # ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][12]))

    # ret = Store(ret, key5, S[3] << 1) #key5 3
    # ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    # x = S[0]
    # x = x ^ (x << 1)
    # ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    # ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][12]))

    # j = BitVecVal(1,8) #j=1
    # ret = Store(ret, 4, S[4] << 1)
    # ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
    # x = S[5]
    # x = x ^ (x << 1)
    # ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    # ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][13]))

    # ret = Store(ret, 5,  S[key6+ 4] << 1) #key6 1
    # ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    # x = S[2 +  key7] #key7 4
    # x = x ^ (x << 1)
    # ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    # ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][13]))

    # ret = Store(ret, 6,  S[6] << 1)
    # ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    # x = S[key8 + 4] #key8 3 
    # x = x ^ (x << 1)  
    # ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    # ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][13]))

    # ret = Store(ret, 7,  S[7] << 1)
    # ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    # x = S[4]
    # x = x ^ (x << 1)
    # ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
    # ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][13]))

    # j = BitVecVal(2,8) #j=2
    # ret = Store(ret, 8, S[8] << 1)
    # ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
    # x = S[9]
    # x = x ^ (x << 1)
    # ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
    # ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][14]))

    # ret = Store(ret, 9,  S[9] << 1)
    # ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
    # x = S[10]
    # x = x ^ (x << 1)
    # ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
    # ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[j * 4] ^ W[1][14]))

    # ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
    # ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
    # x = S[11]
    # x = x ^ (x << 1)
    # ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
    # ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][14]))

    # ret = Store(ret, 11,  S[11] << 1)
    # ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
    # x = S[8]
    # x = x ^ (x << 1)
    # ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
    # ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][14]))

    # j = BitVecVal(3,8)  
    # ret = Store(ret, 12, S[12] << 1)
    # ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
    # x = S[13]
    # x = x ^ (x << 1)
    # ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
    # ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][15]))

    # ret = Store(ret, 13,  S[13] << 1)
    # ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
    # x = S[14]
    # x = x ^ (x << 1)
    # ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
    # ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][15]))

    # ret = Store(ret, 14, S[14] << 1)
    # ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
    # x = S[15]
    # x = x ^ (x << 1)
    # ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
    # ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][15]))

    # ret = Store(ret, 15, S[15] << 1)
    # ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
    # x = S[12]
    # x = x ^ (x << 1)
    # ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
    # ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][15])) 

    # S = Store(S, BitVecVal(0,8), ret[0])
    # S = Store(S, BitVecVal(1,8), ret[1])
    # S = Store(S, BitVecVal(2,8), ret[2])
    # S = Store(S, BitVecVal(3,8), ret[3])
    # S = Store(S, BitVecVal(4,8), ret[4])
    # S = Store(S, BitVecVal(5,8), ret[5])
    # S = Store(S, BitVecVal(6,8), ret[6])
    # S = Store(S, BitVecVal(7,8), ret[7])
    # S = Store(S, BitVecVal(8,8), ret[8])
    # S = Store(S, BitVecVal(9,8), ret[9])
    # S = Store(S, BitVecVal(10,8), ret[10])
    # S = Store(S, BitVecVal(11,8), ret[11])
    # S = Store(S, BitVecVal(12,8), ret[12])
    # S = Store(S, BitVecVal(13,8), ret[13])
    # S = Store(S, BitVecVal(14,8), ret[14])
    # S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 2 -----------------------------------------------------------------------------------
#     s3_0,s3_1,s3_2,s3_3,s3_4,s3_5,s3_6,s3_7,s3_8,s3_9,s3_10,s3_11,s3_12,s3_13,s3_14,s3_15=BitVecs('s3_0 s3_1 s3_2 s3_3 s3_4 s3_5 s3_6 s3_7 s3_8 s3_9 s3_10 s3_11 s3_12 s3_13 s3_14 s3_15',8)
#     s3_0b,s3_1b,s3_2b,s3_3b,s3_4b,s3_5b,s3_6b,s3_7b,s3_8b,s3_9b,s3_10b,s3_11b,s3_12b,s3_13b,s3_14b,s3_15b=BitVecs('s3_0b s3_1b s3_2b s3_3b s3_4b s3_5b s3_6b s3_7b s3_8b s3_9b s3_10b s3_11b s3_12b s3_13b s3_14b s3_15b',8)

#     s3_1 = S[1] >> 4
#     s3_1b = S[1] & 0xf
#     s3_5 = S[5] >> 4
#     s3_5b = S[5] & 0xf
#     s3_9 = S[9] >> 4
#     s3_9b = S[9] & 0xf
#     s3_13= S[13] >> 4
#     s3_13b= S[13] & 0xf


#     s3_2 = S[2] >> 4
#     s3_2b = S[2] & 0xf
#     s3_10= S[10] >> 4
#     s3_10b= S[10] & 0xf
#     s3_6 = S[6] >> 4
#     s3_6b = S[6] & 0xf
#     s3_14 = S[14] >> 4
#     s3_14b = S[14] & 0xf

#     s3_3 = S[3] >> 4
#     s3_3b = S[3] & 0xf
#     s3_15 = S[15] >> 4
#     s3_15b = S[15] & 0xf
#     s3_11 = S[11] >> 4
#     s3_11b = S[11] & 0xf
#     s3_7= S[7] >> 4
#     s3_7b= S[7] & 0xf

#     s3_0=S[0] >> 4
#     s3_0b=S[0] & 0xf
#     s3_4 = S[4] >> 4
#     s3_4b = S[4] & 0xf
#     s3_8 = S[8] >> 4
#     s3_8b = S[8] & 0xf
#     s3_12 = S[12] >> 4
#     s3_12b = S[12] & 0xf

#     temp = I[s3_1][s3_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s3_5][s3_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s3_9][s3_9b])
#     S = Store(S, BitVecVal(9, 8),I[s3_13][s3_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s3_2][s3_2b]
#     S = Store(S, BitVecVal(2, 8), I[s3_10][s3_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s3_6][s3_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s3_14][s3_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s3_3][s3_3b]
#     S = Store(S, BitVecVal(3, 8), I[s3_15][s3_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s3_11][s3_11b])
#     S = Store(S, BitVecVal(11, 8), I[s3_7][s3_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s3_0][s3_0b])
#     S = Store(S, BitVecVal(4, 8), I[s3_4][s3_4b])
#     S = Store(S, BitVecVal(8, 8), I[s3_8][s3_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s3_12][s3_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     j = BitVecVal(0,8)

#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][12]))

#     ret = Store(ret, 1, S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][12]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][12]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][12]))

#     j = BitVecVal(1,8) #j=1
#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][13]))

#     ret = Store(ret, 5,  S[key6+ 4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 +  key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][13]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][13]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][13]))

#     j = BitVecVal(2,8) #j=2
#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][14]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[j * 4] ^ W[1][14]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][14]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][14]))

#     j = BitVecVal(3,8)  
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][15]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][15]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][15]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][15])) 

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 3 -----------------------------------------------------------------------------------
#     s3_0,s3_1,s3_2,s3_3,s3_4,s3_5,s3_6,s3_7,s3_8,s3_9,s3_10,s3_11,s3_12,s3_13,s3_14,s3_15=BitVecs('s3_0 s3_1 s3_2 s3_3 s3_4 s3_5 s3_6 s3_7 s3_8 s3_9 s3_10 s3_11 s3_12 s3_13 s3_14 s3_15',8)
#     s3_0b,s3_1b,s3_2b,s3_3b,s3_4b,s3_5b,s3_6b,s3_7b,s3_8b,s3_9b,s3_10b,s3_11b,s3_12b,s3_13b,s3_14b,s3_15b=BitVecs('s3_0b s3_1b s3_2b s3_3b s3_4b s3_5b s3_6b s3_7b s3_8b s3_9b s3_10b s3_11b s3_12b s3_13b s3_14b s3_15b',8)

#     s3_1 = S[1] >> 4
#     s3_1b = S[1] & 0xf
#     s3_5 = S[5] >> 4
#     s3_5b = S[5] & 0xf
#     s3_9 = S[9] >> 4
#     s3_9b = S[9] & 0xf
#     s3_13= S[13] >> 4
#     s3_13b= S[13] & 0xf


#     s3_2 = S[2] >> 4
#     s3_2b = S[2] & 0xf
#     s3_10= S[10] >> 4
#     s3_10b= S[10] & 0xf
#     s3_6 = S[6] >> 4
#     s3_6b = S[6] & 0xf
#     s3_14 = S[14] >> 4
#     s3_14b = S[14] & 0xf

#     s3_3 = S[3] >> 4
#     s3_3b = S[3] & 0xf
#     s3_15 = S[15] >> 4
#     s3_15b = S[15] & 0xf
#     s3_11 = S[11] >> 4
#     s3_11b = S[11] & 0xf
#     s3_7= S[7] >> 4
#     s3_7b= S[7] & 0xf

#     s3_0=S[0] >> 4
#     s3_0b=S[0] & 0xf
#     s3_4 = S[4] >> 4
#     s3_4b = S[4] & 0xf
#     s3_8 = S[8] >> 4
#     s3_8b = S[8] & 0xf
#     s3_12 = S[12] >> 4
#     s3_12b = S[12] & 0xf

#     temp = I[s3_1][s3_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s3_5][s3_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s3_9][s3_9b])
#     S = Store(S, BitVecVal(9, 8),I[s3_13][s3_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s3_2][s3_2b]
#     S = Store(S, BitVecVal(2, 8), I[s3_10][s3_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s3_6][s3_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s3_14][s3_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s3_3][s3_3b]
#     S = Store(S, BitVecVal(3, 8), I[s3_15][s3_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s3_11][s3_11b])
#     S = Store(S, BitVecVal(11, 8), I[s3_7][s3_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s3_0][s3_0b])
#     S = Store(S, BitVecVal(4, 8), I[s3_4][s3_4b])
#     S = Store(S, BitVecVal(8, 8), I[s3_8][s3_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s3_12][s3_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     j = BitVecVal(0,8)

#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][12]))

#     ret = Store(ret, 1, S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][12]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][12]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][12]))

#     j = BitVecVal(1,8) #j=1
#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][13]))

#     ret = Store(ret, 5,  S[key6+ 4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 +  key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][13]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][13]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][13]))

#     j = BitVecVal(2,8) #j=2
#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][14]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[j * 4] ^ W[1][14]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][14]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][14]))

#     j = BitVecVal(3,8)  
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][15]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][15]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][15]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][15])) 

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 4 -----------------------------------------------------------------------------------
#     s4_0,s4_1,s4_2,s4_3,s4_4,s4_5,s4_6,s4_7,s4_8,s4_9,s4_10,s4_11,s4_12,s4_13,s4_14,s4_15=BitVecs('s4_0 s4_1 s4_2 s4_3 s4_4 s4_5 s4_6 s4_7 s4_8 s4_9 s4_10 s4_11 s4_12 s4_13 s4_14 s4_15',8)
#     s4_0b,s4_1b,s4_2b,s4_3b,s4_4b,s4_5b,s4_6b,s4_7b,s4_8b,s4_9b,s4_10b,s4_11b,s4_12b,s4_13b,s4_14b,s4_15b=BitVecs('s4_0b s4_1b s4_2b s4_3b s4_4b s4_5b s4_6b s4_7b s4_8b s4_9b s4_10b s4_11b s4_12b s4_13b s4_14b s4_15b',8)

#     s4_1 = S[1] >> 4
#     s4_1b = S[1] & 0xf
#     s4_5 = S[5] >> 4
#     s4_5b = S[5] & 0xf
#     s4_9 = S[9] >> 4
#     s4_9b = S[9] & 0xf
#     s4_13= S[13] >> 4
#     s4_13b= S[13] & 0xf


#     s4_2 = S[2] >> 4
#     s4_2b = S[2] & 0xf
#     s4_10= S[10] >> 4
#     s4_10b= S[10] & 0xf
#     s4_6 = S[6] >> 4
#     s4_6b = S[6] & 0xf
#     s4_14 = S[14] >> 4
#     s4_14b = S[14] & 0xf

#     s4_3 = S[3] >> 4
#     s4_3b = S[3] & 0xf
#     s4_15 = S[15] >> 4
#     s4_15b = S[15] & 0xf
#     s4_11 = S[11] >> 4
#     s4_11b = S[11] & 0xf
#     s4_7= S[7] >> 4
#     s4_7b= S[7] & 0xf

#     s4_0=S[0] >> 4
#     s4_0b=S[0] & 0xf
#     s4_4 = S[4] >> 4
#     s4_4b = S[4] & 0xf
#     s4_8 = S[8] >> 4
#     s4_8b = S[8] & 0xf
#     s4_12 = S[12] >> 4
#     s4_12b = S[12] & 0xf

#     temp = I[s4_1][s4_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s4_5][s4_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s4_9][s4_9b])
#     S = Store(S, BitVecVal(9, 8),I[s4_13][s4_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s4_2][s4_2b]
#     S = Store(S, BitVecVal(2, 8), I[s4_10][s4_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s4_6][s4_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s4_14][s4_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s4_3][s4_3b]
#     S = Store(S, BitVecVal(3, 8), I[s4_15][s4_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s4_11][s4_11b])
#     S = Store(S, BitVecVal(11, 8), I[s4_7][s4_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s4_0][s4_0b])
#     S = Store(S, BitVecVal(4, 8), I[s4_4][s4_4b])
#     S = Store(S, BitVecVal(8, 8), I[s4_8][s4_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s4_12][s4_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][16]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][16]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][16]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][16]))

#     ret = Store(ret, 4,S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][17]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][17]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][17]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][17]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][18]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][18]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][18]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][18]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][19]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][19]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][19]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][19]))

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 5 -----------------------------------------------------------------------------------
#     s5_0,s5_1,s5_2,s5_3,s5_4,s5_5,s5_6,s5_7,s5_8,s5_9,s5_10,s5_11,s5_12,s5_13,s5_14,s5_15=BitVecs('s5_0 s5_1 s5_2 s5_3 s5_4 s5_5 s5_6 s5_7 s5_8 s5_9 s5_10 s5_11 s5_12 s5_13 s5_14 s5_15',8)
#     s5_0b,s5_1b,s5_2b,s5_3b,s5_4b,s5_5b,s5_6b,s5_7b,s5_8b,s5_9b,s5_10b,s5_11b,s5_12b,s5_13b,s5_14b,s5_15b=BitVecs('s5_0b s5_1b s5_2b s5_3b s5_4b s5_5b s5_6b s5_7b s5_8b s5_9b s5_10b s5_11b s5_12b s5_13b s5_14b s5_15b',8)

#     s5_1 = S[1] >> 4
#     s5_1b = S[1] & 0xf
#     s5_5 = S[5] >> 4
#     s5_5b = S[5] & 0xf
#     s5_9 = S[9] >> 4
#     s5_9b = S[9] & 0xf
#     s5_13= S[13] >> 4
#     s5_13b= S[13] & 0xf


#     s5_2 = S[2] >> 4
#     s5_2b = S[2] & 0xf
#     s5_10= S[10] >> 4
#     s5_10b= S[10] & 0xf
#     s5_6 = S[6] >> 4
#     s5_6b = S[6] & 0xf
#     s5_14 = S[14] >> 4
#     s5_14b = S[14] & 0xf

#     s5_3 = S[3] >> 4
#     s5_3b = S[3] & 0xf
#     s5_15 = S[15] >> 4
#     s5_15b = S[15] & 0xf
#     s5_11 = S[11] >> 4
#     s5_11b = S[11] & 0xf
#     s5_7= S[7] >> 4
#     s5_7b= S[7] & 0xf

#     s5_0=S[0] >> 4
#     s5_0b=S[0] & 0xf
#     s5_4 = S[4] >> 4
#     s5_4b = S[4] & 0xf
#     s5_8 = S[8] >> 4
#     s5_8b = S[8] & 0xf
#     s5_12 = S[12] >> 4
#     s5_12b = S[12] & 0xf

#     temp = I[s5_1][s5_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s5_5][s5_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s5_9][s5_9b])
#     S = Store(S, BitVecVal(9, 8),I[s5_13][s5_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s5_2][s5_2b]
#     S = Store(S, BitVecVal(2, 8), I[s5_10][s5_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s5_6][s5_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s5_14][s5_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s5_3][s5_3b]
#     S = Store(S, BitVecVal(3, 8), I[s5_15][s5_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s5_11][s5_11b])
#     S = Store(S, BitVecVal(11, 8), I[s5_7][s5_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s5_0][s5_0b])
#     S = Store(S, BitVecVal(4, 8), I[s5_4][s5_4b])
#     S = Store(S, BitVecVal(8, 8), I[s5_8][s5_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s5_12][s5_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][20]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][20]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][20]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][20]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][21]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][21]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][21]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][21]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][22]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][22]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][22]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][22]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][23]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][23]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][23]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][23]))

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 6 -----------------------------------------------------------------------------------
#     s6_0,s6_1,s6_2,s6_3,s6_4,s6_5,s6_6,s6_7,s6_8,s6_9,s6_10,s6_11,s6_12,s6_13,s6_14,s6_15=BitVecs('s6_0 s6_1 s6_2 s6_3 s6_4 s6_5 s6_6 s6_7 s6_8 s6_9 s6_10 s6_11 s6_12 s6_13 s6_14 s6_15',8)
#     s6_0b,s6_1b,s6_2b,s6_3b,s6_4b,s6_5b,s6_6b,s6_7b,s6_8b,s6_9b,s6_10b,s6_11b,s6_12b,s6_13b,s6_14b,s6_15b=BitVecs('s6_0b s6_1b s6_2b s6_3b s6_4b s6_5b s6_6b s6_7b s6_8b s6_9b s6_10b s6_11b s6_12b s6_13b s6_14b s6_15b',8)

#     s6_1 = S[1] >> 4
#     s6_1b = S[1] & 0xf
#     s6_5 = S[5] >> 4
#     s6_5b = S[5] & 0xf
#     s6_9 = S[9] >> 4
#     s6_9b = S[9] & 0xf
#     s6_13= S[13] >> 4
#     s6_13b= S[13] & 0xf


#     s6_2 = S[2] >> 4
#     s6_2b = S[2] & 0xf
#     s6_10= S[10] >> 4
#     s6_10b= S[10] & 0xf
#     s6_6 = S[6] >> 4
#     s6_6b = S[6] & 0xf
#     s6_14 = S[14] >> 4
#     s6_14b = S[14] & 0xf

#     s6_3 = S[3] >> 4
#     s6_3b = S[3] & 0xf
#     s6_15 = S[15] >> 4
#     s6_15b = S[15] & 0xf
#     s6_11 = S[11] >> 4
#     s6_11b = S[11] & 0xf
#     s6_7= S[7] >> 4
#     s6_7b= S[7] & 0xf

#     s6_0=S[0] >> 4
#     s6_0b=S[0] & 0xf
#     s6_4 = S[4] >> 4
#     s6_4b = S[4] & 0xf
#     s6_8 = S[8] >> 4
#     s6_8b = S[8] & 0xf
#     s6_12 = S[12] >> 4
#     s6_12b = S[12] & 0xf

#     temp = I[s6_1][s6_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s6_5][s6_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s6_9][s6_9b])
#     S = Store(S, BitVecVal(9, 8),I[s6_13][s6_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s6_2][s6_2b]
#     S = Store(S, BitVecVal(2, 8), I[s6_10][s6_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s6_6][s6_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s6_14][s6_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s6_3][s6_3b]
#     S = Store(S, BitVecVal(3, 8), I[s6_15][s6_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s6_11][s6_11b])
#     S = Store(S, BitVecVal(11, 8), I[s6_7][s6_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s6_0][s6_0b])
#     S = Store(S, BitVecVal(4, 8), I[s6_4][s6_4b])
#     S = Store(S, BitVecVal(8, 8), I[s6_8][s6_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s6_12][s6_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][24]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][24]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][24]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][24]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][25]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][25]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][25]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][25]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][26]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][26]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][26]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][26]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][27]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][27]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][27]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][27]))

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 7 -----------------------------------------------------------------------------------
#     s7_0,s7_1,s7_2,s7_3,s7_4,s7_5,s7_6,s7_7,s7_8,s7_9,s7_10,s7_11,s7_12,s7_13,s7_14,s7_15=BitVecs('s7_0 s7_1 s7_2 s7_3 s7_4 s7_5 s7_6 s7_7 s7_8 s7_9 s7_10 s7_11 s7_12 s7_13 s7_14 s7_15',8)
#     s7_0b,s7_1b,s7_2b,s7_3b,s7_4b,s7_5b,s7_6b,s7_7b,s7_8b,s7_9b,s7_10b,s7_11b,s7_12b,s7_13b,s7_14b,s7_15b=BitVecs('s7_0b s7_1b s7_2b s7_3b s7_4b s7_5b s7_6b s7_7b s7_8b s7_9b s7_10b s7_11b s7_12b s7_13b s7_14b s7_15b',8)

#     s7_1 = S[1] >> 4
#     s7_1b = S[1] & 0xf
#     s7_5 = S[5] >> 4
#     s7_5b = S[5] & 0xf
#     s7_9 = S[9] >> 4
#     s7_9b = S[9] & 0xf
#     s7_13= S[13] >> 4
#     s7_13b= S[13] & 0xf


#     s7_2 = S[2] >> 4
#     s7_2b = S[2] & 0xf
#     s7_10= S[10] >> 4
#     s7_10b= S[10] & 0xf
#     s7_6 = S[6] >> 4
#     s7_6b = S[6] & 0xf
#     s7_14 = S[14] >> 4
#     s7_14b = S[14] & 0xf

#     s7_3 = S[3] >> 4
#     s7_3b = S[3] & 0xf
#     s7_15 = S[15] >> 4
#     s7_15b = S[15] & 0xf
#     s7_11 = S[11] >> 4
#     s7_11b = S[11] & 0xf
#     s7_7= S[7] >> 4
#     s7_7b= S[7] & 0xf

#     s7_0=S[0] >> 4
#     s7_0b=S[0] & 0xf
#     s7_4 = S[4] >> 4
#     s7_4b = S[4] & 0xf
#     s7_8 = S[8] >> 4
#     s7_8b = S[8] & 0xf
#     s7_12 = S[12] >> 4
#     s7_12b = S[12] & 0xf

#     temp = I[s7_1][s7_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s7_5][s7_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s7_9][s7_9b])
#     S = Store(S, BitVecVal(9, 8),I[s7_13][s7_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s7_2][s7_2b]
#     S = Store(S, BitVecVal(2, 8), I[s7_10][s7_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s7_6][s7_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s7_14][s7_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s7_3][s7_3b]
#     S = Store(S, BitVecVal(3, 8), I[s7_15][s7_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s7_11][s7_11b])
#     S = Store(S, BitVecVal(11, 8), I[s7_7][s7_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s7_0][s7_0b])
#     S = Store(S, BitVecVal(4, 8), I[s7_4][s7_4b])
#     S = Store(S, BitVecVal(8, 8), I[s7_8][s7_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s7_12][s7_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][28]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][28]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][28]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][28]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][29]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][29]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][29]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][29]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][30]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][30]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][30]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][30]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][31]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][31]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][31]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][31]))

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 8 -----------------------------------------------------------------------------------
#     s8_0,s8_1,s8_2,s8_3,s8_4,s8_5,s8_6,s8_7,s8_8,s8_9,s8_10,s8_11,s8_12,s8_13,s8_14,s8_15=BitVecs('s8_0 s8_1 s8_2 s8_3 s8_4 s8_5 s8_6 s8_7 s8_8 s8_9 s8_10 s8_11 s8_12 s8_13 s8_14 s8_15',8)
#     s8_0b,s8_1b,s8_2b,s8_3b,s8_4b,s8_5b,s8_6b,s8_7b,s8_8b,s8_9b,s8_10b,s8_11b,s8_12b,s8_13b,s8_14b,s8_15b=BitVecs('s8_0b s8_1b s8_2b s8_3b s8_4b s8_5b s8_6b s8_7b s8_8b s8_9b s8_10b s8_11b s8_12b s8_13b s8_14b s8_15b',8)

#     s8_1 = S[1] >> 4
#     s8_1b = S[1] & 0xf
#     s8_5 = S[5] >> 4
#     s8_5b = S[5] & 0xf
#     s8_9 = S[9] >> 4
#     s8_9b = S[9] & 0xf
#     s8_13= S[13] >> 4
#     s8_13b= S[13] & 0xf


#     s8_2 = S[2] >> 4
#     s8_2b = S[2] & 0xf
#     s8_10= S[10] >> 4
#     s8_10b= S[10] & 0xf
#     s8_6 = S[6] >> 4
#     s8_6b = S[6] & 0xf
#     s8_14 = S[14] >> 4
#     s8_14b = S[14] & 0xf

#     s8_3 = S[3] >> 4
#     s8_3b = S[3] & 0xf
#     s8_15 = S[15] >> 4
#     s8_15b = S[15] & 0xf
#     s8_11 = S[11] >> 4
#     s8_11b = S[11] & 0xf
#     s8_7= S[7] >> 4
#     s8_7b= S[7] & 0xf

#     s8_0=S[0] >> 4
#     s8_0b=S[0] & 0xf
#     s8_4 = S[4] >> 4
#     s8_4b = S[4] & 0xf
#     s8_8 = S[8] >> 4
#     s8_8b = S[8] & 0xf
#     s8_12 = S[12] >> 4
#     s8_12b = S[12] & 0xf

#     temp = I[s8_1][s8_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s8_5][s8_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s8_9][s8_9b])
#     S = Store(S, BitVecVal(9, 8),I[s8_13][s8_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s8_2][s8_2b]
#     S = Store(S, BitVecVal(2, 8), I[s8_10][s8_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s8_6][s8_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s8_14][s8_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s8_3][s8_3b]
#     S = Store(S, BitVecVal(3, 8), I[s8_15][s8_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s8_11][s8_11b])
#     S = Store(S, BitVecVal(11, 8), I[s8_7][s8_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s8_0][s8_0b])
#     S = Store(S, BitVecVal(4, 8), I[s8_4][s8_4b])
#     S = Store(S, BitVecVal(8, 8), I[s8_8][s8_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s8_12][s8_12b])


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


#     ret = Store(ret, 0, S[0] << 1)
#     ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
#     x = S[1]
#     x = x ^ (x << 1)
#     ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
#     ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][8]))

#     ret = Store(ret, 1 , S[1] << 1)
#     ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
#     x = S[2]
#     x = x ^ (x << 1)
#     ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
#     ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][8]))

#     ret = Store(ret, 2, S[2] << 1)
#     ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
#     x = S[3]
#     x = x ^ (x << 1)
#     ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
#     ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][8]))

#     ret = Store(ret, key5, S[3] << 1) #key5 3
#     ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
#     x = S[0]
#     x = x ^ (x << 1)
#     ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
#     ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][8]))

#     ret = Store(ret, 4, S[4] << 1)
#     ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ 283, ret[4]))
#     x = S[5]
#     x = x ^ (x << 1)
#     ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
#     ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][33]))

#     ret = Store(ret, 5,  S[key6+4] << 1) #key6 1
#     ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
#     x = S[2 + 1 * key7] #key7 4
#     x = x ^ (x << 1)
#     ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
#     ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][33]))

#     ret = Store(ret, 6,  S[6] << 1)
#     ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
#     x = S[key8 + 4] #key8 3 
#     x = x ^ (x << 1)  
#     ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
#     ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][33]))

#     ret = Store(ret, 7,  S[7] << 1)
#     ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
#     x = S[4]
#     x = x ^ (x << 1)
#     ret = Store(ret, 7, If(x >> key9 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
#     ret = Store(ret, 7, ret[7] ^ (S[5] ^ S[6] ^ W[3][33]))

#     ret = Store(ret, 8, S[8] << 1)
#     ret = Store(ret, 8, If( ret[8] >> 8 == 1, ret[8] ^ 283, ret[8]))
#     x = S[9]
#     x = x ^ (x << 1)
#     ret = Store(ret, 8, If( x >> 8 == 1, ret[8] ^ (x ^ 283), ret[8] ^ x))
#     ret = Store(ret, 8, ret[8] ^ (S[10] ^ S[11] ^ W[0][34]))

#     ret = Store(ret, 9,  S[9] << 1)
#     ret = Store(ret, 9, If( ret[9] >> 8 == 1, ret[9] ^ 283, ret[9]))
#     x = S[10]
#     x = x ^ (x << 1)
#     ret = Store(ret, 9, If( x >> 8 == 1, ret[9] ^ (x ^ 283), ret[9] ^ x))
#     ret = Store(ret, 9,  ret[9] ^ (S[11] ^ S[8] ^ W[1][34]))

#     ret = Store(ret, key10 + 8,  S[10] << 1) #key10 2
#     ret = Store(ret, 10, If(ret[10] >> 8 == 1, ret[10] ^ 283, ret[10]))
#     x = S[11]
#     x = x ^ (x << 1)
#     ret = Store(ret, 10, If( x >> 8 == 1, ret[10] ^ (x ^ 283), ret[10] ^ x))
#     ret = Store(ret, 10, ret[10] ^ (S[8] ^ S[9] ^ W[2][34]))

#     ret = Store(ret, 11,  S[11] << 1)
#     ret = Store(ret, 11, If(ret[11] >> 8 == 1, ret[11] ^ 283, ret[11]))
#     x = S[8]
#     x = x ^ (x << 1)
#     ret = Store(ret, 11, If( x >> 8 == 1, ret[11] ^ (x ^ 283), ret[11] ^ x))
#     ret = Store(ret, 11, ret[11] ^ (S[9] ^ S[10] ^ W[3][34]))
 
#     ret = Store(ret, 12, S[12] << 1)
#     ret = Store(ret, 12, If(ret[12] >> 8 == 1, ret[12] ^ 283, ret[12]))
#     x = S[13]
#     x = x ^ (x << 1)
#     ret = Store(ret, 12, If(x >> 8 == 1, ret[12] ^ (x ^ 283), ret[12] ^ x))
#     ret = Store(ret, 12, ret[12] ^ (S[14] ^ S[15] ^ W[0][35]))

#     ret = Store(ret, 13,  S[13] << 1)
#     ret = Store(ret, 13, If(ret[13] >> 8 == 1, ret[13] ^ 283, ret[13]))
#     x = S[14]
#     x = x ^ (x << 1)
#     ret = Store(ret, 13, If( x >> 8 == 1, ret[13] ^ (x ^ 283), ret[13] ^ x)) 
#     ret = Store(ret, 13, ret[13] ^ (S[15] ^ S[12] ^ W[1][35]))

#     ret = Store(ret, 14, S[14] << 1)
#     ret = Store(ret, 14, If(ret[14] >> 8 == 1, ret[14] ^ 283, ret[14]))
#     x = S[15]
#     x = x ^ (x << 1)
#     ret = Store(ret, 14, If( x >> 8 == 1, ret[14] ^ (x ^ 283), ret[14] ^ x))
#     ret = Store(ret, 14,  ret[14] ^ (S[12] ^ S[13] ^ W[2][35]))

#     ret = Store(ret, 15, S[15] << 1)
#     ret = Store(ret, 15, If(ret[15] >> 8 == 1, ret[15] ^ 283, ret[15]))
#     x = S[12]
#     x = x ^ (x << 1)
#     ret = Store(ret, 15, If( x >> 8 == 1, ret[15] ^ (x ^ 283), ret[15] ^ x))
#     ret = Store(ret, 15, ret[15] ^ (S[13] ^ S[14] ^ W[3][35]))

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])


# #---------------------------------Iteration 9 -----------------------------------------------------------------------------------
#     s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',8)
#     s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',8)

#     s9_1 = S[1] >> 4
#     s9_1b = S[1] & 0xf
#     s9_5 = S[5] >> 4
#     s9_5b = S[5] & 0xf
#     s9_9 = S[9] >> 4
#     s9_9b = S[9] & 0xf
#     s9_13= S[13] >> 4
#     s9_13b= S[13] & 0xf


#     s9_2 = S[2] >> 4
#     s9_2b = S[2] & 0xf
#     s9_10= S[10] >> 4
#     s9_10b= S[10] & 0xf
#     s9_6 = S[6] >> 4
#     s9_6b = S[6] & 0xf
#     s9_14 = S[14] >> 4
#     s9_14b = S[14] & 0xf

#     s9_3 = S[3] >> 4
#     s9_3b = S[3] & 0xf
#     s9_15 = S[15] >> 4
#     s9_15b = S[15] & 0xf
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


#     # ------------------------ MixColumn AddRoundKey ---------------------------------


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

#     S = Store(S, BitVecVal(0,8), ret[0])
#     S = Store(S, BitVecVal(1,8), ret[1])
#     S = Store(S, BitVecVal(2,8), ret[2])
#     S = Store(S, BitVecVal(3,8), ret[3])
#     S = Store(S, BitVecVal(4,8), ret[4])
#     S = Store(S, BitVecVal(5,8), ret[5])
#     S = Store(S, BitVecVal(6,8), ret[6])
#     S = Store(S, BitVecVal(7,8), ret[7])
#     S = Store(S, BitVecVal(8,8), ret[8])
#     S = Store(S, BitVecVal(9,8), ret[9])
#     S = Store(S, BitVecVal(10,8), ret[10])
#     S = Store(S, BitVecVal(11,8), ret[11])
#     S = Store(S, BitVecVal(12,8), ret[12])
#     S = Store(S, BitVecVal(13,8), ret[13])
#     S = Store(S, BitVecVal(14,8), ret[14])
#     S = Store(S, BitVecVal(15,8), ret[15])

# #--------------------------------ByteSub_ShiftRow----------------------------------------------------------
    
#     s10_0,s10_1,s10_2,s10_3,s10_4,s10_5,s10_6,s10_7,s10_8,s10_9,s10_10,s10_11,s10_12,s10_13,s10_14,s10_15=BitVecs('s10_0 s10_1 s10_2 s10_3 s10_4 s10_5 s10_6 s10_7 s10_8 s10_9 s10_10 s10_11 s10_12 s10_13 s10_14 s10_15',8)
#     s10_0b,s10_1b,s10_2b,s10_3b,s10_4b,s10_5b,s10_6b,s10_7b,s10_8b,s10_9b,s10_10b,s10_11b,s10_12b,s10_13b,s10_14b,s10_15b=BitVecs('s10_0b s10_1b s10_2b s10_3b s10_4b s10_5b s10_6b s10_7b s10_8b s10_9b s10_10b s10_11b s10_12b s10_13b s10_14b s10_15b',8)

#     s10_1 = S[1] >> 4
#     s10_1b = S[1] & 0xf
#     s10_5 = S[5] >> 4
#     s10_5b = S[5] & 0xf
#     s10_9 = S[9] >> 4
#     s10_9b = S[9] & 0xf
#     s10_13= S[13] >> 4
#     s10_13b= S[13] & 0xf


#     s10_2 = S[2] >> 4
#     s10_2b = S[2] & 0xf
#     s10_10= S[10] >> 4
#     s10_10b= S[10] & 0xf
#     s10_6 = S[6] >> 4
#     s10_6b = S[6] & 0xf
#     s10_14 = S[14] >> 4
#     s10_14b = S[14] & 0xf

#     s10_3 = S[3] >> 4
#     s10_3b = S[3] & 0xf
#     s10_15 = S[15] >> 4
#     s10_15b = S[15] & 0xf
#     s10_11 = S[11] >> 4
#     s10_11b = S[11] & 0xf
#     s10_7= S[7] >> 4
#     s10_7b= S[7] & 0xf

#     s10_0=S[0] >> 4
#     s10_0b=S[0] & 0xf
#     s10_4 = S[4] >> 4
#     s10_4b = S[4] & 0xf
#     s10_8 = S[8] >> 4
#     s10_8b = S[8] & 0xf
#     s10_12 = S[12] >> 4
#     s10_12b = S[12] & 0xf

#     temp = I[s10_1][s10_1b] 
#     S = Store(S, BitVecVal(1, 8),I[s10_5][s10_5b]) #key1=5
#     S = Store(S, BitVecVal(5, 8),I[s10_9][s10_9b])
#     S = Store(S, BitVecVal(9, 8),I[s10_13][s10_13b])
#     S = Store(S, BitVecVal(13, 8),temp)

#     temp = I[s10_2][s10_2b]
#     S = Store(S, BitVecVal(2, 8), I[s10_10][s10_10b]) #key2=10
#     S = Store(S, BitVecVal(10, 8), temp)
#     temp = I[s10_6][s10_6b] 
#     S = Store(S, BitVecVal(6, 8), I[s10_14][s10_14b])
#     S = Store(S, BitVecVal(14, 8),temp)

#     temp = I[s10_3][s10_3b]
#     S = Store(S, BitVecVal(3, 8), I[s10_15][s10_15b]) #key3=15
#     S = Store(S, BitVecVal(15, 8), I[s10_11][s10_11b])
#     S = Store(S, BitVecVal(11, 8), I[s10_7][s10_7b]) 
#     S = Store(S, BitVecVal(7, 8), temp)

#     S = Store(S, BitVecVal(0, 8), I[s10_0][s10_0b])
#     S = Store(S, BitVecVal(4, 8), I[s10_4][s10_4b])
#     S = Store(S, BitVecVal(8, 8), I[s10_8][s10_8b]) 
#     S = Store(S, BitVecVal(12, 8),I[s10_12][s10_12b])

# # ----------------------------------AddroundKey-----------------------------------------------------------------


#     S = Store(S, 0 , S[0]^W[0][40])
#     S = Store(S, 1 , S[1]^W[1][40])
#     S = Store(S, 2 , S[2]^W[2][40])
#     S = Store(S, 3 , S[3]^W[3][40])

#     S = Store(S, 4 , S[4]^W[0][41])
#     S = Store(S, 5 , S[5]^W[1][41])
#     S = Store(S, 6 , S[6]^W[2][41])
#     S = Store(S, 7 , S[7]^W[3][41])

#     S = Store(S, 8 , S[8]^W[0][42])
#     S = Store(S, 9 , S[9]^W[1][42])
#     S = Store(S, 10 , S[10]^W[2][42])
#     S = Store(S, 11 , S[11]^W[3][42])

#     S = Store(S, 12 , S[12]^W[0][43])
#     S = Store(S, 13 , S[13]^W[1][43])
#     S = Store(S, 14 , S[14]^W[2][43])
#     S = Store(S, 15 , S[15]^W[3][43])

#-------------------------------------------------------------------------------------------------------------------------
    o0 = S[0]
    o1 = S[1]
    o2 = S[2]
    o3 = S[3]
    o4 = S[4]
    o5 = S[5] 
    o6 = S[6]
    o7 = S[7]
    o8 = S[8] 
    o9 = S[9]
    o10 = S[10]
    o11 = S[11]
    o12 = S[12]
    o13 = S[13]
    o14 = S[14]
    o15 = S[15]
    #return o5
    return tuple.tuple1(o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15)
    # return S




# gg = Tactic('smt').solver()
# # statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
# ia = str(50)+" "+str(67)+" "+str(246)+" "+str(168)+" "+str(136)+" "+str(90)+" "+str(48)+" "+str(141)+" "+str(49)+" "+str(49)+" "+str(152)+" "+str(162)+" "+str(224)+" "+str(55)+" "+str(7)+" "+str(52)
# [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
# BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8)
# oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))
# print(gg.check(simplify(findOutput1(5,10,15,283,3,1,4,3,8,2))==oa))
#print(gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(oa6,8)))
# print(oa5)
# for jj in range(0,512):
#     if (gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(jj,8))) == sat:
#         print(jj)

#4,6,7,8,9,10,
'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))'''



j = 0


s = Tactic('smt').solver()

#s.add(simplify(findOutput(i1,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)) == out1)
#s.add(simplify(findOutput(i1,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)) == out2)

#o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
#o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)
'''s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1))==out3)
s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2))==out4)'''
s.add(key1_1>=0,key1_1<=15)
s.add(key1_2>=0,key1_2<=15)
s.add(key2_1>=0,key2_1<=15)
s.add(key2_2>=0,key2_2<=15)
s.add(key3_1>=0,key3_1<=15)
s.add(key3_2>=0,key3_2<=15)
s.add(key4_1>=0,key4_1<=511)
s.add(key4_2>=0,key4_2<=511)
s.add(key5_1>=0,key5_1<=3)
s.add(key5_2>=0,key5_2<=3)
s.add(key6_1>=0,key6_1<=11)
s.add(key6_2>=0,key6_2<=11)
s.add(key7_1>=0,key7_1<=13)
s.add(key7_2>=0,key7_2<=13)
s.add(key8_1>=0,key8_1<=11)
s.add(key8_2>=0,key8_2<=11)
s.add(key9_1>=0,key9_1<=31)
s.add(key9_2>=0,key9_2<=31)
s.add(key10_1>=0,key10_1<=7)
s.add(key10_2>=0,key10_2<=7)
s.add(i1>=0,i1<=255)
s.add(i2>=0,i2<=255)
s.add(i3>=0,i3<=255)
s.add(i4>=0,i4<=255)
s.add(i5>=0,i5<=255)
s.add(i6>=0,i6<=255)
s.add(i7>=0,i7<=255)
s.add(i8>=0,i8<=255)
s.add(i9>=0,i9<=255)
s.add(i10>=0,i10<=255)
s.add(i11>=0,i11<=255)
s.add(i12>=0,i12<=255)
s.add(i13>=0,i13<=255)
s.add(i14>=0,i14<=255)
s.add(i15>=0,i15<=255)
s.add(i16>=0,i16<=255)







pos_set = set()
print("loop1 enter")
# s.check()
# print(s.model())
#print(s.check(out1 != out2, Or(k1_1 != k1_2,k2_1 != k2_2 , k3_1 != k3_2 ,k4_1 != k4_2,k5_1 != k5_2 ,key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2)))

start=time.time()
# statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
ia = str(50)+" "+str(67)+" "+str(246)+" "+str(168)+" "+str(136)+" "+str(90)+" "+str(48)+" "+str(141)+" "+str(49)+" "+str(49)+" "+str(152)+" "+str(162)+" "+str(224)+" "+str(55)+" "+str(7)+" "+str(52)
# ia = str(176)+" "+str(180)+" "+str(2)+" "+str(240)+" "+str(18)+" "+str(2)+" "+str(18)+" "+str(57)+" "+str(1)+" "+str(5)+" "+str(37)+" "+str(5)+" "+str(140)+" "+str(156)+" "+str(156)+" "+str(210)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))
oa = simplify(findOutput1(5,10,15,283,3,1,4,3,8,2))
# for i in range(16):
print(oa)
# print(s.check())
# print(s.check(simplify(findOutput1(5,10,15,283,3,1,4,3,8,2))==oa))
exit()
s.add(simplify(findOutput1(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1))==oa)
s.add(simplify(findOutput1(key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2))==oa)
print(s.check())

'''if s.check(out3!=out4,Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1!=key4_2,key5_1!=key5_2,key6_1!=key6_2,key7_1!=key7_2,key8_1!=key8_2,key9_1!=key9_2,key10_1!=key10_2)) == sat:
    m = s.model()
    #print(m)
    #print(m)
    print(str(m[i1])+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16]))
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2]))
    # ia = str(m[i1])#+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16])
    # [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    # #,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
    # oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))
    # s.add(simplify(findOutput(m[i1],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)) == oa)
    # s.add(simplify(findOutput(m[i1],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)) == oa)
    # o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1=findOutput(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
    # o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2=findOutput(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)
    # s.add(o0_1==oa1,o1_1==oa2,o2_1==oa3,o3_1==oa4,o4_1==oa5,o5_1==oa6,o6_1==oa7,o7_1==oa8,o8_1==oa9,o9_1==oa10,o10_1==oa11,o11_1==oa12,o12_1==oa13,o13_1==oa14,o14_1==oa15,o15_1==oa16)
    # s.add(o0_2==oa1,o1_2==oa2,o2_2==oa3,o3_2==oa4,o4_2==oa5,o5_2==oa6,o6_2==oa7,o7_2==oa8,o8_2==oa9,o9_2==oa10,o10_2==oa11,o11_2==oa12,o12_2==oa13,o13_2==oa14,o14_2==oa15,o15_2==oa16)
    print("Iteration %d = %f second" %(j+1,time.time()-start))
    j = j + 1
print("unsat takes %d time" %(time.time()-start))
print("loop1 complete")'''


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


'''pos_l = list(pos_set)

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
        oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))
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

print("Computation took %d iterations and %f seconds." % (j, taken))  '''    

