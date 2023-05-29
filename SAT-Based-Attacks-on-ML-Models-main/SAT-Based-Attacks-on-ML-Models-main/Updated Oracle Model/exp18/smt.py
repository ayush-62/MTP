from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

input = IntVector('inp', 10)
l1n1v1 = IntVector('layer1node1v1', 5)
l1n2v1 = IntVector('layer1node2v1', 5)
l1n3v1 = IntVector('layer1node3v1', 5)
l1n4v1 = IntVector('layer1node4v1', 5)
l1n5v1 = IntVector('layer1node5v1', 5)
l2n1v1 = IntVector('layer2node1v1', 5)
l2n2v1 = IntVector('layer2node2v1', 5)
l2n3v1 = IntVector('layer2node3v1', 5)
l2n4v1 = IntVector('layer2node4v1', 5)
l2n5v1 = IntVector('layer2node5v1', 5)
l3n1v1 = IntVector('layer3node1v1', 1)
l3n2v1 = IntVector('layer3node2v1', 1)
l3n3v1 = IntVector('layer3node3v1', 1)
l3n4v1 = IntVector('layer3node4v1', 1)
l3n5v1 = IntVector('layer3node5v1', 1)
l1n1v2 = IntVector('layer1node1v2', 5)
l1n2v2 = IntVector('layer1node2v2', 5)
l1n3v2 = IntVector('layer1node3v2', 5)
l1n4v2 = IntVector('layer1node4v2', 5)
l1n5v2 = IntVector('layer1node5v2', 5)
l2n1v2 = IntVector('layer2node1v2', 5)
l2n2v2 = IntVector('layer2node2v2', 5)
l2n3v2 = IntVector('layer2node3v2', 5)
l2n4v2 = IntVector('layer2node4v2', 5)
l2n5v2 = IntVector('layer2node5v2', 5)
l3n1v2 = IntVector('layer3node1v2', 1)
l3n2v2 = IntVector('layer3node2v2', 1)
l3n3v2 = IntVector('layer3node3v2', 1)
l3n4v2 = IntVector('layer3node4v2', 1)
l3n5v2 = IntVector('layer3node5v2', 1)
outv1 = IntVector('outv1', 11)
outv2 = IntVector('outv2', 11)

def NN(input, l1n1, l1n2, l1n3, l1n4, l1n5, l2n1, l2n2, l2n3, l2n4, l2n5, l3n1, l3n2, l3n3, l3n4, l3n5):
    l2out = IntVector('l2out', 5)
    l2out[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0]) + (input[2] * l1n3[0]) + (input[3] * l1n4[0]) + (input[4] * l1n5[0])
    l2out[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1]) + (input[2] * l1n3[1]) + (input[3] * l1n4[1]) + (input[4] * l1n5[1])
    l2out[2] = (input[0] * l1n1[2]) + (input[1] * l1n2[2]) + (input[2] * l1n3[2]) + (input[3] * l1n4[2]) + (input[4] * l1n5[2])
    l2out[3] = (input[0] * l1n1[3]) + (input[1] * l1n2[3]) + (input[2] * l1n3[3]) + (input[3] * l1n4[3]) + (input[4] * l1n5[3])
    l2out[4] = (input[0] * l1n1[4]) + (input[1] * l1n2[4]) + (input[2] * l1n3[4]) + (input[3] * l1n4[4]) + (input[4] * l1n5[4])
    
    l3out = IntVector('l3out', 5)
    l3out[0] = (l2out[0] * l2n1[0]) + (l2out[1] * l2n2[0]) + (l2out[2] * l2n3[0]) + (l2out[3] * l2n4[0]) + (l2out[4] * l2n5[0])
    l3out[1] = (l2out[0] * l2n1[1]) + (l2out[1] * l2n2[1]) + (l2out[2] * l2n3[1]) + (l2out[3] * l2n4[1]) + (l2out[4] * l2n5[1])
    l3out[2] = (l2out[0] * l2n1[2]) + (l2out[1] * l2n2[2]) + (l2out[2] * l2n3[2]) + (l2out[3] * l2n4[2]) + (l2out[4] * l2n5[2])
    l3out[3] = (l2out[0] * l2n1[3]) + (l2out[1] * l2n2[3]) + (l2out[2] * l2n3[3]) + (l2out[3] * l2n4[3]) + (l2out[4] * l2n5[3])
    l3out[4] = (l2out[0] * l2n1[4]) + (l2out[1] * l2n2[4]) + (l2out[2] * l2n3[4]) + (l2out[3] * l2n4[4]) + (l2out[4] * l2n5[4])
    
    l4out = IntVector('l4out', 1)
    l4out[0] = (l3out[0] * l3n1[0]) + (l3out[1] * l3n2[0]) + (l3out[2] * l3n3[0]) + (l3out[3] * l3n4[0]) + (l3out[4] * l3n5[0])

    out = IntVector('out', 21)
    out[0] = l2out[0]
    out[1] = l2out[1]
    out[2] = l2out[2]
    out[3] = l2out[3]
    out[4] = l2out[4]
    out[5] = l3out[0]
    out[6] = l3out[1]
    out[7] = l3out[2]
    out[8] = l3out[3]
    out[9] = l3out[4]
    out[10] = l4out[0]
    return out

