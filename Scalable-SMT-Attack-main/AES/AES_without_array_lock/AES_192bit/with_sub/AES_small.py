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
# ,('11' , BitVecSort(10)),('12' , BitVecSort(10)),('13' , BitVecSort(10)),('14' , BitVecSort(10)),('15' , BitVecSort(10)),('16' , BitVecSort(10)),('17' , BitVecSort(10)),('18' , BitVecSort(10)),('19' , BitVecSort(10)),('20' , BitVecSort(10)),('21' , BitVecSort(10)),('22' , BitVecSort(10)),('23' , BitVecSort(10)),('24' , BitVecSort(10)),('25' , BitVecSort(10)),('26' , BitVecSort(10)),('27' , BitVecSort(10)),('28' , BitVecSort(10)),('29' , BitVecSort(10)),('30' , BitVecSort(10)),('31' , BitVecSort(10)),('10' , BitVecSort(10))
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',10)
o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1 = BitVecs('o0_1 o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1',10)
o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2 = BitVecs('o0_2 o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2',10)
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16=BitVecs('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16',10)
oo0_1,oo1_1,oo2_1,oo3_1 = BitVecs('oo0_1 oo1_1 oo2_1 oo3_1',10)
oo0_2,oo1_2,oo2_2,oo3_2 = BitVecs('oo0_2 oo1_2 oo2_2 oo3_2',10)
'''k1_1,k2_1,k3_1,k4_1,k5_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1')
k1_2,k2_2,k3_2,k4_2,k5_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2')'''
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1' , 10)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2' , 10)

bkey1_1,bkey2_1,bkey3_1,bkey4_1,bkey5_1,bkey6_1,bkey7_1,bkey8_1,bkey9_1,bkey10_1 = Bools('bkey1_1 bkey2_1 bkey3_1 bkey4_1 bkey5_1 bkey6_1 bkey7_1 bkey8_1 bkey9_1 bkey10_1')
bkey1_2,bkey2_2,bkey3_2,bkey4_2,bkey5_2,bkey6_2,bkey7_2,bkey8_2,bkey9_2,bkey10_2 = Bools('bkey1_2 bkey2_2 bkey3_2 bkey4_2 bkey5_2 bkey6_2 bkey7_2 bkey8_2 bkey9_2 bkey10_2')

inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16 = BitVecs('inp1 inp2 inp3 inp4 inp5 inp6 inp7 inp8 inp9 inp10 inp11 inp12 inp13 inp14 inp15 inp16',10)


tuple = Datatype('tuple')
tuple.declare('tuple1',('1' , BitVecSort(10)),('2' , BitVecSort(10)),('3' , BitVecSort(10)),('4' , BitVecSort(10)),('5' , BitVecSort(10)),('6' , BitVecSort(10)),('7' , BitVecSort(10)),('8' , BitVecSort(10)),('9' , BitVecSort(10)),('10' , BitVecSort(10)),('11' , BitVecSort(10)),('12' , BitVecSort(10)),('13' , BitVecSort(10)),('14' , BitVecSort(10)),('15' , BitVecSort(10)),('16' , BitVecSort(10)))
tuple.declare('tuple2',('1' , BitVecSort(10)),('2' , BitVecSort(10)),('3' , BitVecSort(10)),('4' , BitVecSort(10)))#,('5' , BitVecSort(10)),('6' , BitVecSort(10)),('7' , BitVecSort(10)),('8' , BitVecSort(10)),('9' , BitVecSort(10)),('10' , BitVecSort(10)),('11' , BitVecSort(10)),('12' , BitVecSort(10)),('13' , BitVecSort(10)),('14' , BitVecSort(10)),('15' , BitVecSort(10)),('16' , BitVecSort(10)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 10


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

