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
nb,n = BitVecs('nb n',8)
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1,o17_1,o18_1,o19_1,o20_1,o21_1,o22_1,o23_1,o24_1,o25_1,o26_1,o27_1,o28_1,o29_1,o30_1,o31_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1 o16_1 o17_1 o18_1 o19_1 o20_1 o21_1 o22_1 o23_1 o24_1 o25_1 o26_1 o27_1 o28_1 o29_1 o30_1 o31_1',8)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2,o17_2,o18_2,o19_2,o20_2,o21_2,o22_2,o23_2,o24_2,o25_2,o26_2,o27_2,o28_2,o29_2,o30_2,o31_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2 o16_2 o17_2 o18_2 o19_2 o20_2 o21_2 o22_2 o23_2 o24_2 o25_2 o26_2 o27_2 o28_2 o29_2 o30_2 o31_2',8)
oo0_1,oo1_1,oo2_1,oo3_1,oo4_1,oo5_1,oo6_1,oo7_1,oo8_1,oo9_1,oo10_1,oo11_1,oo12_1,oo13_1,oo14_1,oo15_1,oo16_1,oo17_1,oo18_1,oo19_1,oo20_1,oo21_1,oo22_1,oo23_1,oo24_1,oo25_1,oo26_1,oo27_1,oo28_1,oo29_1,oo30_1,oo31_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1 oo4_1 oo5_1 oo6_1 oo7_1 oo8_1 oo9_1 oo10_1 oo11_1 oo12_1 oo13_1 oo14_1 oo15_1 oo16_1 oo17_1 oo18_1 oo19_1 oo20_1 oo21_1 oo22_1 oo23_1 oo24_1 oo25_1 oo26_1 oo27_1 oo28_1 oo29_1 oo30_1 oo31_1',8)
oo0_2,oo1_2,oo2_2,oo3_2,oo4_2,oo5_2,oo6_2,oo7_2,oo8_2,oo9_2,oo10_2,oo11_2,oo12_2,oo13_2,oo14_2,oo15_2,oo16_2,oo17_2,oo18_2,oo19_2,oo20_2,oo21_2,oo22_2,oo23_2,oo24_2,oo25_2,oo26_2,oo27_2,oo28_2,oo29_2,oo30_2,oo31_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2 oo4_2 oo5_2 oo6_2 oo7_2 oo8_2 oo9_2 oo10_2 oo11_2 oo12_2 oo13_2 oo14_2 oo15_2 oo16_2 oo17_2 oo18_2 oo19_2 oo20_2 oo21_2 oo22_2 oo23_2 oo24_2 oo25_2 oo26_2 oo27_2 oo28_2 oo29_2 oo30_2 oo31_2',8)
k1_1,k2_1,k3_1,k4_1,k5_1 = BitVecs('k1_1 k2_1 k3_1 k4_1 k5_1',8)
k1_2,k2_2,k3_2,k4_2,k5_2 = BitVecs('k1_2 k2_2 k3_2 k4_2 k5_2',8)
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 8)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 8)

