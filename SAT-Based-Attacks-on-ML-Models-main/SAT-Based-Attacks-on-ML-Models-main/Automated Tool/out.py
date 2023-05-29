from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2 = Ints('in1 in2')
l1n1v1_1 = Int('l1n1v1_1')
l1n2v1_1 = Int('l1n2v1_1')
l1n1v2_1 = Int('l1n1v2_1')
l1n2v2_1 = Int('l1n2v2_1')
ov1_1 = Int('ov1_1')
ov2_1 = Int('ov2_1')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1)
out2 = tuple.tuple(ov2_1)

def NN(in1,in2,l1n1_1,l1n2_1):
	l2out_1 = Int('l2out_1')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	
	out = tuple.tuple(l2out_1)
	
	return out

s = Tactic('smt').solver()

s.add(l2n1v1_1 > -10, l2n1v1_1 < 10)
s.add(l2n1v2_1 > -10, l2n1v2_1 < 10)
s.add(l2n1v1_2 > -10, l2n1v1_2 < 10)
s.add(l2n1v2_2 > -10, l2n1v2_2 < 10)
s.add(l2n1v1_3 > -10, l2n1v1_3 < 10)
s.add(l2n1v2_3 > -10, l2n1v2_3 < 10)
s.add(l2n2v1_1 > -10, l2n2v1_1 < 10)
s.add(l2n2v2_1 > -10, l2n2v2_1 < 10)
s.add(l2n2v1_2 > -10, l2n2v1_2 < 10)
s.add(l2n2v2_2 > -10, l2n2v2_2 < 10)
s.add(l2n2v1_3 > -10, l2n2v1_3 < 10)
s.add(l2n2v2_3 > -10, l2n2v2_3 < 10)
s.add(l2n3v1_1 > -10, l2n3v1_1 < 10)
s.add(l2n3v2_1 > -10, l2n3v2_1 < 10)
s.add(l2n3v1_2 > -10, l2n3v1_2 < 10)
s.add(l2n3v2_2 > -10, l2n3v2_2 < 10)
s.add(l2n3v1_3 > -10, l2n3v1_3 < 10)
s.add(l2n3v2_3 > -10, l2n3v2_3 < 10)

s.add(NN(in1,in2,l1n1v1_1,l1n2v1_1) == out1)
s.add(NN(in1,in2,l1n1v2_1,l1n2v2_1) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]

	out_tup = tuple.tuple(out[0])

	s.add(NN(inp1,inp2,l1n1v1_1,l1n2v1_1) == out_tup)
	s.add(NN(inp1,inp2,l1n1v2_1,l1n2v2_1) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))
