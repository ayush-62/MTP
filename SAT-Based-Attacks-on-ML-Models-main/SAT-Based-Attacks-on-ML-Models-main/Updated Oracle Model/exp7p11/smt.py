from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 2)
l1n2v1 = IntVector('layer1node2v1', 2)
l2n1v1 = IntVector('layer2node1v1', 1)
l2n2v1 = IntVector('layer2node2v1', 1)
l1n1v2 = IntVector('layer1node1v2', 2)
l1n2v2 = IntVector('layer1node2v2', 2)
l2n1v2 = IntVector('layer2node1v2', 1)
l2n2v2 = IntVector('layer2node2v2', 1)
b1 = IntVector('bias1', 2)
b2 = IntVector('bias2', 2)
output1 = IntVector('out1', 3)
output2 = IntVector('out2', 3)


def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, bias):
    hiddenValues = IntVector('hiddenNodeValues', 2)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0]) + bias[0]
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1]) + bias[1]

    hiddenValues[0] = If(hiddenValues[0] < 0, 0, hiddenValues[0])
    hiddenValues[1] = If(hiddenValues[1] < 0, 0, hiddenValues[1])

    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0])

    out = IntVector('out', 3)
    out[0] = hiddenValues[0]
    out[1] = hiddenValues[1]
    out[2] = outputValues[0]

    return out

s = Tactic('smt').solver()

s.add(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[0] == output1[0], neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[1] == output1[1], neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[2] == output1[2])
s.add(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[0] == output2[0], neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[1] == output2[1], neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[2] == output2[2])

while s.check(output1[0] != output2[0], output1[1] != output2[1], output1[2] != output2[2]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
    print(ia)
    out = Cexec(ia)

    ch = str(out[0]) + " " + str(out[1]) + " " + str(out[2])
    print(ch)

    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[0] == out[0], neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[1] == out[1], neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, b1)[2] == out[2])
    s.add(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[0] == out[0], neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[1] == out[1], neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, b2)[2] == out[2])

print(s.check(output1[0] == output2[0], output1[1] == output2[1], output1[2] == output2[2]))
print(s.model())
print("Finished in " + str(time.time() - start_time))
