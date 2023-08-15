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
key1_1,key2_1,key3_1,key4_1,key5_1 = BitVecs('key1_1 key2_1 key3_1 key4_1 key5_1',32)
key1_2,key2_2,key3_2,key4_2,key5_2 = BitVecs('key1_2 key2_2 key3_2 key4_2 key5_2',32)
k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1 = Bools('k1_1 k2_1 k3_1 k4_1 k5_1 k6_1 k7_1 k8_1 k9_1 k10_1')
k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2 = Bools('k1_2 k2_2 k3_2 k4_2 k5_2 k6_2 k7_2 k8_2 k9_2 k10_2')
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
def findOutput(G1,key1,key2,key3,key4,key5,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10):

    op1 = BitVecVal(17,32) * (BitVecVal(1,32) + key1) #key1=23
    op2 = If(k1,BitVecVal(19,32) * BitVecVal(2,32),BitVecVal(0,32)) # k1=True
    op3 = G1 * BitVecVal(2,32)
    op4 = If(k2,BitVecVal(0,32),BitVecVal(13,32) * BitVecVal(1,32)) #k2=False
    op5 = If(Not(Xor(G1>10,k3)), G1 * BitVecVal(3,32), BitVecVal(0,32)) # k3=True
    op5 = If(Not(Xor(G1>10,k3)), op5 + (BitVecVal(17,32) * key2), op5) #key2=11
    op6 = If(Not(Xor(G1>10,k3)), op5 - op4, BitVecVal(0,32))
    op5 = If(Not(Xor(G1>10,k3)), op5, BitVecVal(3,32) * BitVecVal(5,32))
    op6 = If(Not(Xor(G1>10,k3)), op6, op5 - (op3 * key3)) #key3=7
    op6 = If(Xor(op5<op4,k4), BitVecVal(13,32) * BitVecVal(5,32), op6) #k4=False
    op6 = If(Xor(op5<op4,k4), op6 - (BitVecVal(3,32) *key4), op6) #key4=17
    op17 = If(Xor(op5<op4,k4), op6 - BitVecVal(13,32), BitVecVal(0,32))
    op17 = If(Xor(op5<op4,k4), op17, op2 - op4)
    op2 = If(Xor(op5<op4,k4), op2, op4 - (op17 * key5)) #key5=13
    op17 = If(Xor(op5<op4,k4), op17, op17 - op2)
    op7 = If(k5,G1 * BitVecVal(5,32),BitVecVal(0,32)) #k5=True
    op8 = BitVecVal(13,32) * BitVecVal(3,32)
    op9 = If(k6,BitVecVal(0,32),op1 + op2) #k6=False
    op10 = op3 + op4 
    op11 = If(k7,op4 + op6,BitVecVal(0,32)) #k7=True
    op12 = op7 + op8
    op13 = op11 + G1
    o1 = If(k8,BitVecVal(0,32),op13) #k8=False
    op14 = If(k9,BitVecVal(7,32) + op12,BitVecVal(0,32)) #k9=True
    o2 = op14
    op15 = G1 * op14 
    op16 = op13 * BitVecVal(13,32)
    op17 = If(Xor(op13==op14,k10), op17 * op11, op17) #k10=False
    op14 = If(Xor(op13==op14,k10), op14 - op17, op14)
    op15 = If(Xor(op13==op14,k10), op15 + op17, op15)
    op14 = If(Xor(op13==op14,k10), op14, op13 * G1)
    op18 = op14 * BitVecVal(13,32)
    op19 = op15 * op16
    op20 = op17 + op18
    op21 = G1 * op20
    op22 = op19 * BitVecVal(13,32)
    op23 = op19 * G1
    op24 = op20 * BitVecVal(13,32)
    op25 = op21 + op22
    op26 = op23 + op24
    op27 = op9 + op25
    o3 = op27
    op28 = op10 + op26
    o4 = op28
    o = tuple.tuple(o1,o2,o3,o4)

    return o


prune_key_set = False

