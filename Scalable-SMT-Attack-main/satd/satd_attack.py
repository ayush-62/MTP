from z3 import *
from prettytable import PrettyTable
import subprocess
import time

start = time.time()

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)  
    return list(map(int,out.decode('utf-8').split()))

out_1= Int('out_1')
out_2= Int('out_2')
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32=Ints('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16 i17 i18 i19 i20 i21 i22 i23 i24 i25 i26 i27 i28 i29 i30 i31 i32')

key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = Ints('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1')
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = Ints('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2')

def satd(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,key1,key2,key3,key4,key5,key6,key7):
    pix = Array('pix', IntSort(), IntSort())
    tmp = Array('tmp', IntSort(), ArraySort(IntSort(), IntSort()))
    diff = Array('diff', IntSort(), ArraySort(IntSort(), IntSort()))
    out = Int('out')
    out = 0

    pix = Store(pix, 0, i1)
    pix = Store(pix, 1, i2)
    pix = Store(pix, 2, i3)
    pix = Store(pix, 3, i4)
    pix = Store(pix, 4, i5)
    pix = Store(pix, 5, i6)
    pix = Store(pix, 6, i7)
    pix = Store(pix, 7, i8)
    pix = Store(pix, 8, i9)
    pix = Store(pix, 9, i10)
    pix = Store(pix, 10, i11)
    pix = Store(pix, 11, i12)
    pix = Store(pix, 12, i13)
    pix = Store(pix, 13, i14)
    pix = Store(pix, 14, i15)
    pix = Store(pix, 15, i16)
    pix = Store(pix, 16, i17)
    pix = Store(pix, 17, i18)
    pix = Store(pix, 18, i19)
    pix = Store(pix, 19, i20)
    pix = Store(pix, 20, i21)
    pix = Store(pix, 21, i22)
    pix = Store(pix, 22, i23)
    pix = Store(pix, 23, i24)
    pix = Store(pix, 24, i25)
    pix = Store(pix, 25, i26)
    pix = Store(pix, 26, i27)
    pix = Store(pix, 27, i28)
    pix = Store(pix, 28, i29)
    pix = Store(pix, 29, i30)
    pix = Store(pix, 30, i31)
    pix = Store(pix, 31, i32)

    t1 = Array('t1', IntSort(), IntSort())
    t1 = Store(t1, 0, Select(pix, 0) - Select(pix, key1)) #Key1 = 16
    t1 = Store(t1, 1, Select(pix, 1) - Select(pix, 17))
    t1 = Store(t1, 2, Select(pix, 2) - Select(pix, 18))
    t1 = Store(t1, 3, Select(pix, 3) - Select(pix, 19))

    t2 = Array('t2', IntSort(), IntSort())
    t2 = Store(t2, 0, Select(pix, 4) - Select(pix, 20))
    t2 = Store(t2, 1, Select(pix, key2) - Select(pix, 21)) #key2 = 5
    t2 = Store(t2, 2, Select(pix, 6) - Select(pix, 22))
    t2 = Store(t2, 3, Select(pix, 7) - Select(pix, 23))

    t3 = Array('t3', IntSort(), IntSort())
    t3 = Store(t3, 0, Select(pix, 8)  - Select(pix, 24))
    t3 = Store(t3, 1, Select(pix, 9)  - Select(pix, 25))
    t3 = Store(t3, 2, Select(pix, key3) - Select(pix, 26)) #key3 = 10
    t3 = Store(t3, 3, Select(pix, 11) - Select(pix, 27))

    t4 = Array('t4', IntSort(), IntSort())
    t4 = Store(t4, 0, Select(pix, 12) - Select(pix, 28))
    t4 = Store(t4, 1, Select(pix, 13) - Select(pix, 29))
    t4 = Store(t4, 2, Select(pix, key4) - Select(pix, 30)) #key4 = 14
    t4 = Store(t4, 3, Select(pix, 15) - Select(pix, 31))

    diff = Store(diff, 0, t1)
    diff = Store(diff, 1, t2)
    diff = Store(diff, 2, t3)
    diff = Store(diff, 3, t4)

    #----------------------------------Loop 1----------------------------------------


    s01 = Int('S01')
    s23 = Int('S23')
    d01 = Int('d01')
    d23 = Int('d23')

    #-------------------------------Itration 1--------------------------------------
    s01 = Select(Select(diff,0), 0) + Select(Select(diff,0), 1)
    s23 = Select(Select(diff,0), 2) + Select(Select(diff,0), 3)
    d01 = Select(Select(diff,0), 0) - Select(Select(diff,0), 1)
    d23 = Select(Select(diff,0), 2) - Select(Select(diff,0), key6) #key6 = 3

    t5 = Array('t5', IntSort(), IntSort())
    t5 = If(key5 == 5, Store(t5, 0, s01 + s23), Store(t5, 0, s01 - s23)) #key5 = 5
    t5 = Store(t5, 1, s01 - s23)
    t5 = Store(t5, 2, d01 - d23)
    t5 = Store(t5, 3, d01 + d23)


    tmp = Store(tmp, 0, t5)

    #-------------------------------Itration 2--------------------------------------
    s01 = Select(Select(diff,1), 0) + Select(Select(diff,1), 1)
    s23 = Select(Select(diff,1), 2) + Select(Select(diff,1), 3)
    d01 = Select(Select(diff,1), 0) - Select(Select(diff,1), 1)
    d23 = Select(Select(diff,1), 2) - Select(Select(diff,1), key6) #key6 = 3

    t6 = Array('t6', IntSort(), IntSort())
    t6 = If(key5 == 5, Store(t6, 0, s01 + s23), Store(t6, 0, s01 - s23)) #key5 = 5
    t6 = Store(t6, 1, s01 - s23)
    t6 = Store(t6, 2, d01 - d23)
    t6 = Store(t6, 3, d01 + d23)

    tmp = Store(tmp, 1, t6)

    #-------------------------------Itration 3--------------------------------------
    s01 = Select(Select(diff,2), 0) + Select(Select(diff,2), 1)
    s23 = Select(Select(diff,2), 2) + Select(Select(diff,2), 3)
    d01 = Select(Select(diff,2), 0) - Select(Select(diff,2), 1)
    d23 = Select(Select(diff,2), 2) - Select(Select(diff,2), key6) #key6 = 3

    t7 = Array('t7', IntSort(), IntSort())
    t7 = If(key5 == 5, Store(t7, 0, s01 + s23), Store(t7, 0, s01 - s23)) #key5 = 5
    t7 = Store(t7, 1, s01 - s23)
    t7 = Store(t7, 2, d01 - d23)
    t7 = Store(t7, 3, d01 + d23)

    tmp = Store(tmp, 2, t7)

    #-------------------------------Itration 4--------------------------------------
    s01 = Select(Select(diff,3), 0) + Select(Select(diff,3), 1)
    s23 = Select(Select(diff,3), 2) + Select(Select(diff,3), 3)
    d01 = Select(Select(diff,3), 0) - Select(Select(diff,3), 1)
    d23 = Select(Select(diff,3), 2) - Select(Select(diff,3), key6) #key6 = 3

    t8 = Array('t8', IntSort(), IntSort())
    t8 = If(key5 == 5, Store(t8, 0, s01 + s23), Store(t8, 0, s01 - s23)) #key5 = 5
    t8 = Store(t8, 1, s01 - s23)
    t8 = Store(t8, 2, d01 - d23)
    t8 = Store(t8, 3, d01 + d23)

    tmp = Store(tmp, 3, t8)

    # for i in range(4):
    #     for j in range(4):
    #         print(simplify(Select(Select(diff,i), j)))

    #-------------------------------------Loop 2-------------------------------------------------
    
    #-----------------------------------Iteration 1-----------------------------------------------
    s01 = Select(Select(tmp,0),0) + Select(Select(tmp,1),0)
    s23 = Select(Select(tmp,key7),0) + Select(Select(tmp,3),0) #key7 = 2
    d01 = Select(Select(tmp,0),0) - Select(Select(tmp,1),0)
    d23 = Select(Select(tmp,2),0) - Select(Select(tmp,3),0)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    #-----------------------------------Iteration 2-----------------------------------------------
    s01 = Select(Select(tmp,0),1) + Select(Select(tmp,1),1)
    s23 = Select(Select(tmp,key7),1) + Select(Select(tmp,3),1) #key7 = 2
    d01 = Select(Select(tmp,0),1) - Select(Select(tmp,1),1)
    d23 = Select(Select(tmp,2),1) - Select(Select(tmp,3),1)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    #-----------------------------------Iteration 3-----------------------------------------------
    s01 = Select(Select(tmp,0),2) + Select(Select(tmp,1),2)
    s23 = Select(Select(tmp,key7),2) + Select(Select(tmp,3),2) #key7 = 2
    d01 = Select(Select(tmp,0),2) - Select(Select(tmp,1),2)
    d23 = Select(Select(tmp,2),2) - Select(Select(tmp,3),2)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

     #-----------------------------------Iteration 4-----------------------------------------------
    s01 = Select(Select(tmp,0),3) + Select(Select(tmp,1),3)
    s23 = Select(Select(tmp,key7),3) + Select(Select(tmp,3),3) #key7 = 2
    d01 = Select(Select(tmp,0),3) - Select(Select(tmp,1),3)
    d23 = Select(Select(tmp,2),3) - Select(Select(tmp,3),3)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    return out


