from z3 import *
import subprocess
import time


#for executing the oracle ang getting the correct inputs 
def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))
    
    
start_time = time.time()


#variable declaration 
in1,in2,in3,in4,in5,in6,in7,in8,in9,in10 = BitVecs('in1 in2 in3 in4 in5 in6 in7 in8 in9 in10',32)
o1_1,o2_1,o3_1 = BitVecs('o1_1 o2_1 o3_1',32)
o1_2,o2_2,o3_2 = BitVecs('o1_2 o2_2 o3_2',32)
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1',32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2',32)
k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1,k11_1,k12_1,k13_1,k14_1,k15_1,k16_1,k17_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1 k6_1 k7_1 k8_1 k9_1 k10_1 k11_1 k12_1 k13_1 k14_1 k15_1 k16_1 k17_1')
k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2,k11_2,k12_2,k13_2,k14_2,k15_2,k16_2,k17_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2 k6_2 k7_2 k8_2 k9_2 k10_2 k11_2 k12_2 k13_2 k14_2 k15_2 k16_2 k17_2')
kk1_1,kk2_1,kk3_1=Bools('kk1_1 kk2_1 kk3_1')
kk1_2,kk2_2,kk3_2=Bools('kk1_2 kk2_2 kk3_2')

tuple = Datatype('tuple')
tuple.declare('tuple',('1', BitVecSort(32)),('2', BitVecSort(32)),('3', BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple(o1_1,o2_1,o3_1)
out2 = tuple.tuple(o1_2,o2_2,o3_2)


#time-out and key threashold declaration
TO_init = 1600
TO_max = 12800
rem_key_max = 32


#function definition 
def findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,k1,k2,k3,k4,k5):
    mult1 = in1 * in2
    mult2 = in1 * (in3 + key1) #key1=3
    mult3 = in3 * in7
    mult4 = (in4+key2) * in5 #key2=5
    mult5 = in3 * in2
    mult6 = in2 * (in5 + key3) #key3=7
    mult7 = in3 * in6
    mult8 = (in4 + key4) * in7 #key4=11
    mult9 = in4 * in8
    mult10 = in6 * (in9 + key5) #key5=13
    mult11 = in6 * in8
    mult12 = (in7 + key6) * in9 #key6=17
    mult13 = in7 * in8
    mult14 = in9 * (in10 + key7) #key7=19

    add1 = If(k1,in1 * mult2,BitVecVal(0,32)) #k1=True
    add2 = in4 * mult4
    add3 = in5 * mult8
    add4 = If(k2,BitVecVal(0,32),mult10 * in4) #k2=False
    add5 = in10 * mult14


    add6 = mult1 + (add1 * key8) #key8=11
    out1 = If(k3,add6,BitVecVal(0,32)) #k3=True

    add7 = mult3 + add2
    add8 = mult5 + add7

    add10 = mult7 + (add3 * key9) #key9=2
    add9 = mult6 + add10

    shf1 = add9 << key10 #key10=3
    out2 = If(k4,BitVecVal(0,32),add8 + shf1) #k4=False

    add13 = mult9 + add4
    add11 = add13 + mult11

    add15 = mult13 + add5
    add14 = mult12 + add15

    shf2 = add14 >> key10
    out3 = If(k5,add11 + shf2,BitVecVal(0,32)) #k5=True
    o = tuple.tuple(out1,out2,out3)

    return o
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,k1_1,k2_1,k3_1,k4_1,k5_1) == out1)
# s.add(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,k1_2,k2_2,k3_2,k4_2,k5_2) == out2)
'''s.add(i1>=0,i1<=255)
s.add(i2>=0,i2<=255)
s.add(i3>=0,i3<=255)
s.add(i4>=0,i4<=255)
s.add(i6>=0,i6<=255)
s.add(G1>=0,G1<=255)
s.add(G2>=0,G2<=255)
s.add(GG1>=0,GG1<=255)
s.add(GG2>=0,GG2<=255)'''
s.add(key1_1>=0,key1_2>=0)
s.add(key2_1>=0,key2_2>=0)
s.add(key3_1>=0,key3_2>=0)
s.add(key4_1>=0,key4_2>=0)
s.add(key5_1>=0,key5_2>=0)
s.add(key6_1>=0,key6_2>=0)
s.add(key7_1>=0,key7_2>=0)
s.add(key8_1>=0,key8_2>=0)
s.add(key9_1>=0,key9_2>=0)
s.add(key10_1>=0,key10_2>=0)
set_option(html_mode=False)
print(s.units())