tuple = Datatype('tuple')
tuple.declare('tuple1',('1' , BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)),('5' , BitVecSort(8)),('6' , BitVecSort(8)),('7' , BitVecSort(8)),('8' , BitVecSort(8)),('9' , BitVecSort(8)),('10' , BitVecSort(8)),('11' , BitVecSort(8)),('12' , BitVecSort(8)),('13' , BitVecSort(8)),('14' , BitVecSort(8)),('15' , BitVecSort(8)),('16' , BitVecSort(8)))#,('17' , BitVecSort(8)),('18' , BitVecSort(8)),('19' , BitVecSort(8)),('20' , BitVecSort(8)),('21' , BitVecSort(8)),('22' , BitVecSort(8)),('23' , BitVecSort(8)),('24' , BitVecSort(8)),('25' , BitVecSort(8)),('26' , BitVecSort(8)),('27' , BitVecSort(8)),('28' , BitVecSort(8)),('29' , BitVecSort(8)),('30' , BitVecSort(8)),('31' , BitVecSort(8)),('8' , BitVecSort(8)))
tuple.declare('tuple2',('1', BitVecSort(8)),('2' , BitVecSort(8)),('3' , BitVecSort(8)),('4' , BitVecSort(8)))#,('37' , BitVecSort(8)),('38' , BitVecSort(8)),('39' , BitVecSort(8)),('40' , BitVecSort(8)),('41', BitVecSort(8)),('42' , BitVecSort(8)),('43' , BitVecSort(8)),('44' , BitVecSort(8)),('45' , BitVecSort(8)),('46' , BitVecSort(8)),('47' , BitVecSort(8)),('48' , BitVecSort(8)),('49', BitVecSort(8)),('50' , BitVecSort(8)),('51' , BitVecSort(8)),('52' , BitVecSort(8)),('53' , BitVecSort(8)),('54' , BitVecSort(8)),('55' , BitVecSort(8)),('56' , BitVecSort(8)),('57', BitVecSort(8)),('58' , BitVecSort(8)),('59' , BitVecSort(8)),('60' , BitVecSort(8)),('61' , BitVecSort(8)),('62' , BitVecSort(8)),('63' , BitVecSort(8)),('64' , BitVecSort(8)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)#,o16_1,o17_1,o18_1,o19_1,o20_1,o21_1,o22_1,o23_1,o24_1,o25_1,o26_1,o27_1,o28_1,o29_1,o30_1,o31_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)#,o16_1,o17_2,o18_2,o19_2,o20_2,o21_2,o22_2,o23_2,o24_2,o25_2,o26_2,o27_2,o28_2,o29_2,o30_2,o31_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)#,oo3_1,oo4_1,oo5_1,oo6_1,oo7_1,oo8_1,oo9_1,oo10_1,oo11_1,oo12_1,oo13_1,oo14_1,oo15_1,oo16_1,oo17_1,oo18_1,oo19_1,oo20_1,oo21_1,oo22_1,oo23_1,oo24_1,oo25_1,oo26_1,oo27_1,oo28_1,oo29_1,oo30_1,oo31_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)#,oo3_2)#,oo4_2,oo5_2,oo6_2,oo7_2,oo8_2,oo9_2,oo10_2,oo11_2,oo12_2,oo13_2,oo14_2,oo15_2,oo16_2,oo17_2,oo18_2,oo19_2,oo20_2,oo21_2,oo22_2,oo23_2,oo24_2,oo25_2,oo26_2,oo27_2,oo28_2,oo29_2,oo30_2,oo31_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 8

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

