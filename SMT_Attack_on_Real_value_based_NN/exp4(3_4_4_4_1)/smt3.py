from z3 import *
import subprocess
import time

set_option(rational_to_decimal=True)
set_option(precision=15)

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3 = Reals('in1 in2 in3')
# l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4 = Reals('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4')
# l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4 = Reals('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4')
# l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4 = Reals('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4')
# l2n1v1_1,l2n1v1_2,l2n1v1_3,l2n1v1_4 = Reals('l2n1v1_1 l2n1v1_2 l2n1v1_3 l2n1v1_4')
# l2n2v1_1,l2n2v1_2,l2n2v1_3,l2n2v1_4 = Reals('l2n2v1_1 l2n2v1_2 l2n2v1_3 l2n2v1_4')
# l2n3v1_1,l2n3v1_2,l2n3v1_3,l2n3v1_4 = Reals('l2n3v1_1 l2n3v1_2 l2n3v1_3 l2n3v1_4')
# l2n4v1_1,l2n4v1_2,l2n4v1_3,l2n4v1_4 = Reals('l2n4v1_1 l2n4v1_2 l2n4v1_3 l2n4v1_4')
l3n1v1_1,l3n1v1_2,l3n1v1_3,l3n1v1_4 = Reals('l3n1v1_1 l3n1v1_2 l3n1v1_3 l3n1v1_4')
l3n2v1_1,l3n2v1_2,l3n2v1_3,l3n2v1_4 = Reals('l3n2v1_1 l3n2v1_2 l3n2v1_3 l3n2v1_4')
l3n3v1_1,l3n3v1_2,l3n3v1_3,l3n3v1_4 = Reals('l3n3v1_1 l3n3v1_2 l3n3v1_3 l3n3v1_4')
l3n4v1_1,l3n4v1_2,l3n4v1_3,l3n4v1_4 = Reals('l3n4v1_1 l3n4v1_2 l3n4v1_3 l3n4v1_4')
# l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4 = Reals('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4')
# l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4 = Reals('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4')
# l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4 = Reals('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4')
# l2n1v2_1,l2n1v2_2,l2n1v2_3,l2n1v2_4 = Reals('l2n1v2_1 l2n1v2_2 l2n1v2_3 l2n1v2_4')
# l2n2v2_1,l2n2v2_2,l2n2v2_3,l2n2v2_4 = Reals('l2n2v2_1 l2n2v2_2 l2n2v2_3 l2n2v2_4')
# l2n3v2_1,l2n3v2_2,l2n3v2_3,l2n3v2_4 = Reals('l2n3v2_1 l2n3v2_2 l2n3v2_3 l2n3v2_4')
# l2n4v2_1,l2n4v2_2,l2n4v2_3,l2n4v2_4 = Reals('l2n4v2_1 l2n4v2_2 l2n4v2_3 l2n4v2_4')
l3n1v2_1,l3n1v2_2,l3n1v2_3,l3n1v2_4 = Reals('l3n1v2_1 l3n1v2_2 l3n1v2_3 l3n1v2_4')
l3n2v2_1,l3n2v2_2,l3n2v2_3,l3n2v2_4 = Reals('l3n2v2_1 l3n2v2_2 l3n2v2_3 l3n2v2_4')
l3n3v2_1,l3n3v2_2,l3n3v2_3,l3n3v2_4 = Reals('l3n3v2_1 l3n3v2_2 l3n3v2_3 l3n3v2_4')
l3n4v2_1,l3n4v2_2,l3n4v2_3,l3n4v2_4 = Reals('l3n4v2_1 l3n4v2_2 l3n4v2_3 l3n4v2_4')
ov1_1,ov1_2,ov1_3,ov1_4 = Reals('ov1_1 ov1_2 ov1_3 ov1_4')
ov2_1,ov2_2,ov2_3,ov2_4 = Reals('ov2_1 ov2_2 ov2_3 ov2_4')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',RealSort()),('2',RealSort()),('3',RealSort()),('4',RealSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3,ov1_4)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3,ov2_4)

