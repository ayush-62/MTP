from z3 import *
from prettytable import PrettyTable
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


prune_key_set = False

j = 0
gg=Tactic('smt').solver()
ia = str(1) + " " + str(2) + " " + str(3) + " " + str(4) +" "+ str(5)+ " " + str(6) + " " + str(7) + " " + str(8) + " " + str(9)+" "+str(10)
#using the input to get the correct output for the DIP from the oracle 
[oa1,oa2,oa3] = Cexec(ia)
oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32))
print(gg.check(findOutput(1,2,3,4,5,6,7,8,9,10,3,5,7,11,13,17,19,11,2,3,True,False,True,False,True)==oa))


#SMT solver declaration 
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(simplify(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,k1_1,k2_1,k3_1,k4_1,k5_1) == out1))
s.add(simplify(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,k1_2,k2_2,k3_2,k4_2,k5_2) == out2))

s.add(in1 == 2)
s.add(in2 == 4)
# s.add(in3 == 6)
s.add(in4 == 7)
s.add(in5 == 1)
s.add(in6 == 9)
s.add(in7 == 5)
s.add(in8 == 10)
s.add(in9 == 11)
s.add(in10 == 5)

# s.add(in1>=0,in1<255)
# s.add(in2>=0,in2<255)
s.add(in3>=0,in3<255)
# s.add(in4>=0,in4<255)
# s.add(in5>=0,in5<255)
# s.add(in6>=0,in6<255)
# s.add(in7>=0,in7<255)
# s.add(in8>=0,in8<255)
# s.add(in9>=0,in9<255)
# s.add(in10>=0,in10<255)

s.add(key1_1<255,key1_2<255)
s.add(key2_1<255,key2_2<255)
s.add(key3_1<255,key3_2<255)
s.add(key4_1<255,key4_2<255)
s.add(key5_1<255,key5_2<255)
s.add(key6_1<255,key6_2<255)
s.add(key7_1<255,key7_2<255)
s.add(key8_1<255,key8_2<255)
s.add(key9_1<255,key9_2<255)
s.add(key10_1<255,key10_2<255)

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

#learn clause after i1 as variable
# s.add( 7*key2_2 == 2163 +(4294967238 + 4294967292*key3_2 + 4294967295*key9_2*(35 + 5*key4_2) << key10_2))
# s.add( 7*key2_1 == 2163 +(4294967238 + 4294967292*key3_1 + 4294967295*key9_1*(35 + 5*key4_1) << key10_1))

t = PrettyTable(['key1','key2','key3','key4','key5','key6','key7','key8','key9','key10'])

pos_set = set()
print("loop1 enter")
while s.check(out1 != out2, Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1 != key4_2,key5_1 != key5_2,key6_1 != key6_2,key7_1 != key7_2,key8_1 != key8_2,key9_1 != key9_2,key10_1!=key10_2,k1_1!=k1_2,k2_1!=k2_2,k3_1!=k3_2,k4_1!=k4_2,k5_1!=k5_2)) == sat:
    added_new_constraints = True
    #Model to get DIP
    m = s.model()
    #print(m)
    print()
    print("-----------------------------------------DIP----------------------------------------------")
    print(str(m[in1])+" "+str(m[in2])+" "+str(m[in3])+" "+str(m[in4])+" "+str(m[in5])+" "+str(m[in6])+" "+str(m[in7])+" "+str(m[in8])+" "+str(m[in9])+" "+str(m[in10]))
    print(s.non_units())
    # print("The key is:")
    # print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1]))
    # print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2])+" "+str(m[k1_2])+" "+str(m[k2_2])+" "+str(m[k3_2])+" "+str(m[k4_2])+" "+str(m[k5_2]))
    #creating the input with the DIP
    ia = str(m[in1])+" "+str(m[in2])+" "+str(m[in3])+" "+str(m[in4])+" "+str(m[in5])+" "+str(m[in6])+" "+str(m[in7])+" "+str(m[in8])+" "+str(m[in9])+" "+str(m[in10])
    #using the input to get the correct output for the DIP from the oracle 
    [oa1,oa2,oa3] = Cexec(ia)
    oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32))
    #constraints added with the DIP
    s.add(simplify(findOutput(m[in1],m[in2],m[in3],m[in4],m[in5],m[in6],m[in7],m[in8],m[in9],m[in10],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,k1_1,k2_1,k3_1,k4_1,k5_1) == oa))
    s.add(simplify(findOutput(m[in1],m[in2],m[in3],m[in4],m[in5],m[in6],m[in7],m[in8],m[in9],m[in10],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,k1_2,k2_2,k3_2,k4_2,k5_2) == oa))
    j = j + 1

