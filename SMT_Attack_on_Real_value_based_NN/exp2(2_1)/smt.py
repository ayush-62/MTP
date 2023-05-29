from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

# def print_details(model):
#     input = RealVector('inp', 2)
#     print("Model: [")
#     print("  Input : [" + str(model[input[0]].as_long()) + ", " + str(model[input[1]].as_long()) + "]")
#     print("  W1: [ [" + str(model[l1n1v1[0]].as_long()) + ", " + str(model[l1n2v1[0]].as_long()) + "] ]")
#     print("  Output1: [" + str(model[output1[0]].as_long()) + "]")
#     print()
#     print("  W2: [ [" + str(model[l1n1v2[0]].as_long()) + ", " + str(model[l1n2v2[0]].as_long()) + "] ]")
#     print("  Output2: [" + str(model[output2[0]].as_long()) + "]")
#     print("]")
#     return

start_time = time.time()
prev_time = start_time

float_sort = FPSort(6, 24)
inp1 , inp2  = FPs('inp1 inp2' ,float_sort )
l1n1v1 = FP('layer1node1v1' , float_sort)
l1n2v1 = FP('layer1node2v1' , float_sort)
l1n1v2 = FP('layer1node1v2' , float_sort)
l1n2v2 = FP('layer1node2v2' , float_sort)
output1 = FP('out1' , float_sort)
output2 = FP('out2' , float_sort)

def neuralNetwork(inp1 , inp2, l1n1, l1n2):
    outputValues = FP('outputValues' , float_sort)
    outputValues = (inp1 * l1n1) + (inp2 * l1n2)
    return outputValues

s = Tactic('smt').solver()

s.add(inp1 != 0 )
s.add(inp2 != 0 )
s.add(simplify(neuralNetwork(inp1 , inp2, l1n1v1, l1n2v1) == output1))
s.add(simplify(neuralNetwork(inp1 , inp2 ,l1n1v2, l1n2v2) == output2))

while s.check(output1 != output2) == sat:
    m = s.model()
    ia = str(m[inp1]) + " " + str(m[inp2])
    print(ia)
    [out]= Cexec(ia)
    
    inp = RealVector('inp', 2)
    inp1 = m[inp1]
    inp2 = m[inp2]

    s.add(simplify(neuralNetwork(inp1 , inp2, l1n1v1, l1n2v1) == out))
    s.add(simplify(neuralNetwork(inp1, inp2 ,  l1n1v2, l1n2v2) == out))

print("unsat came in " + str(time.time() - start_time))

# print(s.check(output1[0] != output2[0]))
print(s.check(output1 == output2))
print(s.model())
print("Finished in " + str(time.time() - start_time))
