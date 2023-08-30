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
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',32)
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1',32)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2',32)
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16=BitVecs('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16',32)
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',32)
oo0_2,oo1_2,oo2_2,oo3_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2',32)
'''k1_1,k2_1,k3_1,k4_1,k5_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1')
k1_2,k2_2,k3_2,k4_2,k5_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2')'''
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 32)
inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16 = BitVecs('inp1 inp2 inp3 inp4 inp5 inp6 inp7 inp8 inp9 inp10 inp11 inp12 inp13 inp14 inp15 inp16',32)


tuple = Datatype('tuple')
tuple.declare('tuple1',('1' , BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)),('5' , BitVecSort(32)),('6' , BitVecSort(32)),('7' , BitVecSort(32)),('8' , BitVecSort(32)),('9' , BitVecSort(32)),('10' , BitVecSort(32)),('11' , BitVecSort(32)),('12' , BitVecSort(32)),('13' , BitVecSort(32)),('14' , BitVecSort(32)),('15' , BitVecSort(32)),('16' , BitVecSort(32)))
tuple.declare('tuple2',('1' , BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)))#,('5' , BitVecSort(32)),('6' , BitVecSort(32)),('7' , BitVecSort(32)),('8' , BitVecSort(32)),('9' , BitVecSort(32)),('10' , BitVecSort(32)),('11' , BitVecSort(32)),('12' , BitVecSort(32)),('13' , BitVecSort(32)),('14' , BitVecSort(32)),('15' , BitVecSort(32)),('16' , BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 32


Sbox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

#last element changed to 0x20 from 0x16