#key1 = 16, key2 = 5, key3 = 10, key4 = 14, key5 = 5, key6 = 3, key7 = 2
# print(simplify(satd(0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,16,5,10,14,5,3,2)))

s = Tactic('smt').solver()
s.add(key1_1 >=0 , key1_1 < 32)
s.add(key1_2 >=0 , key1_2 < 32)
s.add(key2_1 >=0 , key2_1 < 32)
s.add(key2_2 >=0 , key2_2 < 32)
s.add(key3_1 >=0 , key3_1 < 32)
s.add(key3_2 >=0 , key3_2 < 32)
s.add(key4_1 >=0 , key4_1 < 32)
s.add(key4_2 >=0 , key4_2 < 32)
s.add(key6_1 >=0 , key6_1 < 4)
s.add(key6_2 >=0 , key6_2 < 4)
s.add(key7_1 >=0 , key7_1 < 4)
s.add(key7_2 >=0 , key7_2 < 4)

s.add(i1 >= 0 , i1 <= 255)
s.add(i2 >= 0 , i2 <= 255)
s.add(i3 >= 0 , i3 <= 255)
s.add(i4 >= 0 , i4 <= 255)
s.add(i5 >= 0 , i5 <= 255)
s.add(i6 >= 0 , i6 <= 255)
s.add(i7 >= 0 , i7 <= 255)
s.add(i8 >= 0 , i8 <= 255)
s.add(i9 >= 0 , i9 <= 255)
s.add(i10 >= 0 , i10 <= 255)
s.add(i11 >= 0 , i11 <= 255)
s.add(i12 >= 0 , i12 <= 255)
s.add(i13 >= 0 , i13 <= 255)
s.add(i14 >= 0 , i14 <= 255)
s.add(i15 >= 0 , i15 <= 255)
s.add(i16 >= 0 , i16 <= 255)
s.add(i17 >= 0 , i17 <= 255)
s.add(i18 >= 0 , i18 <= 255)
s.add(i19 >= 0 , i19 <= 255)
s.add(i20 >= 0 , i20 <= 255)
s.add(i21 >= 0 , i21 <= 255)
s.add(i22 >= 0 , i22 <= 255)
s.add(i23 >= 0 , i23 <= 255)
s.add(i24 >= 0 , i24 <= 255)
s.add(i25 >= 0 , i25 <= 255)
s.add(i26 >= 0 , i26 <= 255)
s.add(i27 >= 0 , i27 <= 255)
s.add(i28 >= 0 , i28 <= 255)
s.add(i29 >= 0 , i29 <= 255)
s.add(i30 >= 0 , i30 <= 255)
s.add(i31 >= 0 , i31 <= 255)
s.add(i32 >= 0 , i32 <= 255)