def NN(in1,in2,in3,l3n1_1,l3n1_2,l3n1_3,l3n1_4,l3n2_1,l3n2_2,l3n2_3,l3n2_4,l3n3_1,l3n3_2,l3n3_3,l3n3_4,l3n4_1,l3n4_2,l3n4_3,l3n4_4):
	l2out_1,l2out_2,l2out_3,l2out_4 = Reals('l2out_1 l2out_2 l2out_3 l2out_4')
	l2out_1 = (in1 * -6.6) + (in2 * 8.5) + (in3 * 4.0) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * 10.3) + (in2 * -7.0) + (in3 * 7.9) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * 5.0) + (in2 * 1.2) + (in3 * -3.7) 
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	l2out_4 = (in1 * 1.2) + (in2 * -1.0) + (in3 * -2.0) 
	l2out_4 = If(l2out_4 < 0, 0, l2out_4)
	
	l3out_1,l3out_2,l3out_3,l3out_4 = Reals('l3out_1 l3out_2 l3out_3 l3out_4')
	l3out_1 = (l2out_1 * -3.5) + (l2out_2 * 6.6) + (l2out_3 * 3.5) + (l2out_4 * 3.6) 
	l3out_1 = If(l3out_1 < 0, 0, l3out_1)
	l3out_2 = (l2out_1 * 4.0) + (l2out_2 * -7.0) + (l2out_3 * -3.8) + (l2out_4 * -3.0) 
	l3out_2 = If(l3out_2 < 0, 0, l3out_2)
	l3out_3 = (l2out_1 * 5.0) + (l2out_2 * 1.0) + (l2out_3 * -3.8) + (l2out_4 * -3.7) 
	l3out_3 = If(l3out_3 < 0, 0, l3out_3)
	l3out_4 = (l2out_1 * 9.7) + (l2out_2 * 4.0) + (l2out_3 * -3.0) + (l2out_4 * -3.9) 
	l3out_4 = If(l3out_4 < 0, 0, l3out_4)
	
	l4out_1,l4out_2,l4out_3,l4out_4 = Reals('l4out_1 l4out_2 l4out_3 l4out_4')
	l4out_1 = (l3out_1 * l3n1_1) + (l3out_2 * l3n2_1) + (l3out_3 * l3n3_1) + (l3out_4 * l3n4_1) 
	l4out_1 = If(l4out_1 < 0, 0, l4out_1)
	l4out_2 = (l3out_1 * l3n1_2) + (l3out_2 * l3n2_2) + (l3out_3 * l3n3_2) + (l3out_4 * l3n4_2) 
	l4out_2 = If(l4out_2 < 0, 0, l4out_2)
	l4out_3 = (l3out_1 * l3n1_3) + (l3out_2 * l3n2_3) + (l3out_3 * l3n3_3) + (l3out_4 * l3n4_3) 
	l4out_3 = If(l4out_3 < 0, 0, l4out_3)
	l4out_4 = (l3out_1 * l3n1_4) + (l3out_2 * l3n2_4) + (l3out_3 * l3n3_4) + (l3out_4 * l3n4_4) 
	l4out_4 = If(l4out_4 < 0, 0, l4out_4)
	
	out = tuple.tuple(l4out_1,l4out_2,l4out_3,l4out_4)
	
	return out

s = Tactic('smt').solver()


# s.add(l3n1v1_1 == -3.8)
# s.add(l3n2v1_1 == 6.3)
# s.add(l3n3v1_1 == 3.4)
# s.add(l3n4v1_1 == 3.0)
# s.add(l3n1v1_2 == 4.6)
# s.add(l3n2v1_2 == -7.6)

# s.add(l3n1v2_1 == -3.8)
# s.add(l3n2v2_1 == 6.3)
# s.add(l3n3v2_1 == 3.4)
# s.add(l3n4v2_1 == 3.0)
# s.add(l3n1v2_2 == 4.6)
# s.add(l3n2v2_2 == -7.6)

s.add(NN(in1,in2,in3,l3n1v1_1,l3n1v1_2,l3n1v1_3,l3n1v1_4,l3n2v1_1,l3n2v1_2,l3n2v1_3,l3n2v1_4,l3n3v1_1,l3n3v1_2,l3n3v1_3,l3n3v1_4,l3n4v1_1,l3n4v1_2,l3n4v1_3,l3n4v1_4) == out1)
s.add(NN(in1,in2,in3,l3n1v2_1,l3n1v2_2,l3n1v2_3,l3n1v2_4,l3n2v2_1,l3n2v2_2,l3n2v2_3,l3n2v2_4,l3n3v2_1,l3n3v2_2,l3n3v2_3,l3n3v2_4,l3n4v2_1,l3n4v2_2,l3n4v2_3,l3n4v2_4) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(time.time() - start_time)
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]

	out_tup = tuple.tuple(out[0],out[1],out[2],out[3])

	s.add(NN(inp1,inp2,inp3,l3n1v1_1,l3n1v1_2,l3n1v1_3,l3n1v1_4,l3n2v1_1,l3n2v1_2,l3n2v1_3,l3n2v1_4,l3n3v1_1,l3n3v1_2,l3n3v1_3,l3n3v1_4,l3n4v1_1,l3n4v1_2,l3n4v1_3,l3n4v1_4) == out_tup)
	s.add(NN(inp1,inp2,inp3,l3n1v2_1,l3n1v2_2,l3n1v2_3,l3n1v2_4,l3n2v2_1,l3n2v2_2,l3n2v2_3,l3n2v2_4,l3n3v2_1,l3n3v2_2,l3n3v2_3,l3n3v2_4,l3n4v2_1,l3n4v2_2,l3n4v2_3,l3n4v2_4) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))
