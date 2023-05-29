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
    print("  W1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n2v1[0]].as_long()) + "] ]")
    print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
    print()
    print("  W2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n2v2[0]].as_long()) + "] ]")
    print("  Output2: [" + str(model[output2[0]].as_long()) + "]")
    print("]")
    return

start_time = time.time()
prev_time = start_time

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 1)
l1n2v1 = IntVector('layer1node2v1', 1)
l1n1v2 = IntVector('layer1node1v2', 1)
l1n2v2 = IntVector('layer1node2v2', 1)
output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)

def neuralNetwork(input, l1n1, l1n2):
    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0])
    return outputValues

s = Tactic('smt').solver()

s.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1)[0] == output1[0]))
s.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2)[0] == output2[0]))

while s.check(output1[0] != output2[0]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]])
    print(ia)
    [out]= Cexec(ia)
    
    inp = IntVector('inp', 2)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]

    s.add(simplify(neuralNetwork(inp, l1n1v1, l1n2v1)[0] == out))
    s.add(simplify(neuralNetwork(inp, l1n1v2, l1n2v2)[0] == out))

print("unsat came in " + str(time.time() - start_time))

# print(s.check(output1[0] != output2[0]))
print(s.check(output1[0] == output2[0]))
print_details(s.model())
print("Finished in " + str(time.time() - start_time))