p = 0
# print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1]))
# print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2])+" "+str(m[k1_2])+" "+str(m[k2_2])+" "+str(m[k3_2])+" "+str(m[k4_2])+" "+str(m[k5_2]))
print("checking remaining keys")
while s.check((key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1 == key4_2,key5_1 == key5_2,key6_1 == key6_2,key7_1 == key7_2,key8_1 == key8_2,key9_1 == key9_2,key10_1==key10_2,k1_1==k1_2,k2_1==k2_2,k3_1==k3_2,k4_1==k4_2,k5_1==k5_2) != unsat):
    try:
        m = s.model()
    except:
        break_away = True
        break
    #adding the remaining possible keys 
    pos_set.add(m)
    t.add_row([str(m[key1_1].as_signed_long()),str(m[key2_1].as_signed_long()),str(m[key3_1].as_signed_long()),str(m[key4_1].as_signed_long()),str(m[key5_1].as_signed_long()),str(m[key6_1]),str(m[key7_1]),str(m[key8_1]),str(m[key9_1]),str(m[key10_1])])
    #If size crossed threshold exit
    if len(pos_set) > rem_key_max:
        break

    #adding constraints - K1 & K2 is not equal to current key fetched
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1],key5_1!=m[key5_1],key6_1!=m[key6_1],key7_1!=m[key7_1],key8_1!=m[key8_1],key9_1!=m[key9_1],key10_1!=m[key10_1],k1_1!=m[k1_1],k2_1!=m[k2_1],k3_1!=m[k3_1],k4_1!=m[k4_1],k5_1!=m[k5_1]))
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2],key5_2!=m[key5_2],key6_2!=m[key6_2],key7_2!=m[key7_2],key8_2!=m[key8_2],key9_2!=m[key9_2],key10_2!=m[key10_2],k1_2!=m[k1_2],k2_2!=m[k2_2],k3_2!=m[k3_2],k4_2!=m[k4_2],k5_2!=m[k5_2]))
    p = p + 1


print()
print(t)
print("loop2 enter")


#creating remaining key set list
pos_l = list(pos_set)

#defining a new SMT solver
g = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
g.add(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,k1_1,k2_1,k3_1,k4_1,k5_1) == out1)
g.add(findOutput(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,k1_2,k2_2,k3_2,k4_2,k5_2) == out2)

# print("loop3 enter")

# #Algorithm 3 - SMT on key set 
# while len(pos_l) > 1:
#     #Taking two keys from the key set
#     m1 = pos_l[0]
#     m2 = pos_l[1]
#     #after the push the constaints added can be removed using pop()
#     g.push()
#     #adding constraints - K1 is equal to the first key taken from the list i.e. m1, and K2 is m2
#     g.add(key1_1 == m1[key1_1],key2_1==m1[key2_1],key3_1==m1[key3_1],key4_1==m1[key4_1],key5_1==m1[key5_1],key6_1==m1[key6_1],key7_1==m1[key7_1],key8_1==m1[key8_1],key9_1==m1[key9_1])
#     g.add(key1_2 == m2[key1_2],key2_2==m2[key2_2],key3_2==m2[key3_2],key4_2==m2[key4_2],key5_2==m2[key5_2],key6_2==m2[key6_2],key7_2==m2[key7_2],key8_2==m2[key8_2],key9_2==m2[key9_2])

#     #checking for DIP
#     if g.check(out1 != out2) == sat:
#         #model to get the DIP.
#         m = g.model()
#         ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(m[in4])+ " " + str(m[in6]) + " " + str(m[in7]) + " " + str(m[in8]) + " " + str(m[in9]) + " " + str(m[in10])
#         [oa1,oa2,oa3,oa4] = Cexec(ia)
#         oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
#         #checking m1 is correct key or not is correct or not
#         if g.check(findOutput(m[in1],m[in2],m[in3],m[in4],m[in5],m[in6],m[in7],m[in8],m[in9],m[in10],m1[key1_2],m1[key2_2],m1[key3_2],m1[key4_2],m1[key5_2],m1[key6_2],m1[key7_2],m1[key8_2],m1[key9_2]) == oa) == unsat:
#             pos_l.remove(m1)
#         #checking m2 is correct key or not
#         if g.check(findOutput(m[in1],m[in2],m[in3],m[in4],m[in5],m[in6],m[in7],m[in8],m[in9],m[in10],m2[key1_2],m2[key2_2],m2[key3_2],m2[key4_2],m2[key5_2],m2[key6_2],m2[key7_2],m2[key8_2],m2[key9_2]) == oa) == unsat:
#             pos_l.remove(m2)
#     #no DIP found - keys are from same equivalence class
#     else:
#         pos_l.remove(m1)
#     #here the constaints added are removed - as the next two keys will be taken from the remaining key set
#     g.pop()

# print("The final key is:")
# m = pos_l[0]
# print("key1 = " + str(m[key1_1]) + "\n" + "key2 = " + str(m[key2_1]) + "\n" + "key3 = " + str(m[key3_1]) + "\n" + "key4 = " + str(m[key4_1]) + "\n" + "key5 = " + str(m[key5_1])+ "\n" + "key6 = " + str(m[key6_1])+ "\n" + "key7 = " + str(m[key7_1])+ "\n" + "key8 = " + str(m[key8_1])+ "\n" + "key9 = " + str(m[key9_1]))
# print()


end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (j, taken))   
