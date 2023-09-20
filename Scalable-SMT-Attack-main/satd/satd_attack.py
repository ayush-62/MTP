from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)  
    return list(map(int,out.decode('utf-8').split()))

out_1= Int('out_1')
out_2= Int('out_2')
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32=Ints('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16 i17 i18 i19 i20 i21 i22 i23 i24 i25 i26 i27 i28 i29 i30 i31 i32')

key1_1,key2_1,key3_1,key4_1,key5_1,key6_1,key7_1,key8_1,key9_1,key10_1 = Ints('key1_1 key2_1 key3_1 key4_1 key5_1 key6_1 key7_1 key8_1 key9_1 key10_1')
key1_2,key2_2,key3_2,key4_2,key5_2,key6_2,key7_2,key8_2,key9_2,key10_2 = Ints('key1_2 key2_2 key3_2 key4_2 key5_2 key6_2 key7_2 key8_2 key9_2 key10_2')

def satd(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32):
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
    t1 = Store(t1, 0, Select(pix, 0) - Select(pix, 16))
    t1 = Store(t1, 1, Select(pix, 1) - Select(pix, 17))
    t1 = Store(t1, 2, Select(pix, 2) - Select(pix, 18))
    t1 = Store(t1, 3, Select(pix, 3) - Select(pix, 19))

    t2 = Array('t2', IntSort(), IntSort())
    t2 = Store(t2, 0, Select(pix, 4) - Select(pix, 20))
    t2 = Store(t2, 1, Select(pix, 5) - Select(pix, 21))
    t2 = Store(t2, 2, Select(pix, 6) - Select(pix, 22))
    t2 = Store(t2, 3, Select(pix, 7) - Select(pix, 23))

    t3 = Array('t3', IntSort(), IntSort())
    t3 = Store(t3, 0, Select(pix, 8)  - Select(pix, 24))
    t3 = Store(t3, 1, Select(pix, 9)  - Select(pix, 25))
    t3 = Store(t3, 2, Select(pix, 10) - Select(pix, 26))
    t3 = Store(t3, 3, Select(pix, 11) - Select(pix, 27))

    t4 = Array('t4', IntSort(), IntSort())
    t4 = Store(t4, 0, Select(pix, 12) - Select(pix, 28))
    t4 = Store(t4, 1, Select(pix, 13) - Select(pix, 29))
    t4 = Store(t4, 2, Select(pix, 14) - Select(pix, 30))
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
    d23 = Select(Select(diff,0), 2) - Select(Select(diff,0), 3)

    t5 = Array('t5', IntSort(), IntSort())
    t5 = Store(t5, 0, s01 + s23)
    t5 = Store(t5, 1, s01 - s23)
    t5 = Store(t5, 2, d01 - d23)
    t5 = Store(t5, 3, d01 + d23)


    tmp = Store(tmp, 0, t5)

    #-------------------------------Itration 2--------------------------------------
    s01 = Select(Select(diff,1), 0) + Select(Select(diff,1), 1)
    s23 = Select(Select(diff,1), 2) + Select(Select(diff,1), 3)
    d01 = Select(Select(diff,1), 0) - Select(Select(diff,1), 1)
    d23 = Select(Select(diff,1), 2) - Select(Select(diff,1), 3)

    t6 = Array('t6', IntSort(), IntSort())
    t6 = Store(t6, 0, s01 + s23)
    t6 = Store(t6, 1, s01 - s23)
    t6 = Store(t6, 2, d01 - d23)
    t6 = Store(t6, 3, d01 + d23)

    tmp = Store(tmp, 1, t6)

    #-------------------------------Itration 3--------------------------------------
    s01 = Select(Select(diff,2), 0) + Select(Select(diff,2), 1)
    s23 = Select(Select(diff,2), 2) + Select(Select(diff,2), 3)
    d01 = Select(Select(diff,2), 0) - Select(Select(diff,2), 1)
    d23 = Select(Select(diff,2), 2) - Select(Select(diff,2), 3)

    t7 = Array('t7', IntSort(), IntSort())
    t7 = Store(t7, 0, s01 + s23)
    t7 = Store(t7, 1, s01 - s23)
    t7 = Store(t7, 2, d01 - d23)
    t7 = Store(t7, 3, d01 + d23)

    tmp = Store(tmp, 2, t7)

    #-------------------------------Itration 4--------------------------------------
    s01 = Select(Select(diff,3), 0) + Select(Select(diff,3), 1)
    s23 = Select(Select(diff,3), 2) + Select(Select(diff,3), 3)
    d01 = Select(Select(diff,3), 0) - Select(Select(diff,3), 1)
    d23 = Select(Select(diff,3), 2) - Select(Select(diff,3), 3)

    t8 = Array('t8', IntSort(), IntSort())
    t8 = Store(t8, 0, s01 + s23)
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
    s23 = Select(Select(tmp,2),0) + Select(Select(tmp,3),0)
    d01 = Select(Select(tmp,0),0) - Select(Select(tmp,1),0)
    d23 = Select(Select(tmp,2),0) - Select(Select(tmp,3),0)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    #-----------------------------------Iteration 2-----------------------------------------------
    s01 = Select(Select(tmp,0),1) + Select(Select(tmp,1),1)
    s23 = Select(Select(tmp,2),1) + Select(Select(tmp,3),1)
    d01 = Select(Select(tmp,0),1) - Select(Select(tmp,1),1)
    d23 = Select(Select(tmp,2),1) - Select(Select(tmp,3),1)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    #-----------------------------------Iteration 3-----------------------------------------------
    s01 = Select(Select(tmp,0),2) + Select(Select(tmp,1),2)
    s23 = Select(Select(tmp,2),2) + Select(Select(tmp,3),2)
    d01 = Select(Select(tmp,0),2) - Select(Select(tmp,1),2)
    d23 = Select(Select(tmp,2),2) - Select(Select(tmp,3),2)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

     #-----------------------------------Iteration 4-----------------------------------------------
    s01 = Select(Select(tmp,0),3) + Select(Select(tmp,1),3)
    s23 = Select(Select(tmp,2),3) + Select(Select(tmp,3),3)
    d01 = Select(Select(tmp,0),3) - Select(Select(tmp,1),3)
    d23 = Select(Select(tmp,2),3) - Select(Select(tmp,3),3)

    out += If(s01 + s23 > 0, s01 + s23, -(s01 + s23))
    out += If(s01 - s23 > 0, s01 - s23, -(s01 - s23))
    out += If(d01 + d23 > 0, d01 + d23, -(d01 + d23))
    out += If(d01 - d23 > 0, d01 - d23, -(d01 - d23))

    return out



print(simplify(satd(0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1)))


