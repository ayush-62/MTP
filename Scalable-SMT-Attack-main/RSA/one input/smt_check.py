from z3 import *
import subprocess
import time


#for executing the oracle ang getting the correct inputs 
def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))
    
    
start_time = time.time()


#variable declaration

i1 = BitVec('i1',32)
o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1 = BitVecs('o1_1 o2_1 o3_1 o4_1 o5_1 o6_1 o7_1 o8_1 o9_1 o10_1 o11_1 o12_1 o13_1 o14_1 o15_1 o16_1',32)
o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2 = BitVecs('o1_2 o2_2 o3_2 o4_2 o5_2 o6_2 o7_2 o8_2 o9_2 o10_2 o11_2 o12_2 o13_2 o14_2 o15_2 o16_2',32)

oo1_1,oo2_1,oo3_1,oo4_1,oo5_1 = BitVecs('oo1_1 oo2_1 oo3_1 oo4_1 oo5_1',32)
oo1_2,oo2_2,oo3_2,oo4_2,oo5_2 = BitVecs('oo1_2 oo2_2 oo3_2 oo4_2 oo5_2',32)


key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1',32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2',32)

tuple = Datatype('tuple')
tuple.declare('tuple1',('1', BitVecSort(32)),('2', BitVecSort(32)),('3', BitVecSort(32)),('4', BitVecSort(32)),('5', BitVecSort(32)),('6', BitVecSort(32)),('7', BitVecSort(32)),('8', BitVecSort(32)),('9', BitVecSort(32)),('10', BitVecSort(32)),('11', BitVecSort(32)),('12', BitVecSort(32)),('13', BitVecSort(32)),('14', BitVecSort(32)),('15', BitVecSort(32)),('16', BitVecSort(32)))
tuple.declare('tuple2',('1', BitVecSort(32)),('2', BitVecSort(32)),('3', BitVecSort(32)),('4', BitVecSort(32)),('5', BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple1(o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1,o16_1)
out2 = tuple.tuple1(o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2,o16_2)

out3 = tuple.tuple2(oo1_1,oo2_1,oo3_1,oo4_1,oo5_1)
out4 = tuple.tuple2(oo1_2,oo2_2,oo3_2,oo4_2,oo5_2)


#time-out and key threashold declaration
TO_init = 1600
TO_max = 12800
rem_key_max = 32

prime=[2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,191,193,197,199,211,223,227,229,233,239,241] 
#function definition 

#
def findOutput(i1,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10):
    S = Array('S', BitVecSort(32), BitVecSort(32))
    S = Store(S,BitVecVal(0,32),BitVecVal(97,32))
    S = Store(S,BitVecVal(1,32),i1)
    S = Store(S,BitVecVal(2,32),BitVecVal(99,32))
    S = Store(S,BitVecVal(3,32),BitVecVal(100,32))
    S = Store(S,BitVecVal(4,32),BitVecVal(101,32))
    S = Store(S,BitVecVal(5,32),BitVecVal(102,32))
    S = Store(S,BitVecVal(6,32),BitVecVal(103,32))
    S = Store(S,BitVecVal(7,32),BitVecVal(104,32))
    S = Store(S,BitVecVal(8,32),BitVecVal(105,32))
    S = Store(S,BitVecVal(9,32),BitVecVal(106,32))
    S = Store(S,BitVecVal(10,32),BitVecVal(107,32))
    S = Store(S,BitVecVal(11,32),BitVecVal(108,32))
    S = Store(S,BitVecVal(12,32),BitVecVal(109,32))
    S = Store(S,BitVecVal(13,32),BitVecVal(110,32))
    S = Store(S,BitVecVal(14,32),BitVecVal(111,32))
    S = Store(S,BitVecVal(15,32),BitVecVal(112,32))


    ptr=BitVecVal(15,32)
    prime1= BitVecVal(prime[15],32)
    ptr =ptr + 1
    prime2= BitVecVal(prime[16],32)
    n=BitVecVal(0,32)
    n=prime1 * prime2
    fi=BitVecVal(0,32)
    fi=(prime1-1) * (prime2-1)
    e=BitVecVal(0,32)
    e=e + (fi %13)
    public_key = e

    # enc=BitVecVal(1,32)
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n 
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    S = Store(S,BitVecVal(0,32),BitVecVal(1955,32))

    enc=BitVecVal(1,32)
    enc = enc * S[key1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n 
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    S = Store(S,BitVecVal(1,32),enc)

    enc=BitVecVal(1339,32)
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n 
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    enc = enc * S[key2]
    enc =enc % n
    S = Store(S,BitVecVal(2,32),enc)

    enc=BitVecVal(1110,32)
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n 
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    enc = enc * S[key3]
    enc =enc % n
    S = Store(S,BitVecVal(3,32),enc)

    enc=BitVecVal(352,32)
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n 
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    enc = enc * S[key4]
    enc =enc % n
    S = Store(S,BitVecVal(4,32),enc)

    enc=BitVecVal(1290,32)
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n 
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n
    # enc = enc * S[5]
    # enc =enc % n
    enc = enc * S[key5]
    enc =enc % n
    S = Store(S,BitVecVal(5,32),enc)

    enc=BitVecVal(3431,32)
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n 
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n
    # enc = enc * S[6]
    # enc =enc % n
    enc = enc * S[key6]
    enc =enc % n
    S = Store(S,BitVecVal(6,32),enc)

    enc=BitVecVal(757,32)
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n 
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n
    # enc = enc * S[7]
    # enc =enc % n
    enc = enc * S[key7]
    enc =enc % n
    S = Store(S,BitVecVal(7,32),enc)

    enc=BitVecVal(1913,32)
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n 
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n
    # enc = enc * S[8]
    # enc =enc % n
    enc = enc * S[key8]
    enc =enc % n
    S = Store(S,BitVecVal(8,32),enc)

    enc=BitVecVal(2558,32)
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n 
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n
    # enc = enc * S[9]
    # enc =enc % n
    enc = enc * S[key9]
    enc =enc % n
    S = Store(S,BitVecVal(9,32),enc)

    enc=BitVecVal(1733,32)
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n 
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n
    # enc = enc * S[10]
    # enc =enc % n
    enc = enc * S[key10]
    enc =enc % n
    S = Store(S,BitVecVal(10,32),enc)

    # enc=BitVecVal(1,32)
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n 
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    # enc = enc * S[11]
    # enc =enc % n
    S = Store(S,BitVecVal(11,32),BitVecVal(794,32))

    # enc=BitVecVal(1,32)
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n 
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    # enc = enc * S[12]
    # enc =enc % n
    S = Store(S,BitVecVal(12,32),BitVecVal(1890,32))

    # enc=BitVecVal(1,32)
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n 
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    # enc = enc * S[13]
    # enc =enc % n
    S = Store(S,BitVecVal(13,32),BitVecVal(723,32))

    # enc=BitVecVal(1,32)
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n 
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    # enc = enc * S[14]
    # enc =enc % n
    S = Store(S,BitVecVal(14,32),BitVecVal(1331,32))

    # enc=BitVecVal(1,32)
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n 
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    # enc = enc * S[15]
    # enc =enc % n
    S = Store(S,BitVecVal(15,32),BitVecVal(389,32))

    o0=S[0]
    o1=S[1]
    o2=S[2]
    o3=S[3]
    o4=S[4]
    o5=S[5]
    o6=S[6]
    o7=S[7]
    o8=S[8]
    o9=S[9]
    o10=S[10]
    o11=S[11]
    o12=S[12]
    o13=S[13]
    o14=S[14]
    o15=S[15]

    o = tuple.tuple1(o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15)

    return o

def sub(i1,key1,key2,key3,key4):

    S = Array('S', BitVecSort(32), BitVecSort(32))
    S = Store(S,BitVecVal(0,32),BitVecVal(97,32))
    S = Store(S,BitVecVal(1,32),i1)
    S = Store(S,BitVecVal(2,32),BitVecVal(99,32))
    S = Store(S,BitVecVal(3,32),BitVecVal(100,32))
    S = Store(S,BitVecVal(4,32),BitVecVal(101,32))
    S = Store(S,BitVecVal(5,32),BitVecVal(102,32))
    S = Store(S,BitVecVal(6,32),BitVecVal(103,32))
    S = Store(S,BitVecVal(7,32),BitVecVal(104,32))
    S = Store(S,BitVecVal(8,32),BitVecVal(105,32))
    S = Store(S,BitVecVal(9,32),BitVecVal(106,32))
    S = Store(S,BitVecVal(10,32),BitVecVal(107,32))
    S = Store(S,BitVecVal(11,32),BitVecVal(108,32))
    S = Store(S,BitVecVal(12,32),BitVecVal(109,32))
    S = Store(S,BitVecVal(13,32),BitVecVal(110,32))
    S = Store(S,BitVecVal(14,32),BitVecVal(111,32))
    S = Store(S,BitVecVal(15,32),BitVecVal(112,32))


    ptr=BitVecVal(15,32)
    prime1= BitVecVal(prime[15],32)
    ptr =ptr + 1
    prime2= BitVecVal(prime[16],32)
    n=BitVecVal(0,32)
    n=prime1 * prime2
    fi=BitVecVal(0,32)
    fi=(prime1-1) * (prime2-1)
    e=BitVecVal(0,32)
    e=e + (fi %13)
    public_key = e

    # enc=BitVecVal(1,32)
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n 
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    # enc = enc * S[0]
    # enc =enc % n
    S = Store(S,BitVecVal(0,32),BitVecVal(1955,32))

    enc=BitVecVal(1,32)
    enc = enc * S[key1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n 
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    enc = enc * S[1]
    enc =enc % n
    S = Store(S,BitVecVal(1,32),enc)

    enc=BitVecVal(1339,32)
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n 
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    # enc = enc * S[2]
    # enc =enc % n
    enc = enc * S[key2]
    enc =enc % n
    S = Store(S,BitVecVal(2,32),enc)

    enc=BitVecVal(1110,32)
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n 
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    # enc = enc * S[3]
    # enc =enc % n
    enc = enc * S[key3]
    enc =enc % n
    S = Store(S,BitVecVal(3,32),enc)

    enc=BitVecVal(352,32)
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n 
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    # enc = enc * S[4]
    # enc =enc % n
    enc = enc * S[key4]
    enc =enc % n
    S = Store(S,BitVecVal(4,32),enc)

    o0=S[0]
    o1=S[1]
    o2=S[2]
    o3=S[3]
    o4=S[4]
    return tuple.tuple2(o0,o1,o2,o3,o4)

'''gg = Tactic('smt').solver()
ia = str(97) #+ " " + str(98)+ " " + str(99)+ " " + str(100)+ " " + str(101)+ " " + str(102)+ " " + str(103)+ " " + str(104)+ " " + str(105)+ " " + str(106)+ " " + str(107)+ " " + str(108)+ " " + str(109)+ " " + str(110)+ " " + str(111)+ " " + str(112)
[oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
#,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))

print(gg.check(findOutput(97,1,2,3,4,5,6,7,8,9,10)==oa))'''

prune_key_set = False

j = 0


#SMT solver declaration 
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(sub(i1,key1_1,key2_1,key3_1,key4_1) == out3)
s.add(sub(i1,key1_2,key2_2,key3_2,key4_2) == out4)


Key_Set_Fetch_Count = 0
TO_increase_count = 0
s.add(i1>=1,i1<=127)
# s.add(i2>=1,i2<=127)
# s.add(i3>=1,i3<=127)
# s.add(i4>=1,i4<=127)
# s.add(i5>=1,i5<=127)
# s.add(i6>=1,i6<=127)
# s.add(i7>=1,i7<=127)
# s.add(i8>=1,i8<=127)
# s.add(i9>=1,i9<=127)
# s.add(i10>=1,i10<=127)
# s.add(i11>=1,i11<=127)
# s.add(i12>=1,i12<=127)
# s.add(i13>=1,i13<=127)
# s.add(i14>=1,i14<=127)
# s.add(i15>=1,i15<=127)
# s.add(i16>=1,i16<=127)

s.add(key1_1>=0,key1_1<=15)
s.add(key1_2>=0,key1_2<=15)
s.add(key2_2>=0,key2_2<=15)
s.add(key2_1>=0,key2_1<=15)
s.add(key3_2>=0,key3_2<=15)
s.add(key3_1>=0,key3_1<=15)
s.add(key4_2>=0,key4_2<=15)
s.add(key4_1>=0,key4_1<=15)
s.add(key5_2>=0,key5_2<=15)
s.add(key5_1>=0,key5_1<=15)
s.add(key6_2>=0,key6_2<=15)
s.add(key6_1>=0,key6_1<=15)
s.add(key7_2>=0,key7_2<=15)
s.add(key7_1>=0,key7_1<=15)
s.add(key8_2>=0,key8_2<=15)
s.add(key8_1>=0,key8_1<=15)
s.add(key9_2>=0,key9_2<=15)
s.add(key9_1>=0,key9_1<=15)
s.add(key10_2>=0,key10_2<=15)
s.add(key10_1>=0,key10_1<=15)




pos_set = set()
print("loop1 enter")
start=time.time()
while s.check(out3 != out4, Or(key1_1!=key1_2,key2_1!=key2_2,key3_1!=key3_2,key4_1!=key4_2,key5_1!=key5_2,key6_1!=key6_2,key7_1!=key7_2,key8_1!=key8_2,key9_1!=key9_2,key10_1!=key10_2)) == sat:
    added_new_constraints = True
    #Model to get DIP
    m = s.model()
    #print(m)
    print(str(m[i1]))#+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16]))
    print("The key is:")
    print(str(m[key1_1]) + " " + str(m[key2_1]) + " " + str(m[key3_1]) + " " + str(m[key4_1]) + " " + str(m[key5_1])+" "+str(m[key6_1]) + " " + str(m[key7_1]) + " " + str(m[key8_1]) + " " + str(m[key9_1]) + " " + str(m[key10_1]))
    print(str(m[key1_2]) + " " + str(m[key2_2]) + " " + str(m[key3_2]) + " " + str(m[key4_2]) + " " + str(m[key5_2])+" "+str(m[key6_2]) + " " + str(m[key7_2]) + " " + str(m[key8_2]) + " " + str(m[key9_2]) + " " + str(m[key10_2]))
    #creating the input with the DIP
    ia = str(m[i1])# + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4]) + " " + str(m[i5]) + " " + str(m[i6]) + " " + str(m[i7]) + " " + str(m[i8]) + " " + str(m[i9]) + " " + str(m[i10]) + " " + str(m[i11])+ " " + str(m[i12])+ " " + str(m[i13])+ " " + str(m[i14])+ " " + str(m[i15])+ " " + str(m[i16])
    #using the input to get the correct output for the DIP from the oracle 
    [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16] = Cexec(ia)
    oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
    #constraints added with the DIP
    s.add(findOutput(m[i1],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1) == oa)
    s.add(findOutput(m[i1],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2) == oa)
    print("Iteration %d = %f second" %(j+1,time.time()-start))
    j = j + 1
print("unsat takes %d time" %(time.time()-start))
print("loop1 complete")

p = 0


while s.check(key5_1 == key5_2,key6_1 == key6_2,key7_1 == key7_2,key4_1 == key4_2,key3_1 == key3_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    #adding the remaining possible keys 
    pos_set.add(m)
    print(str(m[key1_1]) + " " + str(m[key2_1]) + " " + str(m[key3_1]) + " " + str(m[key4_1]) + " " + str(m[key5_1])+" "+str(m[key6_1]) + " " + str(m[key7_1]) + " " + str(m[key8_1]) + " " + str(m[key9_1]) + " " + str(m[key10_1]))
    print("Iteration %d = %f second" %(p+1,time.time()-start))
    #If size crossed threshold exit
    if len(pos_set) > rem_key_max:
        break

    #adding constraints - K1 & K2 is not equal to current key fetched
    s.add(Or(key5_1 != m[key5_1],key6_1 != m[key6_1],key7_1 != m[key7_1],key4_1 != m[key4_1],key3_1 != m[key3_1]))
    s.add(Or(key5_2 != m[key5_2],key6_2 != m[key6_2],key7_2 != m[key7_2],key4_2 != m[key4_2],key3_2 != m[key3_2]))
    p = p + 1


print()
print("loop2 enter")


#creating remaining key set list
'''pos_l = list(pos_set)

#defining a new SMT solver
g = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
g.add(findOutput(key5_1,key6_1,key7_1,key4_1,key3_1,i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2) == out1)
g.add(findOutput(key5_2,key6_2,key7_2,key4_2,key3_2,i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2) == out2)

print("loop3 enter")

#Algorithm 3 - SMT on key set 
while len(pos_l) > 1:
    #Taking two keys from the key set
    m1 = pos_l[0]
    m2 = pos_l[1]
    #after the push the constaints added can be removed using pop()
    g.push()
    #adding constraints - K1 is equal to the first key taken from the list i.e. m1, and K2 is m2
    g.add(key5_1 == m1[key5_2],key6_1 == m1[key6_2],key7_1 == m1[key7_2],key4_1 == m1[key4_2],key3_1 == m1[key3_2])
    g.add(key5_2 == m2[key5_2],key6_2 == m2[key6_2],key7_2 == m2[key7_2],key4_2 == m2[key4_2],key3_2 == m2[key3_2])
    #checking for DIP
    if g.check(out1 != out2) == sat:
        #model to get the DIP.
        m = g.model()
        ia = str(m[i1]) + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4]) + " " + str(m[i6]) + " " + str(m[G1]) + " " + str(m[G2]) + " " + str(m[G3]) + " " + str(m[G4]) + " " + str(m[GG1]) + " " + str(m[GG2])
        [oa1,oa2,oa3,oa4] = Cexec(ia)
        oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
        #checking m1 is correct key or not is correct or not
        if g.check(findOutput(m1[key5_2],m1[key6_2],m1[key7_2],m1[key4_2],m1[key3_2],m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[G3],m[G4],m[GG1],m[GG2]) == oa) == unsat:
            pos_l.remove(m1)
        #checking m2 is correct key or not
        if g.check(findOutput(m2[key5_2],m2[key6_2],m2[key7_2],m2[key4_2],m2[key3_2],m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[G3],m[G4],m[GG1],m[GG2]) == oa) == unsat:
            pos_l.remove(m2)
    #no DIP found - keys are from same equivalence class
    else:
        pos_l.remove(m1)
    #here the constaints added are removed - as the next two keys will be taken from the remaining key set
    g.pop()

print("The final key is:")
m = pos_l[0]
print("key5 = " + str(m[key5_1]) + "\n" + "key6 = " + str(m[key6_1]) + "\n" + "key7 = " + str(m[key7_1]) + "\n" + "key4 = " + str(m[key4_1]) + "\n" + "key3 = " + str(m[key3_1]))
print()


end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (j, taken))  
print("Number of times Time-Out increased: %d." % (TO_increase_count))
print("Number of times remaining key set computed: %d." % (Key_Set_Fetch_Count))  '''
