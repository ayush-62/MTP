from z3 import *
import subprocess
import time


#for executing the oracle ang getting the correct inputs 
def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(int,out.decode('utf-8').split()))
    
    
start_time = time.time()


#variable declaration 
i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2 = BitVecs('i1 i2 i3 i4 i6 G1 G2 G3 G4 GG1 GG2',32)
o1_1,o2_1,o3_1,o4_1 = BitVecs('o1_1 o2_1 o3_1 o4_1',32)
o1_2,o2_2,o3_2,o4_2 = BitVecs('o1_2 o2_2 o3_2 o4_2',32)
key5_1,key6_1,key7_1 = Bools('key5_1 key6_1 key7_1')
key5_2,key6_2,key7_2 = Bools('key5_2 key6_2 key7_2')
key4_1,key3_1 = BitVecs('key4_1 key3_1',32)
key4_2,key3_2 = BitVecs('key4_2 key3_2',32)

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
def findOutput(key5,key6,key7,key4,key3,i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2):
    op1 = GG1 * i1
    op2 = GG2 * i2
    op3 = G1 * i2
    op4 = G2 * i1
    op5 = If(G1>10, G1 * i3, BitVecVal(0,32))
    op5 = If(G1>10, op5 + GG1, op5)
    op6 = If(G1>10, op5 - op4, BitVecVal(0,32))
    op5 = If(G1>10, op5, i3 * i4)
    op6 = If(G1>10, op6, op5 - op3)
    op6 = If(Not((Xor((op5<op4), key7))), G2 * i4, op6)
    op6 = If(Not((Xor((op5<op4), key7))), op6 - i3, op6)
    op17 = If(Not((Xor((op5<op4), key7))), op6 - G2, BitVecVal(0,32))
    op17 = If(Not((Xor((op5<op4), key7))), op17, op2 - op4)
    op2 = If(Not((Xor((op5<op4), key7))), op2, op4 - op17)
    op17 = If(Not((Xor((op5<op4), key7))), op17, op17 - op2)
    op7 = G1 * i4
    op8 = G2 * i3
    op9 = op1 + op2
    op10 = op3 + op4
    op11 = op4 + op6
    op12 = op7 + op8
    op13 = op11 + G1
    o1 = op13
    op14 = i6 + op12
    o2 = op14
    op15 = G1 * op14
    op16 = op13 * G2
    op17 = If(op13==op14, op17 * op11, op17)
    op14 = If(op13==op14, op14 - op17, op14)
    op15 = If(op13==op14, op15 + op17, op15)
    op14 = If(op13==op14, op14, op13 * G1)
    op18 = op14 * G2
    op19 = op15 * op16
    op20 = op17 + op18
    op21 = G1 * op20
    op22 = op19 * G2
    op23 = op19 * G1
    op24 = op20 * G2
    op25 = op21 + op22
    op26 = If(key6, op23 + op24, op23 - 1)
    op27 = If(key5, op9 + op25, op9 - 25)
    o3 = op27 + key3
    op28 = op10 + op26
    o4 = op28 + key4

    o = tuple.tuple(o1,o2,o3,o4)

    return o


prune_key_set = False

j = 0


#SMT solver declaration 
s = Tactic('smt').solver()

#addition of constraints - the outputs from the function using K1 and K2 are out1 and out2 respectively 
s.add(findOutput(key5_1,key6_1,key7_1,key4_1,key3_1,i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2) == out1)
s.add(findOutput(key5_2,key6_2,key7_2,key4_2,key3_2,i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2) == out2)

print(s.sexpr())


Key_Set_Fetch_Count = 0
TO_increase_count = 0

