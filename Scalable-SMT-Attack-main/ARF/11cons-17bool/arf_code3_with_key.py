from z3 import *
import subprocess
import time


#for executing the oracle ang getting the correct inputs 
def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))
    
    
start_time = time.time()


#variable declaration 
i1,i2,i3,i4,i5,i6,G1,G2,G3,G4,GG1,GG2 = BitVecs('i1 i2 i3 i4 i6 i5 G1 G2 G3 G4 GG1 GG2',32)
o1_1,o2_1,o3_1,o4_1 = BitVecs('o1_1 o2_1 o3_1 o4_1',32)
o1_2,o2_2,o3_2,o4_2 = BitVecs('o1_2 o2_2 o3_2 o4_2',32)
key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,key11_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1 key11_1',32)
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,key11_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2 key11_2',32)
k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1,k11_1,k12_1,k13_1,k14_1,k15_1,k16_1,k17_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1 k6_1 k7_1 k8_1 k9_1 k10_1 k11_1 k12_1 k13_1 k14_1 k15_1 k16_1 k17_1')
k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2,k11_2,k12_2,k13_2,k14_2,k15_2,k16_2,k17_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2 k6_2 k7_2 k8_2 k9_2 k10_2 k11_2 k12_2 k13_2 k14_2 k15_2 k16_2 k17_2')
kk1_1,kk2_1,kk3_1=Bools('kk1_1 kk2_1 kk3_1')
kk1_2,kk2_2,kk3_2=Bools('kk1_2 kk2_2 kk3_2')

tuple = Datatype('tuple')
tuple.declare('tuple',('1', BitVecSort(32)),('2', BitVecSort(32)),('3', BitVecSort(32)),('4', BitVecSort(32)))
tuple = tuple.create()
out1 = tuple.tuple(o1_1,o2_1,o3_1,o4_1)
out2 = tuple.tuple(o1_2,o2_2,o3_2,o4_2)


#time-out and key threashold declaration
TO_init = 1600
TO_max = 12800
rem_key_max = 32


