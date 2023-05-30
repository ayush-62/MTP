from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(int, out.decode('utf-8').split()))

# set_option(rational_to_decimal=True)
# set_option(precision=5)


# def print_details(model):
#     print("Model: [")
#     print("  Input : [" + str(model[input[0]].as_long()) + ", " + str(model[input[1]].as_long()) + "]")
#     print("  L1Wv1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n1v1[1]].as_long()) + ", " + str(model[l1n1v1[2]].as_long()) + "], [" + str(model[l1n2v1[0]].as_long()) + ", " + str(model[l1n2v1[1]].as_long()) + ", " + str(model[l1n2v1[2]].as_long()) +  "] ]")
#     print("  L2Wv1: [ [" + str(model[l2n1v1[0]].as_long()) + "], [" + str(model[l2n2v1[0]].as_long()) + "],[" + str(model[l2n3v1[0]].as_long()) + " ]")
#     print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
#     print()
#     print("  L1Wv2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n1v2[1]].as_long()) + ", " + str(model[l1n1v2[2]].as_long()) + "], [" + str(model[l1n2v2[0]].as_long()) + ", " + str(model[l1n2v2[1]].as_long()) + ", " + str(model[l1n2v2[2]].as_long()) +  "] ]")
#     print("  L2Wv2: [ [" + str(model[l2n1v2[0]].as_long()) + "], [" + str(model[l2n2v2[0]].as_long()) + "],[" + str(model[l2n3v2[0]].as_long()) + "] ]")
#     print("  Output2: [" + str(model[output2[0]].as_long()) + "]")BitVec
#     print("]")

start_time = time.time()

input_1 = BitVec('inp1', 32)
input_2 = BitVec('inp2', 32)
l1n1v1_1 = BitVec('layer1node1v1_1', 32)
l1n1v1_2 = BitVec('layer1node1v1_2', 32)
l1n1v1_3 = BitVec('layer1node1v1_3', 32)

l1n2v1_1 = BitVec('layer1node2v1_1', 32)
l1n2v1_2 = BitVec('layer1node2v1_2', 32)
l1n2v1_3 = BitVec('layer1node2v1_3', 32)

l1n1v2_1 = BitVec('layer1node1v2_1', 32)
l1n1v2_2 = BitVec('layer1node1v2_2', 32)
l1n1v2_3 = BitVec('layer1node1v2_3', 32)

l1n2v2_1 = BitVec('layer1node2v2_1', 32)
l1n2v2_2 = BitVec('layer1node2v2_2', 32)
l1n2v2_3 = BitVec('layer1node2v2_3', 32)


l1bv1_1 = BitVec('layer1bias1v1', 32)
l1bv1_2 = BitVec('layer1bial2v1', 32)
l1bv1_3 = BitVec('layer1node3v1', 32)

l1bv2_1 = BitVec('layer1bias1v2', 32)
l1bv2_2 = BitVec('layer1bial2v2', 32)
l1bv2_3 = BitVec('layer1node3v2', 32)


output1 = BitVec('out1', 32)
output2 = BitVec('out2', 32)

ov1_1,ov1_2,ov1_3 = BitVecs('ov1_1 ov1_2 ov1_3',32)
ov2_1,ov2_2,ov2_3 = BitVecs('ov2_1 ov2_2 ov2_3',32)

tuple = Datatype('tuple')
tuple.declare('tuple',('1',BitVecSort(32)),('2',BitVecSort(32)),('3',BitVecSort(32)))
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



