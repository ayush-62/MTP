from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 3)
l1n2v1 = IntVector('layer1node2v1', 3)
l2n1v1 = IntVector('layer2node1v1', 1)
l2n2v1 = IntVector('layer2node2v1', 1)
l2n3v1 = IntVector('layer2node3v1', 1)
b1 = IntVector('biasv1', 3)
l1n1v2 = IntVector('layer1node1v2', 3)
l1n2v2 = IntVector('layer1node2v2', 3)
l2n1v2 = IntVector('layer2node1v2', 1)
l2n2v2 = IntVector('layer2node2v2', 1)
l2n3v2 = IntVector('layer2node3v2', 1)
b2 = IntVector('biasv2', 3)
output1 = IntVector('out1', 4)
output2 = IntVector('out2', 4)


def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2, l2n3, b):
    hiddenValues = IntVector('hiddenNodeValues', 3)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0]) + b[0]
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1]) + b[1]
    hiddenValues[2] = (input[0] * l1n1[2]) + (input[1] * l1n2[2]) + b[2]

    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0]) + (hiddenValues[2] * l2n3[0])

    out = IntVector('out', 4)
    out[0] = hiddenValues[0]
    out[1] = hiddenValues[1]
    out[2] = hiddenValues[2]
    out[3] = outputValues[0]

    return out

s = Tactic('smt').solver()

s.add(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[0] == output1[0], neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[1] == output1[1], neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[2] == output1[2], neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[3] == output1[3])
s.add(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[0] == output2[0], neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[1] == output2[1], neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[2] == output2[2], neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[3] == output2[3])

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

    s.add(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[0] == out[0], neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[1] == out[1], neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[2] == out[2], neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1, l2n3v1, b1)[3] == out[3])
    s.add(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[0] == out[0], neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[1] == out[1], neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[2] == out[2], neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2, l2n3v2, b2)[3] == out[3])

print(s.check(output1[0] == output2[0], output1[1] == output2[1], output1[2] == output2[2], output1[3] == output2[3]))
print(s.model())
print("Finished in " + str(time.time() - start_time))
