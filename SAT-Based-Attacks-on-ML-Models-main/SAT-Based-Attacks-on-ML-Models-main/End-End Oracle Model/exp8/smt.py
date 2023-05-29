from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

def print_details(model):
    print("Model: [")
    print("  Input : [" + str(model[input[0]].as_long()) + ", " + str(model[input[1]].as_long()) + "]")
    print("  L1Wv1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n1v1[1]].as_long()) + "], [" + str(model[l1n2v1[0]].as_long()) + ", " + str(model[l1n2v1[1]].as_long()) + "] ]")
    print("  BiasV1: [" + str(model[biasv1[0]].as_long()) + ", " + str(model[biasv1[1]].as_long()) + " ]")
    print("  L2Wv1: [ [" + str(model[l2n1v1[0]].as_long()) + "], [" + str(model[l2n2v1[0]].as_long()) + "] ]")
    print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
    print()
    print("  L1Wv2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n1v2[1]].as_long()) + "], [" + str(model[l1n2v2[0]].as_long()) + ", " + str(model[l1n2v2[1]].as_long()) + "] ]")
    print("  BiasV2: [" + str(model[biasv2[0]].as_long()) + ", " + str(model[biasv2[1]].as_long()) + " ]")
    print("  L2Wv2: [ [" + str(model[l2n1v2[0]].as_long()) + "], [" + str(model[l2n2v2[0]].as_long()) + "] ]")
    print("  Output2: [" + str(model[output2[0]].as_long()) + "]")
    print("]")

start_time = time.time()

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 2)
l1n2v1 = IntVector('layer1node2v1', 2)
l2n1v1 = IntVector('layer2node1v1', 1)
l2n2v1 = IntVector('layer2node2v1', 1)
biasv1 = IntVector('biasv1', 2)
l1n1v2 = IntVector('layer1node1v2', 2)
l1n2v2 = IntVector('layer1node2v2', 2)
l2n1v2 = IntVector('layer2node1v2', 1)
l2n2v2 = IntVector('layer2node2v2', 1)
biasv2 = IntVector('biasv2', 2)
output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)

def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, bias):
    hiddenValues = IntVector('hiddenNodeValues', 2)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0]) + bias[0]
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1]) + bias[1]

    hiddenValues[0] = If(hiddenValues[0] < 0, 0, hiddenValues[0])
    hiddenValues[1] = If(hiddenValues[1] < 0, 0, hiddenValues[1])

    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0])

    return outputValues

s = Tactic('smt').solver()

s.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, biasv1)[0] == output1[0]))
s.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, biasv2)[0] == output2[0]))

while s.check(output1[0] != output2[0]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    [out]= Cexec(ia)
    
    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(simplify(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, biasv1)[0] == out))
    s.add(simplify(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, biasv2)[0] == out))

print(s.check(output1[0] == output2[0]))
print_details(s.model())
print("Finished in " + str(time.time() - start_time))
