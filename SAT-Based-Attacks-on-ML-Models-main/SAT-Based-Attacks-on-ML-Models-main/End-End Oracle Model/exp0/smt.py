from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

def print_details(model):
    input = IntVector('inp', 2)
    print("Model: [")
    print("  Input : [" + str(model[input[0]].as_long()) + ", " + str(model[input[1]].as_long()) + "]")
    print("  L1Wv1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n1v1[1]].as_long()) + ", " + str(model[l1n1v1[2]].as_long()) + "], [" + str(model[l1n2v1[0]].as_long()) + ", " + str(model[l1n2v1[1]].as_long()) + ", " + str(model[l1n2v1[2]].as_long()) + "] ]")
    print("  L1Bv1: [" + str(model[l2bv1[0]].as_long()) + ", " + str(model[l2bv1[1]].as_long()) + ", " + str(model[l2bv1[2]].as_long()) + "]")
    print("  L2Wv1: [ [" + str(model[l2n1v1[0]].as_long()) + "], [" + str(model[l2n2v1[0]].as_long()) + "], [" + str(model[l2n3v1[0]].as_long()) + "] ]")
    print("  L2Bv1: [" + str(model[l3bv1[0]].as_long()) + "]")
    print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
    print()
    print("  L1Wv2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n1v2[1]].as_long()) + ", " + str(model[l1n1v2[2]].as_long()) + "], [" + str(model[l1n2v2[0]].as_long()) + ", " + str(model[l1n2v2[1]].as_long()) + ", " + str(model[l1n2v2[2]].as_long()) + "] ]")
    print("  L1Bv2: [" + str(model[l2bv2[0]].as_long()) + ", " + str(model[l2bv2[1]].as_long()) + ", " + str(model[l2bv2[2]].as_long()) + "]")
    print("  L2Wv2: [ [" + str(model[l2n1v2[0]].as_long()) + "], [" + str(model[l2n2v2[0]].as_long()) + "], [" + str(model[l2n3v2[0]].as_long()) + "] ]")
    print("  L2Bv2: [" + str(model[l3bv2[0]].as_long()) + "]")
    print("  Output2: [" + str(model[output2[0]].as_long()) + "]")
    print("]")
    return

start_time = time.time()
prev_time = start_time

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
l2bv1 = IntVector('layer2basev1', 3)
l2bv2 = IntVector('layer2basev2', 3)
l3bv1 = IntVector('layer3basev1', 1)
l3bv2 = IntVector('layer3basev2', 1)
output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)


def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, l2n3, l2b, l3b):
    hiddenValues = IntVector('hiddenNodeValues', 3)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0])
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1])
    hiddenValues[2] = (input[0] * l1n1[2]) + (input[1] * l1n2[2])

    for i in range(3):
        hiddenValues[i] += l2b[i]

    for i in range(3):
        hiddenValues[i] = If(hiddenValues[i] < 0, 0, hiddenValues[i])

    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0]) + (hiddenValues[2] * l2n3[0])
    outputValues[0] += l3b[0]

    return outputValues

s = Tactic('smt').solver()

s.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, l2bv1, l3bv1)[0] == output1[0]))
s.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, l2bv2, l3bv2)[0] == output2[0]))

while s.check(output1[0] != output2[0]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    [out]= Cexec(ia)
    
    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(simplify(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, l2bv1, l3bv1)[0] == out))
    s.add(simplify(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, l2bv2, l3bv2)[0] == out))

print("unsat came in " + str(time.time() - start_time))

# print(s.check(output1[0] != output2[0]))
print(s.check(output1[0] == output2[0]))
print_details(s.model())
print("")
print("Finished in " + str(time.time() - start_time))