word = [[43,40,171,9,160,136,35,42,242,122,89,115,61,71,30,109,239,168,182,219,212,124,202,17,109,17,219,202,78,95,18,78,234,181,49,127,172,25,40,87,208,201,225,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[126,174,247,207,250,84,163,108,194,150,53,89,128,22,35,122,68,82,113,11,209,131,242,249,136,11,249,0,84,95,166,166,210,141,43,141,119,250,209,92,20,238,63,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[21,210,21,79,254,44,57,118,149,185,128,246,71,254,126,136,165,91,37,173,198,157,184,21,163,62,134,147,247,201,79,220,115,186,245,41,102,220,41,0,249,37,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[22,166,136,60,23,177,57,5,242,67,122,127,125,62,68,59,65,127,59,0,248,135,188,188,122,253,65,253,14,243,178,79,33,210,96,47,243,33,65,110,168,137,200,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

S = Array('S', BitVecSort(8), BitVecSort(8))
I = Array('A', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
tm = Array('tm', BitVecSort(8), BitVecSort(8))


def findOutput(key1,key2,key3,key4,nb,n):
    S = Array('S', BitVecSort(8), BitVecSort(8))
    I = Array('A', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
   # W = Array('W', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    tm = Array('tm', BitVecSort(8), BitVecSort(8))
    #tm2 = Array('tm2', BitVecSort(8), BitVecSort(8))
    ## Initializing the `statemt` array ##
    i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 8), BitVecVal(elem, 8))
        i += 1

    ## Initializing the `Sbox` array ##
    i = 0
    for arr in Sbox:
        j = 0
        for elem in arr:
            tm = Store(tm, BitVecVal(j, 8), BitVecVal(elem, 8))
            j += 1
        I = Store(I, BitVecVal(i, 8), tm)
        i += 1

    # ---------------------- ByetSub ShiftRow ------------------

    temp1 = Select(Select(I,(Select(S,1) >> 4)),(Select(S,1) & 0xf))
    S = Store(S, 1, Select(Select(I, (Select(S, 5) >> 4)), ((Select(S, 5) & 0xf))))
    S = Store(S, 5, Select(Select(I, (Select(S, key1) >> 4)), ((Select(S, 9) & 0xf))))
    S = Store(S, 9, Select(Select(I, (Select(S, 13) >> 4)), ((Select(S, 13) & 0xf))))
    S = Store(S, 13, temp1)


    temp2 = Select(Select(I, (Select(S, 2) >> 4)), ((Select(S, 2) & 0xf)))
    S = Store(S, 2, Select(Select(I, (Select(S, key2) >> 4)), ((Select(S, 10) & 0xf))))
    S = Store(S, 10, temp2)


    temp3 = Select(Select(I, (Select(S, 6) >> 4)), ((Select(S, 6) & 0xf)))
    S = Store(S, 6, Select(Select(I, (Select(S, 14) >> 4)), ((Select(S, key3) & 0xf))))
    S = Store(S, 14, temp3)

    temp4 = Select(Select(I, (Select(S, 3) >> 4)), ((Select(S, 3) & 0xf)))
    S = Store(S, 3, Select(Select(I, (Select(S, key4) >> 4)), ((Select(S, 15) & 0xf))))
    S = Store(S, 15, Select(Select(I, (Select(S, 11) >> 4)), ((Select(S, 11) & 0xf))))
    S = Store(S, 11, Select(Select(I, (Select(S, 7) >> 4)), ((Select(S, 7) & 0xf))))
    S = Store(S, 7, temp4)

    S = Store(S, 0, Select(Select(I, (Select(S, 0) >> 4)), ((Select(S, 0) & 0xf))))
    S = Store(S, 4, Select(Select(I, (Select(S, 4) >> 4)), ((Select(S, 4) & 0xf))))
    S = Store(S, 8, Select(Select(I, (Select(S, 8) >> 4)), ((Select(S, 8) & 0xf))))
    S = Store(S, 12, Select(Select(I, (Select(S, 12) >> 4)), ((Select(S, 12) & 0xf))))


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    o0 = S[0] + n
    o1 = S[1] + n
    o2 = S[2] + n
    o3 = S[3] + n
    o4 = S[4] + n
    o5 = S[5] + n
    o6 = S[6] + n
    o7 = S[7] + n
    o8 = S[8]  + n
    o9 = S[9] + n
    o10 = S[10] + n
    o11 = S[11] + n
    o12 = S[12] + n
    o13 = S[13] + n
    o14 = S[14] + n
    o15 = S[15] + n
    o = tuple.tuple1(o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15)
    return o


def sub(key1,nb,n):
    S = Array('S', BitVecSort(8), BitVecSort(8))
    I = Array('A', BitVecSort(8), ArraySort(BitVecSort(8), BitVecSort(8)))
    tm = Array('tm', BitVecSort(8), BitVecSort(8))
    ## Initializing the `statemt` array ##
    i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 8), BitVecVal(elem, 8))
        i += 1

    ## Initializing the `Sbox` array ##
    i = 0
    for arr in Sbox:
        j = 0
        for elem in arr:
            tm = Store(tm, BitVecVal(j, 8), BitVecVal(elem, 8))
            j += 1
        I = Store(I, BitVecVal(i, 8), tm)
        i += 1
    # ---------------------- ByetSub ShiftRow ------------------

    temp = If(nb==4,  I[S[1] >> 4][S[1] & 0xf], BitVecVal(0, 8)) 
    S = Store(S, BitVecVal(1, 8), If(nb==4,  I[S[5] >> 4][S[5] & 0xf], S[1]))
    S = Store(S, BitVecVal(5, 8), If(nb==4,  I[S[key1] >> 4][S[9] & 0xf], S[5])) #key1=9
    S = Store(S, BitVecVal(9, 8), If(nb==4,  I[S[13] >> 4][S[13] & 0xf], S[9]))
    S = Store(S, BitVecVal(13, 8), If(nb==4, temp, S[13]))



    # ------------------------ MixColumn AddRoundKey ---------------------------------

    o1 = S[1]
    o5 = S[5]  
    o9 = S[9]
    o13 = S[13]
    o=tuple.tuple2(o1,o5,o9,o13)
    return o


gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))#,BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8))

print(gg.check(findOutput(9,10,14,15,4,5)==oa))

'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))'''



j = 0


s = Tactic('smt').solver()

# s.add(simplify(findOutput(key1_1,key2_1,key3_1,key4_1,nb,n)) == out1)
# s.add(simplify(findOutput(key1_2,key2_2,key3_2,key4_2,nb,n)) == out2)

s.add(simplify(sub(key1_1,nb,n)) == out3)
s.add(simplify(sub(key1_2,nb,n)) == out4)
s.add(nb == 4)
s.add(n >= 0, n < 15)

s.add(key1_1>=0,key1_1<=15)
s.add(key1_2>=0,key1_2<=15)
s.add(key2_1>=0,key2_1<=15)
s.add(key2_2>=0,key2_2<=15)
s.add(key3_1>=0,key3_1<=15)
s.add(key3_2>=0,key3_2<=15)
s.add(key4_1>=0,key4_1<=15)
s.add(key4_2>=0,key4_2<=15)

pos_set = set()
print("loop1 enter")
# s.check()
# print(s.model())
#print(s.check(out1 != out2, Or(k1_1 != k1_2,k2_1 != k2_2 , k3_1 != k3_2 ,k4_1 != k4_2,k5_1 != k5_2 ,key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2)))

start=time.time()
while s.check(out3 != out4, Or(key1_1!=key1_2,key2_1!=key2_2,key3_1!=key3_2,key4_1!=key4_2)) == sat:
    m = s.model()
    #print(m)
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2]))
    ia = str(m[nb]) + " " + str(m[n])
    [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    #,BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8)
    oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8))#,BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8))
    s.add(simplify(findOutput(key1_1,key2_1,key3_1,key4_1,m[nb],m[n])) == oa)
    s.add(simplify(findOutput(key1_2,key2_2,key3_2,key4_2,m[nb],m[n])) == oa)
    print("Iteration %d = %f second" %(j+1,time.time()-start))
    j = j + 1