#function definition 
def findOutput(GG1,key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17):

    op1 = GG1 * (BitVecVal(1,32) + key1) #key1=23
    op2 = If(k1,BitVecVal(19,32) * BitVecVal(2,32),BitVecVal(0,32)) # k1=True
    op3 = BitVecVal(11,32) * BitVecVal(2,32)
    op4 = If(k2,BitVecVal(0,32),BitVecVal(13,32) * BitVecVal(1,32)) #k2=False
    op5 = If(Not(Xor(BitVecVal(11,32)>10,k3)), BitVecVal(11,32) * BitVecVal(3,32), BitVecVal(0,32)) # k3=True
    op5 = If(Not(Xor(BitVecVal(11,32)>10,k3)), op5 + (GG1 * key2), op5) #key2=11
    op6 = If(Not(Xor(BitVecVal(11,32)>10,k3)), op5 - op4, BitVecVal(0,32))
    op5 = If(Not(Xor(BitVecVal(11,32)>10,k3)), op5, BitVecVal(3,32) * BitVecVal(5,32))
    op6 = If(Not(Xor(BitVecVal(11,32)>10,k3)), op6, op5 - (op3 * key3)) #key3=7
    op6 = If(Xor(op5<op4,k4), BitVecVal(13,32) * BitVecVal(5,32), op6) #k4=False
    op6 = If(Xor(op5<op4,k4), op6 - (BitVecVal(3,32) *key4), op6) #key4=17
    op17 = If(Xor(op5<op4,k4), op6 - BitVecVal(13,32), BitVecVal(0,32))
    op17 = If(Xor(op5<op4,k4), op17, op2 - op4)
    op2 = If(Xor(op5<op4,k4), op2, op4 - (op17 * key5)) #key5=13
    op17 = If(Xor(op5<op4,k4), op17, op17 - op2)
    op7 = If(k5,BitVecVal(11,32) * BitVecVal(5,32),BitVecVal(0,32)) #k5=True
    op8 = BitVecVal(13,32) * (BitVecVal(3,32) + key6) #key6=8
    op9 = If(k6,BitVecVal(0,32),op1 + op2) #k6=False
    op10 = op3 + (op4 * key7) #key7=31
    op11 = If(k7,op4 + op6,BitVecVal(0,32)) #k7=True
    op12 = op7 + op8
    op13 = op11 + BitVecVal(11,32)
    o1 = If(k8,BitVecVal(0,32),op13) #k8=False
    op14 = If(k9,BitVecVal(7,32) + op12,BitVecVal(0,32)) #k9=True
    o2 = If(k10,BitVecVal(0,32),op14) #k10=False
    op15 = (BitVecVal(11,32)+key8) * op14 #key8=14
    op16 = If(k11,op13 * BitVecVal(13,32),BitVecVal(0,32)) #k11=True
    op17 = If(Xor(op13==op14,k12), op17 * op11, op17) #k12=False
    op14 = If(Xor(op13==op14,k12), op14 - op17, op14)
    op15 = If(Xor(op13==op14,k12), op15 + op17, op15)
    op14 = If(Xor(op13==op14,k12), op14, op13 * BitVecVal(11,32))
    op18 = If(k13,op14 * BitVecVal(13,32),BitVecVal(0,32)) #k13=True
    op19 = op15 * (op16 + key9) #key9=13
    op20 = op17 + op18
    op21 = If(k14,BitVecVal(0,32),BitVecVal(11,32) * op20) #k14=False
    op22 = (op19+key10) * BitVecVal(13,32) #key10=5
    op23 = op19 * BitVecVal(11,32)
    op24 = op20 * (BitVecVal(13,32) + key11) #key11=12
    op25 = If(k15,op21 + op22,BitVecVal(0,32)) #k15=True
    op26 = op23 + op24 
    op27 = op9 + op25
    o3 = If(k16,BitVecVal(0,32),op27) #k16=False
    op28 = op10 + op26
    o4 = If(k17,op28,BitVecVal(0,32)) #k17=True
    o = tuple.tuple(o1,o2,o3,o4)

    return o


prune_key_set = False

j = 0
gg=Tactic('smt').solver()
ia = str(1) + " " + str(2) + " " + str(3) + " " + str(5) +" "+ str(7)+ " " + str(11) + " " + str(13) + " " + str(17) + " " + str(19)
#using the input to get the correct output for the DIP from the oracle 
[oa1,oa2,oa3,oa4] = Cexec(ia)
oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
print(gg.check(findOutput(17,23,11,7,17,13,8,31,14,13,5,12,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True)==oa))


#SMT solver declaration 
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(findOutput(GG1,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,key11_1,k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1,k11_1,k12_1,k13_1,k14_1,k15_1,k16_1,k17_1) == out1)
s.add(findOutput(GG1,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,key11_2,k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2,k11_2,k12_2,k13_2,k14_2,k15_2,k16_2,k17_2) == out2)
s.add(GG1>=0,GG1<=255)
'''s.add(i2>=0,i2<=255)
s.add(i3>=0,i3<=255)
s.add(i4>=0,i4<=255)
s.add(i6>=0,i6<=255)
s.add(G1>=0,G1<=255)
s.add(G2>=0,G2<=255)
s.add(GG1>=0,GG1<=255)
s.add(GG2>=0,GG2<=255)'''
s.add(key3_1==7,key3_2==7)
s.add(key6_1==8,key6_2==8)
s.add(key1_1>=0,key1_2>=0)
s.add(key2_1==11,key2_2==11)
s.add(key4_1==17,key4_2==17)
s.add(key5_1==13,key5_2==13)
s.add(key7_1==31,key7_2==31)
s.add(key8_1==14,key8_2==14)
s.add(key9_1==13,key9_2==13)
s.add(key11_1==12,key11_2==12)
s.add(key10_1>=0,key10_2>=0)
s.add(k1_1==True,k1_2==True)
s.add(k2_1==False,k2_2==False)
s.add(k3_1==True,k3_2==True)
s.add(k4_1==False,k4_2==False)
s.add(k5_1==True,k5_2==True)
s.add(k6_1==False,k6_2==False)
s.add(k7_1==True,k7_2==True)
s.add(k8_1==False,k8_2==False)
s.add(k9_1==True,k9_2==True)
s.add(k10_1==False,k10_2==False)