word = [[43,40,171,9,160,136,35,42,242,122,89,115,61,71,30,109,239,168,182,219,212,124,202,17,109,17,219,202,78,95,132,78,234,181,49,127,172,25,40,87,208,201,225,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[126,174,247,207,250,84,163,108,194,150,53,89,128,22,35,122,68,82,113,11,209,131,242,249,136,11,249,0,84,95,166,166,210,141,43,141,119,250,209,92,20,238,63,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[21,210,21,79,254,44,57,118,149,185,128,246,71,254,126,136,165,91,37,173,198,157,184,21,163,62,134,147,247,201,79,220,115,186,245,41,102,220,41,0,249,37,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[22,166,136,60,23,177,57,5,242,67,122,127,125,62,68,59,65,127,59,0,248,135,188,188,122,253,65,253,14,243,178,79,33,210,96,47,243,33,65,110,168,137,200,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10
def findOutput1(inp3,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    S2 = Array('S2', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    for i in range(16):
        ret = Store(ret,i,0)

    statemt = [73,91,20,4,9,16,0,13,4,13,46,0,15,6,9,19]

    S = Store(S,BitVecVal(0,32),BitVecVal(statemt[0],32))
    S = Store(S,BitVecVal(1,32),BitVecVal(statemt[1],32))
    S = Store(S,BitVecVal(2,32),BitVecVal(statemt[2],32))
    S = Store(S,BitVecVal(3,32),BitVecVal(statemt[3],32))
    S = Store(S,BitVecVal(4,32),BitVecVal(statemt[4],32))
    S = Store(S,BitVecVal(5,32),BitVecVal(statemt[5],32))
    S = Store(S,BitVecVal(6,32),BitVecVal(statemt[6],32))
    S = Store(S,BitVecVal(7,32),BitVecVal(statemt[7],32))
    S = Store(S,BitVecVal(8,32),BitVecVal(statemt[8],32))
    S = Store(S,BitVecVal(9,32),BitVecVal(statemt[9],32))
    S = Store(S,BitVecVal(10,32),BitVecVal(statemt[10],32))
    S = Store(S,BitVecVal(11,32),BitVecVal(statemt[11],32))
    S = Store(S,BitVecVal(12,32),BitVecVal(statemt[12],32))
    S = Store(S,BitVecVal(13,32),BitVecVal(statemt[13],32))
    S = Store(S,BitVecVal(14,32),BitVecVal(statemt[14],32))
    S = Store(S,BitVecVal(15,32),BitVecVal(statemt[5],32))
    
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
    
    S = Store(S,BitVecVal(0,32),BitVecVal(98,32))
    S = Store(S,BitVecVal(1,32),BitVecVal(37,32))
    S = Store(S,BitVecVal(2,32),BitVecVal(1,32))
    S = Store(S,BitVecVal(3,32),BitVecVal(18,32))
    S = Store(S,BitVecVal(4,32),BitVecVal(33,32))
    S = Store(S,BitVecVal(5,32),BitVecVal(190,32))
    S = Store(S,BitVecVal(6,32),BitVecVal(210,32))
    S = Store(S,BitVecVal(7,32),BitVecVal(171,32))
    S = Store(S,BitVecVal(8,32),BitVecVal(175,32))
    S = Store(S,BitVecVal(9,32),BitVecVal(250,32))
    S = Store(S,BitVecVal(10,32),BitVecVal(59,32))
    S = Store(S,BitVecVal(11,32),BitVecVal(136,32))
    S = Store(S,BitVecVal(12,32),BitVecVal(6,32))
    S = Store(S,BitVecVal(13,32),BitVecVal(201,32))
    S = Store(S,BitVecVal(14,32),BitVecVal(70,32))
    S = Store(S,BitVecVal(15,32),BitVecVal(47,32))
    # for i in range(16):
    #     print(simplify(Select(S,i)))
    # print("------------")

# --------------------------------Iteration 1 ----------------------------------------------------------------------------------

    # for i in range(15):
    #     print(simplify(Select(S,i)))
    # print("------------")
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    # print(simplify(I[s9_5][s9_5b]))
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

    # for i in range(15):
    #     print(simplify(Select(S,i)))

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 2-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

# #-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(2,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

# #----------------------------------Iteration 3-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(3,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 4-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(4,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 5-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(5,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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



# --------------------------------Iteration 6 ----------------------------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(6,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 7-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(7,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 8-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(8,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------Iteration 9-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(9,32)
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
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[key5] << 1) #key5 3
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

    ret = Store(ret, 5,  S[key6] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[key8] #key8 7 
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

    ret = Store(ret, 10,  S[key10] << 1) #key10 10
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

#----------------------------------ByteshiftRow--------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[key1] >> 4
    s9_5b = S[key1] & 0xf
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])
    

#----------------------------------AddroundKey-----------------------------------------------------------------


    S = Store(S, 0 , S[0]^W[0][40])
    S = Store(S, 1 , S[1]^W[1][40])
    S = Store(S, 2 , S[2]^W[2][40])
    S = Store(S, 3 , S[3]^W[3][40])

    S = Store(S, 4 , S[4]^W[0][41])
    S = Store(S, 5 , S[5]^W[1][41])
    S = Store(S, 6 , S[6]^W[2][41])
    S = Store(S, 7 , S[7]^W[3][41])

    S = Store(S, 8 , S[8]^W[0][42])
    S = Store(S, 9 , S[9]^W[1][42])
    S = Store(S, 10 , S[10]^W[2][42])
    S = Store(S, 11 , S[11]^W[3][42])

    S = Store(S, 12 , S[12]^W[0][43])
    S = Store(S, 13 , S[13]^W[1][43])
    S = Store(S, 14 , S[14]^W[2][43])
    S = Store(S, 15 , S[15]^W[3][43])

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


def sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1,key2,key3,key4,key5):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    S2 = Array('S2', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))

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
    
    S = Store(S,BitVecVal(0,32),i1)
    S = Store(S,BitVecVal(1,32),i2)
    S = Store(S,BitVecVal(2,32),i3)
    S = Store(S,BitVecVal(3,32),i4)
    S = Store(S,BitVecVal(4,32),i5)
    S = Store(S,BitVecVal(5,32),i6)
    S = Store(S,BitVecVal(6,32),i7)
    S = Store(S,BitVecVal(7,32),i8)
    S = Store(S,BitVecVal(8,32),i9)
    S = Store(S,BitVecVal(9,32),i10)
    S = Store(S,BitVecVal(10,32),i11)
    S = Store(S,BitVecVal(11,32),i12)
    S = Store(S,BitVecVal(12,32),i13)
    S = Store(S,BitVecVal(13,32),i14)
    S = Store(S,BitVecVal(14,32),i15)
    S = Store(S,BitVecVal(15,32),i16)

    # ------------------ Add Round Key ----------------
    n=BitVecVal(0,32)
    nb=BitVecVal(4,32)

    # S = Store(S,BitVecVal(0,32),BitVecVal(25,32))
    # S = Store(S,BitVecVal(1,32),BitVecVal(83,32))
    # S = Store(S,BitVecVal(2,32),BitVecVal(16,32))
    # S = Store(S,BitVecVal(3,32),S[3]^W[3][0])
    # S = Store(S,BitVecVal(4,32),BitVecVal(63,32))
    # S = Store(S,BitVecVal(5,32),BitVecVal(244,32))
    # S = Store(S,BitVecVal(6,32),BitVecVal(169,32))
    # S = Store(S,BitVecVal(7,32),BitVecVal(160,32))
    # S = Store(S,BitVecVal(8,32),BitVecVal(191,32))
    # S = Store(S,BitVecVal(9,32),BitVecVal(178,32))
    # S = Store(S,BitVecVal(10,32),BitVecVal(25,32))
    # S = Store(S,BitVecVal(11,32),BitVecVal(190,32))
    # S = Store(S,BitVecVal(12,32),BitVecVal(80,32))
    # S = Store(S,BitVecVal(13,32),BitVecVal(226,32))
    # S = Store(S,BitVecVal(14,32),BitVecVal(1,32))
    # S = Store(S,BitVecVal(15,32),BitVecVal(102,32))

    S = Store(S, 0 , S[0]^W[0][0])
    S = Store(S, 1 , S[1]^W[1][0])
    S = Store(S, 2 , S[2]^W[2][0])
    S = Store(S, 3 , S[3]^W[3][0])

    S = Store(S, 4 , S[4]^W[0][1])
    S = Store(S, 5 , S[5]^W[1][1])
    S = Store(S, 6 , S[6]^W[2][1])
    S = Store(S, 7 , S[7]^W[3][1])

    S = Store(S, 8 , S[8]^W[0][2])
    S = Store(S, 9 , S[9]^W[1][2])
    S = Store(S, 10 , S[10]^W[2][2])
    S = Store(S, 11 , S[11]^W[3][2])

    S = Store(S, 12 , S[12]^W[0][3])
    S = Store(S, 13 , S[13]^W[1][3])
    S = Store(S, 14 , S[14]^W[2][3])
    S = Store(S, 15 , S[15]^W[3][3])


    # --------------------------------Iteration 1 ----------------------------------------------------------------------------------
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',32)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',32)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[key1] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[10] >> 4
    s9_10b= S[key2] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[15] >> 4
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
    S = Store(S, BitVecVal(1, 32),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 32),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 32), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s9_6][s9_6b] 
    S = Store(S, BitVecVal(6, 32), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 32), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 32), I[s9_7][s9_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 32), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 32), I[s9_8][s9_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s9_12][s9_12b])


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    for i in range(16):
        ret = Store(ret,i,0)
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    nb = BitVecVal(4,32)
    n = BitVecVal(1,32)

    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x)) #key4 283
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    o1=ret[0]
    o2=ret[1]
    o3=ret[2]
    o4=ret[3]
    return tuple.tuple2(o1,o2,o3,o4)