s.add(satd(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1) == out_1)
s.add(satd(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2) == out_2)

while s.check(out_1 != out_2, Or(key1_1 != key1_2,key2_1 != key2_2,key3_1 != key3_2,key4_1 != key4_2,key5_1 != key5_2, key6_1 != key6_2, key7_1 != key7_2)) == sat:
   
    m = s.model()
   
    print("DIP")
    print(str(m[i1]) + " " +str(m[i2]) + " " +str(m[i3]) + " " +str(m[i4]) + " " +str(m[i5]) + " " +str(m[i6]) + " " +str(m[i7]) + " " +str(m[i8]) + " " +str(m[i9]) + " " +str(m[i10]) + " " +str(m[i11]) + " " +str(m[i12]) + " " +str(m[i13]) + " " +str(m[i14]) + " " +str(m[i15]) + " " +str(m[i16]) + " " +str(m[i17]) + " " +str(m[i18]) + " " +str(m[i19]) + " " +str(m[i20]) + " " +str(m[i21]) + " " +str(m[i22]) + " " +str(m[i23]) + " " +str(m[i24]) + " " +str(m[i25]) + " " +str(m[i26]) + " " + str(m[i27]) + " " +str(m[i28]) + " " +str(m[i29]) + " " +str(m[i30]) + " " +str(m[i31]) + " " + str(m[i32]))

    # print("The key is:")
    # print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1]))
    # print(str(m[key1_2])+" "+str(m[key2_2])+" "+str(m[key3_2])+" "+str(m[key4_2])+" "+str(m[key5_2])+" "+str(m[k1_2])+" "+str(m[k2_2])+" "+str(m[k3_2])+" "+str(m[k4_2])+" "+str(m[k5_2])+" "+str(m[k6_2])+" "+str(m[k7_2])+" "+str(m[k8_2])+" "+str(m[k9_2])+" "+str(m[k10_2]))
    #creating the input with the DIP
    ia = str(m[i1]) + " " +str(m[i2]) + " " +str(m[i3]) + " " +str(m[i4]) + " " +str(m[i5]) + " " +str(m[i6]) + " " +str(m[i7]) + " " +str(m[i8]) + " " +str(m[i9]) + " " +str(m[i10]) + " " +str(m[i11]) + " " +str(m[i12]) + " " +str(m[i13]) + " " +str(m[i14]) + " " +str(m[i15]) + " " +str(m[i16]) + " " +str(m[i17]) + " " +str(m[i18]) + " " +str(m[i19]) + " " +str(m[i20]) + " " +str(m[i21]) + " " +str(m[i22]) + " " +str(m[i23]) + " " +str(m[i24]) + " " +str(m[i25]) + " " +str(m[i26]) + " " + str(m[i27]) + " " +str(m[i28]) + " " +str(m[i29]) + " " +str(m[i30]) + " " +str(m[i31]) + " " + str(m[i32]) 
    [oa] = Cexec(ia)
    out = Int('out')
    out = IntVal(oa)
    s.add(simplify(satd(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],m[i17],m[i18],m[i19],m[i20],m[i21],m[i22],m[i23],m[i24],m[i25],m[i26],m[i27],m[i28],m[i29],m[i30],m[i31],m[i32],key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1) == oa))
    s.add(simplify(satd(m[i1],m[i2],m[i3],m[i4],m[i5],m[i6],m[i7],m[i8],m[i9],m[i10],m[i11],m[i12],m[i13],m[i14],m[i15],m[i16],m[i17],m[i18],m[i19],m[i20],m[i21],m[i22],m[i23],m[i24],m[i25],m[i26],m[i27],m[i28],m[i29],m[i30],m[i31],m[i32],key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2) == oa))
    # s.add(simplify(satd(18,17,1,2,52,25,112,4,5,24,1,3,21,53,22,53,69,1,16,25,22,54,90,6,18,1,68,27,55,1,0,63,key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1) == oa))
    # s.add(simplify(satd(18,17,1,2,52,25,112,4,5,24,1,3,21,53,22,53,69,1,16,25,22,54,90,6,18,1,68,27,55,1,0,63,key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2) == oa))

