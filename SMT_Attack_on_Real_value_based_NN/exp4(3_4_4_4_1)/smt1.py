from z3 import *
import subprocess
import time
# set_option(rational_to_decimal=True)
# set_option(precision=5)
def Cexec(init_string):
    result = []
    fractions = init_string.split()
    
    for fraction in fractions:
        if '/' in fraction:
            numerator, denominator = map(int, fraction.split('/'))
            decimal = numerator / denominator
            result.append('{:.11f}'.format(decimal))
        else:
            result.append(fraction)
    out = subprocess.check_output("./a.out %s" % ' '.join(result), shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3 = Reals('in1 in2 in3')
l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4 = Reals('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4')
l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4 = Reals('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4')
l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4 = Reals('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4')
l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4 = Reals('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4')
l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4 = Reals('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4')
l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4 = Reals('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4')
ov1_1,ov1_2,ov1_3,ov1_4 = Reals('ov1_1 ov1_2 ov1_3 ov1_4')
ov2_1,ov2_2,ov2_3,ov2_4 = Reals('ov2_1 ov2_2 ov2_3 ov2_4')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',RealSort()),('2',RealSort()),('3',RealSort()),('4',RealSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3,ov1_4)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3,ov2_4)

def NN(in1,in2,in3,l1n1_1,l1n1_2,l1n1_3,l1n1_4,l1n2_1,l1n2_2,l1n2_3,l1n2_4,l1n3_1,l1n3_2,l1n3_3,l1n3_4):
	l2out_1,l2out_2,l2out_3,l2out_4 = Reals('l2out_1 l2out_2 l2out_3 l2out_4')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + (in3 * l1n3_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * l1n1_2) + (in2 * l1n2_2) + (in3 * l1n3_2) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * l1n1_3) + (in2 * l1n2_3) + (in3 * l1n3_3) 
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	l2out_4 = (in1 * l1n1_4) + (in2 * l1n2_4) + (in3 * l1n3_4) 
	l2out_4 = If(l2out_4 < 0, 0, l2out_4)
	
	out = tuple.tuple(l2out_1,l2out_2,l2out_3,l2out_4)
	
	return out

s = Tactic('smt').solver()





s.add(NN(in1,in2,in3,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4) == out1)
s.add(NN(in1,in2,in3,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3])
	print(ia)
	out = Cexec(ia)
	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]
	# print(m[ov1_1] , m[ov1_2] , m[ov1_3] , m[ov])
	out_tup = tuple.tuple(out[0],out[1],out[2],out[3])

	s.add(NN(inp1,inp2,inp3,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4) == out_tup)
	s.add(NN(inp1,inp2,inp3,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))