s = Tactic('smt').solver()

s.add(NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[0] == outv1[0], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[1] == outv1[1], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[2] == outv1[2], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[3] == outv1[3], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[4] == outv1[4], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[5] == outv1[5], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[6] == outv1[6], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[7] == outv1[7], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[8] == outv1[8], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[9] == outv1[9], NN(input, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[10] == outv1[10])
s.add(NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[0] == outv2[0], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[1] == outv2[1], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[2] == outv2[2], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[3] == outv2[3], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[4] == outv2[4], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[5] == outv2[5], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[6] == outv2[6], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[7] == outv2[7], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[8] == outv2[8], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[9] == outv2[9], NN(input, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[10] == outv2[10])

while s.check(outv1[0] != outv2[0], outv1[1] != outv2[1], outv1[2] != outv2[2], outv1[3] != outv2[3], outv1[4] != outv2[4], outv1[5] != outv2[5], outv1[6] != outv2[6], outv1[7] != outv2[7], outv1[8] != outv2[8], outv1[9] != outv2[9], outv1[10] != outv2[10]) == sat:
    m = s.model()
    ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(m[input[2]]) + " " + str(m[input[3]]) + " " + str(m[input[4]]) + " " + str(m[input[5]]) + str(time.time() - start_time)
    print(ia)
    out = Cexec(ia)

    # ch = str(out[0]) + " " + str(out[1]) + " " + str(out[2])
    # print(ch)

    inp = IntVector('inp', 5)
    inp[0] = m[input[0]]
    inp[1] = m[input[1]]
    inp[2] = m[input[2]]
    inp[3] = m[input[3]]
    inp[4] = m[input[4]]

    s.add(NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[0] == out[0], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[1] == out[1], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[2] == out[2], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[3] == out[3], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[4] == out[4], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[5] == out[5], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[6] == out[6], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[7] == out[7], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[8] == out[8], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[9] == out[9], NN(inp, l1n1v1, l1n2v1, l1n3v1, l1n4v1, l1n5v1, l2n1v1, l2n2v1, l2n3v1, l2n4v1, l2n5v1, l3n1v1, l3n2v1, l3n3v1, l3n4v1, l3n5v1)[10] == out[10])
    s.add(NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[0] == out[0], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[1] == out[1], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[2] == out[2], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[3] == out[3], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[4] == out[4], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[5] == out[5], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[6] == out[6], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[7] == out[7], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[8] == out[8], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[9] == out[9], NN(inp, l1n1v2, l1n2v2, l1n3v2, l1n4v2, l1n5v2, l2n1v2, l2n2v2, l2n3v2, l2n4v2, l2n5v2, l3n1v2, l3n2v2, l3n3v2, l3n4v2, l3n5v2)[10] == out[10])

print(s.check(outv1[0] == outv2[0], outv1[1] == outv2[1], outv1[2] == outv2[2], outv1[3] == outv2[3], outv1[4] == outv2[4], outv1[5] == outv2[5], outv1[6] == outv2[6], outv1[7] == outv2[7], outv1[8] == outv2[8], outv1[9] == outv2[9], outv1[10] == outv2[10]))
print(s.model())

print("Finished in " + str(time.time() - start_time))