#key1 = 5, key2 = 10 , key3 = 15 , key4 = 283 , key5 = 3 , key6 = 5 , key7 = 4 , key8 = 7 , key9 = 8 , key10 = 10

'''gg = Tactic('smt').solver()
ia = str(176)+" "+str(180)+" "+str(2)+" "+str(240)+" "+str(18)+" "+str(2)+" "+str(18)+" "+str(57)+" "+str(1)+" "+str(5)+" "+str(37)+" "+str(5)+" "+str(140)+" "+str(156)+" "+str(156)+" "+str(210)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
print(gg.check(simplify(findOutput1(5,10,15,283,3,1,4,3,8,2))==oa))'''
#print(gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(oa6,32)))
# print(oa5)
# for jj in range(0,512):
#     if (gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(jj,32))) == sat:
#         print(jj)

#4,6,7,8,9,10,
'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))'''



j = 0


s = Tactic('smt').solver()

#s.add(simplify(findOutput(i1,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)) == out1)
#s.add(simplify(findOutput(i1,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)) == out2)

#o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
#o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)
'''s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1))==out3)
s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2))==out4)'''

#key1 = 5, key2 = 10 , key3 = 15 , key4 = 283 , key5 = 3 , key6 = 5 , key7 = 4 , key8 = 7 , key9 = 8 , key10 = 10
s.add(key1_1>=0,key1_1<=15)
s.add(key1_2>=0,key1_2<=15)
s.add(key2_1>=0,key2_1<=15)
s.add(key2_2>=0,key2_2<=15)
s.add(key3_1>=0,key3_1<=15)
s.add(key3_2>=0,key3_2<=15)
s.add(key4_1>=0,key4_1<=511)
s.add(key4_2>=0,key4_2<=511)
s.add(key5_1>=0,key5_1<=10)
s.add(key5_2>=0,key5_2<=10)
s.add(key6_1>=0,key6_1<=11)
s.add(key6_2>=0,key6_2<=11)
s.add(key7_1>=0,key7_1<=13)
s.add(key7_2>=0,key7_2<=13)
s.add(key8_1>=0,key8_1<=11)
s.add(key8_2>=0,key8_2<=11)
s.add(key9_1>=0,key9_1<=31)
s.add(key9_2>=0,key9_2<=31)
s.add(key10_1>=0,key10_1<=10)
s.add(key10_2>=0,key10_2<=10)
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