pos_set = set()
print("loop1 enter")
while s.check(out1 != out2, Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1 != key4_2,key5_1 != key5_2,key6_1 != key6_2,key7_1 != key7_2,key8_1 != key8_2,key9_1 != key9_2,key10_1!=key10_2,key11_1!=key11_2,k1_1!=k1_2,k2_1!=k2_2,k3_1!=k3_2,k4_1!=k4_2,k5_1!=k5_2,k6_1!=k6_2,k7_1!=k7_2,k8_1!=k8_2,k9_1!=k9_2,k10_1!=k10_2,k11_1!=k11_2,k12_1!=k12_2,k13_1!=k13_2,k14_1!=k14_2,k15_1!=k15_2,k16_1!=k16_2,k17_1!=k17_2)) == sat:
    added_new_constraints = True
    #Model to get DIP
    m = s.model()
    #print(m)
    print("DIP")
    print(str(m[GG1]))#+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i6])+" "+str(m[G1])+" "+str(m[G2])+" "+str(m[GG1])+" "+str(m[GG2]))
    print("The key is:")
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1])+" "+str(m[key11_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1])+" "+str(m[k11_1])+" "+str(m[k12_1])+" "+str(m[k13_1])+" "+str(m[k14_1])+" "+str(m[k15_1])+" "+str(m[k16_1])+" "+str(m[k17_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2])+" "+str(m[key11_2])+" "+str(m[k1_2])+" "+str(m[k2_2])+" "+str(m[k3_2])+" "+str(m[k4_2])+" "+str(m[k5_2])+" "+str(m[k6_2])+" "+str(m[k7_2])+" "+str(m[k8_2])+" "+str(m[k9_2])+" "+str(m[k10_2])+" "+str(m[k11_2])+" "+str(m[k12_2])+" "+str(m[k13_2])+" "+str(m[k14_2])+" "+str(m[k15_2])+" "+str(m[k16_2])+" "+str(m[k17_2]))
    #creating the input with the DIP
    ia = str(1) + " " + str(2) + " " + str(3) + " " + str(5) + " " + str(7) + " " + str(11) + " " + str(13) + " " + str(m[GG1]) + " " + str(19)
    #using the input to get the correct output for the DIP from the oracle 
    [oa1,oa2,oa3,oa4] = Cexec(ia)
    oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
    #constraints added with the DIP
    s.add(findOutput(m[GG1],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1,key11_1,k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1,k11_1,k12_1,k13_1,k14_1,k15_1,k16_1,k17_1) == oa)
    s.add(findOutput(m[GG1],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2,key11_2,k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2,k11_2,k12_2,k13_2,k14_2,k15_2,k16_2,k17_2) == oa)
    j = j + 1

