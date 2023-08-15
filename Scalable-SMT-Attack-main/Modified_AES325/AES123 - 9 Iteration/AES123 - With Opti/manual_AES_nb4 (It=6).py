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
tuple.declare('tuple2',('17', BitVecSort(32)),('18' , BitVecSort(32)),('19' , BitVecSort(32)),('20' , BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple1(o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1)
out2 = tuple.tuple1(o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2)

out3 = tuple.tuple2(oo0_1,oo1_1,oo2_1,oo3_1)
out4 = tuple.tuple2(oo0_2,oo1_2,oo2_2,oo3_2)

TO_init = 1600
TO_max = 1280000000
rem_key_max = 32

statemt = [50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt_and=[2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt_shift=[3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt0=[25,61,227,190,160,244,226,43,154,198,141,42,233,248,72,8,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt0_and=[9,13,3,14,0,4,2,11,10,6,13,10,9,8,8,8,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt0_shift=[1,3,14,11,10,15,14,2,9,12,8,2,14,15,4,0,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt1=[146,185,8,191,0,14,28,60,18,146,161,155,202,91,113,49,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt1_and=[2,9,8,15,0,14,12,12,2,2,1,11,10,11,1,1,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt1_shift=[9,11,0,11,0,0,1,3,1,9,10,9,12,5,7,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt2=[192,129,99,90,242,204,137,206,104,4,24,216,147,110,241,75,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt2_and=[0,1,3,10,2,12,9,14,8,4,8,8,3,14,1,11,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt2_shift=[12,8,6,5,15,12,8,12,6,0,1,13,9,6,15,4,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt3=[15,195,177,213,207,76,206,179,47,18,230,230,141,77,143,15,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt3_and=[15,3,1,5,15,12,14,3,15,2,6,6,13,13,15,15,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt3_shift=[0,12,11,13,12,4,12,11,2,1,14,14,8,4,8,0,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt4=[221,7,83,233,32,8,107,242,135,64,189,153,59,60,170,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt4_and=[13,7,3,9,0,8,11,2,7,0,13,9,11,12,10,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt4_shift=[13,0,5,14,2,0,6,15,8,4,11,9,3,3,10,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt5=[230,146,48,80,244,217,173,10,251,195,32,30,241,206,18,136,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt5_and=[6,2,0,0,4,9,13,10,11,3,0,14,1,14,2,8,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt5_shift=[14,9,3,5,15,13,10,0,15,12,2,1,15,12,1,8,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt6=[95,203,85,210,153,81,14,112,234,200,30,227,42,55,148,201,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt6_and=[15,11,5,2,9,1,14,0,10,8,14,3,10,7,4,9,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt6_shift=[5,12,5,13,9,5,0,7,14,12,1,14,2,3,9,12,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt7=[124,23,1,166,215,5,249,126,181,151,215,16,174,145,219,123,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt7_and=[12,7,1,6,7,5,9,14,5,7,7,0,14,1,11,11,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt7_shift=[7,1,0,10,13,0,15,7,11,9,13,1,10,9,13,7,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt8=[216,145,133,137,61,215,138,95,0,26,109,194,159,186,46,27,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt8_and=[8,1,5,9,13,7,10,15,0,10,13,2,15,10,14,11,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt8_shift=[13,9,8,8,3,13,8,5,0,1,6,12,9,11,2,1,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt9=[158,52,144,91,145,160,236,172,25,224,177,227,183,107,7,90,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt9_and=[14,4,0,11,1,0,12,12,9,0,1,3,7,11,7,10,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt9_shift=[9,3,9,5,9,10,14,10,1,14,11,14,11,6,0,5,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt10=[226,87,15,0,65,180,21,4,208,14,148,106,86,84,11,146,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt10_and=[2,7,15,0,1,4,5,4,0,14,4,10,6,4,11,2,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt10_shift=[14,5,0,0,4,11,1,0,13,0,9,6,5,5,0,9,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt11=[50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt11_and=[2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt11_shift=[3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt12=[50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt12_and=[2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt12_shift=[3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt13=[50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt13_and=[2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt13_shift=[3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]

statemt14=[50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52,50,67,246,168,136,90,48,141,49,49,152,162,224,55,7,52]
statemt14_and=[2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4,2,3,6,8,8,10,0,13,1,1,8,2,0,7,7,4]
statemt14_shift=[3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3,3,4,15,10,8,5,3,8,3,3,9,10,14,3,0,3]


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
    S2 = Array('S2', BitVecSort(32), BitVecSort(32))
    S3 = Array('S3', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))
    ## Initializing the `statemt` array ##
    '''i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
        i += 1'''

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
    s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15=BitVecs('s0 s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15',32)
    s0b,s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,s10b,s11b,s12b,s13b,s14b,s15b=BitVecs('s0b s1b s2b s3b s4b s5b s6b s7b s8b s9b s10b s11b s12b s13b s14b s15b',32)
    if n==0:
        i = 0
        for elem in statemt0:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt0_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt0_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==1:
        i = 0
        for elem in statemt1:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt1_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt1_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==2:
        i = 0
        for elem in statemt2:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt2_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt2_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]
    elif n==3:
        i = 0
        for elem in statemt3:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt3_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt3_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==4:
        i = 0
        for elem in statemt4:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt4_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt4_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==5:
        i = 0
        for elem in statemt5:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt5_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt5_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]
    elif n==6:
        i = 0
        for elem in statemt6:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt6_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt6_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==7:
        i = 0
        for elem in statemt7:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt7_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt7_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==8:
        i = 0
        for elem in statemt8:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt8_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt8_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==9:
        i = 0
        for elem in statemt9:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt9_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt9_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==10:
        i = 0
        for elem in statemt10:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt10_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt10_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==11:
        i = 0
        for elem in statemt11:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt11_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt11_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==12:
        i = 0
        for elem in statemt12:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt12_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt12_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==13:
        i = 0
        for elem in statemt13:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt13_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt13_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    else:
        i = 0
        for elem in statemt14:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt14_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt14_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

# --------------------------------Iteration 0 ----------------------------------------------------------------------------------
    # ---------------------- ByetSub ShiftRow ------------------
    

    temp = I[s1][s1b] 
    S = Store(S, BitVecVal(1, 32),I[s5][s5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9][s9b])
    S = Store(S, BitVecVal(9, 32),I[s13][s13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s2][s2b]
    S = Store(S, BitVecVal(2, 32), I[s10][s10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s6][s6b] 
    S = Store(S, BitVecVal(6, 32), I[s14][s14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s3][s3b]
    S = Store(S, BitVecVal(3, 32), I[s15][s15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s11][s11b])
    S = Store(S, BitVecVal(11, 32), I[s7][s7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s0][s0b])
    S = Store(S, BitVecVal(4, 32), I[s4][s4b])
    S = Store(S, BitVecVal(8, 32), I[s8][s8b]) 
    S = Store(S, BitVecVal(12, 32),I[s12][s12b])

# ------------------------ MixColumn AddRoundKey ---------------------------------

    
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3

#----------------------Iteration 1---------------------------------------------------------------------------------

    s1_0,s1_1,s1_2,s1_3,s1_4,s1_5,s1_6,s1_7,s1_8,s1_9,s1_10,s1_11,s1_12,s1_13,s1_14,s1_15=BitVecs('s1_0 s1_1 s1_2 s1_3 s1_4 s1_5 s1_6 s1_7 s1_8 s1_9 s1_10 s1_11 s1_12 s1_13 s1_14 s1_15',32)
    s1_0b,s1_1b,s1_2b,s1_3b,s1_4b,s1_5b,s1_6b,s1_7b,s1_8b,s1_9b,s1_10b,s1_11b,s1_12b,s1_13b,s1_14b,s1_15b=BitVecs('s1_0b s1_1b s1_2b s1_3b s1_4b s1_5b s1_6b s1_7b s1_8b s1_9b s1_10b s1_11b s1_12b s1_13b s1_14b s1_15b',32)


    if n==0:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(11,32)
        s1_5b=BitVecVal(4,32)
        s1_9=BitVecVal(4,32)
        s1_9b=BitVecVal(1,32)
        s1_13=BitVecVal(2,32)
        s1_13b=BitVecVal(7,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(1,32)
        s1_10b=BitVecVal(1,32)
        s1_6=BitVecVal(5,32)
        s1_6b=BitVecVal(2,32)
        s1_14=BitVecVal(9,32)
        s1_14b=BitVecVal(8,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(14,32)
        s1_15b=BitVecVal(5,32)
        s1_11=BitVecVal(15,32)
        s1_11b=BitVecVal(1,32)
        s1_7=BitVecVal(10,32)
        s1_7b=BitVecVal(14,32)

        s1_0=BitVecVal(13,32)
        s1_0b=BitVecVal(4,32)
        s1_4=BitVecVal(14,32)
        s1_4b=BitVecVal(0,32)
        s1_8=BitVecVal(11,32)
        s1_8b=BitVecVal(8,32)
        s1_12=BitVecVal(1,32)
        s1_12b=BitVecVal(14,32)

    elif n==1:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(4,32)
        s1_5b=BitVecVal(15,32)
        s1_9=BitVecVal(3,32)
        s1_9b=BitVecVal(9,32)
        s1_13=BitVecVal(5,32)
        s1_13b=BitVecVal(6,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(3,32)
        s1_10b=BitVecVal(0,32)
        s1_6=BitVecVal(10,32)
        s1_6b=BitVecVal(3,32)
        s1_14=BitVecVal(9,32)
        s1_14b=BitVecVal(12,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(1,32)
        s1_15b=BitVecVal(4,32)
        s1_11=BitVecVal(14,32)
        s1_11b=BitVecVal(11,32)
        s1_7=BitVecVal(0,32)
        s1_7b=BitVecVal(8,32)

        s1_0=BitVecVal(4,32)
        s1_0b=BitVecVal(15,32)
        s1_4=BitVecVal(6,32)
        s1_4b=BitVecVal(3,32)
        s1_8=BitVecVal(12,32)
        s1_8b=BitVecVal(9,32)
        s1_12=BitVecVal(7,32)
        s1_12b=BitVecVal(4,32)

    elif n==2:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(15,32)
        s1_5b=BitVecVal(2,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(15,32)
        s1_13=BitVecVal(0,32)
        s1_13b=BitVecVal(12,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(15,32)
        s1_10b=BitVecVal(11,32)
        s1_6=BitVecVal(10,32)
        s1_6b=BitVecVal(1,32)
        s1_14=BitVecVal(10,32)
        s1_14b=BitVecVal(7,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(16,32)
        s1_15b=BitVecVal(1,32)
        s1_11=BitVecVal(8,32)
        s1_11b=BitVecVal(11,32)
        s1_7=BitVecVal(11,32)
        s1_7b=BitVecVal(14,32)

        s1_0=BitVecVal(11,32)
        s1_0b=BitVecVal(10,32)
        s1_4=BitVecVal(8,32)
        s1_4b=BitVecVal(9,32)
        s1_8=BitVecVal(4,32)
        s1_8b=BitVecVal(5,32)
        s1_12=BitVecVal(13,32)
        s1_12b=BitVecVal(12,32)

    elif n==3:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(12,32)
        s1_5b=BitVecVal(9,32)
        s1_9=BitVecVal(14,32)
        s1_9b=BitVecVal(3,32)
        s1_13=BitVecVal(2,32)
        s1_13b=BitVecVal(14,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(12,32)
        s1_10b=BitVecVal(8,32)
        s1_6=BitVecVal(7,32)
        s1_6b=BitVecVal(3,32)
        s1_14=BitVecVal(8,32)
        s1_14b=BitVecVal(11,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(8,32)
        s1_15b=BitVecVal(14,32)
        s1_11=BitVecVal(6,32)
        s1_11b=BitVecVal(13,32)
        s1_7=BitVecVal(0,32)
        s1_7b=BitVecVal(3,32)

        s1_0=BitVecVal(7,32)
        s1_0b=BitVecVal(6,32)
        s1_4=BitVecVal(8,32)
        s1_4b=BitVecVal(10,32)
        s1_8=BitVecVal(1,32)
        s1_8b=BitVecVal(5,32)
        s1_12=BitVecVal(5,32)
        s1_12b=BitVecVal(13,32)

    elif n==4:

        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(0,32)
        s1_5b=BitVecVal(9,32)
        s1_9=BitVecVal(14,32)
        s1_9b=BitVecVal(11,32)
        s1_13=BitVecVal(12,32)
        s1_13b=BitVecVal(5,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(14,32)
        s1_10b=BitVecVal(13,32)
        s1_6=BitVecVal(10,32)
        s1_6b=BitVecVal(12,32)
        s1_14=BitVecVal(7,32)
        s1_14b=BitVecVal(15,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(14,32)
        s1_15b=BitVecVal(14,32)
        s1_11=BitVecVal(8,32)
        s1_11b=BitVecVal(9,32)
        s1_7=BitVecVal(1,32)
        s1_7b=BitVecVal(14,32)

        s1_0=BitVecVal(12,32)
        s1_0b=BitVecVal(1,32)
        s1_4=BitVecVal(11,32)
        s1_4b=BitVecVal(7,32)
        s1_8=BitVecVal(1,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(2,32)

    elif n==5:

        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(2,32)
        s1_5b=BitVecVal(14,32)
        s1_9=BitVecVal(8,32)
        s1_9b=BitVecVal(11,32)
        s1_13=BitVecVal(4,32)
        s1_13b=BitVecVal(15,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(0,32)
        s1_10b=BitVecVal(4,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(9,32)
        s1_14=BitVecVal(9,32)
        s1_14b=BitVecVal(5,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(7,32)
        s1_15b=BitVecVal(2,32)
        s1_11=BitVecVal(6,32)
        s1_11b=BitVecVal(7,32)
        s1_7=BitVecVal(5,32)
        s1_7b=BitVecVal(3,32)

        s1_0=BitVecVal(8,32)
        s1_0b=BitVecVal(14,32)
        s1_4=BitVecVal(11,32)
        s1_4b=BitVecVal(15,32)
        s1_8=BitVecVal(0,32)
        s1_8b=BitVecVal(15,32)
        s1_12=BitVecVal(10,32)
        s1_12b=BitVecVal(1,32)

    elif n==6:

        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(14,32)
        s1_5b=BitVecVal(8,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(10,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(15,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(15,32)
        s1_10b=BitVecVal(12,32)
        s1_6=BitVecVal(2,32)
        s1_6b=BitVecVal(2,32)
        s1_14=BitVecVal(10,32)
        s1_14b=BitVecVal(11,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(1,32)
        s1_15b=BitVecVal(1,32)
        s1_11=BitVecVal(5,32)
        s1_11b=BitVecVal(1,32)
        s1_7=BitVecVal(11,32)
        s1_7b=BitVecVal(5,32)

        s1_0=BitVecVal(12,32)
        s1_0b=BitVecVal(15,32)
        s1_4=BitVecVal(14,32)
        s1_4b=BitVecVal(14,32)
        s1_8=BitVecVal(8,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(5,32)

    elif n==7:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(8,32)
        s1_5b=BitVecVal(8,32)
        s1_9=BitVecVal(8,32)
        s1_9b=BitVecVal(1,32)
        s1_13=BitVecVal(15,32)
        s1_13b=BitVecVal(0,32)

        s1_2=I[S2[key2]][S3[10]] >>4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(7,32)
        s1_10b=BitVecVal(12,32)
        s1_6=BitVecVal(11,32)
        s1_6b=BitVecVal(9,32)
        s1_14=BitVecVal(9,32)
        s1_14b=BitVecVal(9,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(12,32)
        s1_15b=BitVecVal(10,32)
        s1_11=BitVecVal(15,32)
        s1_11b=BitVecVal(3,32)
        s1_7=BitVecVal(2,32)
        s1_7b=BitVecVal(4,32)

        s1_0=BitVecVal(1,32)
        s1_0b=BitVecVal(0,32)
        s1_4=BitVecVal(0,32)
        s1_4b=BitVecVal(14,32)
        s1_8=BitVecVal(13,32)
        s1_8b=BitVecVal(5,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(4,32)
    elif n==8:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(10,32)
        s1_5b=BitVecVal(2,32)
        s1_9=BitVecVal(15,32)
        s1_9b=BitVecVal(4,32)
        s1_13=BitVecVal(8,32)
        s1_13b=BitVecVal(1,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(9,32)
        s1_10b=BitVecVal(7,32)
        s1_6=BitVecVal(3,32)
        s1_6b=BitVecVal(1,32)
        s1_14=BitVecVal(7,32)
        s1_14b=BitVecVal(14,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(2,32)
        s1_15b=BitVecVal(5,32)
        s1_11=BitVecVal(12,32)
        s1_11b=BitVecVal(15,32)
        s1_7=BitVecVal(10,32)
        s1_7b=BitVecVal(7,32)

        s1_0=BitVecVal(6,32)
        s1_0b=BitVecVal(1,32)
        s1_4=BitVecVal(2,32)
        s1_4b=BitVecVal(7,32)
        s1_8=BitVecVal(6,32)
        s1_8b=BitVecVal(3,32)
        s1_12=BitVecVal(13,32)
        s1_12b=BitVecVal(11,32)

    elif n==9:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(14,32)
        s1_5b=BitVecVal(1,32)
        s1_9=BitVecVal(7,32)
        s1_9b=BitVecVal(15,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(8,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(6,32)
        s1_10b=BitVecVal(0,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(5,32)
        s1_14=BitVecVal(12,32)
        s1_14b=BitVecVal(14,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(1,32)
        s1_15b=BitVecVal(1,32)
        s1_11=BitVecVal(9,32)
        s1_11b=BitVecVal(1,32)
        s1_7=BitVecVal(3,32)
        s1_7b=BitVecVal(9,32)

        s1_0=BitVecVal(0,32)
        s1_0b=BitVecVal(11,32)
        s1_4=BitVecVal(8,32)
        s1_4b=BitVecVal(1,32)
        s1_8=BitVecVal(13,32)
        s1_8b=BitVecVal(4,32)
        s1_12=BitVecVal(10,32)
        s1_12b=BitVecVal(9,32)
    elif n==10:

        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(10,32)
        s1_5b=BitVecVal(11,32)
        s1_9=BitVecVal(2,32)
        s1_9b=BitVecVal(0,32)
        s1_13=BitVecVal(5,32)
        s1_13b=BitVecVal(11,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(7,32)
        s1_10b=BitVecVal(6,32)
        s1_6=BitVecVal(2,32)
        s1_6b=BitVecVal(11,32)
        s1_14=BitVecVal(5,32)
        s1_14b=BitVecVal(9,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(0,32)
        s1_15b=BitVecVal(2,32)
        s1_11=BitVecVal(15,32)
        s1_11b=BitVecVal(2,32)
        s1_7=BitVecVal(6,32)
        s1_7b=BitVecVal(3,32)

        s1_0=BitVecVal(9,32)
        s1_0b=BitVecVal(8,32)
        s1_4=BitVecVal(8,32)
        s1_4b=BitVecVal(3,32)
        s1_8=BitVecVal(7,32)
        s1_8b=BitVecVal(0,32)
        s1_12=BitVecVal(11,32)
        s1_12b=BitVecVal(1,32)
    elif n==11:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(12,32)
        s1_5b=BitVecVal(7,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(10,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(10,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(4,32)
        s1_10b=BitVecVal(2,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(5,32)
        s1_14=BitVecVal(0,32)
        s1_14b=BitVecVal(4,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(3,32)
        s1_15b=BitVecVal(10,32)
        s1_11=BitVecVal(5,32)
        s1_11b=BitVecVal(13,32)
        s1_7=BitVecVal(12,32)
        s1_7b=BitVecVal(2,32)

        s1_0=BitVecVal(2,32)
        s1_0b=BitVecVal(3,32)
        s1_4=BitVecVal(12,32)
        s1_4b=BitVecVal(4,32)
        s1_8=BitVecVal(12,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(1,32)

    elif n==12:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(12,32)
        s1_5b=BitVecVal(7,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(10,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(10,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(4,32)
        s1_10b=BitVecVal(2,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(5,32)
        s1_14=BitVecVal(0,32)
        s1_14b=BitVecVal(4,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(3,32)
        s1_15b=BitVecVal(10,32)
        s1_11=BitVecVal(5,32)
        s1_11b=BitVecVal(13,32)
        s1_7=BitVecVal(12,32)
        s1_7b=BitVecVal(2,32)

        s1_0=BitVecVal(2,32)
        s1_0b=BitVecVal(3,32)
        s1_4=BitVecVal(12,32)
        s1_4b=BitVecVal(4,32)
        s1_8=BitVecVal(12,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(1,32)

    elif n==13:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(12,32)
        s1_5b=BitVecVal(7,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(10,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(10,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(4,32)
        s1_10b=BitVecVal(2,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(5,32)
        s1_14=BitVecVal(0,32)
        s1_14b=BitVecVal(4,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(3,32)
        s1_15b=BitVecVal(10,32)
        s1_11=BitVecVal(5,32)
        s1_11b=BitVecVal(13,32)
        s1_7=BitVecVal(12,32)
        s1_7b=BitVecVal(2,32)

        s1_0=BitVecVal(2,32)
        s1_0b=BitVecVal(3,32)
        s1_4=BitVecVal(12,32)
        s1_4b=BitVecVal(4,32)
        s1_8=BitVecVal(12,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(1,32)

    else:
        s1_1=I[S2[key1]][S3[5]] >> 4
        s1_1b=I[S2[key1]][S3[5]] & 0xf
        s1_5=BitVecVal(12,32)
        s1_5b=BitVecVal(7,32)
        s1_9=BitVecVal(9,32)
        s1_9b=BitVecVal(10,32)
        s1_13=BitVecVal(1,32)
        s1_13b=BitVecVal(10,32)

        s1_2=I[S2[key2]][S3[10]] >> 4
        s1_2b=I[S2[key2]][S3[10]] & 0xf
        s1_10=BitVecVal(4,32)
        s1_10b=BitVecVal(2,32)
        s1_6=BitVecVal(12,32)
        s1_6b=BitVecVal(5,32)
        s1_14=BitVecVal(0,32)
        s1_14b=BitVecVal(4,32)

        s1_3=I[S2[key3]][S3[15]] >>4
        s1_3b=I[S2[key3]][S3[15]] & 0xf
        s1_15=BitVecVal(3,32)
        s1_15b=BitVecVal(10,32)
        s1_11=BitVecVal(5,32)
        s1_11b=BitVecVal(13,32)
        s1_7=BitVecVal(12,32)
        s1_7b=BitVecVal(2,32)

        s1_0=BitVecVal(2,32)
        s1_0b=BitVecVal(3,32)
        s1_4=BitVecVal(12,32)
        s1_4b=BitVecVal(4,32)
        s1_8=BitVecVal(12,32)
        s1_8b=BitVecVal(7,32)
        s1_12=BitVecVal(14,32)
        s1_12b=BitVecVal(1,32)


    temp = I[s1_1][s1_1b] 
    S = Store(S, BitVecVal(1, 32),I[s1_5][s1_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s1_9][s1_9b])
    S = Store(S, BitVecVal(9, 32),I[s1_13][s1_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s1_2][s1_2b]
    S = Store(S, BitVecVal(2, 32), I[s1_10][s1_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s1_6][s1_6b] 
    S = Store(S, BitVecVal(6, 32), I[s1_14][s1_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s1_3][s1_3b]
    S = Store(S, BitVecVal(3, 32), I[s1_15][s1_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s1_11][s1_11b])
    S = Store(S, BitVecVal(11, 32), I[s1_7][s1_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s1_0][s1_0b])
    S = Store(S, BitVecVal(4, 32), I[s1_4][s1_4b])
    S = Store(S, BitVecVal(8, 32), I[s1_8][s1_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s1_12][s1_12b])


    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3


    s2_0,s2_1,s2_2,s2_3,s2_4,s2_5,s2_6,s2_7,s2_8,s2_9,s2_10,s2_11,s2_12,s2_13,s2_14,s2_15=BitVecs('s2_0 s2_1 s2_2 s2_3 s2_4 s2_5 s2_6 s2_7 s2_8 s2_9 s2_10 s2_11 s2_12 s2_13 s2_14 s2_15',32)
    s2_0b,s2_1b,s2_2b,s2_3b,s2_4b,s2_5b,s2_6b,s2_7b,s2_8b,s2_9b,s2_10b,s2_11b,s2_12b,s2_13b,s2_14b,s2_15b=BitVecs('s2_0b s2_1b s2_2b s2_3b s2_4b s2_5b s2_6b s2_7b s2_8b s2_9b s2_10b s2_11b s2_12b s2_13b s2_14b s2_15b',32)


    if n==0:
        s2_1=BitVecVal(8,32)
        s2_1b=BitVecVal(13,32)
        s2_5=BitVecVal(8,32)
        s2_5b=BitVecVal(3,32)
        s2_9=BitVecVal(12,32)
        s2_9b=BitVecVal(12,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(8,32)
        s2_2b=BitVecVal(2,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(4,32)
        s2_6b=BitVecVal(6,32)
        s2_14=BitVecVal(0,32)
        s2_14b=BitVecVal(0,32)

        s2_3=BitVecVal(13,32)
        s2_3b=BitVecVal(9,32)
        s2_15=BitVecVal(10,32)
        s2_15b=BitVecVal(1,32)
        s2_11=BitVecVal(14,32)
        s2_11b=BitVecVal(4,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(4,32)
        s2_0b=BitVecVal(8,32)
        s2_4=BitVecVal(14,32)
        s2_4b=BitVecVal(1,32)
        s2_8=BitVecVal(6,32)
        s2_8b=BitVecVal(12,32)
        s2_12=BitVecVal(7,32)
        s2_12b=BitVecVal(2,32)

    elif n==1:

        s2_1=BitVecVal(8,32)
        s2_1b=BitVecVal(4,32)
        s2_5=BitVecVal(1,32)
        s2_5b=BitVecVal(2,32)
        s2_9=BitVecVal(11,32)
        s2_9b=BitVecVal(1,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(0,32)
        s2_2b=BitVecVal(4,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(13,32)
        s2_6b=BitVecVal(14,32)
        s2_14=BitVecVal(0,32)
        s2_14b=BitVecVal(10,32)

        s2_3=BitVecVal(15,32)
        s2_3b=BitVecVal(10,32)
        s2_15=BitVecVal(14,32)
        s2_15b=BitVecVal(9,32)
        s2_11=BitVecVal(3,32)
        s2_11b=BitVecVal(0,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(8,32)
        s2_0b=BitVecVal(4,32)
        s2_4=BitVecVal(15,32)
        s2_4b=BitVecVal(11,32)
        s2_8=BitVecVal(13,32)
        s2_8b=BitVecVal(13,32)
        s2_12=BitVecVal(9,32)
        s2_12b=BitVecVal(2,32)

    elif n==2:

        s2_1=BitVecVal(8,32)
        s2_1b=BitVecVal(9,32)
        s2_5=BitVecVal(13,32)
        s2_5b=BitVecVal(11,32)
        s2_9=BitVecVal(15,32)
        s2_9b=BitVecVal(14,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(0,32)
        s2_2b=BitVecVal(15,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(5,32)
        s2_6b=BitVecVal(12,32)
        s2_14=BitVecVal(3,32)
        s2_14b=BitVecVal(2,32)

        s2_3=BitVecVal(14,32)
        s2_3b=BitVecVal(15,32)
        s2_15=BitVecVal(3,32)
        s2_15b=BitVecVal(13,32)
        s2_11=BitVecVal(10,32)
        s2_11b=BitVecVal(14,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(15,32)
        s2_0b=BitVecVal(4,32)
        s2_4=BitVecVal(10,32)
        s2_4b=BitVecVal(7,32)
        s2_8=BitVecVal(6,32)
        s2_8b=BitVecVal(14,32)
        s2_12=BitVecVal(8,32)
        s2_12b=BitVecVal(6,32)

    elif n==3:

        s2_1=BitVecVal(13,32)
        s2_1b=BitVecVal(13,32)
        s2_5=BitVecVal(1,32)
        s2_5b=BitVecVal(1,32)
        s2_9=BitVecVal(3,32)
        s2_9b=BitVecVal(1,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(14,32)
        s2_2b=BitVecVal(8,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(3,32)
        s2_6b=BitVecVal(13,32)
        s2_14=BitVecVal(8,32)
        s2_14b=BitVecVal(15,32)

        s2_3=BitVecVal(1,32)
        s2_3b=BitVecVal(9,32)
        s2_15=BitVecVal(3,32)
        s2_15b=BitVecVal(12,32)
        s2_11=BitVecVal(7,32)
        s2_11b=BitVecVal(11,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(3,32)
        s2_0b=BitVecVal(8,32)
        s2_4=BitVecVal(7,32)
        s2_4b=BitVecVal(14,32)
        s2_8=BitVecVal(5,32)
        s2_8b=BitVecVal(9,32)
        s2_12=BitVecVal(4,32)
        s2_12b=BitVecVal(12,32)

    elif n==4:

        s2_1=BitVecVal(0,32)
        s2_1b=BitVecVal(1,32)
        s2_5=BitVecVal(14,32)
        s2_5b=BitVecVal(9,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(6,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(5,32)
        s2_2b=BitVecVal(5,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(13,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(9,32)
        s2_14b=BitVecVal(1,32)

        s2_3=BitVecVal(2,32)
        s2_3b=BitVecVal(8,32)
        s2_15=BitVecVal(10,32)
        s2_15b=BitVecVal(7,32)
        s2_11=BitVecVal(7,32)
        s2_11b=BitVecVal(2,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(7,32)
        s2_0b=BitVecVal(8,32)
        s2_4=BitVecVal(10,32)
        s2_4b=BitVecVal(9,32)
        s2_8=BitVecVal(15,32)
        s2_8b=BitVecVal(0,32)
        s2_12=BitVecVal(9,32)
        s2_12b=BitVecVal(8,32)

    elif n==5:

        s2_1=BitVecVal(3,32)
        s2_1b=BitVecVal(1,32)
        s2_5=BitVecVal(3,32)
        s2_5b=BitVecVal(13,32)
        s2_9=BitVecVal(8,32)
        s2_9b=BitVecVal(4,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(15,32)
        s2_2b=BitVecVal(2,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(2,32)
        s2_6b=BitVecVal(10,32)
        s2_14=BitVecVal(13,32)
        s2_14b=BitVecVal(13,32)

        s2_3=BitVecVal(4,32)
        s2_3b=BitVecVal(0,32)
        s2_15=BitVecVal(8,32)
        s2_15b=BitVecVal(5,32)
        s2_11=BitVecVal(14,32)
        s2_11b=BitVecVal(13,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(1,32)
        s2_0b=BitVecVal(9,32)
        s2_4=BitVecVal(0,32)
        s2_4b=BitVecVal(8,32)
        s2_8=BitVecVal(7,32)
        s2_8b=BitVecVal(6,32)
        s2_12=BitVecVal(3,32)
        s2_12b=BitVecVal(2,32)

    elif n==6:

        s2_1=BitVecVal(9,32)
        s2_1b=BitVecVal(11,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(8,32)
        s2_9=BitVecVal(12,32)
        s2_9b=BitVecVal(0,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(11,32)
        s2_2b=BitVecVal(0,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(6,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(9,32)
        s2_14b=BitVecVal(3,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(2,32)
        s2_15=BitVecVal(13,32)
        s2_15b=BitVecVal(1,32)
        s2_11=BitVecVal(13,32)
        s2_11b=BitVecVal(5,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(8,32)
        s2_0b=BitVecVal(10,32)
        s2_4=BitVecVal(2,32)
        s2_4b=BitVecVal(8,32)
        s2_8=BitVecVal(1,32)
        s2_8b=BitVecVal(7,32)
        s2_12=BitVecVal(13,32)
        s2_12b=BitVecVal(9,32)

    elif n==7:

        s2_1=BitVecVal(12,32)
        s2_1b=BitVecVal(4,32)
        s2_5=BitVecVal(0,32)
        s2_5b=BitVecVal(12,32)
        s2_9=BitVecVal(8,32)
        s2_9b=BitVecVal(12,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(1,32)
        s2_2b=BitVecVal(0,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(14,32)
        s2_6b=BitVecVal(14,32)
        s2_14=BitVecVal(5,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(7,32)
        s2_3b=BitVecVal(4,32)
        s2_15=BitVecVal(0,32)
        s2_15b=BitVecVal(13,32)
        s2_11=BitVecVal(3,32)
        s2_11b=BitVecVal(6,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(12,32)
        s2_0b=BitVecVal(10,32)
        s2_4=BitVecVal(10,32)
        s2_4b=BitVecVal(11,32)
        s2_8=BitVecVal(0,32)
        s2_8b=BitVecVal(3,32)
        s2_12=BitVecVal(6,32)
        s2_12b=BitVecVal(9,32)

    elif n==8:

        s2_1=BitVecVal(3,32)
        s2_1b=BitVecVal(10,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(15,32)
        s2_9=BitVecVal(0,32)
        s2_9b=BitVecVal(12,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(8,32)
        s2_2b=BitVecVal(8,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(15,32)
        s2_6b=BitVecVal(3,32)
        s2_14=BitVecVal(12,32)
        s2_14b=BitVecVal(7,32)

        s2_3=BitVecVal(3,32)
        s2_3b=BitVecVal(15,32)
        s2_15=BitVecVal(8,32)
        s2_15b=BitVecVal(10,32)
        s2_11=BitVecVal(5,32)
        s2_11b=BitVecVal(12,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(14,32)
        s2_0b=BitVecVal(15,32)
        s2_4=BitVecVal(12,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(15,32)
        s2_8b=BitVecVal(11,32)
        s2_12=BitVecVal(11,32)
        s2_12b=BitVecVal(9,32)

    elif n==9:

        s2_1=BitVecVal(15,32)
        s2_1b=BitVecVal(8,32)
        s2_5=BitVecVal(13,32)
        s2_5b=BitVecVal(2,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(13,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(13,32)
        s2_2b=BitVecVal(0,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(8,32)
        s2_6b=BitVecVal(11,32)
        s2_14=BitVecVal(10,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(2,32)
        s2_15=BitVecVal(8,32)
        s2_15b=BitVecVal(1,32)
        s2_11=BitVecVal(1,32)
        s2_11b=BitVecVal(2,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(2,32)
        s2_0b=BitVecVal(11,32)
        s2_4=BitVecVal(0,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(4,32)
        s2_8b=BitVecVal(8,32)
        s2_12=BitVecVal(13,32)
        s2_12b=BitVecVal(3,32)

    elif n==10:

        s2_1=BitVecVal(6,32)
        s2_1b=BitVecVal(2,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(7,32)
        s2_9=BitVecVal(3,32)
        s2_9b=BitVecVal(9,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(3,32)
        s2_2b=BitVecVal(8,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(12,32)
        s2_6b=BitVecVal(11,32)
        s2_14=BitVecVal(15,32)
        s2_14b=BitVecVal(1,32)

        s2_3=BitVecVal(7,32)
        s2_3b=BitVecVal(7,32)
        s2_15=BitVecVal(8,32)
        s2_15b=BitVecVal(9,32)
        s2_11=BitVecVal(15,32)
        s2_11b=BitVecVal(11,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(4,32)
        s2_0b=BitVecVal(6,32)
        s2_4=BitVecVal(14,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(5,32)
        s2_8b=BitVecVal(1,32)
        s2_12=BitVecVal(12,32)
        s2_12b=BitVecVal(8,32)

    elif n==11:

        s2_1=BitVecVal(12,32)
        s2_1b=BitVecVal(6,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(8,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(2,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(2,32)
        s2_2b=BitVecVal(12,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(15,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(10,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(0,32)
        s2_15=BitVecVal(4,32)
        s2_15b=BitVecVal(12,32)
        s2_11=BitVecVal(2,32)
        s2_11b=BitVecVal(5,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(2,32)
        s2_0b=BitVecVal(6,32)
        s2_4=BitVecVal(1,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(12,32)
        s2_8b=BitVecVal(6,32)
        s2_12=BitVecVal(15,32)
        s2_12b=BitVecVal(8,32)

    elif n==12:

        s2_1=BitVecVal(12,32)
        s2_1b=BitVecVal(6,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(8,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(2,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(2,32)
        s2_2b=BitVecVal(12,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(15,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(10,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(0,32)
        s2_15=BitVecVal(4,32)
        s2_15b=BitVecVal(12,32)
        s2_11=BitVecVal(2,32)
        s2_11b=BitVecVal(5,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(2,32)
        s2_0b=BitVecVal(6,32)
        s2_4=BitVecVal(1,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(12,32)
        s2_8b=BitVecVal(6,32)
        s2_12=BitVecVal(15,32)
        s2_12b=BitVecVal(8,32)

    elif n==13:

        s2_1=BitVecVal(12,32)
        s2_1b=BitVecVal(6,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(8,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(2,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(2,32)
        s2_2b=BitVecVal(12,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(15,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(10,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(0,32)
        s2_15=BitVecVal(4,32)
        s2_15b=BitVecVal(12,32)
        s2_11=BitVecVal(2,32)
        s2_11b=BitVecVal(5,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(2,32)
        s2_0b=BitVecVal(6,32)
        s2_4=BitVecVal(1,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(12,32)
        s2_8b=BitVecVal(6,32)
        s2_12=BitVecVal(15,32)
        s2_12b=BitVecVal(8,32)

    else:

        s2_1=BitVecVal(12,32)
        s2_1b=BitVecVal(6,32)
        s2_5=BitVecVal(11,32)
        s2_5b=BitVecVal(8,32)
        s2_9=BitVecVal(10,32)
        s2_9b=BitVecVal(2,32)
        s2_13=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4
        s2_13b=I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf


        s2_2= BitVecVal(2,32)
        s2_2b=BitVecVal(12,32)
        s2_10=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4
        s2_10b=I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf
        s2_6=BitVecVal(15,32)
        s2_6b=BitVecVal(2,32)
        s2_14=BitVecVal(10,32)
        s2_14b=BitVecVal(6,32)

        s2_3=BitVecVal(8,32)
        s2_3b=BitVecVal(0,32)
        s2_15=BitVecVal(4,32)
        s2_15b=BitVecVal(12,32)
        s2_11=BitVecVal(2,32)
        s2_11b=BitVecVal(5,32)
        s2_7=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4
        s2_7b=I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf

        s2_0=BitVecVal(2,32)
        s2_0b=BitVecVal(6,32)
        s2_4=BitVecVal(1,32)
        s2_4b=BitVecVal(12,32)
        s2_8=BitVecVal(12,32)
        s2_8b=BitVecVal(6,32)
        s2_12=BitVecVal(15,32)
        s2_12b=BitVecVal(8,32)


    temp = I[s2_1][s2_1b] 
    S = Store(S, BitVecVal(1, 32),I[s2_5][s2_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s2_9][s2_9b])
    S = Store(S, BitVecVal(9, 32),I[s2_13][s2_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s2_2][s2_2b]
    S = Store(S, BitVecVal(2, 32), I[s2_10][s2_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s2_6][s2_6b] 
    S = Store(S, BitVecVal(6, 32), I[s2_14][s2_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s2_3][s2_3b]
    S = Store(S, BitVecVal(3, 32), I[s2_15][s2_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s2_11][s2_11b])
    S = Store(S, BitVecVal(11, 32), I[s2_7][s2_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s2_0][s2_0b])
    S = Store(S, BitVecVal(4, 32), I[s2_4][s2_4b])
    S = Store(S, BitVecVal(8, 32), I[s2_8][s2_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s2_12][s2_12b])


    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3


    s3_0,s3_1,s3_2,s3_3,s3_4,s3_5,s3_6,s3_7,s3_8,s3_9,s3_10,s3_11,s3_12,s3_13,s3_14,s3_15=BitVecs('s3_0 s3_1 s3_2 s3_3 s3_4 s3_5 s3_6 s3_7 s3_8 s3_9 s3_10 s3_11 s3_12 s3_13 s3_14 s3_15',32)
    s3_0b,s3_1b,s3_2b,s3_3b,s3_4b,s3_5b,s3_6b,s3_7b,s3_8b,s3_9b,s3_10b,s3_11b,s3_12b,s3_13b,s3_14b,s3_15b=BitVecs('s3_0b s3_1b s3_2b s3_3b s3_4b s3_5b s3_6b s3_7b s3_8b s3_9b s3_10b s3_11b s3_12b s3_13b s3_14b s3_15b',32)

    if n==0:

        s3_1=BitVecVal(14,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(4,32)
        s3_5b=BitVecVal(11,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(5,32)
        s3_13b=BitVecVal(13,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(1,32)
        s3_10b=BitVecVal(3,32)
        s3_6=BitVecVal(6,32)
        s3_6b=BitVecVal(3,32)
        s3_14=BitVecVal(5,32)
        s3_14b=BitVecVal(10,32)


        s3_3=BitVecVal(3,32)
        s3_3b=BitVecVal(2,32)
        s3_15=BitVecVal(6,32)
        s3_15b=BitVecVal(9,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(3,32)
        s3_7b=BitVecVal(5,32)

        s3_0=BitVecVal(5,32)
        s3_0b=BitVecVal(2,32)
        s3_4=BitVecVal(15,32)
        s3_4b=BitVecVal(8,32)
        s3_8=BitVecVal(5,32)
        s3_8b=BitVecVal(0,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(0,32)

    elif n==1:

        s3_1=BitVecVal(12,32)
        s3_1b=BitVecVal(9,32)
        s3_5=BitVecVal(12,32)
        s3_5b=BitVecVal(8,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(5,32)
        s3_13b=BitVecVal(15,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(15,32)
        s3_10b=BitVecVal(2,32)
        s3_6=BitVecVal(6,32)
        s3_6b=BitVecVal(7,32)
        s3_14=BitVecVal(1,32)
        s3_14b=BitVecVal(13,32)


        s3_3=BitVecVal(1,32)
        s3_3b=BitVecVal(14,32)
        s3_15=BitVecVal(0,32)
        s3_15b=BitVecVal(4,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(2,32)
        s3_7b=BitVecVal(13,32)

        s3_0=BitVecVal(5,32)
        s3_0b=BitVecVal(15,32)
        s3_4=BitVecVal(0,32)
        s3_4b=BitVecVal(15,32)
        s3_8=BitVecVal(12,32)
        s3_8b=BitVecVal(1,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(15,32)

    elif n==2:

        s3_1=BitVecVal(11,32)
        s3_1b=BitVecVal(9,32)
        s3_5=BitVecVal(11,32)
        s3_5b=BitVecVal(11,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(10,32)
        s3_13b=BitVecVal(7,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(6,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(3,32)
        s3_14=BitVecVal(4,32)
        s3_14b=BitVecVal(10,32)


        s3_3=BitVecVal(2,32)
        s3_3b=BitVecVal(7,32)
        s3_15=BitVecVal(14,32)
        s3_15b=BitVecVal(4,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(13,32)
        s3_7b=BitVecVal(15,32)

        s3_0=BitVecVal(11,32)
        s3_0b=BitVecVal(15,32)
        s3_4=BitVecVal(5,32)
        s3_4b=BitVecVal(12,32)
        s3_8=BitVecVal(9,32)
        s3_8b=BitVecVal(15,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(4,32)

    elif n==3:

        s3_1=BitVecVal(8,32)
        s3_1b=BitVecVal(2,32)
        s3_5=BitVecVal(12,32)
        s3_5b=BitVecVal(7,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(12,32)
        s3_13b=BitVecVal(1,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(9,32)
        s3_10b=BitVecVal(11,32)
        s3_6=BitVecVal(7,32)
        s3_6b=BitVecVal(3,32)
        s3_14=BitVecVal(2,32)
        s3_14b=BitVecVal(7,32)


        s3_3=BitVecVal(14,32)
        s3_3b=BitVecVal(11,32)
        s3_15=BitVecVal(2,32)
        s3_15b=BitVecVal(1,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(13,32)
        s3_7b=BitVecVal(4,32)

        s3_0=BitVecVal(0,32)
        s3_0b=BitVecVal(7,32)
        s3_4=BitVecVal(15,32)
        s3_4b=BitVecVal(3,32)
        s3_8=BitVecVal(12,32)
        s3_8b=BitVecVal(11,32)
        s3_12=BitVecVal(2,32)
        s3_12b=BitVecVal(9,32)

    elif n==4:

        s3_1=BitVecVal(1,32)
        s3_1b=BitVecVal(14,32)
        s3_5=BitVecVal(2,32)
        s3_5b=BitVecVal(4,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(7,32)
        s3_13b=BitVecVal(12,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(15,32)
        s3_10b=BitVecVal(12,32)
        s3_6=BitVecVal(8,32)
        s3_6b=BitVecVal(1,32)
        s3_14=BitVecVal(11,32)
        s3_14b=BitVecVal(5,32)


        s3_3=BitVecVal(5,32)
        s3_3b=BitVecVal(12,32)
        s3_15=BitVecVal(4,32)
        s3_15b=BitVecVal(0,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(3,32)
        s3_7b=BitVecVal(4,32)

        s3_0=BitVecVal(11,32)
        s3_0b=BitVecVal(12,32)
        s3_4=BitVecVal(13,32)
        s3_4b=BitVecVal(3,32)
        s3_8=BitVecVal(8,32)
        s3_8b=BitVecVal(12,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(6,32)

    elif n==5:

        s3_1=BitVecVal(2,32)
        s3_1b=BitVecVal(7,32)
        s3_5=BitVecVal(5,32)
        s3_5b=BitVecVal(15,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(12,32)
        s3_13b=BitVecVal(7,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(8,32)
        s3_10b=BitVecVal(9,32)
        s3_6=BitVecVal(12,32)
        s3_6b=BitVecVal(1,32)
        s3_14=BitVecVal(14,32)
        s3_14b=BitVecVal(5,32)


        s3_3=BitVecVal(9,32)
        s3_3b=BitVecVal(7,32)
        s3_15=BitVecVal(5,32)
        s3_15b=BitVecVal(5,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(0,32)
        s3_7b=BitVecVal(9,32)

        s3_0=BitVecVal(13,32)
        s3_0b=BitVecVal(4,32)
        s3_4=BitVecVal(3,32)
        s3_4b=BitVecVal(0,32)
        s3_8=BitVecVal(3,32)
        s3_8b=BitVecVal(8,32)
        s3_12=BitVecVal(2,32)
        s3_12b=BitVecVal(3,32)

    elif n==6:

        s3_1=BitVecVal(6,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(11,32)
        s3_5b=BitVecVal(10,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(1,32)
        s3_13b=BitVecVal(4,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(14,32)
        s3_10b=BitVecVal(7,32)
        s3_6=BitVecVal(13,32)
        s3_6b=BitVecVal(12,32)
        s3_14=BitVecVal(10,32)
        s3_14b=BitVecVal(10,32)


        s3_3=BitVecVal(3,32)
        s3_3b=BitVecVal(14,32)
        s3_15=BitVecVal(0,32)
        s3_15b=BitVecVal(3,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(1,32)
        s3_7b=BitVecVal(3,32)

        s3_0=BitVecVal(7,32)
        s3_0b=BitVecVal(14,32)
        s3_4=BitVecVal(3,32)
        s3_4b=BitVecVal(4,32)
        s3_8=BitVecVal(15,32)
        s3_8b=BitVecVal(0,32)
        s3_12=BitVecVal(3,32)
        s3_12b=BitVecVal(5,32)

    elif n==7:

        s3_1=BitVecVal(15,32)
        s3_1b=BitVecVal(14,32)
        s3_5=BitVecVal(6,32)
        s3_5b=BitVecVal(4,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(1,32)
        s3_13b=BitVecVal(12,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(12,32)
        s3_10b=BitVecVal(10,32)
        s3_6=BitVecVal(11,32)
        s3_6b=BitVecVal(1,32)
        s3_14=BitVecVal(2,32)
        s3_14b=BitVecVal(8,32)


        s3_3=BitVecVal(13,32)
        s3_3b=BitVecVal(7,32)
        s3_15=BitVecVal(0,32)
        s3_15b=BitVecVal(5,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(9,32)
        s3_7b=BitVecVal(2,32)

        s3_0=BitVecVal(7,32)
        s3_0b=BitVecVal(4,32)
        s3_4=BitVecVal(6,32)
        s3_4b=BitVecVal(2,32)
        s3_8=BitVecVal(7,32)
        s3_8b=BitVecVal(11,32)
        s3_12=BitVecVal(15,32)
        s3_12b=BitVecVal(9,32)

    elif n==8:

        s3_1=BitVecVal(0,32)
        s3_1b=BitVecVal(8,32)
        s3_5=BitVecVal(15,32)
        s3_5b=BitVecVal(14,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(8,32)
        s3_13b=BitVecVal(0,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(12,32)
        s3_10b=BitVecVal(4,32)
        s3_6=BitVecVal(12,32)
        s3_6b=BitVecVal(6,32)
        s3_14=BitVecVal(0,32)
        s3_14b=BitVecVal(13,32)


        s3_3=BitVecVal(7,32)
        s3_3b=BitVecVal(14,32)
        s3_15=BitVecVal(4,32)
        s3_15b=BitVecVal(10,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(7,32)
        s3_7b=BitVecVal(5,32)

        s3_0=BitVecVal(13,32)
        s3_0b=BitVecVal(15,32)
        s3_4=BitVecVal(4,32)
        s3_4b=BitVecVal(11,32)
        s3_8=BitVecVal(0,32)
        s3_8b=BitVecVal(15,32)
        s3_12=BitVecVal(5,32)
        s3_12b=BitVecVal(6,32)

    elif n==9:

        s3_1=BitVecVal(11,32)
        s3_1b=BitVecVal(5,32)
        s3_5=BitVecVal(9,32)
        s3_5b=BitVecVal(5,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(4,32)
        s3_13b=BitVecVal(1,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(0,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(4,32)
        s3_14=BitVecVal(3,32)
        s3_14b=BitVecVal(13,32)


        s3_3=BitVecVal(0,32)
        s3_3b=BitVecVal(12,32)
        s3_15=BitVecVal(12,32)
        s3_15b=BitVecVal(9,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(1,32)
        s3_7b=BitVecVal(3,32)

        s3_0=BitVecVal(15,32)
        s3_0b=BitVecVal(1,32)
        s3_4=BitVecVal(15,32)
        s3_4b=BitVecVal(14,32)
        s3_8=BitVecVal(5,32)
        s3_8b=BitVecVal(2,32)
        s3_12=BitVecVal(6,32)
        s3_12b=BitVecVal(6,32)

    elif n==10:

        s3_1=BitVecVal(10,32)
        s3_1b=BitVecVal(9,32)
        s3_5=BitVecVal(1,32)
        s3_5b=BitVecVal(2,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(10,32)
        s3_13b=BitVecVal(10,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(0,32)
        s3_10b=BitVecVal(7,32)
        s3_6=BitVecVal(10,32)
        s3_6b=BitVecVal(1,32)
        s3_14=BitVecVal(1,32)
        s3_14b=BitVecVal(15,32)


        s3_3=BitVecVal(10,32)
        s3_3b=BitVecVal(7,32)
        s3_15=BitVecVal(0,32)
        s3_15b=BitVecVal(15,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(15,32)
        s3_7b=BitVecVal(5,32)

        s3_0=BitVecVal(5,32)
        s3_0b=BitVecVal(10,32)
        s3_4=BitVecVal(12,32)
        s3_4b=BitVecVal(14,32)
        s3_8=BitVecVal(13,32)
        s3_8b=BitVecVal(1,32)
        s3_12=BitVecVal(14,32)
        s3_12b=BitVecVal(8,32)

    elif n==11:

        s3_1=BitVecVal(6,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(3,32)
        s3_5b=BitVecVal(10,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(11,32)
        s3_13b=BitVecVal(4,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(1,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(4,32)
        s3_14=BitVecVal(8,32)
        s3_14b=BitVecVal(9,32)


        s3_3=BitVecVal(2,32)
        s3_3b=BitVecVal(9,32)
        s3_15=BitVecVal(3,32)
        s3_15b=BitVecVal(15,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(12,32)
        s3_7b=BitVecVal(13,32)

        s3_0=BitVecVal(15,32)
        s3_0b=BitVecVal(7,32)
        s3_4=BitVecVal(9,32)
        s3_4b=BitVecVal(12,32)
        s3_8=BitVecVal(11,32)
        s3_8b=BitVecVal(4,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(1,32)

    elif n==12:

        s3_1=BitVecVal(6,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(3,32)
        s3_5b=BitVecVal(10,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(11,32)
        s3_13b=BitVecVal(4,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(1,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(4,32)
        s3_14=BitVecVal(8,32)
        s3_14b=BitVecVal(9,32)


        s3_3=BitVecVal(2,32)
        s3_3b=BitVecVal(9,32)
        s3_15=BitVecVal(3,32)
        s3_15b=BitVecVal(15,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(12,32)
        s3_7b=BitVecVal(13,32)

        s3_0=BitVecVal(15,32)
        s3_0b=BitVecVal(7,32)
        s3_4=BitVecVal(9,32)
        s3_4b=BitVecVal(12,32)
        s3_8=BitVecVal(11,32)
        s3_8b=BitVecVal(4,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(1,32)

    elif n==13:

        s3_1=BitVecVal(6,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(3,32)
        s3_5b=BitVecVal(10,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(11,32)
        s3_13b=BitVecVal(4,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(1,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(4,32)
        s3_14=BitVecVal(8,32)
        s3_14b=BitVecVal(9,32)


        s3_3=BitVecVal(2,32)
        s3_3b=BitVecVal(9,32)
        s3_15=BitVecVal(3,32)
        s3_15b=BitVecVal(15,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(12,32)
        s3_7b=BitVecVal(13,32)

        s3_0=BitVecVal(15,32)
        s3_0b=BitVecVal(7,32)
        s3_4=BitVecVal(9,32)
        s3_4b=BitVecVal(12,32)
        s3_8=BitVecVal(11,32)
        s3_8b=BitVecVal(4,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(1,32)

    else:

        s3_1=BitVecVal(6,32)
        s3_1b=BitVecVal(12,32)
        s3_5=BitVecVal(3,32)
        s3_5b=BitVecVal(10,32)
        s3_9=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4
        s3_9b=I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf
        s3_13=BitVecVal(11,32)
        s3_13b=BitVecVal(4,32)

        s3_2=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4
        s3_2b=I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf
        s3_10=BitVecVal(7,32)
        s3_10b=BitVecVal(1,32)
        s3_6=BitVecVal(2,32)
        s3_6b=BitVecVal(4,32)
        s3_14=BitVecVal(8,32)
        s3_14b=BitVecVal(9,32)


        s3_3=BitVecVal(2,32)
        s3_3b=BitVecVal(9,32)
        s3_15=BitVecVal(3,32)
        s3_15b=BitVecVal(15,32)
        s3_11= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4
        s3_11b= I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf
        s3_7=BitVecVal(12,32)
        s3_7b=BitVecVal(13,32)

        s3_0=BitVecVal(15,32)
        s3_0b=BitVecVal(7,32)
        s3_4=BitVecVal(9,32)
        s3_4b=BitVecVal(12,32)
        s3_8=BitVecVal(11,32)
        s3_8b=BitVecVal(4,32)
        s3_12=BitVecVal(4,32)
        s3_12b=BitVecVal(1,32)

    temp = I[s3_1][s3_1b] 
    S = Store(S, BitVecVal(1, 32),I[s3_5][s3_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s3_9][s3_9b])
    S = Store(S, BitVecVal(9, 32),I[s3_13][s3_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s3_2][s3_2b]
    S = Store(S, BitVecVal(2, 32), I[s3_10][s3_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s3_6][s3_6b] 
    S = Store(S, BitVecVal(6, 32), I[s3_14][s3_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s3_3][s3_3b]
    S = Store(S, BitVecVal(3, 32), I[s3_15][s3_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s3_11][s3_11b])
    S = Store(S, BitVecVal(11, 32), I[s3_7][s3_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s3_0][s3_0b])
    S = Store(S, BitVecVal(4, 32), I[s3_4][s3_4b])
    S = Store(S, BitVecVal(8, 32), I[s3_8][s3_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s3_12][s3_12b])


    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3


    s4_0,s4_1,s4_2,s4_3,s4_4,s4_5,s4_6,s4_7,s4_8,s4_9,s4_10,s4_11,s4_12,s4_13,s4_14,s4_15=BitVecs('s4_0 s4_1 s4_2 s4_3 s4_4 s4_5 s4_6 s4_7 s4_8 s4_9 s4_10 s4_11 s4_12 s4_13 s4_14 s4_15',32)
    s4_0b,s4_1b,s4_2b,s4_3b,s4_4b,s4_5b,s4_6b,s4_7b,s4_8b,s4_9b,s4_10b,s4_11b,s4_12b,s4_13b,s4_14b,s4_15b=BitVecs('s4_0b s4_1b s4_2b s4_3b s4_4b s4_5b s4_6b s4_7b s4_8b s4_9b s4_10b s4_11b s4_12b s4_13b s4_14b s4_15b',32)

    if n==0:

        s4_1=BitVecVal(11,32)
        s4_1b=BitVecVal(3,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(4,32)
        s4_9b=BitVecVal(12,32)
        s4_13=BitVecVal(12,32)
        s4_13b=BitVecVal(14,32)

        s4_2=BitVecVal(7,32)
        s4_2b=BitVecVal(13,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(11,32)
        s4_6b=BitVecVal(14,32)
        s4_14=BitVecVal(15,32)
        s4_14b=BitVecVal(11,32)


        s4_3=BitVecVal(15,32)
        s4_3b=BitVecVal(9,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(9,32) 
        s4_11b=BitVecVal(6,32) 
        s4_7=BitVecVal(2,32)
        s4_7b=BitVecVal(3,32)

        s4_0=BitVecVal(0,32)
        s4_0b=BitVecVal(0,32)
        s4_4=BitVecVal(4,32)
        s4_4b=BitVecVal(1,32)
        s4_8=BitVecVal(5,32)
        s4_8b=BitVecVal(3,32)
        s4_12=BitVecVal(0,32)
        s4_12b=BitVecVal(9,32)

    elif n==1:

        s4_1=BitVecVal(14,32)
        s4_1b=BitVecVal(8,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(12,32)
        s4_9b=BitVecVal(15,32)
        s4_13=BitVecVal(13,32)
        s4_13b=BitVecVal(13,32)

        s4_2=BitVecVal(8,32)
        s4_2b=BitVecVal(9,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(4,32)
        s4_14=BitVecVal(8,32)
        s4_14b=BitVecVal(5,32)


        s4_3=BitVecVal(15,32)
        s4_3b=BitVecVal(2,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(13,32) 
        s4_11b=BitVecVal(8,32) 
        s4_7=BitVecVal(7,32)
        s4_7b=BitVecVal(2,32)

        s4_0=BitVecVal(12,32)
        s4_0b=BitVecVal(15,32)
        s4_4=BitVecVal(7,32)
        s4_4b=BitVecVal(6,32)
        s4_8=BitVecVal(7,32)
        s4_8b=BitVecVal(8,32)
        s4_12=BitVecVal(8,32)
        s4_12b=BitVecVal(4,32)

    elif n==2:

        s4_1=BitVecVal(14,32)
        s4_1b=BitVecVal(10,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(5,32)
        s4_9b=BitVecVal(12,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(6,32)

        s4_2=BitVecVal(3,32)
        s4_2b=BitVecVal(8,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(13,32)
        s4_6b=BitVecVal(6,32)
        s4_14=BitVecVal(2,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(6,32)
        s4_3b=BitVecVal(9,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(9,32) 
        s4_11b=BitVecVal(14,32) 
        s4_7=BitVecVal(12,32)
        s4_7b=BitVecVal(12,32)

        s4_0=BitVecVal(0,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(4,32)
        s4_4b=BitVecVal(10,32)
        s4_8=BitVecVal(13,32)
        s4_8b=BitVecVal(11,32)
        s4_12=BitVecVal(1,32)
        s4_12b=BitVecVal(11,32)

    elif n==3:

        s4_1=BitVecVal(12,32)
        s4_1b=BitVecVal(6,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(7,32)
        s4_9b=BitVecVal(8,32)
        s4_13=BitVecVal(1,32)
        s4_13b=BitVecVal(3,32)

        s4_2=BitVecVal(1,32)
        s4_2b=BitVecVal(4,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(12,32)
        s4_6b=BitVecVal(12,32)
        s4_14=BitVecVal(8,32)
        s4_14b=BitVecVal(15,32)


        s4_3=BitVecVal(15,32)
        s4_3b=BitVecVal(13,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(4,32) 
        s4_11b=BitVecVal(8,32) 
        s4_7=BitVecVal(14,32)
        s4_7b=BitVecVal(9,32)

        s4_0=BitVecVal(12,32)
        s4_0b=BitVecVal(5,32)
        s4_4=BitVecVal(0,32)
        s4_4b=BitVecVal(13,32)
        s4_8=BitVecVal(1,32)
        s4_8b=BitVecVal(15,32)
        s4_12=BitVecVal(10,32)
        s4_12b=BitVecVal(5,32)

    elif n==4:

        s4_1=BitVecVal(3,32)
        s4_1b=BitVecVal(6,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(1,32)
        s4_9b=BitVecVal(0,32)
        s4_13=BitVecVal(7,32)
        s4_13b=BitVecVal(2,32)

        s4_2=BitVecVal(11,32)
        s4_2b=BitVecVal(0,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(13,32)
        s4_6b=BitVecVal(5,32)
        s4_14=BitVecVal(0,32)
        s4_14b=BitVecVal(12,32)


        s4_3=BitVecVal(0,32)
        s4_3b=BitVecVal(9,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(1,32) 
        s4_11b=BitVecVal(8,32) 
        s4_7=BitVecVal(4,32)
        s4_7b=BitVecVal(10,32)

        s4_0=BitVecVal(6,32)
        s4_0b=BitVecVal(5,32)
        s4_4=BitVecVal(6,32)
        s4_4b=BitVecVal(6,32)
        s4_8=BitVecVal(6,32)
        s4_8b=BitVecVal(4,32)
        s4_12=BitVecVal(5,32)
        s4_12b=BitVecVal(10,32)

    elif n==5:

        s4_1=BitVecVal(12,32)
        s4_1b=BitVecVal(15,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(12,32)
        s4_9b=BitVecVal(6,32)
        s4_13=BitVecVal(12,32)
        s4_13b=BitVecVal(12,32)

        s4_2=BitVecVal(10,32)
        s4_2b=BitVecVal(7,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(13,32)
        s4_6b=BitVecVal(9,32)
        s4_14=BitVecVal(7,32)
        s4_14b=BitVecVal(8,32)


        s4_3=BitVecVal(15,32)
        s4_3b=BitVecVal(12,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(0,32) 
        s4_11b=BitVecVal(1,32) 
        s4_7=BitVecVal(8,32)
        s4_7b=BitVecVal(8,32)

        s4_0=BitVecVal(4,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(0,32)
        s4_4b=BitVecVal(4,32)
        s4_8=BitVecVal(0,32)
        s4_8b=BitVecVal(7,32)
        s4_12=BitVecVal(2,32)
        s4_12b=BitVecVal(6,32)

    elif n==6:

        s4_1=BitVecVal(15,32)
        s4_1b=BitVecVal(4,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(15,32)
        s4_9b=BitVecVal(10,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(9,32)
        s4_2b=BitVecVal(4,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(12,32)
        s4_14=BitVecVal(8,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(11,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(7,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(11,32)
        s4_7b=BitVecVal(2,32)

        s4_0=BitVecVal(15,32)
        s4_0b=BitVecVal(3,32)
        s4_4=BitVecVal(1,32)
        s4_4b=BitVecVal(8,32)
        s4_8=BitVecVal(8,32)
        s4_8b=BitVecVal(12,32)
        s4_12=BitVecVal(9,32)
        s4_12b=BitVecVal(6,32)

    elif n==7:

        s4_1=BitVecVal(4,32)
        s4_1b=BitVecVal(3,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(9,32)
        s4_9b=BitVecVal(12,32)
        s4_13=BitVecVal(11,32)
        s4_13b=BitVecVal(11,32)

        s4_2=BitVecVal(7,32)
        s4_2b=BitVecVal(4,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(3,32)
        s4_6b=BitVecVal(4,32)
        s4_14=BitVecVal(12,32)
        s4_14b=BitVecVal(8,32)


        s4_3=BitVecVal(6,32)
        s4_3b=BitVecVal(11,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(4,32) 
        s4_11b=BitVecVal(15,32) 
        s4_7=BitVecVal(0,32)
        s4_7b=BitVecVal(14,32)

        s4_0=BitVecVal(9,32)
        s4_0b=BitVecVal(2,32)
        s4_4=BitVecVal(10,32)
        s4_4b=BitVecVal(10,32)
        s4_8=BitVecVal(2,32)
        s4_8b=BitVecVal(1,32)
        s4_12=BitVecVal(9,32)
        s4_12b=BitVecVal(9,32)

    elif n==8:

        s4_1=BitVecVal(11,32)
        s4_1b=BitVecVal(11,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(12,32)
        s4_9b=BitVecVal(13,32)
        s4_13=BitVecVal(3,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(1,32)
        s4_2b=BitVecVal(12,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(13,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(11,32)
        s4_14b=BitVecVal(4,32)


        s4_3=BitVecVal(13,32)
        s4_3b=BitVecVal(6,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(9,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(15,32)
        s4_7b=BitVecVal(3,32)

        s4_0=BitVecVal(9,32)
        s4_0b=BitVecVal(14,32)
        s4_4=BitVecVal(11,32)
        s4_4b=BitVecVal(3,32)
        s4_8=BitVecVal(7,32)
        s4_8b=BitVecVal(6,32)
        s4_12=BitVecVal(11,32)
        s4_12b=BitVecVal(1,32)

    elif n==9:

        s4_1=BitVecVal(2,32)
        s4_1b=BitVecVal(10,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(8,32)
        s4_9b=BitVecVal(3,32)
        s4_13=BitVecVal(13,32)
        s4_13b=BitVecVal(5,32)

        s4_2=BitVecVal(5,32)
        s4_2b=BitVecVal(1,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(2,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(13,32)
        s4_3b=BitVecVal(13,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(7,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(15,32)
        s4_7b=BitVecVal(14,32)

        s4_0=BitVecVal(10,32)
        s4_0b=BitVecVal(1,32)
        s4_4=BitVecVal(11,32)
        s4_4b=BitVecVal(11,32)
        s4_8=BitVecVal(0,32)
        s4_8b=BitVecVal(0,32)
        s4_12=BitVecVal(3,32)
        s4_12b=BitVecVal(3,32)

    elif n==10:

        s4_1=BitVecVal(12,32)
        s4_1b=BitVecVal(9,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(10,32)
        s4_9b=BitVecVal(12,32)
        s4_13=BitVecVal(13,32)
        s4_13b=BitVecVal(3,32)

        s4_2=BitVecVal(12,32)
        s4_2b=BitVecVal(5,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(12,32)
        s4_6b=BitVecVal(0,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(2,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(6,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(14,32) 
        s4_11b=BitVecVal(6,32) 
        s4_7=BitVecVal(5,32)
        s4_7b=BitVecVal(12,32)

        s4_0=BitVecVal(11,32)
        s4_0b=BitVecVal(14,32)
        s4_4=BitVecVal(8,32)
        s4_4b=BitVecVal(11,32)
        s4_8=BitVecVal(3,32)
        s4_8b=BitVecVal(14,32)
        s4_12=BitVecVal(9,32)
        s4_12b=BitVecVal(11,32)

    elif n==11:

        s4_1=BitVecVal(8,32)
        s4_1b=BitVecVal(0,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(8,32)
        s4_9b=BitVecVal(13,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(10,32)
        s4_2b=BitVecVal(3,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(5,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(11,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(10,32)
        s4_7b=BitVecVal(5,32)

        s4_0=BitVecVal(6,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(13,32)
        s4_4b=BitVecVal(14,32)
        s4_8=BitVecVal(8,32)
        s4_8b=BitVecVal(13,32)
        s4_12=BitVecVal(8,32)
        s4_12b=BitVecVal(3,32)

    elif n==12:

        s4_1=BitVecVal(8,32)
        s4_1b=BitVecVal(0,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(8,32)
        s4_9b=BitVecVal(13,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(10,32)
        s4_2b=BitVecVal(3,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(5,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(11,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(10,32)
        s4_7b=BitVecVal(5,32)

        s4_0=BitVecVal(6,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(13,32)
        s4_4b=BitVecVal(14,32)
        s4_8=BitVecVal(8,32)
        s4_8b=BitVecVal(13,32)
        s4_12=BitVecVal(8,32)
        s4_12b=BitVecVal(3,32)

    elif n==13:

        s4_1=BitVecVal(8,32)
        s4_1b=BitVecVal(0,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(8,32)
        s4_9b=BitVecVal(13,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(10,32)
        s4_2b=BitVecVal(3,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(5,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(11,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(10,32)
        s4_7b=BitVecVal(5,32)

        s4_0=BitVecVal(6,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(13,32)
        s4_4b=BitVecVal(14,32)
        s4_8=BitVecVal(8,32)
        s4_8b=BitVecVal(13,32)
        s4_12=BitVecVal(8,32)
        s4_12b=BitVecVal(3,32)

    else:

        s4_1=BitVecVal(8,32)
        s4_1b=BitVecVal(0,32)
        s4_5=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4
        s4_5b=I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_9=BitVecVal(8,32)
        s4_9b=BitVecVal(13,32)
        s4_13=BitVecVal(5,32)
        s4_13b=BitVecVal(0,32)

        s4_2=BitVecVal(10,32)
        s4_2b=BitVecVal(3,32)
        s4_10=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4
        s4_10b=I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_6=BitVecVal(10,32)
        s4_6b=BitVecVal(7,32)
        s4_14=BitVecVal(3,32)
        s4_14b=BitVecVal(6,32)


        s4_3=BitVecVal(7,32)
        s4_3b=BitVecVal(5,32)
        s4_15=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4
        s4_15b=I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf
        s4_11=BitVecVal(11,32) 
        s4_11b=BitVecVal(13,32) 
        s4_7=BitVecVal(10,32)
        s4_7b=BitVecVal(5,32)

        s4_0=BitVecVal(6,32)
        s4_0b=BitVecVal(8,32)
        s4_4=BitVecVal(13,32)
        s4_4b=BitVecVal(14,32)
        s4_8=BitVecVal(8,32)
        s4_8b=BitVecVal(13,32)
        s4_12=BitVecVal(8,32)
        s4_12b=BitVecVal(3,32)


    temp = I[s4_1][s4_1b] 
    S = Store(S, BitVecVal(1, 32),I[s4_5][s4_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s4_9][s4_9b])
    S = Store(S, BitVecVal(9, 32),I[s4_13][s4_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s4_2][s4_2b]
    S = Store(S, BitVecVal(2, 32), I[s4_10][s4_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s4_6][s4_6b] 
    S = Store(S, BitVecVal(6, 32), I[s4_14][s4_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s4_3][s4_3b]
    S = Store(S, BitVecVal(3, 32), I[s4_15][s4_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s4_11][s4_11b])
    S = Store(S, BitVecVal(11, 32), I[s4_7][s4_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s4_0][s4_0b])
    S = Store(S, BitVecVal(4, 32), I[s4_4][s4_4b])
    S = Store(S, BitVecVal(8, 32), I[s4_8][s4_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s4_12][s4_12b])


    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3


    s5_0,s5_1,s5_2,s5_3,s5_4,s5_5,s5_6,s5_7,s5_8,s5_9,s5_10,s5_11,s5_12,s5_13,s5_14,s5_15=BitVecs('s5_0 s5_1 s5_2 s5_3 s5_4 s5_5 s5_6 s5_7 s5_8 s5_9 s5_10 s5_11 s5_12 s5_13 s5_14 s5_15',32)
    s5_0b,s5_1b,s5_2b,s5_3b,s5_4b,s5_5b,s5_6b,s5_7b,s5_8b,s5_9b,s5_10b,s5_11b,s5_12b,s5_13b,s5_14b,s5_15b=BitVecs('s5_0b s5_1b s5_2b s5_3b s5_4b s5_5b s5_6b s5_7b s5_8b s5_9b s5_10b s5_11b s5_12b s5_13b s5_14b s5_15b',32)

    if n==0:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(2,32)
        s5_5b=BitVecVal(9,32)
        s5_9=BitVecVal(8,32)
        s5_9b=BitVecVal(11,32)
        s5_13=BitVecVal(6,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(15,32)
        s5_10b=BitVecVal(15,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(15,32)
        s5_14=BitVecVal(10,32)
        s5_14b=BitVecVal(14,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(9,32)
        s5_15b=BitVecVal(0,32)
        s5_11=BitVecVal(2,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(9,32)
        s5_7b=BitVecVal(9,32)

        s5_0=BitVecVal(6,32)
        s5_0b=BitVecVal(3,32)
        s5_4=BitVecVal(8,32)
        s5_4b=BitVecVal(3,32)
        s5_8=BitVecVal(14,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(0,32)
        s5_12b=BitVecVal(1,32)

    elif n==1:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(8,32)
        s5_5b=BitVecVal(10,32)
        s5_9=BitVecVal(12,32)
        s5_9b=BitVecVal(1,32)
        s5_13=BitVecVal(9,32)
        s5_13b=BitVecVal(11,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(10,32)
        s5_10b=BitVecVal(7,32)
        s5_6=BitVecVal(9,32)
        s5_6b=BitVecVal(7,32)
        s5_14=BitVecVal(4,32)
        s5_14b=BitVecVal(9,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(6,32)
        s5_15b=BitVecVal(1,32)
        s5_11=BitVecVal(4,32) 
        s5_11b=BitVecVal(0,32) 
        s5_7=BitVecVal(8,32)
        s5_7b=BitVecVal(9,32)

        s5_0=BitVecVal(8,32)
        s5_0b=BitVecVal(10,32)
        s5_4=BitVecVal(3,32)
        s5_4b=BitVecVal(8,32)
        s5_8=BitVecVal(11,32)
        s5_8b=BitVecVal(12,32)
        s5_12=BitVecVal(5,32)
        s5_12b=BitVecVal(15,32)

    elif n==2:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(4,32)
        s5_5b=BitVecVal(10,32)
        s5_9=BitVecVal(11,32)
        s5_9b=BitVecVal(1,32)
        s5_13=BitVecVal(8,32)
        s5_13b=BitVecVal(7,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(0,32)
        s5_10b=BitVecVal(7,32)
        s5_6=BitVecVal(15,32)
        s5_6b=BitVecVal(7,32)
        s5_14=BitVecVal(15,32)
        s5_14b=BitVecVal(6,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(0,32)
        s5_15b=BitVecVal(11,32)
        s5_11=BitVecVal(4,32) 
        s5_11b=BitVecVal(11,32) 
        s5_7=BitVecVal(15,32)
        s5_7b=BitVecVal(9,32)

        s5_0=BitVecVal(3,32)
        s5_0b=BitVecVal(0,32)
        s5_4=BitVecVal(13,32)
        s5_4b=BitVecVal(6,32)
        s5_8=BitVecVal(11,32)
        s5_8b=BitVecVal(9,32)
        s5_12=BitVecVal(10,32)
        s5_12b=BitVecVal(15,32)

    elif n==3:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(11,32)
        s5_5b=BitVecVal(12,32)
        s5_9=BitVecVal(7,32)
        s5_9b=BitVecVal(13,32)
        s5_13=BitVecVal(11,32)
        s5_13b=BitVecVal(4,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(15,32)
        s5_10b=BitVecVal(10,32)
        s5_6=BitVecVal(7,32)
        s5_6b=BitVecVal(3,32)
        s5_14=BitVecVal(4,32)
        s5_14b=BitVecVal(11,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(5,32)
        s5_15b=BitVecVal(2,32)
        s5_11=BitVecVal(1,32) 
        s5_11b=BitVecVal(14,32) 
        s5_7=BitVecVal(5,32)
        s5_7b=BitVecVal(4,32)

        s5_0=BitVecVal(10,32)
        s5_0b=BitVecVal(6,32)
        s5_4=BitVecVal(13,32)
        s5_4b=BitVecVal(7,32)
        s5_8=BitVecVal(12,32)
        s5_8b=BitVecVal(0,32)
        s5_12=BitVecVal(0,32)
        s5_12b=BitVecVal(6,32)

    elif n==4:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(12,32)
        s5_5b=BitVecVal(10,32)
        s5_9=BitVecVal(4,32)
        s5_9b=BitVecVal(0,32)
        s5_13=BitVecVal(0,32)
        s5_13b=BitVecVal(5,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(14,32)
        s5_10b=BitVecVal(7,32)
        s5_6=BitVecVal(15,32)
        s5_6b=BitVecVal(14,32)
        s5_14=BitVecVal(0,32)
        s5_14b=BitVecVal(3,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(10,32)
        s5_15b=BitVecVal(13,32)
        s5_11=BitVecVal(13,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(0,32)
        s5_7b=BitVecVal(1,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(13,32)
        s5_4=BitVecVal(3,32)
        s5_4b=BitVecVal(3,32)
        s5_8=BitVecVal(4,32)
        s5_8b=BitVecVal(3,32)
        s5_12=BitVecVal(11,32)
        s5_12b=BitVecVal(14,32)

    elif n==5:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(11,32)
        s5_5b=BitVecVal(4,32)
        s5_9=BitVecVal(4,32)
        s5_9b=BitVecVal(11,32)
        s5_13=BitVecVal(8,32)
        s5_13b=BitVecVal(10,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(5,32)
        s5_10b=BitVecVal(12,32)
        s5_6=BitVecVal(11,32)
        s5_6b=BitVecVal(12,32)
        s5_14=BitVecVal(3,32)
        s5_14b=BitVecVal(5,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(7,32)
        s5_15b=BitVecVal(12,32)
        s5_11=BitVecVal(12,32) 
        s5_11b=BitVecVal(4,32) 
        s5_7=BitVecVal(11,32)
        s5_7b=BitVecVal(0,32)

        s5_0=BitVecVal(5,32)
        s5_0b=BitVecVal(2,32)
        s5_4=BitVecVal(15,32)
        s5_4b=BitVecVal(2,32)
        s5_8=BitVecVal(12,32)
        s5_8b=BitVecVal(5,32)
        s5_12=BitVecVal(15,32)
        s5_12b=BitVecVal(7,32)

    elif n==6:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(2,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(5,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(11,32)
        s5_13b=BitVecVal(15,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(2,32)
        s5_10b=BitVecVal(2,32)
        s5_6=BitVecVal(4,32)
        s5_6b=BitVecVal(4,32)
        s5_14=BitVecVal(9,32)
        s5_14b=BitVecVal(1,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(15,32)
        s5_15b=BitVecVal(15,32)
        s5_11=BitVecVal(3,32) 
        s5_11b=BitVecVal(7,32) 
        s5_7=BitVecVal(2,32)
        s5_7b=BitVecVal(1,32)

        s5_0=BitVecVal(0,32)
        s5_0b=BitVecVal(13,32)
        s5_4=BitVecVal(10,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(6,32)
        s5_8b=BitVecVal(4,32)
        s5_12=BitVecVal(9,32)
        s5_12b=BitVecVal(0,32)

    elif n==7:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(13,32)
        s5_5b=BitVecVal(14,32)
        s5_9=BitVecVal(14,32)
        s5_9b=BitVecVal(10,32)
        s5_13=BitVecVal(1,32)
        s5_13b=BitVecVal(10,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(9,32)
        s5_10b=BitVecVal(2,32)
        s5_6=BitVecVal(14,32)
        s5_6b=BitVecVal(8,32)
        s5_14=BitVecVal(1,32)
        s5_14b=BitVecVal(8,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(8,32)
        s5_15b=BitVecVal(4,32)
        s5_11=BitVecVal(10,32) 
        s5_11b=BitVecVal(11,32) 
        s5_7=BitVecVal(7,32)
        s5_7b=BitVecVal(15,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(15,32)
        s5_4=BitVecVal(10,32)
        s5_4b=BitVecVal(12,32)
        s5_8=BitVecVal(15,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(14,32)
        s5_12b=BitVecVal(14,32)

    elif n==8:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(11,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(0,32)
        s5_9b=BitVecVal(4,32)
        s5_13=BitVecVal(14,32)
        s5_13b=BitVecVal(10,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(9,32)
        s5_10b=BitVecVal(12,32)
        s5_6=BitVecVal(8,32)
        s5_6b=BitVecVal(13,32)
        s5_14=BitVecVal(0,32)
        s5_14b=BitVecVal(14,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(5,32)
        s5_15b=BitVecVal(14,32)
        s5_11=BitVecVal(0,32) 
        s5_11b=BitVecVal(13,32) 
        s5_7=BitVecVal(15,32)
        s5_7b=BitVecVal(6,32)

        s5_0=BitVecVal(0,32)
        s5_0b=BitVecVal(11,32)
        s5_4=BitVecVal(6,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(3,32)
        s5_8b=BitVecVal(8,32)
        s5_12=BitVecVal(12,32)
        s5_12b=BitVecVal(8,32)

    elif n==9:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(14,32)
        s5_5b=BitVecVal(12,32)
        s5_9=BitVecVal(0,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(14,32)
        s5_13b=BitVecVal(5,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(13,32)
        s5_10b=BitVecVal(1,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(5,32)
        s5_14=BitVecVal(12,32)
        s5_14b=BitVecVal(12,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(15,32)
        s5_15b=BitVecVal(15,32)
        s5_11=BitVecVal(11,32) 
        s5_11b=BitVecVal(11,32) 
        s5_7=BitVecVal(12,32)
        s5_7b=BitVecVal(1,32)

        s5_0=BitVecVal(3,32)
        s5_0b=BitVecVal(2,32)
        s5_4=BitVecVal(14,32)
        s5_4b=BitVecVal(10,32)
        s5_8=BitVecVal(6,32)
        s5_8b=BitVecVal(3,32)
        s5_12=BitVecVal(12,32)
        s5_12b=BitVecVal(3,32)

    elif n==10:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(9,32)
        s5_5b=BitVecVal(1,32)
        s5_9=BitVecVal(6,32)
        s5_9b=BitVecVal(6,32)
        s5_13=BitVecVal(13,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(10,32)
        s5_10b=BitVecVal(6,32)
        s5_6=BitVecVal(2,32)
        s5_6b=BitVecVal(3,32)
        s5_14=BitVecVal(11,32)
        s5_14b=BitVecVal(10,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(8,32)
        s5_15b=BitVecVal(14,32)
        s5_11=BitVecVal(4,32) 
        s5_11b=BitVecVal(10,32) 
        s5_7=BitVecVal(3,32)
        s5_7b=BitVecVal(8,32)

        s5_0=BitVecVal(10,32)
        s5_0b=BitVecVal(14,32)
        s5_4=BitVecVal(3,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(11,32)
        s5_8b=BitVecVal(2,32)
        s5_12=BitVecVal(1,32)
        s5_12b=BitVecVal(4,32)

    elif n==11:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(5,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(5,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(12,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(0,32)
        s5_10b=BitVecVal(10,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(5,32)
        s5_14=BitVecVal(5,32)
        s5_14b=BitVecVal(12,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(7,32)
        s5_15b=BitVecVal(10,32)
        s5_11=BitVecVal(0,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(9,32)
        s5_7b=BitVecVal(13,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(5,32)
        s5_4=BitVecVal(1,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(5,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(14,32)
        s5_12b=BitVecVal(12,32)

    elif n==12:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(5,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(5,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(12,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(0,32)
        s5_10b=BitVecVal(10,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(5,32)
        s5_14=BitVecVal(5,32)
        s5_14b=BitVecVal(12,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(7,32)
        s5_15b=BitVecVal(10,32)
        s5_11=BitVecVal(0,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(9,32)
        s5_7b=BitVecVal(13,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(5,32)
        s5_4=BitVecVal(1,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(5,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(14,32)
        s5_12b=BitVecVal(12,32)

    elif n==13:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(5,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(5,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(12,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(0,32)
        s5_10b=BitVecVal(10,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(5,32)
        s5_14=BitVecVal(5,32)
        s5_14b=BitVecVal(12,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(7,32)
        s5_15b=BitVecVal(10,32)
        s5_11=BitVecVal(0,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(9,32)
        s5_7b=BitVecVal(13,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(5,32)
        s5_4=BitVecVal(1,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(5,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(14,32)
        s5_12b=BitVecVal(12,32)

    else:

        s5_1=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_1b=I[I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] >>4][I[I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] >> 4][I[I[S2[key1]][S3[5]]>>4][I[S2[key1]][S3[5]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_5=BitVecVal(5,32)
        s5_5b=BitVecVal(13,32)
        s5_9=BitVecVal(5,32)
        s5_9b=BitVecVal(3,32)
        s5_13=BitVecVal(12,32)
        s5_13b=BitVecVal(13,32)

        s5_2=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_2b=I[I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] >> 4][I[I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] >> 4][I[I[S2[key2]][S3[10]]>>4][I[S2[key2]][S3[10]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_10=BitVecVal(0,32)
        s5_10b=BitVecVal(10,32)
        s5_6=BitVecVal(0,32)
        s5_6b=BitVecVal(5,32)
        s5_14=BitVecVal(5,32)
        s5_14b=BitVecVal(12,32)


        s5_3=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] >> 4
        s5_3b=I[I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] >> 4][I[I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] >>4][I[I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] >> 4][I[I[S2[key3]][S3[15]]>>4][I[S2[key3]][S3[15]] & 0xf] & 0xf] & 0xf] & 0xf] & 0xf
        s5_15=BitVecVal(7,32)
        s5_15b=BitVecVal(10,32)
        s5_11=BitVecVal(0,32) 
        s5_11b=BitVecVal(6,32) 
        s5_7=BitVecVal(9,32)
        s5_7b=BitVecVal(13,32)

        s5_0=BitVecVal(4,32)
        s5_0b=BitVecVal(5,32)
        s5_4=BitVecVal(1,32)
        s5_4b=BitVecVal(13,32)
        s5_8=BitVecVal(5,32)
        s5_8b=BitVecVal(13,32)
        s5_12=BitVecVal(14,32)
        s5_12b=BitVecVal(12,32)



    temp = I[s5_1][s5_1b] 
    S = Store(S, BitVecVal(1, 32),I[s5_5][s5_5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s5_9][s5_9b])
    S = Store(S, BitVecVal(9, 32),I[s5_13][s5_13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s5_2][s5_2b]
    S = Store(S, BitVecVal(2, 32), I[s5_10][s5_10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s5_6][s5_6b] 
    S = Store(S, BitVecVal(6, 32), I[s5_14][s5_14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s5_3][s5_3b]
    S = Store(S, BitVecVal(3, 32), I[s5_15][s5_15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s5_11][s5_11b])
    S = Store(S, BitVecVal(11, 32), I[s5_7][s5_7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s5_0][s5_0b])
    S = Store(S, BitVecVal(4, 32), I[s5_4][s5_4b])
    S = Store(S, BitVecVal(8, 32), I[s5_8][s5_8b]) 
    S = Store(S, BitVecVal(12, 32),I[s5_12][s5_12b])


    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=1
    ret = Store(ret, j * 4,S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[key6 + j * 4] << 1) #key6 1
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * key7] #key7 4
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If(x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) 
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4,  S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If( ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[key8 + j * 4]  # key8 3
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283),  ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)),, ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If(x >> key9 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x)) #key9 8
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #j=2
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If( ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If( ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    #ret = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4,  ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, key10 + j * 4,  S[2 + j * 4] << 1) #key10 2
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, 3 + j * 4,  S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))

    j = j + 1 #key8 1 
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If(x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4,  S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x)) #
    #ret = Store(ret, 1 + j * 4, If(Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ 283), ret[2 + j * 4] ^ x))
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4,  ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n])) #key9 2

    ret = Store(ret, 3 + j * 4, S[3 + j * 4] << 1)
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n])) #key10 3



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


def sub(key1,key2,key3,key4,key5,nb,n):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    S2 = Array('S2', BitVecSort(32), BitVecSort(32))
    S3 = Array('S3', BitVecSort(32), BitVecSort(32))
    I = Array('A', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    W = Array('W', BitVecSort(32), ArraySort(BitVecSort(32), BitVecSort(32)))
    tm = Array('tm', BitVecSort(32), BitVecSort(32))
    tm2 = Array('tm2', BitVecSort(32), BitVecSort(32))
    ## Initializing the `statemt` array ##
    '''i = 0
    for elem in statemt:
        S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
        i += 1'''

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
    s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15=BitVecs('s0 s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15',32)
    s0b,s1b,s2b,s3b,s4b,s5b,s6b,s7b,s8b,s9b,s10b,s11b,s12b,s13b,s14b,s15b=BitVecs('s0b s1b s2b s3b s4b s5b s6b s7b s8b s9b s10b s11b s12b s13b s14b s15b',32)
    if n==0:
        i = 0
        for elem in statemt0:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt0_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt0_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==1:
        i = 0
        for elem in statemt1:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt1_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt1_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==2:
        i = 0
        for elem in statemt2:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt2_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt2_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]
    elif n==3:
        i = 0
        for elem in statemt3:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt3_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt3_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==4:
        i = 0
        for elem in statemt4:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt4_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt4_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==5:
        i = 0
        for elem in statemt5:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt5_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt5_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]
    elif n==6:
        i = 0
        for elem in statemt6:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt6_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt6_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==7:
        i = 0
        for elem in statemt7:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt7_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt7_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==8:
        i = 0
        for elem in statemt8:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt8_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt8_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==9:
        i = 0
        for elem in statemt9:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt9_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt9_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==10:
        i = 0
        for elem in statemt10:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt10_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt10_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==11:
        i = 0
        for elem in statemt11:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt11_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt11_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==12:
        i = 0
        for elem in statemt12:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt12_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt12_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    elif n==13:
        i = 0
        for elem in statemt13:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt13_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt13_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

    else:
        i = 0
        for elem in statemt14:
            S = Store(S, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt14_shift:
            S2 = Store(S2, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1
        i = 0
        for elem in statemt14_and:
            S3 = Store(S3, BitVecVal(i, 32), BitVecVal(elem, 32))
            i += 1

        s1=S2[1]
        s1b=S3[1]
        s5=S2[key1]
        s5b=S3[5]
        s9=S2[9]
        s9b=S3[9]
        s13=S2[13]
        s13b=S3[13]

        s2=S2[2]
        s2b=S3[2]
        s10=S2[key2]
        s10b=S3[10]
        s6=S2[6]
        s6b=S3[6]
        s14=S2[14]
        s14b=S3[14]

        s3=S2[3]
        s3b=S3[3]
        s15=S2[key3]
        s15b=S3[15]
        s11=S2[11]
        s11b=S3[11]
        s7=S2[7]
        s7b=S3[7]

        s0=S2[0]
        s0b=S3[0]
        s4=S2[4]
        s4b=S3[4]
        s8=S2[8]
        s8b=S3[8]
        s12=S2[12]
        s12b=S3[12]

# --------------------------------Iteration 0 ----------------------------------------------------------------------------------
    # ---------------------- ByetSub ShiftRow ------------------

    

    temp = I[s1][s1b]
    S = Store(S, BitVecVal(1, 32),I[s5][s5b]) #key1=5
    S = Store(S, BitVecVal(5, 32),I[s9][s9b])
    S = Store(S, BitVecVal(9, 32),I[s13][s13b])
    S = Store(S, BitVecVal(13, 32),temp)

    temp = I[s2][s2b]
    S = Store(S, BitVecVal(2, 32), I[s10][s10b]) #key2=10
    S = Store(S, BitVecVal(10, 32), temp)
    temp = I[s6][s6b] 
    S = Store(S, BitVecVal(6, 32), I[s14][s14b])
    S = Store(S, BitVecVal(14, 32),temp)

    temp = I[s3][s3b]
    S = Store(S, BitVecVal(3, 32), I[s15][s15b]) #key3=15
    S = Store(S, BitVecVal(15, 32), I[s11][s11b])
    S = Store(S, BitVecVal(11, 32), I[s7][s7b]) 
    S = Store(S, BitVecVal(7, 32), temp)

    S = Store(S, BitVecVal(0, 32), I[s0][s0b])
    S = Store(S, BitVecVal(4, 32), I[s4][s4b])
    S = Store(S, BitVecVal(8, 32), I[s8][s8b]) 
    S = Store(S, BitVecVal(12, 32),I[s12][s12b])


    # ------------------------ MixColumn AddRoundKey ---------------------------------

    
    ret = Array('ret', BitVecSort(32), BitVecSort(32))
    x = BitVecVal(0, 32)
    j = BitVecVal(0, 32)

    # j = j + 1
    ret = Store(ret, j * 4, S[j * 4] << 1)
    ret = Store(ret, j * 4, If(ret[j * 4] >> 8 == 1, ret[j * 4] ^ 283, ret[j * 4]))
    x = S[1 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, j * 4, If( x >> 8 == 1, ret[j * 4] ^ (x ^ 283), ret[j * 4] ^ x))
    #ret = Store(ret, j * 4, If( Not(x >> 8 == 1), , ret[j * 4]))
    ret = Store(ret, j * 4, ret[j * 4] ^ (S[2 + j * 4] ^ S[3 + j * 4] ^ W[0][j + nb * n]))

    ret = Store(ret, 1 + j * 4, S[1 + j * 4] << 1)
    ret = Store(ret, 1 + j * 4, If(ret[1 + j * 4] >> 8 == 1, ret[1 + j * 4] ^ 283, ret[1 + j * 4]))
    x = S[2 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 1 + j * 4, If( x >> 8 == 1, ret[1 + j * 4] ^ (x ^ 283), ret[1 + j * 4] ^ x))
    # = Store(ret, 1 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[1 + j * 4]))
    ret = Store(ret, 1 + j * 4, ret[1 + j * 4] ^ (S[3 + j * 4] ^ S[j * 4] ^ W[1][j + nb * n]))

    ret = Store(ret, 2 + j * 4, S[2 + j * 4] << 1)
    ret = Store(ret, 2 + j * 4, If(ret[2 + j * 4] >> 8 == 1, ret[2 + j * 4] ^ 283, ret[2 + j * 4]))
    x = S[3 + j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 2 + j * 4, If( x >> 8 == 1, ret[2 + j * 4] ^ (x ^ key4), ret[2 + j * 4] ^ x)) #key4 283
    #ret = Store(ret, 2 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[2 + j * 4]))
    ret = Store(ret, 2 + j * 4, ret[2 + j * 4] ^ (S[j * 4] ^ S[1 + j * 4] ^ W[2][j + nb * n]))

    ret = Store(ret, key5 + j * 4, S[3 + j * 4] << 1) #key5 3
    ret = Store(ret, 3 + j * 4, If(ret[3 + j * 4] >> 8 == 1, ret[3 + j * 4] ^ 283, ret[3 + j * 4]))
    x = S[j * 4]
    x = x ^ (x << 1)
    ret = Store(ret, 3 + j * 4, If( x >> 8 == 1, ret[3 + j * 4] ^ (x ^ 283), ret[3 + j * 4] ^ x))
    #ret = Store(ret, 3 + j * 4, If(And(j < nb, Not(x >> 8 == 1)), , ret[3 + j * 4]))
    ret = Store(ret, 3 + j * 4, ret[3 + j * 4] ^ (S[1 + j * 4] ^ S[2 + j * 4] ^ W[3][j + nb * n]))


    o0=ret[0]
    o1=ret[1]
    o2=ret[2]
    o3=ret[3]

    o=tuple.tuple2(o0,o1,o2,o3)
    return o


for kk in range(0,15):
    gg = Tactic('smt').solver()
    ia = str(4) + " " + str(kk)
    [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    #,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
    oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))

    print(str(kk)+"="+str(gg.check(findOutput(5,10,15,283,3,1,4,3,8,2,4,kk)==oa)))

'''gg = Tactic('smt').solver()
ia = str(4) + " " + str(5)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))'''



j = 0


s = Tactic('smt').solver()

#s.add(simplify(findOutput(k1_1,k2_1,k3_1,k4_1,k5_1,key1_1,key2_1,key3_1,nb,n)) == out1)
#s.add(simplify(findOutput(k1_2,k2_2,k3_2,k4_2,k5_2,key1_2,key2_2,key3_2,nb,n)) == out2)

s.add(simplify(sub(key1_1,key2_1,key3_1,key4_1,key5_1,nb,n)) == out3)
s.add(simplify(sub(key1_2,key2_2,key3_2,key4_2,key5_2,nb,n)) == out4)
s.add(nb == 4)
s.add(n >= 0, n < 15)
'''key1=283
key2=3 ==> 3
key3=1 ==>27
key4=4 ==>30
key5=3 ==>27
key6=8 ==>31
key7=2 ==>23
key8=1 ==>14
key9=2 ==>3
key10=3==>3'''
s.add(key1_1>=0,key1_1<=15)
s.add(key1_2>=0,key1_2<=15)
s.add(key2_1>=0,key2_1<=15)
s.add(key2_2>=0,key2_2<=15)
s.add(key3_1>=0,key3_1<=15)
s.add(key3_2>=0,key3_2<=15)
s.add(key5_1>=0,key5_1<=3)
s.add(key5_2>=0,key5_2<=3)
s.add(key6_1>=0,key6_1<=27)
s.add(key6_2>=0,key6_2<=27)
s.add(key7_1>=0,key7_1<=30)
s.add(key7_2>=0,key7_2<=30)
s.add(key8_1>=0,key8_1<=27)
s.add(key8_2>=0,key8_2<=27)
s.add(key9_1>=0,key9_1<=30)
s.add(key9_2>=0,key9_2<=30)
s.add(key10_1>=0,key10_1<=23)
s.add(key10_2>=0,key10_2<=23)



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