while not prune_key_set:

    break_away = False
    added_new_constraints = False

    #time-out for the SMT solver is set 
    s.set("timeout", TO_init)

    pos_set = set()
    print("loop1 enter")

    '''
        Algorithm 2 - Modified version of Baseline algorith (Algorithm 1)

        Algo1 has only constraint of out1 != out2.
        In Algo2, along with that constraint, k1 != k2 is also added,
        because in algo1 such scenario might happen where one one key is correct,
        and both k1 and k2 refers to that key and loop gets stuck.
    '''
    while s.check(out1 != out2, Or(key5_1 != key5_2,key6_1 != key6_2,key7_1 != key7_2,key4_1 != key4_2,key3_1 != key3_2)) == sat:
        added_new_constraints = True
        #Model to get DIP
        m = s.model()
        #print(m)
        print("DIP")
        print(str(m[i1])+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i6])+" "+str(m[G1])+" "+str(m[G2])+" "+str(m[G3])+" "+str(m[G4])+" "+str(m[GG1])+" "+str(m[GG2]))
        print("The key is:")
        print(str(m[key5_1]) + " " + str(m[key6_1]) + " " + str(m[key7_1]) + " " + str(m[key4_1]) + " " + str(m[key3_1]))
        print(str(m[key5_2]) + " " + str(m[key6_2]) + " " + str(m[key7_2]) + " " + str(m[key4_2]) + " " + str(m[key3_2]))
        #creating the input with the DIP
        ia = str(m[i1]) + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4]) + " " + str(m[i6]) + " " + str(m[G1]) + " " + str(m[G2]) + " " + str(m[G3]) + " " + str(m[G4]) + " " + str(m[GG1]) + " " + str(m[GG2])
        #using the input to get the correct output for the DIP from the oracle 
        [oa1,oa2,oa3,oa4] = Cexec(ia)
        oa = tuple.tuple(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32))
        #constraints added with the DIP
        s.add(findOutput(key5_1,key6_1,key7_1,key4_1,key3_1,m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[G3],m[G4],m[GG1],m[GG2]) == oa)
        s.add(findOutput(key5_2,key6_2,key7_2,key4_2,key3_2,m[i1],m[i2],m[i3],m[i4],m[i6],m[G1],m[G2],m[G3],m[G4],m[GG1],m[GG2]) == oa)
        j = j + 1
        
    p = 0


    '''
        If no new constraints are being added, no use of fetching the remaining keys,
        so increase the time-out and proceed for algo2 once again.
    '''
    if not added_new_constraints:
        TO_init = 2 * TO_init
        TO_increase_count+=1
        if TO_init > TO_max:
            raise Exception("Key couldn't be found in the given time limit and remaining key limit")
        continue

    '''
        Algorthm 4 - Find reamining keys 
    '''
    while s.check(key5_1 == key5_2,key6_1 == key6_2,key7_1 == key7_2,key4_1 == key4_2,key3_1 == key3_2) != unsat:
        try:
            m = s.model()
        except:
            break_away = True
            break
        #adding the remaining possible keys 
        pos_set.add(m)

        #If size crossed threshold exit
        if len(pos_set) > rem_key_max:
            break

        #adding constraints - K1 & K2 is not equal to current key fetched
        s.add(Or(key5_1 != m[key5_1],key6_1 != m[key6_1],key7_1 != m[key7_1],key4_1 != m[key4_1],key3_1 != m[key3_1]))
        s.add(Or(key5_2 != m[key5_2],key6_2 != m[key6_2],key7_2 != m[key7_2],key4_2 != m[key4_2],key3_2 != m[key3_2]))
        p = p + 1


    if p > 0:
        Key_Set_Fetch_Count+=1

    #Check whether the key count is exceding the threshold or not
    if break_away or len(pos_set) > rem_key_max or len(pos_set) == 0:
        TO_init = 2 * TO_init
        TO_increase_count+=1
        if TO_init > TO_max:
            raise Exception("Key couldn't be found in the given time limit and remaining key limit")
    else:
        prune_key_set = True

print()
print("loop2 enter")

#printing the remaining keys
print("Possible keys:",p)
for m in pos_set:
    print(str(m[key5_1]) + " " + str(m[key6_1]) + " " + str(m[key7_1]) + " " + str(m[key4_1]) + " " + str(m[key3_1]))
print()


#creating remaining key set list
pos_l = list(pos_set)

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
print("Number of times remaining key set computed: %d." % (Key_Set_Fetch_Count))  