S = Array('S', BitVecSort(10), BitVecSort(10))
I = Array('A', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
W = Array('W', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
ret = Array('ret', BitVecSort(10), BitVecSort(10))


I = Array('A', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
tm0 = Array('tm0', BitVecSort(10), BitVecSort(10))
tm0 = Store(tm0, BitVecVal(0, 10), BitVecVal(99, 10))
tm0 = Store(tm0, BitVecVal(1, 10), BitVecVal(124, 10))
tm0 = Store(tm0, BitVecVal(2, 10), BitVecVal(119, 10))
tm0 = Store(tm0, BitVecVal(3, 10), BitVecVal(123, 10))
tm0 = Store(tm0, BitVecVal(4, 10), BitVecVal(242, 10))
tm0 = Store(tm0, BitVecVal(5, 10), BitVecVal(107, 10))
tm0 = Store(tm0, BitVecVal(6, 10), BitVecVal(111, 10))
tm0 = Store(tm0, BitVecVal(7, 10), BitVecVal(197, 10))
tm0 = Store(tm0, BitVecVal(8, 10), BitVecVal(48, 10))
tm0 = Store(tm0, BitVecVal(9, 10), BitVecVal(1, 10))
tm0 = Store(tm0, BitVecVal(10, 10), BitVecVal(103, 10))
tm0 = Store(tm0, BitVecVal(11, 10), BitVecVal(43, 10))
tm0 = Store(tm0, BitVecVal(12, 10), BitVecVal(254, 10))
tm0 = Store(tm0, BitVecVal(13, 10), BitVecVal(215, 10))
tm0 = Store(tm0, BitVecVal(14, 10), BitVecVal(171, 10))
tm0 = Store(tm0, BitVecVal(15, 10), BitVecVal(118, 10))
I = Store(I, BitVecVal(0, 10), tm0)
tm1 = Array('tm1', BitVecSort(10), BitVecSort(10))
tm1 = Store(tm1, BitVecVal(0, 10), BitVecVal(202, 10))
tm1 = Store(tm1, BitVecVal(1, 10), BitVecVal(130, 10))
tm1 = Store(tm1, BitVecVal(2, 10), BitVecVal(201, 10))
tm1 = Store(tm1, BitVecVal(3, 10), BitVecVal(125, 10))
tm1 = Store(tm1, BitVecVal(4, 10), BitVecVal(250, 10))
tm1 = Store(tm1, BitVecVal(5, 10), BitVecVal(89, 10))
tm1 = Store(tm1, BitVecVal(6, 10), BitVecVal(71, 10))
tm1 = Store(tm1, BitVecVal(7, 10), BitVecVal(240, 10))
tm1 = Store(tm1, BitVecVal(8, 10), BitVecVal(173, 10))
tm1 = Store(tm1, BitVecVal(9, 10), BitVecVal(212, 10))
tm1 = Store(tm1, BitVecVal(10, 10), BitVecVal(162, 10))
tm1 = Store(tm1, BitVecVal(11, 10), BitVecVal(175, 10))
tm1 = Store(tm1, BitVecVal(12, 10), BitVecVal(156, 10))
tm1 = Store(tm1, BitVecVal(13, 10), BitVecVal(164, 10))
tm1 = Store(tm1, BitVecVal(14, 10), BitVecVal(114, 10))
tm1 = Store(tm1, BitVecVal(15, 10), BitVecVal(192, 10))
I = Store(I, BitVecVal(1, 10), tm1)
tm2 = Array('tm2', BitVecSort(10), BitVecSort(10))
tm2 = Store(tm2, BitVecVal(0, 10), BitVecVal(183, 10))
tm2 = Store(tm2, BitVecVal(1, 10), BitVecVal(253, 10))
tm2 = Store(tm2, BitVecVal(2, 10), BitVecVal(147, 10))
tm2 = Store(tm2, BitVecVal(3, 10), BitVecVal(38, 10))
tm2 = Store(tm2, BitVecVal(4, 10), BitVecVal(54, 10))
tm2 = Store(tm2, BitVecVal(5, 10), BitVecVal(63, 10))
tm2 = Store(tm2, BitVecVal(6, 10), BitVecVal(247, 10))
tm2 = Store(tm2, BitVecVal(7, 10), BitVecVal(204, 10))
tm2 = Store(tm2, BitVecVal(8, 10), BitVecVal(52, 10))
tm2 = Store(tm2, BitVecVal(9, 10), BitVecVal(165, 10))
tm2 = Store(tm2, BitVecVal(10, 10), BitVecVal(229, 10))
tm2 = Store(tm2, BitVecVal(11, 10), BitVecVal(241, 10))
tm2 = Store(tm2, BitVecVal(12, 10), BitVecVal(113, 10))
tm2 = Store(tm2, BitVecVal(13, 10), BitVecVal(216, 10))
tm2 = Store(tm2, BitVecVal(14, 10), BitVecVal(49, 10))
tm2 = Store(tm2, BitVecVal(15, 10), BitVecVal(21, 10))
I = Store(I, BitVecVal(2, 10), tm2)
tm3 = Array('tm3', BitVecSort(10), BitVecSort(10))
tm3 = Store(tm3, BitVecVal(0, 10), BitVecVal(4, 10))
tm3 = Store(tm3, BitVecVal(1, 10), BitVecVal(199, 10))
tm3 = Store(tm3, BitVecVal(2, 10), BitVecVal(35, 10))
tm3 = Store(tm3, BitVecVal(3, 10), BitVecVal(195, 10))
tm3 = Store(tm3, BitVecVal(4, 10), BitVecVal(24, 10))
tm3 = Store(tm3, BitVecVal(5, 10), BitVecVal(150, 10))
tm3 = Store(tm3, BitVecVal(6, 10), BitVecVal(5, 10))
tm3 = Store(tm3, BitVecVal(7, 10), BitVecVal(154, 10))
tm3 = Store(tm3, BitVecVal(8, 10), BitVecVal(7, 10))
tm3 = Store(tm3, BitVecVal(9, 10), BitVecVal(18, 10))
tm3 = Store(tm3, BitVecVal(10, 10), BitVecVal(128, 10))
tm3 = Store(tm3, BitVecVal(11, 10), BitVecVal(226, 10))
tm3 = Store(tm3, BitVecVal(12, 10), BitVecVal(235, 10))
tm3 = Store(tm3, BitVecVal(13, 10), BitVecVal(39, 10))
tm3 = Store(tm3, BitVecVal(14, 10), BitVecVal(178, 10))
tm3 = Store(tm3, BitVecVal(15, 10), BitVecVal(117, 10))
I = Store(I, BitVecVal(3, 10), tm3)
tm4 = Array('tm4', BitVecSort(10), BitVecSort(10))
tm4 = Store(tm4, BitVecVal(0, 10), BitVecVal(9, 10))
tm4 = Store(tm4, BitVecVal(1, 10), BitVecVal(131, 10))
tm4 = Store(tm4, BitVecVal(2, 10), BitVecVal(44, 10))
tm4 = Store(tm4, BitVecVal(3, 10), BitVecVal(26, 10))
tm4 = Store(tm4, BitVecVal(4, 10), BitVecVal(27, 10))
tm4 = Store(tm4, BitVecVal(5, 10), BitVecVal(110, 10))
tm4 = Store(tm4, BitVecVal(6, 10), BitVecVal(90, 10))
tm4 = Store(tm4, BitVecVal(7, 10), BitVecVal(160, 10))
tm4 = Store(tm4, BitVecVal(8, 10), BitVecVal(82, 10))
tm4 = Store(tm4, BitVecVal(9, 10), BitVecVal(59, 10))
tm4 = Store(tm4, BitVecVal(10, 10), BitVecVal(214, 10))
tm4 = Store(tm4, BitVecVal(11, 10), BitVecVal(179, 10))
tm4 = Store(tm4, BitVecVal(12, 10), BitVecVal(41, 10))
tm4 = Store(tm4, BitVecVal(13, 10), BitVecVal(227, 10))
tm4 = Store(tm4, BitVecVal(14, 10), BitVecVal(47, 10))
tm4 = Store(tm4, BitVecVal(15, 10), BitVecVal(132, 10))
I = Store(I, BitVecVal(4, 10), tm4)
tm5 = Array('tm5', BitVecSort(10), BitVecSort(10))
tm5 = Store(tm5, BitVecVal(0, 10), BitVecVal(83, 10))
tm5 = Store(tm5, BitVecVal(1, 10), BitVecVal(209, 10))
tm5 = Store(tm5, BitVecVal(2, 10), BitVecVal(0, 10))
tm5 = Store(tm5, BitVecVal(3, 10), BitVecVal(237, 10))
tm5 = Store(tm5, BitVecVal(4, 10), BitVecVal(32, 10))
tm5 = Store(tm5, BitVecVal(5, 10), BitVecVal(252, 10))
tm5 = Store(tm5, BitVecVal(6, 10), BitVecVal(177, 10))
tm5 = Store(tm5, BitVecVal(7, 10), BitVecVal(91, 10))
tm5 = Store(tm5, BitVecVal(8, 10), BitVecVal(106, 10))
tm5 = Store(tm5, BitVecVal(9, 10), BitVecVal(203, 10))
tm5 = Store(tm5, BitVecVal(10, 10), BitVecVal(190, 10))
tm5 = Store(tm5, BitVecVal(11, 10), BitVecVal(57, 10))
tm5 = Store(tm5, BitVecVal(12, 10), BitVecVal(74, 10))
tm5 = Store(tm5, BitVecVal(13, 10), BitVecVal(76, 10))
tm5 = Store(tm5, BitVecVal(14, 10), BitVecVal(88, 10))
tm5 = Store(tm5, BitVecVal(15, 10), BitVecVal(207, 10))
I = Store(I, BitVecVal(5, 10), tm5)
tm6 = Array('tm6', BitVecSort(10), BitVecSort(10))
tm6 = Store(tm6, BitVecVal(0, 10), BitVecVal(208, 10))
tm6 = Store(tm6, BitVecVal(1, 10), BitVecVal(239, 10))
tm6 = Store(tm6, BitVecVal(2, 10), BitVecVal(170, 10))
tm6 = Store(tm6, BitVecVal(3, 10), BitVecVal(251, 10))
tm6 = Store(tm6, BitVecVal(4, 10), BitVecVal(67, 10))
tm6 = Store(tm6, BitVecVal(5, 10), BitVecVal(77, 10))
tm6 = Store(tm6, BitVecVal(6, 10), BitVecVal(51, 10))
tm6 = Store(tm6, BitVecVal(7, 10), BitVecVal(133, 10))
tm6 = Store(tm6, BitVecVal(8, 10), BitVecVal(69, 10))
tm6 = Store(tm6, BitVecVal(9, 10), BitVecVal(249, 10))
tm6 = Store(tm6, BitVecVal(10, 10), BitVecVal(2, 10))
tm6 = Store(tm6, BitVecVal(11, 10), BitVecVal(127, 10))
tm6 = Store(tm6, BitVecVal(12, 10), BitVecVal(80, 10))
tm6 = Store(tm6, BitVecVal(13, 10), BitVecVal(60, 10))
tm6 = Store(tm6, BitVecVal(14, 10), BitVecVal(159, 10))
tm6 = Store(tm6, BitVecVal(15, 10), BitVecVal(168, 10))
I = Store(I, BitVecVal(6, 10), tm6)
tm7 = Array('tm7', BitVecSort(10), BitVecSort(10))
tm7 = Store(tm7, BitVecVal(0, 10), BitVecVal(81, 10))
tm7 = Store(tm7, BitVecVal(1, 10), BitVecVal(163, 10))
tm7 = Store(tm7, BitVecVal(2, 10), BitVecVal(64, 10))
tm7 = Store(tm7, BitVecVal(3, 10), BitVecVal(143, 10))
tm7 = Store(tm7, BitVecVal(4, 10), BitVecVal(146, 10))
tm7 = Store(tm7, BitVecVal(5, 10), BitVecVal(157, 10))
tm7 = Store(tm7, BitVecVal(6, 10), BitVecVal(56, 10))
tm7 = Store(tm7, BitVecVal(7, 10), BitVecVal(245, 10))
tm7 = Store(tm7, BitVecVal(8, 10), BitVecVal(188, 10))
tm7 = Store(tm7, BitVecVal(9, 10), BitVecVal(182, 10))
tm7 = Store(tm7, BitVecVal(10, 10), BitVecVal(218, 10))
tm7 = Store(tm7, BitVecVal(11, 10), BitVecVal(33, 10))
tm7 = Store(tm7, BitVecVal(12, 10), BitVecVal(16, 10))
tm7 = Store(tm7, BitVecVal(13, 10), BitVecVal(255, 10))
tm7 = Store(tm7, BitVecVal(14, 10), BitVecVal(243, 10))
tm7 = Store(tm7, BitVecVal(15, 10), BitVecVal(210, 10))
I = Store(I, BitVecVal(7, 10), tm7)
tm8 = Array('tm8', BitVecSort(10), BitVecSort(10))
tm8 = Store(tm8, BitVecVal(0, 10), BitVecVal(205, 10))
tm8 = Store(tm8, BitVecVal(1, 10), BitVecVal(12, 10))
tm8 = Store(tm8, BitVecVal(2, 10), BitVecVal(19, 10))
tm8 = Store(tm8, BitVecVal(3, 10), BitVecVal(236, 10))
tm8 = Store(tm8, BitVecVal(4, 10), BitVecVal(95, 10))
tm8 = Store(tm8, BitVecVal(5, 10), BitVecVal(151, 10))
tm8 = Store(tm8, BitVecVal(6, 10), BitVecVal(68, 10))
tm8 = Store(tm8, BitVecVal(7, 10), BitVecVal(23, 10))
tm8 = Store(tm8, BitVecVal(8, 10), BitVecVal(196, 10))
tm8 = Store(tm8, BitVecVal(9, 10), BitVecVal(167, 10))
tm8 = Store(tm8, BitVecVal(10, 10), BitVecVal(126, 10))
tm8 = Store(tm8, BitVecVal(11, 10), BitVecVal(61, 10))
tm8 = Store(tm8, BitVecVal(12, 10), BitVecVal(100, 10))
tm8 = Store(tm8, BitVecVal(13, 10), BitVecVal(93, 10))
tm8 = Store(tm8, BitVecVal(14, 10), BitVecVal(25, 10))
tm8 = Store(tm8, BitVecVal(15, 10), BitVecVal(115, 10))
I = Store(I, BitVecVal(8, 10), tm8)
tm9 = Array('tm9', BitVecSort(10), BitVecSort(10))
tm9 = Store(tm9, BitVecVal(0, 10), BitVecVal(96, 10))
tm9 = Store(tm9, BitVecVal(1, 10), BitVecVal(129, 10))
tm9 = Store(tm9, BitVecVal(2, 10), BitVecVal(79, 10))
tm9 = Store(tm9, BitVecVal(3, 10), BitVecVal(220, 10))
tm9 = Store(tm9, BitVecVal(4, 10), BitVecVal(34, 10))
tm9 = Store(tm9, BitVecVal(5, 10), BitVecVal(42, 10))
tm9 = Store(tm9, BitVecVal(6, 10), BitVecVal(144, 10))
tm9 = Store(tm9, BitVecVal(7, 10), BitVecVal(136, 10))
tm9 = Store(tm9, BitVecVal(8, 10), BitVecVal(70, 10))
tm9 = Store(tm9, BitVecVal(9, 10), BitVecVal(238, 10))
tm9 = Store(tm9, BitVecVal(10, 10), BitVecVal(184, 10))
tm9 = Store(tm9, BitVecVal(11, 10), BitVecVal(20, 10))
tm9 = Store(tm9, BitVecVal(12, 10), BitVecVal(222, 10))
tm9 = Store(tm9, BitVecVal(13, 10), BitVecVal(94, 10))
tm9 = Store(tm9, BitVecVal(14, 10), BitVecVal(11, 10))
tm9 = Store(tm9, BitVecVal(15, 10), BitVecVal(219, 10))
I = Store(I, BitVecVal(9, 10), tm9)
tm10 = Array('tm10', BitVecSort(10), BitVecSort(10))
tm10 = Store(tm10, BitVecVal(0, 10), BitVecVal(224, 10))
tm10 = Store(tm10, BitVecVal(1, 10), BitVecVal(50, 10))
tm10 = Store(tm10, BitVecVal(2, 10), BitVecVal(58, 10))
tm10 = Store(tm10, BitVecVal(3, 10), BitVecVal(10, 10))
tm10 = Store(tm10, BitVecVal(4, 10), BitVecVal(73, 10))
tm10 = Store(tm10, BitVecVal(5, 10), BitVecVal(6, 10))
tm10 = Store(tm10, BitVecVal(6, 10), BitVecVal(36, 10))
tm10 = Store(tm10, BitVecVal(7, 10), BitVecVal(92, 10))
tm10 = Store(tm10, BitVecVal(8, 10), BitVecVal(194, 10))
tm10 = Store(tm10, BitVecVal(9, 10), BitVecVal(211, 10))
tm10 = Store(tm10, BitVecVal(10, 10), BitVecVal(172, 10))
tm10 = Store(tm10, BitVecVal(11, 10), BitVecVal(98, 10))
tm10 = Store(tm10, BitVecVal(12, 10), BitVecVal(145, 10))
tm10 = Store(tm10, BitVecVal(13, 10), BitVecVal(149, 10))
tm10 = Store(tm10, BitVecVal(14, 10), BitVecVal(228, 10))
tm10 = Store(tm10, BitVecVal(15, 10), BitVecVal(121, 10))
I = Store(I, BitVecVal(10, 10), tm10)
tm11 = Array('tm11', BitVecSort(10), BitVecSort(10))
tm11 = Store(tm11, BitVecVal(0, 10), BitVecVal(231, 10))
tm11 = Store(tm11, BitVecVal(1, 10), BitVecVal(200, 10))
tm11 = Store(tm11, BitVecVal(2, 10), BitVecVal(55, 10))
tm11 = Store(tm11, BitVecVal(3, 10), BitVecVal(109, 10))
tm11 = Store(tm11, BitVecVal(4, 10), BitVecVal(141, 10))
tm11 = Store(tm11, BitVecVal(5, 10), BitVecVal(213, 10))
tm11 = Store(tm11, BitVecVal(6, 10), BitVecVal(78, 10))
tm11 = Store(tm11, BitVecVal(7, 10), BitVecVal(169, 10))
tm11 = Store(tm11, BitVecVal(8, 10), BitVecVal(108, 10))
tm11 = Store(tm11, BitVecVal(9, 10), BitVecVal(86, 10))
tm11 = Store(tm11, BitVecVal(10, 10), BitVecVal(244, 10))
tm11 = Store(tm11, BitVecVal(11, 10), BitVecVal(234, 10))
tm11 = Store(tm11, BitVecVal(12, 10), BitVecVal(101, 10))
tm11 = Store(tm11, BitVecVal(13, 10), BitVecVal(122, 10))
tm11 = Store(tm11, BitVecVal(14, 10), BitVecVal(174, 10))
tm11 = Store(tm11, BitVecVal(15, 10), BitVecVal(8, 10))
I = Store(I, BitVecVal(11, 10), tm11)
tm12 = Array('tm12', BitVecSort(10), BitVecSort(10))
tm12 = Store(tm12, BitVecVal(0, 10), BitVecVal(186, 10))
tm12 = Store(tm12, BitVecVal(1, 10), BitVecVal(120, 10))
tm12 = Store(tm12, BitVecVal(2, 10), BitVecVal(37, 10))
tm12 = Store(tm12, BitVecVal(3, 10), BitVecVal(46, 10))
tm12 = Store(tm12, BitVecVal(4, 10), BitVecVal(28, 10))
tm12 = Store(tm12, BitVecVal(5, 10), BitVecVal(166, 10))
tm12 = Store(tm12, BitVecVal(6, 10), BitVecVal(180, 10))
tm12 = Store(tm12, BitVecVal(7, 10), BitVecVal(198, 10))
tm12 = Store(tm12, BitVecVal(8, 10), BitVecVal(232, 10))
tm12 = Store(tm12, BitVecVal(9, 10), BitVecVal(221, 10))
tm12 = Store(tm12, BitVecVal(10, 10), BitVecVal(116, 10))
tm12 = Store(tm12, BitVecVal(11, 10), BitVecVal(31, 10))
tm12 = Store(tm12, BitVecVal(12, 10), BitVecVal(75, 10))
tm12 = Store(tm12, BitVecVal(13, 10), BitVecVal(189, 10))
tm12 = Store(tm12, BitVecVal(14, 10), BitVecVal(139, 10))
tm12 = Store(tm12, BitVecVal(15, 10), BitVecVal(138, 10))
I = Store(I, BitVecVal(12, 10), tm12)
tm13 = Array('tm13', BitVecSort(10), BitVecSort(10))
tm13 = Store(tm13, BitVecVal(0, 10), BitVecVal(112, 10))
tm13 = Store(tm13, BitVecVal(1, 10), BitVecVal(62, 10))
tm13 = Store(tm13, BitVecVal(2, 10), BitVecVal(181, 10))
tm13 = Store(tm13, BitVecVal(3, 10), BitVecVal(102, 10))
tm13 = Store(tm13, BitVecVal(4, 10), BitVecVal(72, 10))
tm13 = Store(tm13, BitVecVal(5, 10), BitVecVal(3, 10))
tm13 = Store(tm13, BitVecVal(6, 10), BitVecVal(246, 10))
tm13 = Store(tm13, BitVecVal(7, 10), BitVecVal(14, 10))
tm13 = Store(tm13, BitVecVal(8, 10), BitVecVal(97, 10))
tm13 = Store(tm13, BitVecVal(9, 10), BitVecVal(53, 10))
tm13 = Store(tm13, BitVecVal(10, 10), BitVecVal(87, 10))
tm13 = Store(tm13, BitVecVal(11, 10), BitVecVal(185, 10))
tm13 = Store(tm13, BitVecVal(12, 10), BitVecVal(134, 10))
tm13 = Store(tm13, BitVecVal(13, 10), BitVecVal(193, 10))
tm13 = Store(tm13, BitVecVal(14, 10), BitVecVal(29, 10))
tm13 = Store(tm13, BitVecVal(15, 10), BitVecVal(158, 10))
I = Store(I, BitVecVal(13, 10), tm13)
tm14 = Array('tm14', BitVecSort(10), BitVecSort(10))
tm14 = Store(tm14, BitVecVal(0, 10), BitVecVal(225, 10))
tm14 = Store(tm14, BitVecVal(1, 10), BitVecVal(248, 10))
tm14 = Store(tm14, BitVecVal(2, 10), BitVecVal(152, 10))
tm14 = Store(tm14, BitVecVal(3, 10), BitVecVal(17, 10))
tm14 = Store(tm14, BitVecVal(4, 10), BitVecVal(105, 10))
tm14 = Store(tm14, BitVecVal(5, 10), BitVecVal(217, 10))
tm14 = Store(tm14, BitVecVal(6, 10), BitVecVal(142, 10))
tm14 = Store(tm14, BitVecVal(7, 10), BitVecVal(148, 10))
tm14 = Store(tm14, BitVecVal(8, 10), BitVecVal(155, 10))
tm14 = Store(tm14, BitVecVal(9, 10), BitVecVal(30, 10))
tm14 = Store(tm14, BitVecVal(10, 10), BitVecVal(135, 10))
tm14 = Store(tm14, BitVecVal(11, 10), BitVecVal(233, 10))
tm14 = Store(tm14, BitVecVal(12, 10), BitVecVal(206, 10))
tm14 = Store(tm14, BitVecVal(13, 10), BitVecVal(85, 10))
tm14 = Store(tm14, BitVecVal(14, 10), BitVecVal(40, 10))
tm14 = Store(tm14, BitVecVal(15, 10), BitVecVal(223, 10))
I = Store(I, BitVecVal(14, 10), tm14)
tm15 = Array('tm15', BitVecSort(10), BitVecSort(10))
tm15 = Store(tm15, BitVecVal(0, 10), BitVecVal(140, 10))
tm15 = Store(tm15, BitVecVal(1, 10), BitVecVal(161, 10))
tm15 = Store(tm15, BitVecVal(2, 10), BitVecVal(137, 10))
tm15 = Store(tm15, BitVecVal(3, 10), BitVecVal(13, 10))
tm15 = Store(tm15, BitVecVal(4, 10), BitVecVal(191, 10))
tm15 = Store(tm15, BitVecVal(5, 10), BitVecVal(230, 10))
tm15 = Store(tm15, BitVecVal(6, 10), BitVecVal(66, 10))
tm15 = Store(tm15, BitVecVal(7, 10), BitVecVal(104, 10))
tm15 = Store(tm15, BitVecVal(8, 10), BitVecVal(65, 10))
tm15 = Store(tm15, BitVecVal(9, 10), BitVecVal(153, 10))
tm15 = Store(tm15, BitVecVal(10, 10), BitVecVal(45, 10))
tm15 = Store(tm15, BitVecVal(11, 10), BitVecVal(15, 10))
tm15 = Store(tm15, BitVecVal(12, 10), BitVecVal(176, 10))
tm15 = Store(tm15, BitVecVal(13, 10), BitVecVal(84, 10))
tm15 = Store(tm15, BitVecVal(14, 10), BitVecVal(187, 10))
tm15 = Store(tm15, BitVecVal(15, 10), BitVecVal(22, 10))
I = Store(I, BitVecVal(15, 10), tm15)

W = Array('W', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
tm16 = Array('tm0', BitVecSort(10), BitVecSort(10))
tm16 = Store(tm16, BitVecVal(0, 10), BitVecVal(43, 10))
tm16 = Store(tm16, BitVecVal(1, 10), BitVecVal(40, 10))
tm16 = Store(tm16, BitVecVal(2, 10), BitVecVal(171, 10))
tm16 = Store(tm16, BitVecVal(3, 10), BitVecVal(9, 10))
tm16 = Store(tm16, BitVecVal(4, 10), BitVecVal(160, 10))
tm16 = Store(tm16, BitVecVal(5, 10), BitVecVal(136, 10))
tm16 = Store(tm16, BitVecVal(6, 10), BitVecVal(35, 10))
tm16 = Store(tm16, BitVecVal(7, 10), BitVecVal(42, 10))
tm16 = Store(tm16, BitVecVal(8, 10), BitVecVal(242, 10))
tm16 = Store(tm16, BitVecVal(9, 10), BitVecVal(122, 10))
tm16 = Store(tm16, BitVecVal(10, 10), BitVecVal(89, 10))
tm16 = Store(tm16, BitVecVal(11, 10), BitVecVal(115, 10))
tm16 = Store(tm16, BitVecVal(12, 10), BitVecVal(61, 10))
tm16 = Store(tm16, BitVecVal(13, 10), BitVecVal(71, 10))
tm16 = Store(tm16, BitVecVal(14, 10), BitVecVal(30, 10))
tm16 = Store(tm16, BitVecVal(15, 10), BitVecVal(109, 10))
tm16 = Store(tm16, BitVecVal(16, 10), BitVecVal(239, 10))
tm16 = Store(tm16, BitVecVal(17, 10), BitVecVal(168, 10))
tm16 = Store(tm16, BitVecVal(18, 10), BitVecVal(182, 10))
tm16 = Store(tm16, BitVecVal(19, 10), BitVecVal(219, 10))
tm16 = Store(tm16, BitVecVal(20, 10), BitVecVal(212, 10))
tm16 = Store(tm16, BitVecVal(21, 10), BitVecVal(124, 10))
tm16 = Store(tm16, BitVecVal(22, 10), BitVecVal(202, 10))
tm16 = Store(tm16, BitVecVal(23, 10), BitVecVal(17, 10))
tm16 = Store(tm16, BitVecVal(24, 10), BitVecVal(109, 10))
tm16 = Store(tm16, BitVecVal(25, 10), BitVecVal(17, 10))
tm16 = Store(tm16, BitVecVal(26, 10), BitVecVal(219, 10))
tm16 = Store(tm16, BitVecVal(27, 10), BitVecVal(202, 10))
tm16 = Store(tm16, BitVecVal(28, 10), BitVecVal(78, 10))
tm16 = Store(tm16, BitVecVal(29, 10), BitVecVal(95, 10))
tm16 = Store(tm16, BitVecVal(30, 10), BitVecVal(132, 10))
tm16 = Store(tm16, BitVecVal(31, 10), BitVecVal(78, 10))
tm16 = Store(tm16, BitVecVal(32, 10), BitVecVal(234, 10))
tm16 = Store(tm16, BitVecVal(33, 10), BitVecVal(181, 10))
tm16 = Store(tm16, BitVecVal(34, 10), BitVecVal(49, 10))
tm16 = Store(tm16, BitVecVal(35, 10), BitVecVal(127, 10))
tm16 = Store(tm16, BitVecVal(36, 10), BitVecVal(172, 10))
tm16 = Store(tm16, BitVecVal(37, 10), BitVecVal(25, 10))
tm16 = Store(tm16, BitVecVal(38, 10), BitVecVal(40, 10))
tm16 = Store(tm16, BitVecVal(39, 10), BitVecVal(87, 10))
tm16 = Store(tm16, BitVecVal(40, 10), BitVecVal(208, 10))
tm16 = Store(tm16, BitVecVal(41, 10), BitVecVal(201, 10))
tm16 = Store(tm16, BitVecVal(42, 10), BitVecVal(225, 10))
tm16 = Store(tm16, BitVecVal(43, 10), BitVecVal(182, 10))
tm16 = Store(tm16, BitVecVal(44, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(45, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(46, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(47, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(48, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(49, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(50, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(51, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(52, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(53, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(54, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(55, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(56, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(57, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(58, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(59, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(60, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(61, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(62, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(63, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(64, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(65, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(66, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(67, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(68, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(69, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(70, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(71, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(72, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(73, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(74, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(75, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(76, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(77, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(78, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(79, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(80, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(81, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(82, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(83, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(84, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(85, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(86, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(87, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(88, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(89, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(90, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(91, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(92, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(93, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(94, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(95, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(96, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(97, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(98, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(99, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(100, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(101, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(102, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(103, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(104, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(105, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(106, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(107, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(108, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(109, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(110, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(111, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(112, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(113, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(114, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(115, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(116, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(117, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(118, 10), BitVecVal(0, 10))
tm16 = Store(tm16, BitVecVal(119, 10), BitVecVal(0, 10))
W = Store(W, BitVecVal(0, 10), tm16)
tm17 = Array('tm1', BitVecSort(10), BitVecSort(10))
tm17 = Store(tm17, BitVecVal(0, 10), BitVecVal(126, 10))
tm17 = Store(tm17, BitVecVal(1, 10), BitVecVal(174, 10))
tm17 = Store(tm17, BitVecVal(2, 10), BitVecVal(247, 10))
tm17 = Store(tm17, BitVecVal(3, 10), BitVecVal(207, 10))
tm17 = Store(tm17, BitVecVal(4, 10), BitVecVal(250, 10))
tm17 = Store(tm17, BitVecVal(5, 10), BitVecVal(84, 10))
tm17 = Store(tm17, BitVecVal(6, 10), BitVecVal(163, 10))
tm17 = Store(tm17, BitVecVal(7, 10), BitVecVal(108, 10))
tm17 = Store(tm17, BitVecVal(8, 10), BitVecVal(194, 10))
tm17 = Store(tm17, BitVecVal(9, 10), BitVecVal(150, 10))
tm17 = Store(tm17, BitVecVal(10, 10), BitVecVal(53, 10))
tm17 = Store(tm17, BitVecVal(11, 10), BitVecVal(89, 10))
tm17 = Store(tm17, BitVecVal(12, 10), BitVecVal(128, 10))
tm17 = Store(tm17, BitVecVal(13, 10), BitVecVal(22, 10))
tm17 = Store(tm17, BitVecVal(14, 10), BitVecVal(35, 10))
tm17 = Store(tm17, BitVecVal(15, 10), BitVecVal(122, 10))
tm17 = Store(tm17, BitVecVal(16, 10), BitVecVal(68, 10))
tm17 = Store(tm17, BitVecVal(17, 10), BitVecVal(82, 10))
tm17 = Store(tm17, BitVecVal(18, 10), BitVecVal(113, 10))
tm17 = Store(tm17, BitVecVal(19, 10), BitVecVal(11, 10))
tm17 = Store(tm17, BitVecVal(20, 10), BitVecVal(209, 10))
tm17 = Store(tm17, BitVecVal(21, 10), BitVecVal(131, 10))
tm17 = Store(tm17, BitVecVal(22, 10), BitVecVal(242, 10))
tm17 = Store(tm17, BitVecVal(23, 10), BitVecVal(249, 10))
tm17 = Store(tm17, BitVecVal(24, 10), BitVecVal(136, 10))
tm17 = Store(tm17, BitVecVal(25, 10), BitVecVal(11, 10))
tm17 = Store(tm17, BitVecVal(26, 10), BitVecVal(249, 10))
tm17 = Store(tm17, BitVecVal(27, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(28, 10), BitVecVal(84, 10))
tm17 = Store(tm17, BitVecVal(29, 10), BitVecVal(95, 10))
tm17 = Store(tm17, BitVecVal(30, 10), BitVecVal(166, 10))
tm17 = Store(tm17, BitVecVal(31, 10), BitVecVal(166, 10))
tm17 = Store(tm17, BitVecVal(32, 10), BitVecVal(210, 10))
tm17 = Store(tm17, BitVecVal(33, 10), BitVecVal(141, 10))
tm17 = Store(tm17, BitVecVal(34, 10), BitVecVal(43, 10))
tm17 = Store(tm17, BitVecVal(35, 10), BitVecVal(141, 10))
tm17 = Store(tm17, BitVecVal(36, 10), BitVecVal(119, 10))
tm17 = Store(tm17, BitVecVal(37, 10), BitVecVal(250, 10))
tm17 = Store(tm17, BitVecVal(38, 10), BitVecVal(209, 10))
tm17 = Store(tm17, BitVecVal(39, 10), BitVecVal(92, 10))
tm17 = Store(tm17, BitVecVal(40, 10), BitVecVal(20, 10))
tm17 = Store(tm17, BitVecVal(41, 10), BitVecVal(238, 10))
tm17 = Store(tm17, BitVecVal(42, 10), BitVecVal(63, 10))
tm17 = Store(tm17, BitVecVal(43, 10), BitVecVal(99, 10))
tm17 = Store(tm17, BitVecVal(44, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(45, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(46, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(47, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(48, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(49, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(50, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(51, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(52, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(53, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(54, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(55, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(56, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(57, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(58, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(59, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(60, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(61, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(62, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(63, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(64, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(65, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(66, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(67, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(68, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(69, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(70, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(71, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(72, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(73, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(74, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(75, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(76, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(77, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(78, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(79, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(80, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(81, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(82, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(83, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(84, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(85, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(86, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(87, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(88, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(89, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(90, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(91, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(92, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(93, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(94, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(95, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(96, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(97, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(98, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(99, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(100, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(101, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(102, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(103, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(104, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(105, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(106, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(107, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(108, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(109, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(110, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(111, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(112, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(113, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(114, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(115, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(116, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(117, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(118, 10), BitVecVal(0, 10))
tm17 = Store(tm17, BitVecVal(119, 10), BitVecVal(0, 10))
W = Store(W, BitVecVal(1, 10), tm17)
tm18 = Array('tm2', BitVecSort(10), BitVecSort(10))
tm18 = Store(tm18, BitVecVal(0, 10), BitVecVal(21, 10))
tm18 = Store(tm18, BitVecVal(1, 10), BitVecVal(210, 10))
tm18 = Store(tm18, BitVecVal(2, 10), BitVecVal(21, 10))
tm18 = Store(tm18, BitVecVal(3, 10), BitVecVal(79, 10))
tm18 = Store(tm18, BitVecVal(4, 10), BitVecVal(254, 10))
tm18 = Store(tm18, BitVecVal(5, 10), BitVecVal(44, 10))
tm18 = Store(tm18, BitVecVal(6, 10), BitVecVal(57, 10))
tm18 = Store(tm18, BitVecVal(7, 10), BitVecVal(118, 10))
tm18 = Store(tm18, BitVecVal(8, 10), BitVecVal(149, 10))
tm18 = Store(tm18, BitVecVal(9, 10), BitVecVal(185, 10))
tm18 = Store(tm18, BitVecVal(10, 10), BitVecVal(128, 10))
tm18 = Store(tm18, BitVecVal(11, 10), BitVecVal(246, 10))
tm18 = Store(tm18, BitVecVal(12, 10), BitVecVal(71, 10))
tm18 = Store(tm18, BitVecVal(13, 10), BitVecVal(254, 10))
tm18 = Store(tm18, BitVecVal(14, 10), BitVecVal(126, 10))
tm18 = Store(tm18, BitVecVal(15, 10), BitVecVal(136, 10))
tm18 = Store(tm18, BitVecVal(16, 10), BitVecVal(165, 10))
tm18 = Store(tm18, BitVecVal(17, 10), BitVecVal(91, 10))
tm18 = Store(tm18, BitVecVal(18, 10), BitVecVal(37, 10))
tm18 = Store(tm18, BitVecVal(19, 10), BitVecVal(173, 10))
tm18 = Store(tm18, BitVecVal(20, 10), BitVecVal(198, 10))
tm18 = Store(tm18, BitVecVal(21, 10), BitVecVal(157, 10))
tm18 = Store(tm18, BitVecVal(22, 10), BitVecVal(184, 10))
tm18 = Store(tm18, BitVecVal(23, 10), BitVecVal(21, 10))
tm18 = Store(tm18, BitVecVal(24, 10), BitVecVal(163, 10))
tm18 = Store(tm18, BitVecVal(25, 10), BitVecVal(62, 10))
tm18 = Store(tm18, BitVecVal(26, 10), BitVecVal(134, 10))
tm18 = Store(tm18, BitVecVal(27, 10), BitVecVal(147, 10))
tm18 = Store(tm18, BitVecVal(28, 10), BitVecVal(247, 10))
tm18 = Store(tm18, BitVecVal(29, 10), BitVecVal(201, 10))
tm18 = Store(tm18, BitVecVal(30, 10), BitVecVal(79, 10))
tm18 = Store(tm18, BitVecVal(31, 10), BitVecVal(220, 10))
tm18 = Store(tm18, BitVecVal(32, 10), BitVecVal(115, 10))
tm18 = Store(tm18, BitVecVal(33, 10), BitVecVal(186, 10))
tm18 = Store(tm18, BitVecVal(34, 10), BitVecVal(245, 10))
tm18 = Store(tm18, BitVecVal(35, 10), BitVecVal(41, 10))
tm18 = Store(tm18, BitVecVal(36, 10), BitVecVal(102, 10))
tm18 = Store(tm18, BitVecVal(37, 10), BitVecVal(220, 10))
tm18 = Store(tm18, BitVecVal(38, 10), BitVecVal(41, 10))
tm18 = Store(tm18, BitVecVal(39, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(40, 10), BitVecVal(249, 10))
tm18 = Store(tm18, BitVecVal(41, 10), BitVecVal(37, 10))
tm18 = Store(tm18, BitVecVal(42, 10), BitVecVal(12, 10))
tm18 = Store(tm18, BitVecVal(43, 10), BitVecVal(12, 10))
tm18 = Store(tm18, BitVecVal(44, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(45, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(46, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(47, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(48, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(49, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(50, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(51, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(52, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(53, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(54, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(55, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(56, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(57, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(58, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(59, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(60, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(61, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(62, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(63, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(64, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(65, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(66, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(67, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(68, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(69, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(70, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(71, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(72, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(73, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(74, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(75, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(76, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(77, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(78, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(79, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(80, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(81, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(82, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(83, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(84, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(85, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(86, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(87, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(88, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(89, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(90, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(91, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(92, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(93, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(94, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(95, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(96, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(97, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(98, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(99, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(100, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(101, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(102, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(103, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(104, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(105, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(106, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(107, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(108, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(109, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(110, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(111, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(112, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(113, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(114, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(115, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(116, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(117, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(118, 10), BitVecVal(0, 10))
tm18 = Store(tm18, BitVecVal(119, 10), BitVecVal(0, 10))
W = Store(W, BitVecVal(2, 10), tm18)
tm19 = Array('tm3', BitVecSort(10), BitVecSort(10))
tm19 = Store(tm19, BitVecVal(0, 10), BitVecVal(22, 10))
tm19 = Store(tm19, BitVecVal(1, 10), BitVecVal(166, 10))
tm19 = Store(tm19, BitVecVal(2, 10), BitVecVal(136, 10))
tm19 = Store(tm19, BitVecVal(3, 10), BitVecVal(60, 10))
tm19 = Store(tm19, BitVecVal(4, 10), BitVecVal(23, 10))
tm19 = Store(tm19, BitVecVal(5, 10), BitVecVal(177, 10))
tm19 = Store(tm19, BitVecVal(6, 10), BitVecVal(57, 10))
tm19 = Store(tm19, BitVecVal(7, 10), BitVecVal(5, 10))
tm19 = Store(tm19, BitVecVal(8, 10), BitVecVal(242, 10))
tm19 = Store(tm19, BitVecVal(9, 10), BitVecVal(67, 10))
tm19 = Store(tm19, BitVecVal(10, 10), BitVecVal(122, 10))
tm19 = Store(tm19, BitVecVal(11, 10), BitVecVal(127, 10))
tm19 = Store(tm19, BitVecVal(12, 10), BitVecVal(125, 10))
tm19 = Store(tm19, BitVecVal(13, 10), BitVecVal(62, 10))
tm19 = Store(tm19, BitVecVal(14, 10), BitVecVal(68, 10))
tm19 = Store(tm19, BitVecVal(15, 10), BitVecVal(59, 10))
tm19 = Store(tm19, BitVecVal(16, 10), BitVecVal(65, 10))
tm19 = Store(tm19, BitVecVal(17, 10), BitVecVal(127, 10))
tm19 = Store(tm19, BitVecVal(18, 10), BitVecVal(59, 10))
tm19 = Store(tm19, BitVecVal(19, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(20, 10), BitVecVal(248, 10))
tm19 = Store(tm19, BitVecVal(21, 10), BitVecVal(135, 10))
tm19 = Store(tm19, BitVecVal(22, 10), BitVecVal(188, 10))
tm19 = Store(tm19, BitVecVal(23, 10), BitVecVal(188, 10))
tm19 = Store(tm19, BitVecVal(24, 10), BitVecVal(122, 10))
tm19 = Store(tm19, BitVecVal(25, 10), BitVecVal(253, 10))
tm19 = Store(tm19, BitVecVal(26, 10), BitVecVal(65, 10))
tm19 = Store(tm19, BitVecVal(27, 10), BitVecVal(253, 10))
tm19 = Store(tm19, BitVecVal(28, 10), BitVecVal(14, 10))
tm19 = Store(tm19, BitVecVal(29, 10), BitVecVal(243, 10))
tm19 = Store(tm19, BitVecVal(30, 10), BitVecVal(178, 10))
tm19 = Store(tm19, BitVecVal(31, 10), BitVecVal(79, 10))
tm19 = Store(tm19, BitVecVal(32, 10), BitVecVal(33, 10))
tm19 = Store(tm19, BitVecVal(33, 10), BitVecVal(210, 10))
tm19 = Store(tm19, BitVecVal(34, 10), BitVecVal(96, 10))
tm19 = Store(tm19, BitVecVal(35, 10), BitVecVal(47, 10))
tm19 = Store(tm19, BitVecVal(36, 10), BitVecVal(243, 10))
tm19 = Store(tm19, BitVecVal(37, 10), BitVecVal(33, 10))
tm19 = Store(tm19, BitVecVal(38, 10), BitVecVal(65, 10))
tm19 = Store(tm19, BitVecVal(39, 10), BitVecVal(110, 10))
tm19 = Store(tm19, BitVecVal(40, 10), BitVecVal(168, 10))
tm19 = Store(tm19, BitVecVal(41, 10), BitVecVal(137, 10))
tm19 = Store(tm19, BitVecVal(42, 10), BitVecVal(200, 10))
tm19 = Store(tm19, BitVecVal(43, 10), BitVecVal(166, 10))
tm19 = Store(tm19, BitVecVal(44, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(45, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(46, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(47, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(48, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(49, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(50, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(51, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(52, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(53, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(54, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(55, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(56, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(57, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(58, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(59, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(60, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(61, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(62, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(63, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(64, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(65, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(66, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(67, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(68, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(69, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(70, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(71, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(72, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(73, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(74, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(75, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(76, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(77, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(78, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(79, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(80, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(81, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(82, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(83, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(84, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(85, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(86, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(87, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(88, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(89, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(90, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(91, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(92, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(93, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(94, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(95, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(96, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(97, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(98, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(99, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(100, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(101, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(102, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(103, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(104, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(105, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(106, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(107, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(108, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(109, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(110, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(111, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(112, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(113, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(114, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(115, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(116, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(117, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(118, 10), BitVecVal(0, 10))
tm19 = Store(tm19, BitVecVal(119, 10), BitVecVal(0, 10))
W = Store(W, BitVecVal(3, 10), tm19)

ret = Store(ret,BitVecVal(0, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(1, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(2, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(3, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(4, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(5, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(6, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(7, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(8, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(9, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(10, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(11, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(12, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(13, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(14, 10),BitVecVal(0, 10))
ret = Store(ret,BitVecVal(15, 10),BitVecVal(0, 10))


#,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10
def findOutput1(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,in16,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,S,W,I,ret):
    # S = Array('S', BitVecSort(10), BitVecSort(10))
    # S2 = Array('S2', BitVecSort(10), BitVecSort(10))
    # I = Array('A', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
    # W = Array('W', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
    # tm = Array('tm', BitVecSort(10), BitVecSort(10))
    # tm2 = Array('tm2', BitVecSort(10), BitVecSort(10))
    # ret = Array('ret', BitVecSort(10), BitVecSort(10))
    # for i in range(16):
    #     ret = Store(ret,i,0)

    # # DIP1 =  73,91,20,4,9,16,0,13,4,13,46,0,15,6,9,19

    # ## Initializing the `Sbox` array ##
    # i = 0
    # for arr in Sbox:
    #     j = 0
    #     for elem in arr:
    #         tm = Store(tm, BitVecVal(j, 10), BitVecVal(elem, 10))
    #         j += 1
    #     I = Store(I, BitVecVal(i, 10), tm)
    #     i += 1

    #  ## Initilaizing the `word` array ##
    # i = 0
    # for arr in word:
    #     j = 0
    #     for elem in arr:
    #         tm2 = Store(tm2, BitVecVal(j, 10), BitVecVal(elem, 10))
    #         j += 1
    #     W = Store(W, BitVecVal(i, 10), tm2)
    #     i += 1
    # #print(S[0])

# ------------------ Add Round Key ----------------

    S = Store(S, 0, in1)
    S = Store(S, 1, in2)
    S = Store(S, 2, in3)
    S = Store(S, 3, in4)
    S = Store(S, 4, in5)
    S = Store(S, 5, in6)
    S = Store(S, 6, in7)
    S = Store(S, 7, in8)
    S = Store(S, 8, in9)
    S = Store(S, 9, in10)
    S = Store(S, 10, in11)
    S = Store(S, 11, in12)
    S = Store(S, 12, in13)
    S = Store(S, 13, in14)
    S = Store(S, 14, in15)
    S = Store(S, 15, in16)


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

    s1_0,s1_1,s1_2,s1_3,s1_4,s1_5,s1_6,s1_7,s1_8,s1_9,s1_10,s1_11,s1_12,s1_13,s1_14,s1_15=BitVecs('s1_0 s1_1 s1_2 s1_3 s1_4 s1_5 s1_6 s1_7 s1_8 s1_9 s1_10 s1_11 s1_12 s1_13 s1_14 s1_15',10)
    s1_0b,s1_1b,s1_2b,s1_3b,s1_4b,s1_5b,s1_6b,s1_7b,s1_8b,s1_9b,s1_10b,s1_11b,s1_12b,s1_13b,s1_14b,s1_15b=BitVecs('s1_0b s1_1b s1_2b s1_3b s1_4b s1_5b s1_6b s1_7b s1_8b s1_9b s1_10b s1_11b s1_12b s1_13b s1_14b s1_15b',10)

    s1_1 = S[1] >> 4
    s1_1b = S[1] & 0xf
    s1_5 = S[5] >> 4
    s1_5b = S[5] & 0xf
    s1_9 = S[9] >> 4
    s1_9b = S[9] & 0xf
    s1_13= S[13] >> 4
    s1_13b= S[13] & 0xf


    s1_2 = S[2] >> 4
    s1_2b = S[2] & 0xf
    s1_10= S[10] >> 4
    s1_10b= S[10] & 0xf
    s1_6 = S[6] >> 4
    s1_6b = S[6] & 0xf
    s1_14 = S[14] >> 4
    s1_14b = S[14] & 0xf

    s1_3 = S[3] >> 4
    s1_3b = S[3] & 0xf
    s1_15 = S[15] >> 4
    s1_15b = S[15] & 0xf
    s1_11 = S[11] >> 4
    s1_11b = S[11] & 0xf
    s1_7= S[7] >> 4
    s1_7b= S[7] & 0xf

    s1_0=S[0] >> 4
    s1_0b=S[0] & 0xf
    s1_4 = S[4] >> 4
    s1_4b = S[4] & 0xf
    s1_8 = S[8] >> 4
    s1_8b = S[8] & 0xf
    s1_12 = S[12] >> 4
    s1_12b = S[12] & 0xf

    temp = I[s1_1][s1_1b]
    S = Store(S, BitVecVal(1, 10),I[s1_5][s1_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s1_9][s1_9b])
    S = Store(S, BitVecVal(9, 10),I[s1_13][s1_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s1_2][s1_2b]
    S = Store(S, BitVecVal(2, 10), I[s1_10][s1_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s1_6][s1_6b]
    S = Store(S, BitVecVal(6, 10), I[s1_14][s1_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s1_3][s1_3b]
    S = Store(S, BitVecVal(3, 10), I[s1_15][s1_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s1_11][s1_11b])
    S = Store(S, BitVecVal(11, 10), I[s1_7][s1_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s1_0][s1_0b])
    S = Store(S, BitVecVal(4, 10), I[s1_4][s1_4b])
    S = Store(S, BitVecVal(8, 10), I[s1_8][s1_8b])
    S = Store(S, BitVecVal(12, 10),I[s1_12][s1_12b])


#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(1,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    
    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1)
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] 
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] 
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) 
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

    ret = Store(ret, 10,  S[10] << 1) 
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 2-----------------------------------------------------------------

    s2_0,s2_1,s2_2,s2_3,s2_4,s2_5,s2_6,s2_7,s2_8,s2_9,s2_10,s2_11,s2_12,s2_13,s2_14,s2_15=BitVecs('s2_0 s2_1 s2_2 s2_3 s2_4 s2_5 s2_6 s2_7 s2_8 s2_9 s2_10 s2_11 s2_12 s2_13 s2_14 s2_15',10)
    s2_0b,s2_1b,s2_2b,s2_3b,s2_4b,s2_5b,s2_6b,s2_7b,s2_8b,s2_9b,s2_10b,s2_11b,s2_12b,s2_13b,s2_14b,s2_15b=BitVecs('s2_0b s2_1b s2_2b s2_3b s2_4b s2_5b s2_6b s2_7b s2_8b s2_9b s2_10b s2_11b s2_12b s2_13b s2_14b s2_15b',10)

    s2_1 = S[1] >> 4
    s2_1b = S[1] & 0xf
    s2_5 = S[5] >> 4
    s2_5b = S[5] & 0xf
    s2_9 = S[9] >> 4
    s2_9b = S[9] & 0xf
    s2_13= S[13] >> 4
    s2_13b= S[13] & 0xf


    s2_2 = S[2] >> 4
    s2_2b = S[2] & 0xf
    s2_10= S[10] >> 4
    s2_10b= S[10] & 0xf
    s2_6 = S[6] >> 4
    s2_6b = S[6] & 0xf
    s2_14 = S[14] >> 4
    s2_14b = S[14] & 0xf

    s2_3 = S[3] >> 4
    s2_3b = S[3] & 0xf
    s2_15 = S[15] >> 4
    s2_15b = S[15] & 0xf
    s2_11 = S[11] >> 4
    s2_11b = S[11] & 0xf
    s2_7= S[7] >> 4
    s2_7b= S[7] & 0xf

    s2_0=S[0] >> 4
    s2_0b=S[0] & 0xf
    s2_4 = S[4] >> 4
    s2_4b = S[4] & 0xf
    s2_8 = S[8] >> 4
    s2_8b = S[8] & 0xf
    s2_12 = S[12] >> 4
    s2_12b = S[12] & 0xf

    temp = I[s2_1][s2_1b]
    S = Store(S, BitVecVal(1, 10),I[s2_5][s2_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s2_9][s2_9b])
    S = Store(S, BitVecVal(9, 10),I[s2_13][s2_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s2_2][s2_2b]
    S = Store(S, BitVecVal(2, 10), I[s2_10][s2_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s2_6][s2_6b]
    S = Store(S, BitVecVal(6, 10), I[s2_14][s2_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s2_3][s2_3b]
    S = Store(S, BitVecVal(3, 10), I[s2_15][s2_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s2_11][s2_11b])
    S = Store(S, BitVecVal(11, 10), I[s2_7][s2_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s2_0][s2_0b])
    S = Store(S, BitVecVal(4, 10), I[s2_4][s2_4b])
    S = Store(S, BitVecVal(8, 10), I[s2_8][s2_8b])
    S = Store(S, BitVecVal(12, 10),I[s2_12][s2_12b])


# #-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(2,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

# #----------------------------------Iteration 3-----------------------------------------------------------------

    s3_0,s3_1,s3_2,s3_3,s3_4,s3_5,s3_6,s3_7,s3_8,s3_9,s3_10,s3_11,s3_12,s3_13,s3_14,s3_15=BitVecs('s3_0 s3_1 s3_2 s3_3 s3_4 s3_5 s3_6 s3_7 s3_8 s3_9 s3_10 s3_11 s3_12 s3_13 s3_14 s3_15',10)
    s3_0b,s3_1b,s3_2b,s3_3b,s3_4b,s3_5b,s3_6b,s3_7b,s3_8b,s3_9b,s3_10b,s3_11b,s3_12b,s3_13b,s3_14b,s3_15b=BitVecs('s3_0b s3_1b s3_2b s3_3b s3_4b s3_5b s3_6b s3_7b s3_8b s3_9b s3_10b s3_11b s3_12b s3_13b s3_14b s3_15b',10)

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
    S = Store(S, BitVecVal(1, 10),I[s3_5][s3_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s3_9][s3_9b])
    S = Store(S, BitVecVal(9, 10),I[s3_13][s3_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s3_2][s3_2b]
    S = Store(S, BitVecVal(2, 10), I[s3_10][s3_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s3_6][s3_6b]
    S = Store(S, BitVecVal(6, 10), I[s3_14][s3_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s3_3][s3_3b]
    S = Store(S, BitVecVal(3, 10), I[s3_15][s3_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s3_11][s3_11b])
    S = Store(S, BitVecVal(11, 10), I[s3_7][s3_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s3_0][s3_0b])
    S = Store(S, BitVecVal(4, 10), I[s3_4][s3_4b])
    S = Store(S, BitVecVal(8, 10), I[s3_8][s3_8b])
    S = Store(S, BitVecVal(12, 10),I[s3_12][s3_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(3,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 4-----------------------------------------------------------------

    s4_0,s4_1,s4_2,s4_3,s4_4,s4_5,s4_6,s4_7,s4_8,s4_9,s4_10,s4_11,s4_12,s4_13,s4_14,s4_15=BitVecs('s4_0 s4_1 s4_2 s4_3 s4_4 s4_5 s4_6 s4_7 s4_8 s4_9 s4_10 s4_11 s4_12 s4_13 s4_14 s4_15',10)
    s4_0b,s4_1b,s4_2b,s4_3b,s4_4b,s4_5b,s4_6b,s4_7b,s4_8b,s4_9b,s4_10b,s4_11b,s4_12b,s4_13b,s4_14b,s4_15b=BitVecs('s4_0b s4_1b s4_2b s4_3b s4_4b s4_5b s4_6b s4_7b s4_8b s4_9b s4_10b s4_11b s4_12b s4_13b s4_14b s4_15b',10)

    s4_1 = S[1] >> 4
    s4_1b = S[1] & 0xf
    s4_5 = S[5] >> 4
    s4_5b = S[5] & 0xf
    s4_9 = S[9] >> 4
    s4_9b = S[9] & 0xf
    s4_13= S[13] >> 4
    s4_13b= S[13] & 0xf


    s4_2 = S[2] >> 4
    s4_2b = S[2] & 0xf
    s4_10= S[10] >> 4
    s4_10b= S[10] & 0xf
    s4_6 = S[6] >> 4
    s4_6b = S[6] & 0xf
    s4_14 = S[14] >> 4
    s4_14b = S[14] & 0xf

    s4_3 = S[3] >> 4
    s4_3b = S[3] & 0xf
    s4_15 = S[15] >> 4
    s4_15b = S[15] & 0xf
    s4_11 = S[11] >> 4
    s4_11b = S[11] & 0xf
    s4_7= S[7] >> 4
    s4_7b= S[7] & 0xf

    s4_0=S[0] >> 4
    s4_0b=S[0] & 0xf
    s4_4 = S[4] >> 4
    s4_4b = S[4] & 0xf
    s4_8 = S[8] >> 4
    s4_8b = S[8] & 0xf
    s4_12 = S[12] >> 4
    s4_12b = S[12] & 0xf

    temp = I[s4_1][s4_1b]
    S = Store(S, BitVecVal(1, 10),I[s4_5][s4_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s4_9][s4_9b])
    S = Store(S, BitVecVal(9, 10),I[s4_13][s4_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s4_2][s4_2b]
    S = Store(S, BitVecVal(2, 10), I[s4_10][s4_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s4_6][s4_6b]
    S = Store(S, BitVecVal(6, 10), I[s4_14][s4_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s4_3][s4_3b]
    S = Store(S, BitVecVal(3, 10), I[s4_15][s4_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s4_11][s4_11b])
    S = Store(S, BitVecVal(11, 10), I[s4_7][s4_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s4_0][s4_0b])
    S = Store(S, BitVecVal(4, 10), I[s4_4][s4_4b])
    S = Store(S, BitVecVal(8, 10), I[s4_8][s4_8b])
    S = Store(S, BitVecVal(12, 10),I[s4_12][s4_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(4,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 5-----------------------------------------------------------------

    s5_0,s5_1,s5_2,s5_3,s5_4,s5_5,s5_6,s5_7,s5_8,s5_9,s5_10,s5_11,s5_12,s5_13,s5_14,s5_15=BitVecs('s5_0 s5_1 s5_2 s5_3 s5_4 s5_5 s5_6 s5_7 s5_8 s5_9 s5_10 s5_11 s5_12 s5_13 s5_14 s5_15',10)
    s5_0b,s5_1b,s5_2b,s5_3b,s5_4b,s5_5b,s5_6b,s5_7b,s5_8b,s5_9b,s5_10b,s5_11b,s5_12b,s5_13b,s5_14b,s5_15b=BitVecs('s5_0b s5_1b s5_2b s5_3b s5_4b s5_5b s5_6b s5_7b s5_8b s5_9b s5_10b s5_11b s5_12b s5_13b s5_14b s5_15b',10)

    s5_1 = S[1] >> 4
    s5_1b = S[1] & 0xf
    s5_5 = S[5] >> 4
    s5_5b = S[5] & 0xf
    s5_9 = S[9] >> 4
    s5_9b = S[9] & 0xf
    s5_13= S[13] >> 4
    s5_13b= S[13] & 0xf


    s5_2 = S[2] >> 4
    s5_2b = S[2] & 0xf
    s5_10= S[10] >> 4
    s5_10b= S[10] & 0xf
    s5_6 = S[6] >> 4
    s5_6b = S[6] & 0xf
    s5_14 = S[14] >> 4
    s5_14b = S[14] & 0xf

    s5_3 = S[3] >> 4
    s5_3b = S[3] & 0xf
    s5_15 = S[15] >> 4
    s5_15b = S[15] & 0xf
    s5_11 = S[11] >> 4
    s5_11b = S[11] & 0xf
    s5_7= S[7] >> 4
    s5_7b= S[7] & 0xf

    s5_0=S[0] >> 4
    s5_0b=S[0] & 0xf
    s5_4 = S[4] >> 4
    s5_4b = S[4] & 0xf
    s5_8 = S[8] >> 4
    s5_8b = S[8] & 0xf
    s5_12 = S[12] >> 4
    s5_12b = S[12] & 0xf

    temp = I[s5_1][s5_1b]
    S = Store(S, BitVecVal(1, 10),I[s5_5][s5_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s5_9][s5_9b])
    S = Store(S, BitVecVal(9, 10),I[s5_13][s5_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s5_2][s5_2b]
    S = Store(S, BitVecVal(2, 10), I[s5_10][s5_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s5_6][s5_6b]
    S = Store(S, BitVecVal(6, 10), I[s5_14][s5_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s5_3][s5_3b]
    S = Store(S, BitVecVal(3, 10), I[s5_15][s5_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s5_11][s5_11b])
    S = Store(S, BitVecVal(11, 10), I[s5_7][s5_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s5_0][s5_0b])
    S = Store(S, BitVecVal(4, 10), I[s5_4][s5_4b])
    S = Store(S, BitVecVal(8, 10), I[s5_8][s5_8b])
    S = Store(S, BitVecVal(12, 10),I[s5_12][s5_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(5,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])



# --------------------------------Iteration 6 ----------------------------------------------------------------------------------

    s6_0,s6_1,s6_2,s6_3,s6_4,s6_5,s6_6,s6_7,s6_8,s6_9,s6_10,s6_11,s6_12,s6_13,s6_14,s6_15=BitVecs('s6_0 s6_1 s6_2 s6_3 s6_4 s6_5 s6_6 s6_7 s6_8 s6_9 s6_10 s6_11 s6_12 s6_13 s6_14 s6_15',10)
    s6_0b,s6_1b,s6_2b,s6_3b,s6_4b,s6_5b,s6_6b,s6_7b,s6_8b,s6_9b,s6_10b,s6_11b,s6_12b,s6_13b,s6_14b,s6_15b=BitVecs('s6_0b s6_1b s6_2b s6_3b s6_4b s6_5b s6_6b s6_7b s6_8b s6_9b s6_10b s6_11b s6_12b s6_13b s6_14b s6_15b',10)

    s6_1 = S[1] >> 4
    s6_1b = S[1] & 0xf
    s6_5 = S[5] >> 4
    s6_5b = S[5] & 0xf
    s6_9 = S[9] >> 4
    s6_9b = S[9] & 0xf
    s6_13= S[13] >> 4
    s6_13b= S[13] & 0xf


    s6_2 = S[2] >> 4
    s6_2b = S[2] & 0xf
    s6_10= S[10] >> 4
    s6_10b= S[10] & 0xf
    s6_6 = S[6] >> 4
    s6_6b = S[6] & 0xf
    s6_14 = S[14] >> 4
    s6_14b = S[14] & 0xf

    s6_3 = S[3] >> 4
    s6_3b = S[3] & 0xf
    s6_15 = S[15] >> 4
    s6_15b = S[15] & 0xf
    s6_11 = S[11] >> 4
    s6_11b = S[11] & 0xf
    s6_7= S[7] >> 4
    s6_7b= S[7] & 0xf

    s6_0=S[0] >> 4
    s6_0b=S[0] & 0xf
    s6_4 = S[4] >> 4
    s6_4b = S[4] & 0xf
    s6_8 = S[8] >> 4
    s6_8b = S[8] & 0xf
    s6_12 = S[12] >> 4
    s6_12b = S[12] & 0xf

    temp = I[s6_1][s6_1b]
    S = Store(S, BitVecVal(1, 10),I[s6_5][s6_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s6_9][s6_9b])
    S = Store(S, BitVecVal(9, 10),I[s6_13][s6_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s6_2][s6_2b]
    S = Store(S, BitVecVal(2, 10), I[s6_10][s6_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s6_6][s6_6b]
    S = Store(S, BitVecVal(6, 10), I[s6_14][s6_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s6_3][s6_3b]
    S = Store(S, BitVecVal(3, 10), I[s6_15][s6_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s6_11][s6_11b])
    S = Store(S, BitVecVal(11, 10), I[s6_7][s6_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s6_0][s6_0b])
    S = Store(S, BitVecVal(4, 10), I[s6_4][s6_4b])
    S = Store(S, BitVecVal(8, 10), I[s6_8][s6_8b])
    S = Store(S, BitVecVal(12, 10),I[s6_12][s6_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(6,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 7-----------------------------------------------------------------

    s7_0,s7_1,s7_2,s7_3,s7_4,s7_5,s7_6,s7_7,s7_8,s7_9,s7_10,s7_11,s7_12,s7_13,s7_14,s7_15=BitVecs('s7_0 s7_1 s7_2 s7_3 s7_4 s7_5 s7_6 s7_7 s7_8 s7_9 s7_10 s7_11 s7_12 s7_13 s7_14 s7_15',10)
    s7_0b,s7_1b,s7_2b,s7_3b,s7_4b,s7_5b,s7_6b,s7_7b,s7_8b,s7_9b,s7_10b,s7_11b,s7_12b,s7_13b,s7_14b,s7_15b=BitVecs('s7_0b s7_1b s7_2b s7_3b s7_4b s7_5b s7_6b s7_7b s7_8b s7_9b s7_10b s7_11b s7_12b s7_13b s7_14b s7_15b',10)

    s7_1 = S[1] >> 4
    s7_1b = S[1] & 0xf
    s7_5 = S[5] >> 4
    s7_5b = S[5] & 0xf
    s7_9 = S[9] >> 4
    s7_9b = S[9] & 0xf
    s7_13= S[13] >> 4
    s7_13b= S[13] & 0xf


    s7_2 = S[2] >> 4
    s7_2b = S[2] & 0xf
    s7_10= S[10] >> 4
    s7_10b= S[10] & 0xf
    s7_6 = S[6] >> 4
    s7_6b = S[6] & 0xf
    s7_14 = S[14] >> 4
    s7_14b = S[14] & 0xf

    s7_3 = S[3] >> 4
    s7_3b = S[3] & 0xf
    s7_15 = S[15] >> 4
    s7_15b = S[15] & 0xf
    s7_11 = S[11] >> 4
    s7_11b = S[11] & 0xf
    s7_7= S[7] >> 4
    s7_7b= S[7] & 0xf

    s7_0=S[0] >> 4
    s7_0b=S[0] & 0xf
    s7_4 = S[4] >> 4
    s7_4b = S[4] & 0xf
    s7_8 = S[8] >> 4
    s7_8b = S[8] & 0xf
    s7_12 = S[12] >> 4
    s7_12b = S[12] & 0xf

    temp = I[s7_1][s7_1b]
    S = Store(S, BitVecVal(1, 10),I[s7_5][s7_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s7_9][s7_9b])
    S = Store(S, BitVecVal(9, 10),I[s7_13][s7_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s7_2][s7_2b]
    S = Store(S, BitVecVal(2, 10), I[s7_10][s7_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s7_6][s7_6b]
    S = Store(S, BitVecVal(6, 10), I[s7_14][s7_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s7_3][s7_3b]
    S = Store(S, BitVecVal(3, 10), I[s7_15][s7_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s7_11][s7_11b])
    S = Store(S, BitVecVal(11, 10), I[s7_7][s7_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s7_0][s7_0b])
    S = Store(S, BitVecVal(4, 10), I[s7_4][s7_4b])
    S = Store(S, BitVecVal(8, 10), I[s7_8][s7_8b])
    S = Store(S, BitVecVal(12, 10),I[s7_12][s7_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(7,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 8-----------------------------------------------------------------

    s8_0,s8_1,s8_2,s8_3,s8_4,s8_5,s8_6,s8_7,s8_8,s8_9,s8_10,s8_11,s8_12,s8_13,s8_14,s8_15=BitVecs('s8_0 s8_1 s8_2 s8_3 s8_4 s8_5 s8_6 s8_7 s8_8 s8_9 s8_10 s8_11 s8_12 s8_13 s8_14 s8_15',10)
    s8_0b,s8_1b,s8_2b,s8_3b,s8_4b,s8_5b,s8_6b,s8_7b,s8_8b,s8_9b,s8_10b,s8_11b,s8_12b,s8_13b,s8_14b,s8_15b=BitVecs('s8_0b s8_1b s8_2b s8_3b s8_4b s8_5b s8_6b s8_7b s8_8b s8_9b s8_10b s8_11b s8_12b s8_13b s8_14b s8_15b',10)

    s8_1 = S[1] >> 4
    s8_1b = S[1] & 0xf
    s8_5 = S[5] >> 4
    s8_5b = S[5] & 0xf
    s8_9 = S[9] >> 4
    s8_9b = S[9] & 0xf
    s8_13= S[13] >> 4
    s8_13b= S[13] & 0xf


    s8_2 = S[2] >> 4
    s8_2b = S[2] & 0xf
    s8_10= S[10] >> 4
    s8_10b= S[10] & 0xf
    s8_6 = S[6] >> 4
    s8_6b = S[6] & 0xf
    s8_14 = S[14] >> 4
    s8_14b = S[14] & 0xf

    s8_3 = S[3] >> 4
    s8_3b = S[3] & 0xf
    s8_15 = S[15] >> 4
    s8_15b = S[15] & 0xf
    s8_11 = S[11] >> 4
    s8_11b = S[11] & 0xf
    s8_7= S[7] >> 4
    s8_7b= S[7] & 0xf

    s8_0=S[0] >> 4
    s8_0b=S[0] & 0xf
    s8_4 = S[4] >> 4
    s8_4b = S[4] & 0xf
    s8_8 = S[8] >> 4
    s8_8b = S[8] & 0xf
    s8_12 = S[12] >> 4
    s8_12b = S[12] & 0xf

    temp = I[s8_1][s8_1b]
    S = Store(S, BitVecVal(1, 10),I[s8_5][s8_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s8_9][s8_9b])
    S = Store(S, BitVecVal(9, 10),I[s8_13][s8_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s8_2][s8_2b]
    S = Store(S, BitVecVal(2, 10), I[s8_10][s8_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s8_6][s8_6b]
    S = Store(S, BitVecVal(6, 10), I[s8_14][s8_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s8_3][s8_3b]
    S = Store(S, BitVecVal(3, 10), I[s8_15][s8_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s8_11][s8_11b])
    S = Store(S, BitVecVal(11, 10), I[s8_7][s8_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s8_0][s8_0b])
    S = Store(S, BitVecVal(4, 10), I[s8_4][s8_4b])
    S = Store(S, BitVecVal(8, 10), I[s8_8][s8_8b])
    S = Store(S, BitVecVal(12, 10),I[s8_12][s8_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(8,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
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

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------Iteration 9-----------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',10)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',10)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[10] >> 4
    s9_10b= S[10] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[15] >> 4
    s9_15b = S[15] & 0xf
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
    S = Store(S, BitVecVal(1, 10),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 10),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 10), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s9_6][s9_6b]
    S = Store(S, BitVecVal(6, 10), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 10), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 10), I[s9_7][s9_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 10), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 10), I[s9_8][s9_8b])
    S = Store(S, BitVecVal(12, 10),I[s9_12][s9_12b])

#-----------------------------------MixColumn AddRoundKey-----------------------------------------------------

    n = BitVecVal(9,10)
    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2] ^ S[3] ^ W[0][4*n]))

    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1, If(ret[1] >> 8 == 1, ret[1] ^ 283, ret[1]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1] ^ (x ^ 283), ret[1] ^ x))
    ret = Store(ret, 1, ret[1] ^ (S[3] ^ S[0] ^ W[1][4*n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
    ret = Store(ret, 3, If(ret[3] >> 8 == 1, ret[3] ^ 283, ret[3]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3] ^ (x ^ 283), ret[3] ^ x))
    ret = Store(ret, 3, ret[3] ^ (S[1] ^ S[2] ^ W[3][4*n]))

    ret = Store(ret, 4, S[4] << 1)
    ret = Store(ret, 4, If(ret[4] >> 8 == 1, ret[4] ^ key5, ret[4]))
    x = S[5]
    x = x ^ (x << 1)
    ret = Store(ret, 4, If(x >> 8 == 1, ret[4] ^ (x ^ 283), ret[4] ^ x))
    ret = Store(ret, 4, ret[4] ^ (S[6] ^ S[7] ^ W[0][1+4*n]))

    ret = Store(ret, 5,  S[5] << 1) #key6 5
    ret = Store(ret, 5, If(ret[5] >> 8 == 1, ret[5] ^ 283, ret[5]))
    x = S[6] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 5, If(x >> 8 == 1, ret[5] ^ (x ^ 283), ret[5] ^ x))
    ret = Store(ret, 5, ret[5] ^ (S[7] ^ S[4] ^ W[1][1+4*n]))

    ret = Store(ret, 6,  S[6] << 1)
    ret = Store(ret, 6, If( ret[6] >> 8 == 1, ret[6] ^ 283, ret[6]))
    x = S[7] #key8 7
    x = x ^ (x << 1)
    ret = Store(ret, 6, If( x >> 8 == 1, ret[6] ^ (x ^ 283),  ret[6] ^ x))
    ret = Store(ret, 6, ret[6] ^ (S[4] ^ S[5] ^ W[2][1+4*n]))

    ret = Store(ret, 7,  S[7] << 1)
    ret = Store(ret, 7, If(ret[7] >> 8 == 1, ret[7] ^ 283, ret[7]))
    x = S[4]
    x = x ^ (x << 1)
    ret = Store(ret, 7, If(x >> 8 == 1, ret[7] ^ (x ^ 283), ret[7] ^ x)) #key9 8
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

    ret = Store(ret, 10,  S[10] << 1) #key10 10
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

    S = Store(S, BitVecVal(0,10), ret[0])
    S = Store(S, BitVecVal(1,10), ret[1])
    S = Store(S, BitVecVal(2,10), ret[2])
    S = Store(S, BitVecVal(3,10), ret[3])
    S = Store(S, BitVecVal(4,10), ret[4])
    S = Store(S, BitVecVal(5,10), ret[5])
    S = Store(S, BitVecVal(6,10), ret[6])
    S = Store(S, BitVecVal(7,10), ret[7])
    S = Store(S, BitVecVal(8,10), ret[8])
    S = Store(S, BitVecVal(9,10), ret[9])
    S = Store(S, BitVecVal(10,10), ret[10])
    S = Store(S, BitVecVal(11,10), ret[11])
    S = Store(S, BitVecVal(12,10), ret[12])
    S = Store(S, BitVecVal(13,10), ret[13])
    S = Store(S, BitVecVal(14,10), ret[14])
    S = Store(S, BitVecVal(15,10), ret[15])

#----------------------------------ByteshiftRow--------------------------------------------------------------

    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',10)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',10)

    s9_1 = S[1] >> 4
    s9_1b = S[1] & 0xf
    s9_5 = S[5] >> 4
    s9_5b = S[5] & 0xf
    s9_9 = S[9] >> 4
    s9_9b = S[9] & 0xf
    s9_13= S[13] >> 4
    s9_13b= S[13] & 0xf


    s9_2 = S[2] >> 4
    s9_2b = S[2] & 0xf
    s9_10= S[10] >> 4
    s9_10b= S[10] & 0xf
    s9_6 = S[6] >> 4
    s9_6b = S[6] & 0xf
    s9_14 = S[14] >> 4
    s9_14b = S[14] & 0xf

    s9_3 = S[3] >> 4
    s9_3b = S[3] & 0xf
    s9_15 = S[15] >> 4
    s9_15b = S[15] & 0xf
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
    S = Store(S, BitVecVal(1, 10),I[s9_5][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),I[s9_9][s9_9b])
    S = Store(S, BitVecVal(9, 10),I[s9_13][s9_13b])
    S = Store(S, BitVecVal(13, 10),temp)

    temp = I[s9_2][s9_2b]
    S = Store(S, BitVecVal(2, 10), I[s9_10][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), temp)
    temp = I[s9_6][s9_6b]
    S = Store(S, BitVecVal(6, 10), I[s9_14][s9_14b])
    S = Store(S, BitVecVal(14, 10),temp)

    temp = I[s9_3][s9_3b]
    S = Store(S, BitVecVal(3, 10), I[s9_15][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), I[s9_11][s9_11b])
    S = Store(S, BitVecVal(11, 10), I[s9_7][s9_7b])
    S = Store(S, BitVecVal(7, 10), temp)

    S = Store(S, BitVecVal(0, 10), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 10), I[s9_4][s9_4b])
    S = Store(S, BitVecVal(8, 10), I[s9_8][s9_8b])
    S = Store(S, BitVecVal(12, 10),I[s9_12][s9_12b])


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


def sub(in1 , in2 , in3 , in4 , in5 , in6 , in7 , in8 , in9, in10 , in11 , in12 , in13 , in14 , in15 , in16 ,key1,key2,key3,key4,key5,S,W,I,ret):
    # S = Array('S', BitVecSort(10), BitVecSort(10))
    # S2 = Array('S2', BitVecSort(10), BitVecSort(10))
    # I = Array('A', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
    # W = Array('W', BitVecSort(10), ArraySort(BitVecSort(10), BitVecSort(10)))
    # tm = Array('tm', BitVecSort(10), BitVecSort(10))
    # tm2 = Array('tm2', BitVecSort(10), BitVecSort(10))

    # ## Initializing the `Sbox` array ##
    # i = 0
    # for arr in Sbox:
    #     j = 0
    #     for elem in arr:
    #         # tm = Store(tm, BitVecVal(j, 10), BitVecVal(elem, 10))
    #         tm[j] == BitVecVal(elem, 10)
    #         j += 1
    #     I = Store(I, BitVecVal(i, 10), tm)
    #     i += 1

    #  ## Initilaizing the `word` array ##
    # i = 0
    # for arr in word:
    #     j = 0
    #     for elem in arr:
    #         tm2 = Store(tm2, BitVecVal(j, 10), BitVecVal(elem, 10))
    #         j += 1
    #     W = Store(W, BitVecVal(i, 10), tm2)
    #     i += 1



    # ------------------ Add Round Key ----------------
    n=BitVecVal(0,10)
    nb=BitVecVal(4,10)


    S = Store(S, 0, in1)
    S = Store(S, 1, in2)
    S = Store(S, 2, in3)
    S = Store(S, 3, in4)
    S = Store(S, 4, in5)
    S = Store(S, 5, in6)
    S = Store(S, 6, in7)
    S = Store(S, 7, in8)
    S = Store(S, 8, in9)
    S = Store(S, 9, in10)
    S = Store(S, 10, in11)
    S = Store(S, 11, in12)
    S = Store(S, 12, in13)
    S = Store(S, 13, in14)
    S = Store(S, 14, in15)
    S = Store(S, 15, in16)


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
    s9_0,s9_1,s9_2,s9_3,s9_4,s9_5,s9_6,s9_7,s9_8,s9_9,s9_10,s9_11,s9_12,s9_13,s9_14,s9_15=BitVecs('s9_0 s9_1 s9_2 s9_3 s9_4 s9_5 s9_6 s9_7 s9_8 s9_9 s9_10 s9_11 s9_12 s9_13 s9_14 s9_15',10)
    s9_0b,s9_1b,s9_2b,s9_3b,s9_4b,s9_5b,s9_6b,s9_7b,s9_8b,s9_9b,s9_10b,s9_11b,s9_12b,s9_13b,s9_14b,s9_15b=BitVecs('s9_0b s9_1b s9_2b s9_3b s9_4b s9_5b s9_6b s9_7b s9_8b s9_9b s9_10b s9_11b s9_12b s9_13b s9_14b s9_15b',10)

    s9_5b = S[5] & 0xf
    s9_10b= S[10] & 0xf
    s9_15b = S[15] & 0xf
    s9_0 = S[0] >> 4
    s9_0b = S[0] & 0xf



    S = Store(S, BitVecVal(1, 10),I[10][s9_5b]) #key1=5
    S = Store(S, BitVecVal(5, 10),78)
    S = Store(S, BitVecVal(9, 10),198)
    S = Store(S, BitVecVal(13, 10),249)


    S = Store(S, BitVecVal(2, 10), I[0][s9_10b]) #key2=10
    S = Store(S, BitVecVal(10, 10), BitVecVal(150,10))

    S = Store(S, BitVecVal(6, 10), BitVecVal(132,10))
    S = Store(S, BitVecVal(14, 10),BitVecVal(53,10))

    S = Store(S, BitVecVal(3, 10), I[3][s9_15b]) #key3=15
    S = Store(S, BitVecVal(15, 10), BitVecVal(236,10))
    S = Store(S, BitVecVal(11, 10), BitVecVal(68,10))
    S = Store(S, BitVecVal(7, 10), BitVecVal(175,10))

    S = Store(S, BitVecVal(0, 10), I[s9_0][s9_0b])
    S = Store(S, BitVecVal(4, 10), BitVecVal(249,10))
    S = Store(S, BitVecVal(8, 10), BitVecVal(217,10))
    S = Store(S, BitVecVal(12, 10), BitVecVal(165,10))



    # ------------------------ MixColumn AddRoundKey ---------------------------------


    ret = Array('ret', BitVecSort(10), BitVecSort(10))
    x = BitVecVal(0, 10)
    j = BitVecVal(0, 10)

    nb = BitVecVal(4,10)
    n = BitVecVal(1,10)

    ret = If(key1 == 1,Store(ret, 0, S[0] << 1),Store(ret, 0, S[2] << 1))
    ret = Store(ret, 0, If(ret[0] >> 8 == 1, ret[0] ^ 283, ret[0]))
    x = S[1]
    x = x ^ (x << 1)
    ret = Store(ret, 0, If( x >> 8 == 1, ret[0] ^ (x ^ 283), ret[0] ^ x))
    ret = Store(ret, 0, ret[0] ^ (S[2 ] ^ S[3 ] ^ W[0][j + nb * n]))


    ret = If(key2 == 2 , Store(ret, 1 , S[1 ] << 1), Store(ret, 1 , S[3] << 1))
    ret = Store(ret, 1 , If(ret[1 ] >> 8 == 1, ret[1 ] ^ 283, ret[1 ]))
    x = S[2]
    x = x ^ (x << 1)
    ret = Store(ret, 1, If( x >> 8 == 1, ret[1 ] ^ (x ^ 283), ret[1 ] ^ x))
    ret = Store(ret, 1, ret[1 ] ^ (S[3 ] ^ S[0] ^ W[1][j + nb * n]))

    #ret = Store(ret, 2, S[2] << 1)
    ret = If(key3 == 3 , Store(ret, 2, S[2] << 1), Store(ret, 2 , S[4] << 1))
    ret = Store(ret, 2, If(ret[2] >> 8 == 1, ret[2] ^ 283, ret[2]))
    x = S[3]
    x = x ^ (x << 1)
    ret = Store(ret, 2, If( x >> 8 == 1, ret[2] ^ (x ^ 283), ret[2] ^ x)) #key4 283
    ret = Store(ret, 2, ret[2] ^ (S[0] ^ S[1] ^ W[2][4*n]))

    # ret = Store(ret, 3, S[3] << 1) #key5 3
    ret = If(key4 == 4 , Store(ret, 3, S[3] << 1), Store(ret, 3 , S[4] << 1))
    ret = Store(ret, 3, If(ret[3 ] >> 8 == 1, ret[3 ] ^ 283, ret[3 ]))
    x = S[0]
    x = x ^ (x << 1)
    ret = Store(ret, 3, If( x >> 8 == 1, ret[3 ] ^ (x ^ 283), ret[3 ] ^ x))
    ret = Store(ret, 3, ret[3 ] ^ (S[1 ] ^ S[2 ] ^ W[3][j + nb * n]))


    o1=ret[0]
    o2=ret[1]
    o3=ret[2]
    o4=ret[3]
    return tuple.tuple2(o1,o2,o3,o4)


#key1 = 5, key2 = 10 , key3 = 15 , key4 = 283 , key5 = 3 , key6 = 5 , key7 = 4 , key8 = 7 , key9 = 8 , key10 = 10

'''gg = Tactic('smt').solver()
ia = str(176)+" "+str(180)+" "+str(2)+" "+str(240)+" "+str(18)+" "+str(2)+" "+str(18)+" "+str(57)+" "+str(1)+" "+str(5)+" "+str(37)+" "+str(5)+" "+str(140)+" "+str(156)+" "+str(156)+" "+str(210)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,10),BitVecVal(oa12,10),BitVecVal(oa13,10),BitVecVal(oa14,10),BitVecVal(oa15,10),BitVecVal(oa16,10),BitVecVal(oa17,10),BitVecVal(oa18,10),BitVecVal(oa19,10),BitVecVal(oa20,10),BitVecVal(oa21,10),BitVecVal(oa22,10),BitVecVal(oa23,10),BitVecVal(oa24,10),BitVecVal(oa25,10),BitVecVal(oa26,10),BitVecVal(oa27,10),BitVecVal(oa28,10),BitVecVal(oa29,10),BitVecVal(oa30,10),BitVecVal(oa31,10),BitVecVal(oa32,10)
oa = tuple.tuple1(BitVecVal(oa1,10),BitVecVal(oa2,10),BitVecVal(oa3,10),BitVecVal(oa4,10),BitVecVal(oa5,10),BitVecVal(oa6,10),BitVecVal(oa7,10),BitVecVal(oa8,10),BitVecVal(oa9,10),BitVecVal(oa10,10),BitVecVal(oa11,10),BitVecVal(oa12,10),BitVecVal(oa13,10),BitVecVal(oa14,10),BitVecVal(oa15,10),BitVecVal(oa16,10))
print(gg.check(simplify(findOutput1(5,10,15,283,3,1,4,3,8,2))==oa))'''
#print(gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(oa6,10)))
# print(oa5)
# for jj in range(0,512):
#     if (gg.check(findOutput1(5,10,15,283,3,1,4,3,8,2)==BitVecVal(jj,10))) == sat:
#         print(jj)

#4,6,7,8,9,10,
'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,10),BitVecVal(oa12,10),BitVecVal(oa13,10),BitVecVal(oa14,10),BitVecVal(oa15,10),BitVecVal(oa16,10),BitVecVal(oa17,10),BitVecVal(oa18,10),BitVecVal(oa19,10),BitVecVal(oa20,10),BitVecVal(oa21,10),BitVecVal(oa22,10),BitVecVal(oa23,10),BitVecVal(oa24,10),BitVecVal(oa25,10),BitVecVal(oa26,10),BitVecVal(oa27,10),BitVecVal(oa28,10),BitVecVal(oa29,10),BitVecVal(oa30,10),BitVecVal(oa31,10),BitVecVal(oa32,10)
oa = tuple.tuple1(BitVecVal(oa1,10),BitVecVal(oa2,10),BitVecVal(oa3,10),BitVecVal(oa4,10),BitVecVal(oa5,10),BitVecVal(oa6,10),BitVecVal(oa7,10),BitVecVal(oa8,10),BitVecVal(oa9,10),BitVecVal(oa10,10),BitVecVal(oa11,10),BitVecVal(oa12,10),BitVecVal(oa13,10),BitVecVal(oa14,10),BitVecVal(oa15,10),BitVecVal(oa16,10))'''



j = 0


s = Tactic('smt').solver()

#s.add(simplify(findOutput(i1,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)) == out1)
#s.add(simplify(findOutput(i1,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)) == out2)

#o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
#o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2=findOutput(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)
'''s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_1,key2_1,key3_1,key4_1,key5_1))==out3)
s.add(simplify(sub(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,key1_2,key2_2,key3_2,key4_2,key5_2))==out4)'''

#key1 = 5, key2 = 10 , key3 = 15 , key4 = 283 , key5 = 3 , key6 = 5 , key7 = 4 , key8 = 7 , key9 = 8 , key10 = 10
s.add(key1_1>=0,key1_1<=255)
s.add(key1_2>=0,key1_2<=255)
s.add(key2_1>=0,key2_1<=255)
s.add(key2_2>=0,key2_2<=255)
s.add(key3_1>=0,key3_1<=255)
s.add(key3_2>=0,key3_2<=255)
s.add(key4_1>=0,key4_1<=255)
s.add(key4_2>=0,key4_2<=511)
s.add(key5_1>=0,key5_1<=500)
s.add(key5_2>=0,key5_2<=500)
s.add(key6_1>=0,key6_1<=255)
s.add(key6_2>=0,key6_2<=255)
s.add(key7_1>=0,key7_1<=255)
s.add(key7_2>=0,key7_2<=255)
s.add(key8_1>=0,key8_1<=255)
s.add(key8_2>=0,key8_2<=255)
s.add(key9_1>=0,key9_1<=255)
s.add(key9_2>=0,key9_2<=255)
s.add(key10_1>=0,key10_1<=255)
s.add(key10_2>=0,key10_2<=255)
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



# findOutput1(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
# print(simplify(findOutput1(1,2,3,4,5,6,7,8,9,100,120,2,13,14,15,16,1,2,3,4,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,S,W,I,ret)))
# print((simplify(findOutput1(5,10,15,283,3,5,4,7,8,10,S,W,I,ret))))
# exit()



# dip1 [73,91,20,4,9,16,0,13,4,13,46,0,15,6,9,19]
# dip2 = [inp1,23,32,13,65,0,11,32,78,65,23,11,32,8,0,11]
# print(simplify(sub(0,5,10,15,283,3)))
# exit()

# oa = tuple.tuple1(BitVecVal(10,10),BitVecVal(66,10),BitVecVal(15,10),BitVecVal(210,10),BitVecVal(62,10),BitVecVal(119,10),BitVecVal(231,10),BitVecVal(201,10),BitVecVal(162,10),BitVecVal(76,10),BitVecVal(192,10),BitVecVal(172,10),BitVecVal(190,10),BitVecVal(152,10),BitVecVal(45,10),BitVecVal(189,10))
# s.add(simplify(findOutput1(key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,S,W,I,ret))==oa)
# s.add(simplify(findOutput1(key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,S,W,I,ret))==oa)

# s.add(simplify(findOutput1(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9 , i10 , i11 , i12 , i13 , i14 , i15 , i16 ,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,S,W,I,ret))==out1)
# s.add(simplify(findOutput1(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9 , i10 , i11 , i12 , i13 , i14 , i15 , i16 ,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,S,W,I,ret))==out2)

s.add(simplify(sub(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9 , i10 , i11 , i12 , i13 , i14 , i15 , i16 ,key1_1,key2_1,key3_1,key4_1,key5_1,S,W,I,ret))==out3)
s.add(simplify(sub(i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9 , i10 , i11 , i12 , i13 , i14 , i15 , i16 ,key1_2,key2_2,key3_2,key4_2,key5_2,S,W,I,ret))==out4)
j = 0
start1 = time.time()
while(s.check(out3!=out4,   Or(key1_1 != key1_2, key2_1 != key2_2, key3_1 != key3_2, key4_1 != key4_2, key5_1 != key5_2)) == sat):
    m = s.model()
    #print(m)
    #print(m)
    print(str(m[i1])+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16]))
    print(str(m[key1_1])+" "+str(m[key2_1])+ " "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+ " "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2]))
    ia = str(m[i1])+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16])
    [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    # BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
    oa = tuple.tuple1(BitVecVal(oa1,10),BitVecVal(oa2,10),BitVecVal(oa3,10),BitVecVal(oa4,10),BitVecVal(oa5,10),BitVecVal(oa6,10),BitVecVal(oa7,10),BitVecVal(oa8,10),BitVecVal(oa9,10),BitVecVal(oa10,10),BitVecVal(oa11,10),BitVecVal(oa12,10),BitVecVal(oa13,10),BitVecVal(oa14,10),BitVecVal(oa15,10),BitVecVal(oa16,10))
    # print(simplify(findOutput1(m[i1], m[i2], m[i3], m[i4], m[i5], m[i6], m[i7], m[i8], m[i9], m[i10], m[i11], m[i12], m[i13], m[i14], m[i15], m[i16],0,0,0,0,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,S,W,I,ret)))
    s.add(simplify(findOutput1(m[i1], m[i2], m[i3], m[i4], m[i5], m[i6], m[i7], m[i8], m[i9], m[i10], m[i11], m[i12], m[i13], m[i14], m[i15], m[i16],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,S,W,I,ret)) == oa)
    s.add(simplify(findOutput1(m[i1], m[i2], m[i3], m[i4], m[i5], m[i6], m[i7], m[i8], m[i9], m[i10], m[i11], m[i12], m[i13], m[i14], m[i15], m[i16],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,S,W,I,ret)) == oa)
  
    print("Iteration %d = %f second" %(j+1,time.time()-start1))
    j = j + 1
print("unsat takes %f time" %(time.time()-start1))
print("loop1 complete")

p=0
start2=time.time()
while s.check(key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1 == key4_2, key5_1 == key5_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1]))
    print("Iteration %d = %f second" %(p+1,time.time()-start2))
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1]),key5_1!=m[key5_1])
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2]),key5_2!=m[key5_2])
    p = p + 1
print("total time = %f", time.time() - start1)