j = 0
gg=Tactic('smt').solver()
ia = str(1) + " " + str(2) + " " + str(3) + " " + str(5) +" "+ str(7)+ " " + str(11) + " " + str(13) + " " + str(17) + " " + str(19)
#using the input to get the correct output for the DIP from the oracle 
[oa1,oa2,oa3,oa4] = Cexec(ia)
oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
print(gg.check(findOutput(11,23,11,7,17,13,True,False,True,False,True,False,True,False,True,False)==oa))


#SMT solver declaration 
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(findOutput(i1,key1_1,key2_1,key3_1,key4_1,key5_1,k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1) == out1)
s.add(findOutput(i1,key1_2,key2_2,key3_2,key4_2,key5_2,k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2) == out2)
s.add(G1>=0,G1<=255)
'''s.add(i2>=0,i2<=255)
s.add(i3>=0,i3<=255)
s.add(i4>=0,i4<=255)
s.add(i6>=0,i6<=255)
s.add(G1>=0,G1<=255)
s.add(G2>=0,G2<=255)
s.add(GG1>=0,GG1<=255)
s.add(GG2>=0,GG2<=255)'''
s.add(key1_1==23,key1_2==23)
s.add(key2_1==11,key2_2==11)
s.add(key3_1>=0,key3_2>=0)
s.add(key4_1==17,key4_2==17)
s.add(key5_1==13,key5_2==13)
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
while s.check(out1 != out2, Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1 != key4_2,key5_1 != key5_2,k1_1!=k1_2,k2_1!=k2_2,k3_1!=k3_2,k4_1!=k4_2,k5_1!=k5_2,k6_1!=k6_2,k7_1!=k7_2,k8_1!=k8_2,k9_1!=k9_2,k10_1!=k10_2)) == sat:
    added_new_constraints = True
    #Model to get DIP
    m = s.model()
    #print(m)
    print("DIP")
    print(str(m[G1]))#+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i6])+" "+str(m[G1])+" "+str(m[G2])+" "+str(m[GG1])+" "+str(m[GG2]))
    print("The key is:")
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[k1_2])+" "+str(m[k2_2])+" "+str(m[k3_2])+" "+str(m[k4_2])+" "+str(m[k5_2])+" "+str(m[k6_2])+" "+str(m[k7_2])+" "+str(m[k8_2])+" "+str(m[k9_2])+" "+str(m[k10_2]))
    #creating the input with the DIP
    ia = str(1) + " " + str(2) + " " + str(3) + " " + str(5) + " " + str(7) + " " + str(m[G1]) + " " + str(13) + " " + str(17) + " " + str(19)
    #using the input to get the correct output for the DIP from the oracle 
    [oa1,oa2,oa3,oa4] = Cexec(ia)
    oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
    #constraints added with the DIP
    s.add(findOutput(m[G1],key1_1,key2_1,key3_1,key4_1,key5_1,k1_1,k2_1,k3_1,k4_1,k5_1,k6_1,k7_1,k8_1,k9_1,k10_1) == oa)
    s.add(findOutput(m[G1],key1_2,key2_2,key3_2,key4_2,key5_2,k1_2,k2_2,k3_2,k4_2,k5_2,k6_2,k7_2,k8_2,k9_2,k10_2) == oa)
    
    j = j + 1
    s.add(G1!=m[G1])
    if j==7:
        break

p = 0
print()
print()
print(s.statistics())
print("checking remaining keys")
while s.check(key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1 == key4_2,key5_1 == key5_2,k1_1==k1_2,k2_1==k2_2,k3_1==k3_2,k4_1==k4_2,k5_1==k5_2,k6_1==k6_2,k7_1==k7_2,k8_1==k8_2,k9_1==k9_2,k10_1==k10_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    #adding the remaining possible keys 
    pos_set.add(m)
    print(str(m[key1_1].as_signed_long())+" "+str(m[key2_1].as_signed_long())+" "+str(m[key3_1].as_signed_long())+" "+str(m[key4_1].as_signed_long())+" "+str(m[key5_1].as_signed_long())+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1]))
    #If size crossed threshold exit
    if len(pos_set) > rem_key_max:
        break

    #adding constraints - K1 & K2 is not equal to current key fetched
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1],key5_1!=m[key5_1],k1_1!=m[k1_1],k2_1!=m[k2_1],k3_1!=m[k3_1],k4_1!=m[k4_1],k5_1!=m[k5_1],k6_1!=m[k6_1],k7_1!=m[k7_1],k8_1!=m[k8_1],k9_1!=m[k9_1],k10_1!=m[k10_1]))
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2],key5_2!=m[key5_2],k1_2!=m[k1_2],k2_2!=m[k2_2],k3_2!=m[k3_2],k4_2!=m[k4_2],k5_2!=m[k5_2],k6_2!=m[k6_2],k7_2!=m[k7_2],k8_2!=m[k8_2],k9_2!=m[k9_2],k10_2!=m[k10_2]))
    p = p + 1


