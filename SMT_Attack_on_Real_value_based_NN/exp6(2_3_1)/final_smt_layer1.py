from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

set_option(rational_to_decimal=True)
set_option(precision=15)

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


l1bv1 = IntVector('layer1bias1v1' , 3)
l1bv2 = IntVector('layer1bias1v2' , 3)

ov1_1,ov1_2,ov1_3 = Reals('ov1_1 ov1_2 ov1_3')
ov2_1,ov2_2,ov2_3 = Reals('ov2_1 ov2_2 ov2_3')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',RealSort()),('2',RealSort()),('3',RealSort()))
tuple = tuple.create()

out1 = tuple.tuple(ov1_1,ov1_2,ov1_3)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3)

q_w1 =  Int('q_w1')
shift_w1 = Int('shift_w1')
q_b1 = Int('q_b1')
shift_b1 = Int('shift_b1')


zp_i = IntVector('zp_i' , 2)
zp_w = IntVector('zp_w' , 2)
zp_b = IntVector('zp_b' , 2)

def neuralNetwork(input, l1n1, l1n2, l1b , q_b1 , zp_b , shift_b1):

    valw = round(1559941072/(2**(9+31)) , 3)
    updated_l1n1 = RealVector('updated_l1n1' , 3)
    
    updated_l1n1[0] = ((l1n1[0] - 78)*valw)
    updated_l1n1[1] = ((l1n1[1] - 78)*valw)
    updated_l1n1[2] = ((l1n1[2] - 78)*valw)

    updated_l1n2 = RealVector('updated_l1n2' , 3)
    updated_l1n2[0] = ((l1n2[0] - 78)*valw)
    updated_l1n2[1] = ((l1n2[1] - 78)*valw)
    updated_l1n2[2] = ((l1n2[2] - 78)*valw)

    updated_bias  =  RealVector('updated_bias' , 3)
    valb = round(1529762159/(2**(2+31)) , 3)
    updated_bias[0] = ((l1b[0]-124)*valb)
    updated_bias[1] = ((l1b[1]-124)*valb)
    updated_bias[2] = ((l1b[2]-124)*valb)

    updated_input = IntVector('updated_input' , 2)
    updated_input[0] = input[0]
    updated_input[1] = input[1] 

    
    hiddenValues = RealVector('hiddenNodeValues', 3)
    hiddenValues[0] = (updated_input[0] * updated_l1n1[0]) + (updated_input[1] * updated_l1n2[0]) + l1b[0]
    hiddenValues[0] = If(hiddenValues[0] < 0, 0, hiddenValues[0]) 
    hiddenValues[0] = hiddenValues[0] 

    hiddenValues[1] = (updated_input[0] * updated_l1n1[1]) + (updated_input[1] * updated_l1n2[1]) + l1b[1]
    hiddenValues[1] = If(hiddenValues[1] < 0, 0, hiddenValues[1]) 
    hiddenValues[1] = hiddenValues[1] 

    hiddenValues[2] = (updated_input[0] * updated_l1n1[2]) + (updated_input[1] * updated_l1n2[2]) + l1b[2]
    hiddenValues[2] = If(hiddenValues[2] < 0, 0, hiddenValues[2]) 
    hiddenValues[2] = hiddenValues[2] 
    
    # outputValues = IntVector('outputValues', 1)
    # outputValues[0] = (hiddenValues[0] * l1n1[0]) + (hiddenValues[1] * l2n2[0]) + (hiddenValues[2] * l2n3[0])
    return tuple.tuple(hiddenValues[0],hiddenValues[1],hiddenValues[2])





s = Tactic('smt').solver()

s.add(shift_w1 == 9, q_b1 == 1529762159, shift_b1 == 2 , q_w1 == 1559941072)
s.add(zp_i[0] == 0 , zp_i[1] == 0, zp_w[0] == 78 , zp_w[1] == 89 , zp_b[0] == 124 , zp_b[1] == 1)

s.add(input[0] > 0 , input[0] <= 255)
s.add(input[1] > 0 , input[1] <= 255)
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

s.add(neuralNetwork(input, l1n1v1, l1n2v1 , l1bv1 , q_b1 , zp_b , shift_b1) == out1)
s.add(neuralNetwork(input, l1n1v2, l1n2v2 , l1bv2 , q_b1 , zp_b , shift_b1) == out2)
ia = str(255) + " " + str(1) + " " + str(time.time() - start_time)
out= Cexec(ia)
print(out)
out_tup = tuple.tuple(out[0],out[1],out[2])
print(simplify(neuralNetwork([255,1], [96 , 228 , 0], [62 , 254, 47] , [116 , 0 , 454] , 1529762159 , [124 , 1] , 2)))
print(s.check(neuralNetwork([255,1], [96 , 228 , 0], [62 , 254, 47] , [116 , 0 , 454] , 1529762159 , [124 , 1] , 2) == out_tup))

while s.check(out1 != out2) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    #print(m)
    out= Cexec(ia)
    print(out)
    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]
    out_tup = tuple.tuple(out[0],out[1],out[2])
    s.add((neuralNetwork(inp, l1n1v1, l1n2v1, l1bv1 , q_b1 , zp_b , shift_b1) == out_tup))
    s.add((neuralNetwork(inp, l1n1v2, l1n2v2, l1bv2 , q_b1 , zp_b , shift_b1) == out_tup))
    
print(s.check(out1 != out2))
print(s.check(out1 == out2))
print(s.model())
print("Finished in " + str(time.time() - start_time))