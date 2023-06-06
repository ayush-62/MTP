from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True)
    return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 = Ints('i1 i2 i3 i4 i5 i6 i7 i8 i9 i10')
o1_1, o2_1, o3_1 = Ints('o1_1 o2_1 o3_1')
o1_2, o2_2, o3_2 = Ints('o1_2 o2_2 o3_2')
key1_1, key2_1, key3_1, key4_1 = Ints('key1_1 key2_1 key3_1 key4_1')
key1_2, key2_2, key3_2, key4_2 = Ints('key1_2 key2_2 key3_2 key4_2')

my_tuple = Datatype('my_tuple')
my_tuple.declare('tuple', ('1', IntSort()), ('2', IntSort()), ('3', IntSort()))
my_tuple = my_tuple.create()
out1 = my_tuple.tuple(o1_1, o2_1, o3_1)
out2 = my_tuple.tuple(o1_2, o2_2, o3_2)

def motion(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, key_1, key_2, key_3, key_4):
    mult1 = i1 * i2
    mult2 = i1 * (2 * key_1)
    mult3 = i3 * (4 + key_2)
    mult4 = i4 * i5
    mult5 = i3 * i2
    mult6 = i2 * i5
    mult7 = i3 * i6
    mult8 = i4 * i7
    mult9 = i4 * i8
    mult10 = i6 * i9
    mult11 = i6 * i8
    mult12 = i7 * i9
    mult13 = i7 * i8
    mult14 = i9 * i10

    add1 = i1 * mult2
    add2 = (2 * key_3 + 3) * mult4

    add3 = If(add1 > add2, i5 * mult8, i5 + mult8)
    add4 = If(add1 > add2, mult10 * i4, mult10 * i3)
    add5 = If(add1 > add2, i10 * mult14, i10 / mult14)

    add6 = mult1 + add1
    out1 = add6

    add7 = mult3 + add2
    add8 = mult5 + add7

    add10 = mult7 + add3
    add9 = mult6 + add10

    # shf1 = add9 << 3
    shf1 = add9 * 8
    out2 = add8 + shf1

    add13 = mult9 + add4
    add11 = add13 + mult11

    add15 = mult13 + add5
    add14 = mult12 + add15

    # shf2 = add14 >> key_4
    shf2 = add14 / key_4
    out3 = add11 + shf2

    o = my_tuple.tuple(out1, out2, out3)
    return o

prune_key_set = False
j = 0
gg = Tactic('smt').solver()
ia = str(1) + " " + str(2) + " " + str(3) + " " + str(4) + " " + str(5) + " " + str(6) + " " + str(7) + " " + str(
    8) + " " + str(9) + " " + str(10)
out = Cexec(ia)
out_tup = my_tuple.tuple(out[0], out[1], out[2])
print(gg.check(motion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 12, 6, 3) == out_tup))

s = Tactic('smt').solver()
s.add(motion(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, key1_1, key2_1, key3_1, key4_1) == out1)
s.add(motion(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, key1_2, key2_2, key3_2, key4_2))

while s.check(out1 != out2) == sat:
    m = s.model()
    ia = str(m[i1]) + " " + str(m[i2]) + " " + str(m[i3]) + " " + str(m[i4]) + " " + str(m[i5]) + " " + str(m[i6]) + " " + str(m[i7]) + " " + str(m[i8]) + " " + str(m[i9]) + " " + str(m[i10])
    print(ia)
    out = Cexec(ia)
    print(out)
    i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9, i_10 = Ints('i_1 i_2 i_3 i_4 i_5 i_6 i_7 i_8 i_9 i_10')
    i_1 = m[i1]
    i_2 = m[i2]
    i_3 = m[i3]
    i_4 = m[i4]
    i_5 = m[i5]
    i_6 = m[i6]
    i_7 = m[i7]
    i_8 = m[i8]
    i_9 = m[i9]
    i_10 = m[i10]

    out_tup = my_tuple.tuple(out[0], out[1], out[2])
    s.add((motion(i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9, i_10, key1_1, key2_1, key3_1, key4_1) == out_tup))
    s.add((motion(i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9, i_10, key1_2, key2_2, key3_2, key4_2) == out_tup))

print(s.check(out1 == out2))
print(s.model())