# ia = str(50)+" "+str(67)+" "+str(246)+" "+str(168)+" "+str(136)+" "+str(90)+" "+str(48)+" "+str(141)+" "+str(49)+" "+str(49)+" "+str(152)+" "+str(162)+" "+str(224)+" "+str(55)+" "+str(7)+" "+str(52)
# ia = str(176)+" "+str(180)+" "+str(2)+" "+str(240)+" "+str(18)+" "+str(2)+" "+str(18)+" "+str(57)+" "+str(1)+" "+str(5)+" "+str(37)+" "+str(5)+" "+str(140)+" "+str(156)+" "+str(156)+" "+str(210)
# [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
# oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
# S = findOutput1(inp3,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
# for i in range(16):
#     print(simplify(Select(S,i)).sexpr())
# print(s.check())
# print((simplify(findOutput1(6,5,10,15,283,3,5,4,7,8,10))))
# exit()

# s.add(simplify(findOutput1(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1))==out1)
# s.add(simplify(findOutput1(key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2))==out2)
# statemt = [50,45,5,6,23,90,123,6,20,69,12,54,89,45,78,90]


# print(simplify(sub(50,45,5,6,23,90,123,6,20,69,12,54,89,45,78,90,5,1,15,283,3)))
# print(simplify(sub(50,45,5,6,23,90,123,6,20,69,12,54,89,45,78,90,1,10,5,283,2)))


# s.add(simplify(sub(50,45,5,6,23,90,123,6,20,69,12,54,89,45,78,90,5,1,15,283,3) == out1))
# s.add(simplify(sub(50,45,5,1,23,90,123,6,20,69,12,54,89,45,78,90,5,1,15,283,3) == out2))



# s.add(simplify(sub(50,45,5,inp3,23,90,123,6,20,69,12,54,89,45,78,90,key1_1,key2_1,key3_1,key4_1,key5_1) == out1))
# s.add(simplify(sub(50,45,5,inp3,23,90,123,6,20,69,12,54,89,45,78,90,key1_2,key2_2,key3_2,key4_2,key5_2) == out2))

s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1))==out3)
s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2))==out4)

# print(s.check(out3 != out4))
if(s.check(out3 != out4) == sat):
    m = s.model()
    print(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16])