curr_time = time.time()
taken = curr_time-start
print("unsat took %f seconds." %taken)  

t = PrettyTable(['key1','key2','key3','key4','key5','key6','key7'])
pos_set = set()
TO_init = 1600
TO_max = 12800
rem_key_max = 32
print()
print("checking remaining keys")
while s.check(key1_1 == key1_2,key2_1 == key2_2,key3_1 == key3_2,key4_1 == key4_2,key5_1 == key5_2,key6_1 == key6_2,key7_1 == key7_2) != unsat:
    try:
        m = s.model()
    except:
        break_away = True
        break
    #adding the remaining possible keys 
    pos_set.add(m)
    t.add_row([str(m[key1_1]),str(m[key2_1]),str(m[key3_1]),str(m[key4_1]),str(m[key5_1]),str(m[key6_1]),str(m[key7_1])])
    # print(str(m[key1_1])+" "+str(m[key2_1])+" "+str(m[key3_1])+" "+str(m[key4_1])+" "+str(m[key5_1])+" "+str(m[k1_1])+" "+str(m[k2_1])+" "+str(m[k3_1])+" "+str(m[k4_1])+" "+str(m[k5_1])+" "+str(m[k6_1])+" "+str(m[k7_1])+" "+str(m[k8_1])+" "+str(m[k9_1])+" "+str(m[k10_1]))
    #If size crossed threshold exit
    if len(pos_set) > rem_key_max:
        break

    #adding constraints - K1 & K2 is not equal to current key fetched
    s.add(Or(key1_1 != m[key1_1],key2_1!=m[key2_1],key3_1!=m[key3_1],key4_1!=m[key4_1],key5_1!=m[key5_1],key6_1!=m[key6_1],key7_1!=m[key7_1]))
    s.add(Or(key1_2 != m[key1_2],key2_2!=m[key2_2],key3_2!=m[key3_2],key4_2!=m[key4_2],key5_2!=m[key5_2],key6_2!=m[key6_2],key7_2!=m[key7_2]))
    # p = p + 1

print(t)
end_time = time.time()
taken = end_time-start
print("Computation took  %f seconds." % (taken))   