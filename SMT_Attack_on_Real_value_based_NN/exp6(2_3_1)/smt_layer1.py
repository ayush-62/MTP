from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(int, out.decode('utf-8').split()))

set_option(rational_to_decimal=True)
set_option(precision=5)


# def print_details(model):
#     print("Model: [")
#     print("  Input : [" + str(model[input[0]].as_long()) + ", " + str(model[input[1]].as_long()) + "]")
#     print("  L1Wv1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n1v1[1]].as_long()) + ", " + str(model[l1n1v1[2]].as_long()) + "], [" + str(model[l1n2v1[0]].as_long()) + ", " + str(model[l1n2v1[1]].as_long()) + ", " + str(model[l1n2v1[2]].as_long()) +  "] ]")
#     print("  L2Wv1: [ [" + str(model[l2n1v1[0]].as_long()) + "], [" + str(model[l2n2v1[0]].as_long()) + "],[" + str(model[l2n3v1[0]].as_long()) + " ]")
#     print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
#     print()
#     print("  L1Wv2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n1v2[1]].as_long()) + ", " + str(model[l1n1v2[2]].as_long()) + "], [" + str(model[l1n2v2[0]].as_long()) + ", " + str(model[l1n2v2[1]].as_long()) + ", " + str(model[l1n2v2[2]].as_long()) +  "] ]")
#     print("  L2Wv2: [ [" + str(model[l2n1v2[0]].as_long()) + "], [" + str(model[l2n2v2[0]].as_long()) + "],[" + str(model[l2n3v2[0]].as_long()) + "] ]")
#     print("  Output2: [" + str(model[output2[0]].as_long()) + "]")
#     print("]")

start_time = time.time()

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 3)
l1n2v1 = IntVector('layer1node2v1', 3)
l2n1v1 = IntVector('layer2node1v1', 1)
l2n2v1 = IntVector('layer2node2v1', 1)
l2n3v1 = IntVector('layer2node3v1', 1)

l1n1v2 = IntVector('layer1node1v2', 3)
l1n2v2 = IntVector('layer1node2v2', 3)
l2n1v2 = IntVector('layer2node1v2', 1)
l2n2v2 = IntVector('layer2node2v2', 1)
l2n3v2 = IntVector('layer2node3v2', 1)

l1bv1 = Ints('l1b1v1 , l1b2v1 , l1b3v1')
l1bv2 = Ints('l1b1v1 , l1b2v1 , l1b3v1')


output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)

ov1_1,ov1_2,ov1_3 = Ints('ov1_1 ov1_2 ov1_3')
ov2_1,ov2_2,ov2_3 = Ints('ov2_1 ov2_2 ov2_3')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()),('2',IntSort()),('3',IntSort()))
tuple = tuple.create()

out1 = tuple.tuple(ov1_1,ov1_2,ov1_3)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3)

q_w1 = 1559941072
shift_w1 = 9

q_b1 = 1529762159
shift_b1 = 2

zp_i = [0,0]
zp_w = [78 , 89]
zp_b = [124 , 1]



def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, l2n3 , l1b):
    
    updated_l1n1 = []
    updated_l1n1.append((q_w1*(l1n1[0] - zp_w[0]))/(2**(shift_w1+31)))
    updated_l1n1.append((q_w1*(l1n1[1] - zp_w[0]))/(2**(shift_w1+31)))
    updated_l1n1.append((q_w1*(l1n1[2] - zp_w[0]))/(2**(shift_w1+31)))

    updated_l1n2 = []
    updated_l1n2.append((q_w1*(l1n2[0] - zp_w[0]))/(2**(shift_w1+31)))
    updated_l1n2.append((q_w1*(l1n2[1] - zp_w[0]))/(2**(shift_w1+31)))
    updated_l1n2.append((q_w1*(l1n2[2] - zp_w[0]))/(2**(shift_w1+31)))

    updated_bias = []
    updated_bias.append((q_w1*(l1b[0] - zp_b[0]))/(2**(shift_b1+31)))
    updated_bias.append((q_w1*(l1b[1] - zp_b[0]))/(2**(shift_b1+31)))
    updated_bias.append((q_w1*(l1b[2] - zp_b[0]))/(2**(shift_b1+31)))

    updated_input = []
    updated_input.append(input[0] - zp_i[0])
    updated_input.append(input[1] - zp_i[0])
    

    output = IntVector('hiddenNodeValues', 3)
    output[0] = (updated_input[0] * updated_l1n1[0]) + (updated_input[1] * updated_l1n2[0]) + updated_bias[0]
    output[0] = If(output[0] < 0, 0, output[0]) 
    
    output[1] = (updated_input[0] * updated_l1n1[1]) + (updated_input[1] * updated_l1n2[1]) + updated_bias[1]
    output[1] = If(output[1] < 0, 0, output[1]) 

    output[2] = (updated_input[0] * updated_l1n1[2]) + (updated_input[1] * updated_l1n2[2]) + updated_bias[2]
    output[2] = If(output[2] < 0, 0, output[2]) 

    # outputValues = IntVector('outputValues', 1)
    # outputValues[0] = (output[0] * l2n1[0]) + (output[1] * l2n2[0]) + (output[2] * l2n3[0])

    out = tuple.tuple(output[0],output[1],output[2])
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

s.add(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1 , l1bv1) == out1)
s.add(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2 , l1bv2) == out2)

while s.check(out1 != out2) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    out = Cexec(ia)
    out_tup = tuple.tuple(out[0],out[1],out[2])
    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1 , l1bv1) == out_tup)
    s.add(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2 , l1bv2) == out_tup)

print(s.check(output1[0] == output2[0]))
print(s.model())
print("Finished in " + str(time.time() - start_time))
