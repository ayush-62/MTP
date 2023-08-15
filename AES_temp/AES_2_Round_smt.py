from z3 import*
import subprocess

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))




def create_array(arr, data):
    for i in range(len(data)):
        a = Select(arr, i)
        for j in range(len(data[i])):
            a = Store(a, j, data[i][j])
        arr = Store(arr, i, a) 
    return arr

def store(arr,data):
    for i in range(16):
        arr = Store(arr,i,data[i])
    return arr


inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16 = BitVecs('inp1 inp2 inp3 inp4 inp5 inp6 inp7 inp8 inp9 inp10 inp11 inp12 inp1 inp14 inp15 inp16' , 32)
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1= BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1', 32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2= BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2', 32)

o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1 = BitVecs('o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1 o16_1', 32)
o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2 = BitVecs('o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2 o16_2', 32)


tuple = Datatype('tuple')
tuple.declare('tuple', ('1', BitVecSort(32)),('2', BitVecSort(32)),('3', BitVecSort(32)),('4', BitVecSort(32)),
                       ('5', BitVecSort(32)),('6', BitVecSort(32)),('7', BitVecSort(32)),('8', BitVecSort(32)),
                       ('9', BitVecSort(32)),('10', BitVecSort(32)),('11', BitVecSort(32)),('12', BitVecSort(32)),
                       ('13', BitVecSort(32)),('14', BitVecSort(32)),('15', BitVecSort(32)),('16', BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple(o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1)
out2 = tuple.tuple(o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2)


statemt = Array('statemt', BitVecSort(32), BitVecSort(32))
# out1 = Array('out1', BitVecSort(32), BitVecSort(32))
# out2 = Array('out2', BitVecSort(32), BitVecSort(32))

word = Array('word',  BitVecSort(32), ArraySort( BitVecSort(32),  BitVecSort(32)))

worddata = [[43,40,171,9,160,136,35,42,242,122,89,115,61,71,30,109,239,168,182,219,212,124,202,17,109,17,219,202,78,95,132,78,234,181,49,127,172,25,40,87,208,201,225,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
           ,[126,174,247,207,250,84,163,108,194,150,53,89,128,22,35,122,68,82,113,11,209,131,242,249,136,11,249,0,84,95,166,166,210,141,43,141,119,250,209,92,20,238,63,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
           ,[21,210,21,79,254,44,57,118,149,185,128,246,71,254,126,136,165,91,37,173,198,157,184,21,163,62,134,147,247,201,79,220,115,186,245,41,102,220,41,0,249,37,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
           ,[22,166,136,60,23,177,57,5,242,67,122,127,125,62,68,59,65,127,59,0,248,135,188,188,122,253,65,253,14,243,178,79,33,210,96,47,243,33,65,110,168,137,200,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
word = create_array(word , worddata)

Sbox = Array('Sbox',  BitVecSort(32), ArraySort( BitVecSort(32),  BitVecSort(32)))
Sboxdata = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
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
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]
Sbox = create_array(Sbox , Sboxdata)
ret = [0]*16


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


def ByteSub_ShiftRow(statemt , Sbox , word , key1 , key2 , key3 , key4 , key5 , key6):
    if (key6 == 3):
        temp = Sbox[statemt[1] >> 4][statemt[1] & 0xf]
    else :
        temp = Sbox[statemt[1] << 4][statemt[1] & 0xf]
    
    print(key6)

    # print((simplify(Or((((simplify(Select(statemt,key1)))>>4) >= 16) , ((simplify(Select(statemt,key1))& 0xf) >= 16)))))
    
    statemt =  If((simplify(Or((((simplify(Select(statemt,key1)))>>4) >= 16) , ((simplify(Select(statemt,key1))& 0xf) >= 16)))),
    Store(statemt , 1 , 0) ,Store(statemt , 1 , Sbox[statemt[key1] >> 4][statemt[key1] & 0xf]))

    statemt = Store(statemt , key1 , Sbox[statemt[9] >> 4][statemt[9] & 0xf])
    statemt = Store(statemt , 9 , Sbox[statemt[13] >> 4][statemt[13] & 0xf])
    statemt = Store(statemt , 13 , temp)

    temp =  If((simplify(Or((((simplify(Select(statemt,key2)))>>4) >= 16) , ((simplify(Select(statemt,key2))& 0xf) >= 16)))),
    0,Sbox[statemt[key2] >> 4][statemt[key2] & 0xf])

    statemt = Store(statemt , key2 , Sbox[statemt[10] >> 4][statemt[10] & 0xf])
    statemt = Store(statemt , 10 , temp)
    temp = Sbox[statemt[6] >> 4][statemt[6] & 0xf]
    statemt = Store(statemt , 6 , Sbox[statemt[14] >> 4][statemt[14] & 0xf])
    statemt = Store(statemt , 14 , temp)

    temp = If(simplify(Or((((simplify(Select(statemt,key3)))>>4) >= 16) , ((simplify(Select(statemt,key3))& 0xf) >= 16))),
    0,Sbox[statemt[key3] >> 4][statemt[key3] & 0xf])
    statemt = Store(statemt , key3 , Sbox[statemt[15] >> 4][statemt[15] & 0xf])
    statemt = Store(statemt , 15 , Sbox[statemt[11] >> 4][statemt[11] & 0xf])
    statemt = Store(statemt , 11 , Sbox[statemt[7] >> 4][statemt[7] & 0xf])
    statemt = Store(statemt , 7 , temp)

    statemt = Store(statemt , 0 , Sbox[statemt[0] >> 4][statemt[0] & 0xf])
    statemt = Store(statemt , 4 , Sbox[statemt[4] >> 4][statemt[4] & 0xf])
    
    statemt =  If(simplify(Or((((simplify(Select(statemt,key4)))>>4) >= 16) , ((simplify(Select(statemt,key4))& 0xf) >= 16))),
    Store(statemt , key4 , 0) , Store(statemt , key4 , Sbox[statemt[key4] >> 4][statemt[key4] & 0xf]))
    
    statemt = If(simplify(Or((((simplify(Select(statemt,key5)))>>4) >= 16) , ((simplify(Select(statemt,key5))& 0xf) >= 16))),
    Store(statemt , key5 , 0) , Store(statemt , key5 , Sbox[statemt[key5] >> 4][statemt[key5] & 0xf]))

    return statemt

def MixColumn_AddRoundKey(statemt , Sbox , word, nb, n ,ret):
    for j in range(nb):
        ret[j * 4] = (statemt[j * 4] << 1)
        if (simplify(ret[j * 4] >> 8) == 1):
            ret[j * 4] ^= 283

        x = statemt[1 + j * 4]
        x ^= (x << 1)
        if (simplify(x >> 8) == 1):
            ret[j * 4] ^= (x ^ 283)
        else:
            ret[j * 4] ^= x

        ret[j * 4] ^= statemt[2 + j * 4] ^ statemt[3 + j * 4] ^ word[0][j + nb * n]

        ret[1 + j * 4] = (statemt[1 + j * 4] << 1)
        if (simplify(ret[1 + j * 4] >> 8) == 1):
            ret[1 + j * 4] ^= 283

        x = statemt[2 + j * 4]
        x ^= (x << 1)
        if (simplify(x >> 8) == 1):
            ret[1 + j * 4] ^= (x ^ 283)
        else:
            ret[1 + j * 4] ^= x

        ret[1 + j * 4] ^= statemt[3 + j * 4] ^ statemt[j * 4] ^ word[1][j + nb * n]

        ret[2 + j * 4] = (statemt[2 + j * 4] << 1)
        if (simplify(ret[2 + j * 4] >> 8) == 1):
            ret[2 + j * 4] ^= 283

        x = statemt[3 + j * 4]
        x ^= (x << 1)
        if (simplify(x >> 8) == 1):
            ret[2 + j * 4] ^= (x ^ 283)
        else:
            ret[2 + j * 4] ^= x

        ret[2 + j * 4] ^= statemt[j * 4] ^ statemt[1 + j * 4] ^ word[2][j + nb * n]

        ret[3 + j * 4] = (statemt[3 + j * 4] << 1)
        if (simplify(ret[3 + j * 4] >> 8) == 1):
            ret[3 + j * 4] ^= 283

        x = statemt[j * 4]
        x ^= (x << 1)
        if (simplify(x >> 8) == 1):
            ret[3 + j * 4] ^= (x ^ 283)
        else:
            ret[3 + j * 4] ^= x

        ret[3 + j * 4] ^= statemt[1 + j * 4] ^ statemt[2 + j * 4] ^ word[3][j + nb * n]

    for j in range(nb):
        statemt = Store(statemt , j * 4 ,ret[j * 4])
        statemt = Store(statemt , 1 + j * 4 ,ret[1 + j * 4] )
        statemt = Store(statemt , 2 + j * 4 , ret[2 + j * 4])
        statemt = Store(statemt , 3 + j * 4 , ret[3 + j * 4])

    return [statemt, ret]



def AES_2_Round(statemt , Sbox , word , ret ,in1 , in2 , in3 , in4 , in5 , in6 , in7 , in8 , in9 , in10 , in11 , in12 , in13 , in14 , in15 , in16 , key1 , key2 , key3 , key4 , key5 , key6):
    
    statemt =  Store(statemt , 0 , in1)
    statemt =  Store(statemt , 1 , in2)
    statemt =  Store(statemt , 2 , in3)
    statemt =  Store(statemt , 3 , in4)
    statemt =  Store(statemt , 4 , in5)
    statemt =  Store(statemt , 5 , in6)
    statemt =  Store(statemt , 6 , in7)
    statemt =  Store(statemt , 7 , in8)
    statemt =  Store(statemt , 8 , in9)
    statemt =  Store(statemt , 9 , in10)
    statemt = Store(statemt , 10 , in11)
    statemt = Store(statemt , 11 , in12)
    statemt = Store(statemt , 12 , in13)
    statemt = Store(statemt , 13 , in14)
    statemt = Store(statemt , 14 , in15)
    statemt = Store(statemt , 15 , in16)
    

    statemt = AddRoundKey(statemt , Sbox , word , 0)
    for i in range(2):
        statemt =  ByteSub_ShiftRow(statemt , Sbox , word , key1 , key2 , key3 , key4 , key5 , key6)
        rv =  MixColumn_AddRoundKey(statemt , Sbox , word, 4, i+1 ,ret)
        statemt = rv[0]
        ret = rv[1]    
    statemt =  ByteSub_ShiftRow(statemt , Sbox , word, key1 , key2 , key3 ,key4 , key5 , key6)
    statemt =  AddRoundKey(statemt , Sbox , word , 10)
    o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16 = BitVecs('o1 o2 o3 o4 o5 o6 o7 o8 o9 o10 o11 o12 o13 o14 o15 o16', 32)
    o1 = simplify(Select(statemt,0))
    o2 = simplify(Select(statemt,1))
    o3 = simplify(Select(statemt,2))
    o4 = simplify(Select(statemt,3))
    o5 = simplify(Select(statemt,4))
    o6 = simplify(Select(statemt,5))
    o7 = simplify(Select(statemt,6))
    o8 = simplify(Select(statemt,7))
    o9 = simplify(Select(statemt,8))
    o10 = simplify(Select(statemt,9))
    o11 = simplify(Select(statemt,10))
    o12 = simplify(Select(statemt,11))
    o13 = simplify(Select(statemt,12))
    o14 = simplify(Select(statemt,13))
    o15 = simplify(Select(statemt,14))
    o16 = simplify(Select(statemt,15))
    out = tuple.tuple(o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16)
    return statemt


s = Tactic('smt').solver()

#====================================    Array value checking    ========================================
# code to check whether values are stores in array or not.
# print(Sbox[0][0].val())
# for i in range(16):
#     for j in range(16):
#         s.add(Sbox[i][j] == Sboxdata[i][j])

# for i in range(4):
#     for j in range(120):
#         s.add(word[i][j] == worddata[i][j])
        

# # print(s.model()[statemt])
# if s.check() == sat:
#     print("aray values are Correct")
#     # print(s.model())
# else :
#     print('aray values are NOT Correct')
# # exit()
#========================================================================================================


# ----------------------------------function output checking---------------------------------------------------------
# out = tuple.tuple(179,171,119,252,157,106,218,47,169,156,193,205,199,66,131,149)
# s.add(key1_1 == 5)
# s.add(key1_2 == 5)
# s.add(key2_1 == 3)
# s.add(key2_2 == 3)
# s.add(key3_1 == 283)
# s.add(key3_2 == 283)
out = AES_2_Round(statemt , Sbox , word , ret ,33,106,49,58,17,168,148,174,201,253,123,132,4,193,64,44,5,2,3,8,12,8)
# s.add(simplify(AES_2_Round(statemt , Sbox , word ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,5,3,283) == out))
# print(s.check())

# print(simplify(statemt[0]))
# for i in range(16):
#     for j in range(16):
#         print(simplify(Sbox[i][j]))
for i in range(16):
    print(simplify(Select(out,i)))
exit()
# -------------------------------------------------------------------------------------------------------------------


s.add(key1_1 >= 0 , key1_1 <= 15)
s.add(key1_2 >= 0 , key1_2 <= 15)
s.add(key2_1 >= 0 , key2_1 <= 15)
s.add(key2_2 >= 0 , key2_2 <= 15)
s.add(key3_1 >= 0 , key3_1 <= 15)
s.add(key3_2 >= 0 , key3_2 <= 15)

s.add(inp1 < 500)
s.add(inp2 < 500)
s.add(inp3 < 500)
s.add(inp4 < 500)
s.add(inp5 < 500)
s.add(inp6 < 500)
s.add(inp7 < 500)
s.add(inp8 < 500)
s.add(inp9 < 500)
s.add(inp10 < 500)
s.add(inp11 < 500)
s.add(inp12 < 500)
s.add(inp13 < 500)
s.add(inp14 < 500)
s.add(inp15 < 500)
s.add(inp16 < 500)

s.add(simplify(AES_2_Round(statemt , Sbox , word , ret ,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16,key1_1,key2_1,key3_1 , key4_1 , key5_1 , key6_1) == out1))
s.add(simplify(AES_2_Round(statemt , Sbox , word , ret ,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16,key1_2,key2_2,key3_1 , key4_1 , key5_1 , key6_1) == out2))
# s.add(inp1 == 1)
# s.add(inp2 == 2)
# s.add(inp3 == 3)
# s.add(inp4 == 4)
# s.add(inp5 == 5)
# s.add(inp6 == 6)
# s.add(inp7 == 7)
# s.add(inp8 == 8)
# s.add(inp9 == 9)
# s.add(inp10 == 10)
# s.add(inp11 == 11)
# s.add(inp12 == 12)
# s.add(inp13 == 13)
# s.add(inp14 == 14)
# s.add(inp15 == 15)
# s.add(inp16 == 16)
print(s.check(out1 != out2))
# while s.check(out1 != out2) != unsat:
#     m = s.model()
#     ia = str(m[inp1]) + " " + str(m[inp2]) + " " + str(m[inp3]) + " " + str(m[inp4]) + " " + str(m[inp5]) + " " + str(m[inp6]) + " " + str(m[inp7]) + " " + str(m[inp8]) + " " +str(m[inp9]) + " " +str(m[inp10])+ " " +str(m[inp11])+ " " +str(m[inp12])+ " " +str(m[inp13])+ " " +str(m[inp14])+ " " +str(m[inp15])+ " " +str(m[inp16])
#     print("DIP : ",ia)
#     print("Key pair 1 : " , m[key1_1] , m[key2_1] , m[key3_1])
#     print("Key pair 2 : " , m[key1_2] , m[key2_2] , m[key3_2])
    
#     # print(s.check(out1 != out2))
#     #print(m)
#     out= Cexec(ia)
#     # print(out)
#     out_data = tuple.tuple(out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7],out[8],out[9],out[10],out[11],out[12],out[13],out[14],out[15])
#     s.add(AES_2_Round(statemt , Sbox , word,m[inp1],m[inp2],m[inp3],m[inp4],m[inp5],m[inp6],m[inp7],m[inp8],m[inp9],m[inp10],m[inp11],m[inp12],m[inp13],m[inp14],m[inp15],m[inp16],key1_1,key2_1,key3_1) == out_data)
#     s.add(AES_2_Round(statemt , Sbox , word,m[inp1],m[inp2],m[inp3],m[inp4],m[inp5],m[inp6],m[inp7],m[inp8],m[inp9],m[inp10],m[inp11],m[inp12],m[inp13],m[inp14],m[inp15],m[inp16],key1_2,key2_2,key3_2) == out_data)

# print(s.check(out1 == out2))
# print(s.model())

