from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3 = Ints('in1 in2 in3')
# l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4 = Ints('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4')
# l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4 = Ints('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4')
# l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4 = Ints('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4')
# l2n1v1_1,l2n1v1_2,l2n1v1_3,l2n1v1_4 = Ints('l2n1v1_1 l2n1v1_2 l2n1v1_3 l2n1v1_4')
# l2n2v1_1,l2n2v1_2,l2n2v1_3,l2n2v1_4 = Ints('l2n2v1_1 l2n2v1_2 l2n2v1_3 l2n2v1_4')
# l2n3v1_1,l2n3v1_2,l2n3v1_3,l2n3v1_4 = Ints('l2n3v1_1 l2n3v1_2 l2n3v1_3 l2n3v1_4')
# l2n4v1_1,l2n4v1_2,l2n4v1_3,l2n4v1_4 = Ints('l2n4v1_1 l2n4v1_2 l2n4v1_3 l2n4v1_4')
l3n1v1_1 = Int('l3n1v1_1')
l3n2v1_1 = Int('l3n2v1_1')
l3n3v1_1 = Int('l3n3v1_1')
l3n4v1_1 = Int('l3n4v1_1')
# l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4 = Ints('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4')
# l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4 = Ints('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4')
# l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4 = Ints('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4')
# l2n1v2_1,l2n1v2_2,l2n1v2_3,l2n1v2_4 = Ints('l2n1v2_1 l2n1v2_2 l2n1v2_3 l2n1v2_4')
# l2n2v2_1,l2n2v2_2,l2n2v2_3,l2n2v2_4 = Ints('l2n2v2_1 l2n2v2_2 l2n2v2_3 l2n2v2_4')
# l2n3v2_1,l2n3v2_2,l2n3v2_3,l2n3v2_4 = Ints('l2n3v2_1 l2n3v2_2 l2n3v2_3 l2n3v2_4')
# l2n4v2_1,l2n4v2_2,l2n4v2_3,l2n4v2_4 = Ints('l2n4v2_1 l2n4v2_2 l2n4v2_3 l2n4v2_4')
l3n1v2_1 = Int('l3n1v2_1')
l3n2v2_1 = Int('l3n2v2_1')
l3n3v2_1 = Int('l3n3v2_1')
l3n4v2_1 = Int('l3n4v2_1')
ov1_1 = Ints('ov1_1')
ov2_1 = Ints('ov2_1')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1)
out2 = tuple.tuple(ov2_1)

def NN(in1,in2,in3,l3n1_1,l3n2_1,l3n3_1,l3n4_1):
	l2out_1,l2out_2,l2out_3,l2out_4 = Ints('l2out_1 l2out_2 l2out_3 l2out_4')
	l2out_1 = (in1 * -60) + (in2 * 800) + (in3 * 400) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * 1060) + (in2 * -700) + (in3 * 700) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * 500) + (in2 * 100) + (in3 * -350) 
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	l2out_4 = (in1 * 120) + (in2 * -100) + (in3 * -200) 
	l2out_4 = If(l2out_4 < 0, 0, l2out_4)
	
	l3out_1,l3out_2,l3out_3,l3out_4 = Ints('l3out_1 l3out_2 l3out_3 l3out_4')
	l3out_1 = (l2out_1 * -300) + (l2out_2 * 600) + (l2out_3 * 300) + (l2out_4 * 300) 
	l3out_1 = If(l3out_1 < 0, 0, l3out_1)
	l3out_2 = (l2out_1 * 440) + (l2out_2 * -760) + (l2out_3 * -300) + (l2out_4 * -300) 
	l3out_2 = If(l3out_2 < 0, 0, l3out_2)
	l3out_3 = (l2out_1 * 500) + (l2out_2 * 100) + (l2out_3 * -300) + (l2out_4 * -300) 
	l3out_3 = If(l3out_3 < 0, 0, l3out_3)
	l3out_4 = (l2out_1 * 900) + (l2out_2 * 400) + (l2out_3 * -380) + (l2out_4 * -300) 
	l3out_4 = If(l3out_4 < 0, 0, l3out_4)
	
	l4out_1 = Int('l4out_1')
	l4out_1 = (l3out_1 * l3n1_1) + (l3out_2 * l3n2_1) + (l3out_3 * l3n3_1) + (l3out_4 * l3n4_1) 
	l4out_1 = If(l4out_1 < 0, 0, l4out_1)
	
	out = tuple.tuple(l4out_1)
	
	return out

s = Tactic('smt').solver()


s.add(NN(in1,in2,in3,l3n1v1_1,l3n2v1_1,l3n3v1_1,l3n4v1_1) == out1)
s.add(NN(in1,in2,in3,l3n1v2_1,l3n2v2_1,l3n3v2_1,l3n4v2_1) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]

	out_tup = tuple.tuple(out[8])

	s.add(NN(inp1,inp2,inp3,l3n1v1_1,l3n2v1_1,l3n3v1_1,l3n4v1_1) == out_tup)
	s.add(NN(inp1,inp2,inp3,l3n1v2_1,l3n2v2_1,l3n3v2_1,l3n4v2_1) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))