p = 0
print()
print()
print(s.statistics())
print("checking remaining keys")
while s.check(key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1 == key4_2,key5_1 == key5_2,key6_1 == key6_2,key7_1 == key7_2,key8_1 == key8_2,key9_1 == key9_2,key10_1==key10_2,key11_1==key11_2,k1_1==k1_2,k2_1==k2_2,k3_1==k3_2,k4_1==k4_2,k5_1==k5_2,k6_1==k6_2,k7_1==k7_2,k8_1==k8_2,k9_1==k9_2,k10_1==k10_2,k11_1==k11_2,k12_1==k12_2,k13_1==k13_2,k14_1==k14_2,k15_1==k15_2,k16_1==k16_2,k17_1==k17_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    #adding the remaining possible keys 
    pos_set.add(m)
    print(str(m[key1_1].as_signed_long())+" "+str(m[key2_1].as_signed_long())+" "+str(m[key3_1].as_signed_long())+" "+str(m[key4_1].as_signed_long())+" "+str(m[key5_1].as_signed_long())+" "+str(m[key6_1].as_signed_long())+" "+str(m[key7_1].as_signed_long())+" "+str(m[key8_1].as_signed_long())+" "+str(m[key9_1].as_signed_long())+" "+str(m[key10_1].as_signed_long())+" "+str(m[key11_1].as_signed_long())+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1])+" "+str(m[k11_1])+" "+str(m[k12_1])+" "+str(m[k13_1])+" "+str(m[k14_1])+" "+str(m[k15_1])+" "+str(m[k16_1])+" "+str(m[k17_1]))
    #If size crossed threshold exit
    if len(pos_set) > rem_key_max:
        break

    #adding constraints - K1 & K2 is not equal to current key fetched
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1],key5_1!=m[key5_1],key6_1!=m[key6_1],key7_1!=m[key7_1],key8_1!=m[key8_1],key9_1!=m[key9_1],key10_1!=m[key10_1],key11_1!=m[key11_1],k1_1!=m[k1_1],k2_1!=m[k2_1],k3_1!=m[k3_1],k4_1!=m[k4_1],k5_1!=m[k5_1],k6_1!=m[k6_1],k7_1!=m[k7_1],k8_1!=m[k8_1],k9_1!=m[k9_1],k10_1!=m[k10_1],k11_1!=m[k11_1],k12_1!=m[k12_1],k13_1!=m[k13_1],k14_1!=m[k14_1],k15_1!=m[k15_1],k16_1!=m[k16_1],k17_1!=m[k17_1]))
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2],key5_2!=m[key5_2],key6_2!=m[key6_2],key7_2!=m[key7_2],key8_2!=m[key8_2],key9_2!=m[key9_2],key10_2!=m[key10_2],key11_2!=m[key11_2],k1_2!=m[k1_2],k2_2!=m[k2_2],k3_2!=m[k3_2],k4_2!=m[k4_2],k5_2!=m[k5_2],k6_2!=m[k6_2],k7_2!=m[k7_2],k8_2!=m[k8_2],k9_2!=m[k9_2],k10_2!=m[k10_2],k11_2!=m[k11_2],k12_2!=m[k12_2],k13_2!=m[k13_2],k14_2!=m[k14_2],k15_2!=m[k15_2],k16_2!=m[k16_2],k17_2!=m[k17_2]))
    p = p + 1


print()
print("loop2 enter")


# #creating remaining key set list
# pos_l = list(pos_set)

# #defining a new SMT solver
# g = Tactic('smt').solver()

# #addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
# g.add(findOutput(i1,i2,i3,i4,i6,G1,G2,GG1,GG2,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1) == out1)
# g.add(findOutput(i1,i2,i3,i4,i6,G1,G2,GG1,GG2,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2) == out2)

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
#         ia = str(m[i1]) + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4])+ " " + str(m[i6]) + " " + str(m[G1]) + " " + str(m[G2]) + " " + str(m[G3]) + " " + str(m[G4]) + " " + str(m[GG1]) + " " + str(m[GG2])
#         [oa1,oa2,oa3,oa4] = Cexec(ia)
#         oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
#         #checking m1 is correct key or not is correct or not
#         if g.check(findOutput(m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[GG1],m[GG2],m1[key1_2],m1[key2_2],m1[key3_2],m1[key4_2],m1[key5_2],m1[key6_2],m1[key7_2],m1[key8_2],m1[key9_2]) == oa) == unsat:
#             pos_l.remove(m1)
#         #checking m2 is correct key or not
#         if g.check(findOutput(m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[GG1],m[GG2],m2[key1_2],m2[key2_2],m2[key3_2],m2[key4_2],m2[key5_2],m2[key6_2],m2[key7_2],m2[key8_2],m2[key9_2]) == oa) == unsat:
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
