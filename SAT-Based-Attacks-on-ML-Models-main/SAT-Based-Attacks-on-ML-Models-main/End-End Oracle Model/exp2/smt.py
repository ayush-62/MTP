from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()
prev_time = start_time

input = IntVector('inp', 4)
l1n1v1 = IntVector('layer1node1v1', 1)
l1n2v1 = IntVector('layer1node2v1', 1)
l1n3v1 = IntVector('layer1node3v1', 1)
l1n4v1 = IntVector('layer1node4v1', 1)
l1n1v2 = IntVector('layer1node1v2', 1)
l1n2v2 = IntVector('layer1node2v2', 1)
l1n3v2 = IntVector('layer1node3v2', 1)
l1n4v2 = IntVector('layer1node4v2', 1)
output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)

def neuralNetwork(input, l1n1, l1n2, l1n3, l1n4):
    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0]) + (input[2] * l1n3[0]) + (input[3] * l1n4[0])
    return outputValues

s = Tactic('smt').solver()

s.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1)[0] == output1[0]))
s.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2)[0] == output2[0]))

while s.check(output1[0] != output2[0]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(m[input[2]]) + " " + str(m[input[3]])
    [out]= Cexec(ia)
    ia = ia + " " + str(out)
    print(ia)
    
    inp = IntVector('inp2', 4)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]
    inp[2] = m[input[2]]
    inp[3] = m[input[3]]

    s.add(simplify(neuralNetwork(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1)[0] == out))
    s.add(simplify(neuralNetwork(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2)[0] == out))

print(s.check(output1[0] == output2[0]))
print(s.model())
# print(s.model())
print("Finished in " + str(time.time() - start_time))
