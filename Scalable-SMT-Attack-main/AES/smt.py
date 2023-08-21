'''if s.check(out3!=out4,Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1!=key4_2,key5_1!=key5_2,key6_1!=key6_2,key7_1!=key7_2,key8_1!=key8_2,key9_1!=key9_2,key10_1!=key10_2)) == sat:
    m = s.model()
    #print(m)
    #print(m)
    print(str(m[i1])+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16]))
    print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[key6_1])+" "+str(m[key7_1])+" "+str(m[key8_1])+" "+str(m[key9_1])+" "+str(m[key10_1]))
    print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[key6_2])+" "+str(m[key7_2])+" "+str(m[key8_2])+" "+str(m[key9_2])+" "+str(m[key10_2]))
    # ia = str(m[i1])#+" "+str(m[i2])+" "+str(m[i3])+" "+str(m[i4])+" "+str(m[i5])+" "+str(m[i6])+" "+str(m[i7])+" "+str(m[i8])+" "+str(m[i9])+" "+str(m[i10])+" "+str(m[i11])+" "+str(m[i12])+" "+str(m[i13])+" "+str(m[i14])+" "+str(m[i15])+" "+str(m[i16])
    # [oa1,oa2,oa3,oa4,oa5,oa6,oa7,oa8,oa9,oa10,oa11,oa12,oa13,oa14,oa15,oa16]= Cexec(ia)
    # #,BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32),BitVecVal(oa17,32),BitVecVal(oa18,32),BitVecVal(oa19,32),BitVecVal(oa20,32),BitVecVal(oa21,32),BitVecVal(oa22,32),BitVecVal(oa23,32),BitVecVal(oa24,32),BitVecVal(oa25,32),BitVecVal(oa26,32),BitVecVal(oa27,32),BitVecVal(oa28,32),BitVecVal(oa29,32),BitVecVal(oa30,32),BitVecVal(oa31,32),BitVecVal(oa32,32)
    # oa = tuple.tuple1(BitVecVal(oa1,32),BitVecVal(oa2,32),BitVecVal(oa3,32),BitVecVal(oa4,32),BitVecVal(oa5,32),BitVecVal(oa6,32),BitVecVal(oa7,32),BitVecVal(oa8,32),BitVecVal(oa9,32),BitVecVal(oa10,32),BitVecVal(oa11,32),BitVecVal(oa12,32),BitVecVal(oa13,32),BitVecVal(oa14,32),BitVecVal(oa15,32),BitVecVal(oa16,32))
    # s.add(simplify(findOutput(m[i1],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)) == oa)
    # s.add(simplify(findOutput(m[i1],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)) == oa)
    # o0_1,o1_1,o2_1,o3_1,o4_1,o5_1,o6_1,o7_1,o8_1,o9_1,o10_1,o11_1,o12_1,o13_1,o14_1,o15_1=findOutput(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1)
    # o0_2,o1_2,o2_2,o3_2,o4_2,o5_2,o6_2,o7_2,o8_2,o9_2,o10_2,o11_2,o12_2,o13_2,o14_2,o15_2=findOutput(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2)
    # s.add(o0_1==oa1,o1_1==oa2,o2_1==oa3,o3_1==oa4,o4_1==oa5,o5_1==oa6,o6_1==oa7,o7_1==oa8,o8_1==oa9,o9_1==oa10,o10_1==oa11,o11_1==oa12,o12_1==oa13,o13_1==oa14,o14_1==oa15,o15_1==oa16)
    # s.add(o0_2==oa1,o1_2==oa2,o2_2==oa3,o3_2==oa4,o4_2==oa5,o5_2==oa6,o6_2==oa7,o7_2==oa8,o8_2==oa9,o9_2==oa10,o10_2==oa11,o11_2==oa12,o12_2==oa13,o13_2==oa14,o14_2==oa15,o15_2==oa16)
    print("Iteration %d = %f second" %(j+1,time.time()-start))
    j = j + 1
print("unsat takes %d time" %(time.time()-start))
print("loop1 complete")'''


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


'''pos_l = list(pos_set)

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

print("Computation took %d iterations and %f seconds." % (j, taken))  '''    