print("unsat takes %f second time" %(time.time()-start))
print("loop1 complete")




p=0
#print(s)
while s.check(key1_1==key1_2,key2_1==key2_2,key3_1==key3_2,key4_1==key4_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    pos_set.add(m)
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1]))
    print("Iteration %d = %f second" %(p+1,time.time()-start))
    if len(pos_set) > rem_key_max:
        break
    s.add(Or(key1_1!=m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1]))
    s.add(Or(key1_2!=m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2]))
    p = p + 1
print("done")
pos_l = list(pos_set)

g = Tactic('smt').solver()

g.add(simplify(findOutput(k1_1,key1_1,key2_1,key3_1,nb,n)) == out1)
g.add(simplify(findOutput(k1_2,key1_2,key2_2,key3_2,nb,n)) == out2)
g.add(nb==4)
g.add(n>=0 ,n<15)

print("loop3 enter")

while len(pos_l) > 1:
    m1 = pos_l[0]
    m2 = pos_l[1]
    #print(str(m1[key1_2])+" "+str(m1[key2_2])+" "+str(m1[key3_2]))
    #print(str(m2[key1_2])+" "+str(m2[key2_2])+" "+str(m2[key3_2]))
    g.push()
    g.add(key1_1==m1[key1_2],key2_1==m1[key2_2],key3_1==m1[key3_2])
    g.add(key1_2==m2[key1_2],key2_2==m2[key2_2],key3_2==m2[key3_2])
    if g.check(out1 != out2) == sat:
        m = g.model()
        #print(str(m[nb])+"  "+str(m[n]))
        ia = str(m[nb]) + " " + str(m[n])
        [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16,oa17,oa18,oa19,oa20,oa21,oa22,oa23,oa24,oa25,oa26,oa27,oa28,oa29,oa30,oa31,oa8] = Cexec(ia)
        oa = tuple.tuple1(BitVecVal(oa1,8),BitVecVal(oa2,8),BitVecVal(oa3,8),BitVecVal(oa4,8),BitVecVal(oa5,8),BitVecVal(oa6,8),BitVecVal(oa7,8),BitVecVal(oa8,8),BitVecVal(oa9,8),BitVecVal(oa10,8),BitVecVal(oa11,8),BitVecVal(oa12,8),BitVecVal(oa13,8),BitVecVal(oa14,8),BitVecVal(oa15,8),BitVecVal(oa16,8),BitVecVal(oa17,8),BitVecVal(oa18,8),BitVecVal(oa19,8),BitVecVal(oa20,8),BitVecVal(oa21,8),BitVecVal(oa22,8),BitVecVal(oa23,8),BitVecVal(oa24,8),BitVecVal(oa25,8),BitVecVal(oa26,8),BitVecVal(oa27,8),BitVecVal(oa28,8),BitVecVal(oa29,8),BitVecVal(oa30,8),BitVecVal(oa31,8),BitVecVal(oa8,8))
        if g.check(simplify(findOutput(m1[key1_2],m1[key2_2],m1[key3_2],m[nb],m[n])) == oa) == unsat:
            pos_l.remove(m1)
        if g.check(simplify(findOutput(m2[key1_2],m2[key2_2],m2[key3_2],m[nb],m[n])) == oa) == unsat:
            pos_l.remove(m2)
    else:
        pos_l.remove(m1)
    g.pop()

print("The final key is:")
m = pos_l[0]
print(str(m[key1_2]))
print(str(m[key2_2]))
print(str(m[key3_2]))
print()


end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (j, taken))      

