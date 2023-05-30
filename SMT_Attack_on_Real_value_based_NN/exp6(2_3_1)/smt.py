from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

set_option(rational_to_decimal=True)
set_option(precision=3)


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

input = RealVector('inp', 2)
l1n1v1 = RealVector('layer1node1v1', 3)
l1n2v1 = RealVector('layer1node2v1', 3)
l2n1v1 = RealVector('layer2node1v1', 1)
l2n2v1 = RealVector('layer2node2v1', 1)
l2n3v1 = RealVector('layer2node3v1', 1)
l1n1v2 = RealVector('layer1node1v2', 3)
l1n2v2 = RealVector('layer1node2v2', 3)
l2n1v2 = RealVector('layer2node1v2', 1)
l2n2v2 = RealVector('layer2node2v2', 1)
l2n3v2 = RealVector('layer2node3v2', 1)

l2b1v1 = RealVector('layer2bias1v1', 1)
l2b2v1 = RealVector('layer2bias2v1', 1)
l2b3v1 = RealVector('layer2node3v1', 1)

l2b1v2 = RealVector('layer2bias1v2', 1)
l2b2v2 = RealVector('layer2bias2v2', 1)
l2b3v2 = RealVector('layer2node3v2', 1)

output1 = RealVector('out1', 1)
output2 = RealVector('out2', 1)

ov1_1,ov1_2,ov1_3 = Reals('ov1_1 ov1_2 ov1_3')
ov2_1,ov2_2,ov2_3 = Reals('ov2_1 ov2_2 ov2_3')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',RealSort()),('2',RealSort()),('3',RealSort()))
tuple = tuple.create()

out1 = tuple.tuple(ov1_1,ov1_2,ov1_3)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3)

def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, l2n3 , l2b1 , l2b2 , l2b3):
    hiddenValues = RealVector('hiddenNodeValues', 3)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0] + l2b1)
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1] + l2b2)
    hiddenValues[2] = (input[0] * l1n1[2]) + (input[1] * l1n2[2] + l2b3)

    # outputValues = RealVector('outputValues', 1)
    # outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0]) + (hiddenValues[2] * l2n3[0])

    out = tuple.tuple(hiddenValues[0],hiddenValues[1],hiddenValues[2])
    return out

s = Tactic('smt').solver()
s.add(input[0] != 0 , input[1] != 0)
s.add(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1 , l2b1v1 , l2b2v1 , l2b3v1) == out1)
s.add(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2 , l2b1v2 , l2b2v2 , l2b3v2) == out2)

while s.check(out1 != out2) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    out = Cexec(ia)
    out_tup = tuple.tuple(out[0],out[1],out[2])
    inp = RealVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1 , l2b1v1 , l2b2v1 , l2b3v1) == out_tup)
    s.add(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2 , l2b1v2 , l2b2v2 , l2b3v2) == out_tup)

print(s.check(output1[0] == output2[0]))
print(s.model())
print("Finished in " + str(time.time() - start_time))