print()
print("loop2 enter")


# #creating remaining key set list
pos_l = list(pos_set)

#defining a new SMT solver
g = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
g.add(findOutput(i1,i2,i3,i4,i6,G1,G2,GG1,GG2,key1_1,key2_1,key3_1,key4_1,key5_1,k6_1,k7_1,k8_1,k9_1,k10_1) == out1)
g.add(findOutput(i1,i2,i3,i4,i6,G1,G2,GG1,GG2,key1_2,key2_2,key3_2,key4_2,key5_2,k6_2,k7_2,k8_2,k9_2,k10_2) == out2)

print("loop3 enter")

# #Algorithm 3 - SMT on key set 
while len(pos_l) > 1:
    #Taking two keys from the key set
    m1 = pos_l[0]
    m2 = pos_l[1]
    #after the push the constaints added can be removed using pop()
    g.push()
    #adding constraints - K1 is equal to the first key taken from the list i.e. m1, and K2 is m2
    g.add(key1_1 == m1[key1_1],key2_1==m1[key2_1],key3_1==m1[key3_1],key4_1==m1[key4_1],key5_1==m1[key5_1],k6_1==m1[k6_1],k7_1==m1[k7_1],k8_1==m1[k8_1],k9_1==m1[k9_1])
    g.add(key1_2 == m2[key1_2],key2_2==m2[key2_2],key3_2==m2[key3_2],key4_2==m2[key4_2],key5_2==m2[key5_2],k6_2==m2[k6_2],k7_2==m2[k7_2],k8_2==m2[k8_2],k9_2==m2[k9_2])

    #checking for DIP
    if g.check(out1 != out2) == sat:
        #model to get the DIP.
        m = g.model()
        ia = str(m[i1]) + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4])+ " " + str(m[i6]) + " " + str(m[G1]) + " " + str(m[G2]) + " " + str(m[G3]) + " " + str(m[G4]) + " " + str(m[GG1]) + " " + str(m[GG2])
        [oa1,oa2,oa3,oa4] = Cexec(ia)
        oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
        #checking m1 is correct key or not is correct or not
        if g.check(findOutput(m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[GG1],m[GG2],m1[key1_2],m1[key2_2],m1[key3_2],m1[key4_2],m1[key5_2],m1[k6_2],m1[k7_2],m1[k8_2],m1[k9_2]) == oa) == unsat:
            pos_l.remove(m1)
        #checking m2 is correct key or not
        if g.check(findOutput(m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[GG1],m[GG2],m2[key1_2],m2[key2_2],m2[key3_2],m2[key4_2],m2[key5_2],m2[k6_2],m2[k7_2],m2[k8_2],m2[k9_2]) == oa) == unsat:
            pos_l.remove(m2)
    #no DIP found - keys are from same equivalence class
    else:
        pos_l.remove(m1)
    #here the constaints added are removed - as the next two keys will be taken from the remaining key set
    g.pop()

print("The final key is:")
m = pos_l[0]
print("key1 = " + str(m[key1_1]) + "\n" + "key2 = " + str(m[key2_1]) + "\n" + "key3 = " + str(m[key3_1]) + "\n" + "key4 = " + str(m[key4_1]) + "\n" + "key5 = " + str(m[key5_1])+ "\n" + "key6 = " + str(m[key6_1])+ "\n" + "key7 = " + str(m[key7_1])+ "\n" + "key8 = " + str(m[key8_1])+ "\n" + "key9 = " + str(m[key9_1]))
print()


end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (j, taken))   