def neuralNetwork(input_1 , input_2 , l1n1_1 , l1n1_2 , l1n1_3 , l1n2_1 , l1n2_2 , l1n2_3 , l1b1 , l1b2 , l1b3):
    
    updated_l1n1_1 = ((BitVecVal(q_w1,32)*(l1n1_1 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_l1n1_2 = ((BitVecVal(q_w1,32)*(l1n1_2 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_l1n1_3 = ((BitVecVal(q_w1,32)*(l1n1_3 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_l1n2_1 = ((BitVecVal(q_w1,32)*(l1n2_1 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_l1n2_2 = ((BitVecVal(q_w1,32)*(l1n2_2 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_l1n2_3 = ((BitVecVal(q_w1,32)*(l1n2_3 - BitVecVal(zp_w[0],32)))>>(BitVecVal(shift_w1,32)+BitVecVal(31,32)))
    updated_bias_1 = ((BitVecVal(q_b1,32)*(l1b1 - BitVecVal(zp_b[0],32)))>>(BitVecVal(shift_b1,32)+BitVecVal(31,32)))
    updated_bias_2 = ((BitVecVal(q_b1,32)*(l1b2 - BitVecVal(zp_b[0],32)))>>(BitVecVal(shift_b1,32)+BitVecVal(31,32)))
    updated_bias_3 = ((BitVecVal(q_b1,32)*(l1b3 - BitVecVal(zp_b[0],32)))>>(BitVecVal(shift_b1,32)+BitVecVal(31,32)))

    updated_input_1 = (input_1 - BitVecVal(zp_i[0],32))
    updated_input_2 = (input_2 - BitVecVal(zp_i[0],32))
    

    output_1 = BitVec('hiddenNodeValues1',32)
    output_2 = BitVec('hiddenNodeValues2',32)
    output_3 = BitVec('hiddenNodeValues3',32)

    output_1 = (updated_input_1 * updated_l1n1_1) + (updated_input_2 * updated_l1n2_1) + updated_bias_1 
    output_1 = If(output_1 < 0, 0, output_1)
    output_1 = output1 - BitVecVal(zp_i[1],32)
    output_1 = output_1 & BitVecVal(255 , 32)
    
    output_2 = (updated_input_1 * updated_l1n1_2) + (updated_input_2 * updated_l1n2_2) + updated_bias_2
    output_2 = If(output_2 < 0, 0, output_2)
    output_2 = output2 - BitVecVal(zp_i[1],32)
    output_2 = output_2 & BitVecVal(255 , 32)

    output_3 = (updated_input_1 * updated_l1n1_3) + (updated_input_2 * updated_l1n2_3) + updated_bias_3
    output_3 = If(output_3 < 0, 0, output_3)
    output_3 = output_3 - BitVecVal(zp_i[1],32)
    output_3 = output_3 & BitVecVal(255 , 32)

    # outputValues = BitVec('outputValues', 1)
    # outputValues[0] = (output[0] * l2n1[0]) + (output[1] * l2n2[0]) + (output[2] * l2n3[0])


    out = tuple.tuple(output_1,output_1,output_1)
    return out

gg=Tactic('smt').solver()
ia = str(1) + " " + str(2)
out = Cexec(ia)
out_tup = tuple.tuple(out[0],out[1],out[2])

print(gg.check(neuralNetwork(1 , 2 , 0.3572 , 3.0436 , -1.606 , -0.3158 , 3.5808 , -0.6303 ,  -0.1541 , -2.2765 , 2.3786) == out_tup))

s = Tactic('smt').solver()

s.add(input_1 >= 0 , input_1 <= 255)
s.add(input_2 >= 0 , input_2 <= 255)

s.add(l1n1v1_1>=0 , l1n1v1_1 <= 255)
s.add(l1n1v1_2>=0 , l1n1v1_2 <= 255)
s.add(l1n1v1_3>=0 , l1n1v1_3 <= 255)
s.add(l1n2v1_1>=0 , l1n2v1_1 <= 255)
s.add(l1n2v1_2>=0 , l1n2v1_2 <= 255)
s.add(l1n2v1_3>=0 , l1n2v1_3 <= 255)

s.add(l1n1v2_1>=0 , l1n1v2_1 <= 255)
s.add(l1n1v2_2>=0 , l1n1v2_2 <= 255)
s.add(l1n1v2_3>=0 , l1n1v2_3 <= 255)
s.add(l1n2v2_1>=0 , l1n2v2_1 <= 255)
s.add(l1n2v2_2>=0 , l1n2v2_2 <= 255)
s.add(l1n2v2_3>=0 , l1n2v2_3 <= 255)

s.add(neuralNetwork(input_1 , input_2 , l1n1v1_1 , l1n1v1_2 , l1n1v1_3 , l1n2v1_1 , l1n2v1_2 , l1n2v1_3 , l1bv1_1 , l1bv1_2 , l1bv1_3) == out1)
s.add(neuralNetwork(input_1 , input_2 , l1n1v2_1 , l1n1v2_2 , l1n1v2_3 , l1n2v2_1 , l1n2v2_2 , l1n2v2_3 , l1bv2_1 , l1bv2_2 , l1bv2_3) == out2)

while s.check(out1 != out2) == sat:
    m = s.model()
    ia = str(m[input_1]) + " " + str(m[input_2]) + " " + str(time.time() - start_time)
    print(ia)
    out = Cexec(ia)
    print(out)
    out_tup = tuple.tuple(out[0],out[1],out[2])
    inp1 , inp2 = BitVecs('inp1 inp2', 32)
    inp1 = m[input_1]
    inp2 = m[input_2]

    s.add(neuralNetwork(inp1 , inp2 , l1n1v1_1 , l1n1v1_2 , l1n1v1_3 , l1n2v1_1 , l1n2v1_2 , l1n2v1_3 ,  l1bv1_1 , l1bv1_2 , l1bv1_3) == out_tup)
    s.add(neuralNetwork(inp1,  inp2 , l1n1v2_1 , l1n1v2_2 , l1n1v2_3 , l1n2v2_1 , l1n2v2_2 , l1n2v2_3 , l1bv2_1 , l1bv2_2 , l1bv2_3) == out_tup)

print(s.check(out1 == out2))
print(s.model())
print("Finished in " + str(time.time() - start_time))
