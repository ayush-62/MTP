from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2 = Ints('in1 in2')
l1n1v1_1,l1n1v1_2,l1n1v1_3 = Ints('l1n1v1_1 l1n1v1_2 l1n1v1_3')
l1n2v1_1,l1n2v1_2,l1n2v1_3 = Ints('l1n2v1_1 l1n2v1_2 l1n2v1_3')
l1n1v2_1,l1n1v2_2,l1n1v2_3 = Ints('l1n1v2_1 l1n1v2_2 l1n1v2_3')
l1n2v2_1,l1n2v2_2,l1n2v2_3 = Ints('l1n2v2_1 l1n2v2_2 l1n2v2_3')

l1bv1_1,l1bv1_2,l1bv1_3 = Ints('l1bv1_1 l1bv1_2 l1bv1_3')
l1bv2_1,l1bv2_2,l1bv2_3 = Ints('l1bv2_1 l1bv2_2 l1bv2_3')

ov1_1,ov1_2,ov1_3 = Ints('ov1_1 ov1_2 ov1_3')
ov2_1,ov2_2,ov2_3 = Ints('ov2_1 ov2_2 ov2_3')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()),('2',IntSort()),('3',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3)

def NN(in1,in2,l1n1_1,l1n1_2,l1n1_3,l1n2_1,l1n2_2,l1n2_3,l1b1,l1b2,l1b3):
	l2out_1,l2out_2,l2out_3 = Ints('l2out_1 l2out_2 l2out_3')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + l1b1
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * l1n1_2) + (in2 * l1n2_2) + l1b2
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * l1n1_3) + (in2 * l1n2_3) + l1b3
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	
	out = tuple.tuple(l2out_1,l2out_2,l2out_3)
	
	return out

s = Tactic('smt').solver()

s.add(input[0] >= 0 , input[0] <= 255)
s.add(input[1] >= 0 , input[1] <= 255)
s.add(l1n1v1[0]>=0 , l1n1v1[0] <= 255)
s.add(l1n1v1[1]>=0 , l1n1v1[1] <= 255)
s.add(l1n1v1[2]>=0 , l1n1v1[2] <= 255)
s.add(l1n2v1[0]>=0 , l1n2v1[0] <= 255)
s.add(l1n2v1[1]>=0 , l1n2v1[1] <= 255)
s.add(l1n2v1[2]>=0 , l1n2v1[2] <= 255)

s.add(l1n1v2[0]>=0 , l1n1v2[0] <= 255)
s.add(l1n1v2[1]>=0 , l1n1v2[1] <= 255)
s.add(l1n1v2[2]>=0 , l1n1v2[2] <= 255)
s.add(l1n2v2[0]>=0 , l1n2v2[0] <= 255)
s.add(l1n2v2[1]>=0 , l1n2v2[1] <= 255)
s.add(l1n2v2[2]>=0 , l1n2v2[2] <= 255)
s.add(NN(in1,in2,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1bv1_1,l1bv1_2,l1bv1_3 ) == out1)
s.add(NN(in1,in2,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1bv2_1,l1bv2_2,l1bv2_3) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]

	out_tup = tuple.tuple(out[0],out[1],out[2])

	s.add(NN(inp1,inp2,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1bv1_1,l1bv1_2,l1bv1_3 ) == out_tup)
	s.add(NN(inp1,inp2,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1bv2_1,l1bv2_2,l1bv2_3) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))