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
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1,o17_1,o18_1,o19_1,o20_1,o21_1,o22_1,o23_1,o24_1,o25_1,o26_1,o27_1,o28_1,o29_1,o30_1,o31_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1 o16_1 o17_1 o18_1 o19_1 o20_1 o21_1 o22_1 o23_1 o24_1 o25_1 o26_1 o27_1 o28_1 o29_1 o30_1 o31_1',32)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2,o17_2,o18_2,o19_2,o20_2,o21_2,o22_2,o23_2,o24_2,o25_2,o26_2,o27_2,o28_2,o29_2,o30_2,o31_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2 o16_2 o17_2 o18_2 o19_2 o20_2 o21_2 o22_2 o23_2 o24_2 o25_2 o26_2 o27_2 o28_2 o29_2 o30_2 o31_2',32)
oo0_1,oo1_1,oo2_1,oo3_1,oo4_1,oo5_1,oo6_1,oo7_1,oo8_1,oo9_1,oo10_1,oo11_1,oo12_1,oo13_1,oo14_1,oo15_1,oo16_1,oo17_1,oo18_1,oo19_1,oo20_1,oo21_1,oo22_1,oo23_1,oo24_1,oo25_1,oo26_1,oo27_1,oo28_1,oo29_1,oo30_1,oo31_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1 oo4_1 oo5_1 oo6_1 oo7_1 oo8_1 oo9_1 oo10_1 oo11_1 oo12_1 oo13_1 oo14_1 oo15_1 oo16_1 oo17_1 oo18_1 oo19_1 oo20_1 oo21_1 oo22_1 oo23_1 oo24_1 oo25_1 oo26_1 oo27_1 oo28_1 oo29_1 oo30_1 oo31_1',32)
oo0_2,oo1_2,oo2_2,oo3_2,oo4_2,oo5_2,oo6_2,oo7_2,oo8_2,oo9_2,oo10_2,oo11_2,oo12_2,oo13_2,oo14_2,oo15_2,oo16_2,oo17_2,oo18_2,oo19_2,oo20_2,oo21_2,oo22_2,oo23_2,oo24_2,oo25_2,oo26_2,oo27_2,oo28_2,oo29_2,oo30_2,oo31_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2 oo4_2 oo5_2 oo6_2 oo7_2 oo8_2 oo9_2 oo10_2 oo11_2 oo12_2 oo13_2 oo14_2 oo15_2 oo16_2 oo17_2 oo18_2 oo19_2 oo20_2 oo21_2 oo22_2 oo23_2 oo24_2 oo25_2 oo26_2 oo27_2 oo28_2 oo29_2 oo30_2 oo31_2',32)
k1_1,k2_1,k3_1,k4_1,k5_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1')
k1_2,k2_2,k3_2,k4_2,k5_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2')
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 32)

tuple = Datatype('tuple')
tuple.declare('tuple1',('1' , BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)),('5' , BitVecSort(32)),('6' , BitVecSort(32)),('7' , BitVecSort(32)),('8' , BitVecSort(32)),('9' , BitVecSort(32)),('10' , BitVecSort(32)),('11' , BitVecSort(32)),('12' , BitVecSort(32)),('13' , BitVecSort(32)),('14' , BitVecSort(32)),('15' , BitVecSort(32)),('16' , BitVecSort(32)))
tuple.declare('tuple2',('1', BitVecSort(32)),('2' , BitVecSort(32)),('3' , BitVecSort(32)),('4' , BitVecSort(32)))#,('37' , BitVecSort(32)),('38' , BitVecSort(32)),('39' , BitVecSort(32)),('40' , BitVecSort(32)),('41', BitVecSort(32)),('42' , BitVecSort(32)),('43' , BitVecSort(32)),('44' , BitVecSort(32)),('45' , BitVecSort(32)),('46' , BitVecSort(32)),('47' , BitVecSort(32)),('48' , BitVecSort(32)),('49', BitVecSort(32)),('50' , BitVecSort(32)),('51' , BitVecSort(32)),('52' , BitVecSort(32)),('53' , BitVecSort(32)),('54' , BitVecSort(32)),('55' , BitVecSort(32)),('56' , BitVecSort(32)),('57', BitVecSort(32)),('58' , BitVecSort(32)),('59' , BitVecSort(32)),('60' , BitVecSort(32)),('61' , BitVecSort(32)),('62' , BitVecSort(32)),('63' , BitVecSort(32)),('64' , BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)#,oo4_1,oo5_1,oo6_1,oo7_1,oo8_1,oo9_1,oo10_1,oo11_1,oo12_1,oo13_1,oo14_1,oo15_1,oo16_1,oo17_1,oo18_1,oo19_1,oo20_1,oo21_1,oo22_1,oo23_1,oo24_1,oo25_1,oo26_1,oo27_1,oo28_1,oo29_1,oo30_1,oo31_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)#,oo4_2,oo5_2,oo6_2,oo7_2,oo8_2,oo9_2,oo10_2,oo11_2,oo12_2,oo13_2,oo14_2,oo15_2,oo16_2,oo17_2,oo18_2,oo19_2,oo20_2,oo21_2,oo22_2,oo23_2,oo24_2,oo25_2,oo26_2,oo27_2,oo28_2,oo29_2,oo30_2,oo31_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 32

statemt = [3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]
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

# statemt2= [2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]

#last element changed to 0x20 from 0x16

word = [[43,40,171,9,160,136,35,42,242,122,89,115,61,71,30,109,239,168,182,219,212,124,202,17,109,17,219,202,78,95,132,78,234,181,49,127,172,25,40,87,208,201,225,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[126,174,247,207,250,84,163,108,194,150,53,89,128,22,35,122,68,82,113,11,209,131,242,249,136,11,249,0,84,95,166,166,210,141,43,141,119,250,209,92,20,238,63,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[21,210,21,79,254,44,57,118,149,185,128,246,71,254,126,136,165,91,37,173,198,157,184,21,163,62,134,147,247,201,79,220,115,186,245,41,102,220,41,0,249,37,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[22,166,136,60,23,177,57,5,242,67,122,127,125,62,68,59,65,127,59,0,248,135,188,188,122,253,65,253,14,243,178,79,33,210,96,47,243,33,65,110,168,137,200,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
