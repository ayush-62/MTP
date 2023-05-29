from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()
prev_time = start_time

input = IntVector('inp', 2)
l1n1v1 = IntVector('layer1node1v1', 2)
l1n2v1 = IntVector('layer1node2v1', 2)
l2n1v1 = IntVector('layer2node1v1', 1)
l2n2v1 = IntVector('layer2node2v1', 1)
l1n1v2 = IntVector('layer1node1v2', 2)
l1n2v2 = IntVector('layer1node2v2', 2)
l2n1v2 = IntVector('layer2node1v2', 1)
l2n2v2 = IntVector('layer2node2v2', 1)
output1 = IntVector('out1', 1)
output2 = IntVector('out2', 1)


def neuralNetwork(input, l1n1, l1n2, l2n1, l2n2):
    hiddenValues = IntVector('hiddenNodeValues', 2)
    hiddenValues[0] = (input[0] * l1n1[0]) + (input[1] * l1n2[0])
    hiddenValues[1] = (input[0] * l1n1[1]) + (input[1] * l1n2[1])

    outputValues = IntVector('outputValues', 1)
    outputValues[0] = (hiddenValues[0] * l2n1[0]) + (hiddenValues[1] * l2n2[0])

    return outputValues

TO_init = 1600
TO_max = 12800000000
rem_key_max = 32

iterations = 0
prune_key_set = False
Key_Set_Fetch_Count = 0
TO_increase_count = 0

s = Tactic('smt').solver()

s.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1)[0] == output1[0]))
s.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2)[0] == output2[0]))

while not prune_key_set:
    break_away = False
    added_new_constraints = False
    s.set("timeout", TO_init)

    pos_set = set()
    print("loop1 enter")

    while s.check(output1[0] != output2[0], Or(l1n1v1[0] != l1n1v2[0], l1n1v1[1] != l1n1v2[1], l1n2v1[0] != l1n2v2[0], l1n2v1[1] != l1n2v2[1], l2n1v1[0] != l2n1v2[0], l2n2v1[0] != l2n2v2[0])) == sat:
        added_new_constraints = True
        m = s.model()
        ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
        print(ia)
        [out]= Cexec(ia)
        
        
        inp = IntVector('inp', 2)
        inp[0] = m[input[0]]
        inp[1] = m[input[1]]

        s.add(simplify(neuralNetwork(inp, l1n1v1, l1n2v1, l2n1v1, l2n2v1)[0] == out))
        s.add(simplify(neuralNetwork(inp, l1n1v2, l1n2v2, l2n1v2, l2n2v2)[0] == out))
        iterations = iterations + 1

    print("loop1 ended")
    p = 0

    if not added_new_constraints:
        TO_init = 2 * TO_init
        TO_increase_count+=1
        if TO_init > TO_max:
            print(time.time() - start_time)
            raise Exception("Key couldn't be found in the given time limit and remaining key limit")
        continue

    while s.check(l1n1v1[0] == l1n1v2[0], l1n1v1[1] == l1n1v2[1], l1n2v1[0] == l1n2v2[0], l1n2v1[1] == l1n2v2[1], l2n1v1[0] == l2n1v2[0], l2n2v1[0] == l2n2v2[0]) != unsat:
        try:
            m = s.model()
        except:
            break_away = True
            break
        pos_set.add(m)

        if len(pos_set) > rem_key_max:
            break

        s.add(Or(l1n1v1[0] != m[l1n1v1[0]], l1n1v1[1] != m[l1n1v1[1]], l1n2v1[0] != m[l1n2v1[0]], l1n2v1[1] != m[l1n2v1[1]], l2n1v1[0] != m[l2n1v1[0]], l2n2v1[0] != m[l2n2v1[0]]))
        s.add(Or(l1n1v2[0] != m[l1n1v2[0]], l1n1v2[1] != m[l1n1v2[1]], l1n2v2[0] != m[l1n2v2[0]], l1n2v2[1] != m[l1n2v2[1]], l2n1v2[0] != m[l2n1v2[0]], l2n2v2[0] != m[l2n2v2[0]]))
        p = p + 1

    if p > 0:
        Key_Set_Fetch_Count+=1

    if break_away or len(pos_set) > rem_key_max or len(pos_set) == 0:
        TO_init = 2 * TO_init
        TO_increase_count+=1
        if TO_init > TO_max:
            print(time.time() - start_time)
            raise Exception("Key couldn't be found in the given time limit and remaining key limit")
    else:
        prune_key_set = True


print()
print("loop2 enter")
print("Possible keys: ", p)

pos_l = list(pos_set)

g = Tactic('smt').solver()

g.add(simplify(neuralNetwork(input, l1n1v1, l1n2v1, l2n1v1, l2n2v1)[0] == output1[0]))
g.add(simplify(neuralNetwork(input, l1n1v2, l1n2v2, l2n1v2, l2n2v2)[0] == output2[0]))

print("loop3 enter")

while len(pos_l) > 1:
    m1 = pos_l[0]
    m2 = pos_l[1]
    g.push()
    g.add(l1n1v1[0] != m1[l1n1v1[0]], l1n1v1[1] != m1[l1n1v1[1]], l1n2v1[0] != m1[l1n2v1[0]], l1n2v1[1] != m1[l1n2v1[1]], l2n1v1[0] != m1[l2n1v1[0]], l2n2v1[0] != m1[l2n2v1[0]])
    g.add(l1n1v2[0] != m2[l1n1v2[0]], l1n1v2[1] != m2[l1n1v2[1]], l1n2v2[0] != m2[l1n2v2[0]], l1n2v2[1] != m2[l1n2v2[1]], l2n1v2[0] != m2[l2n1v2[0]], l2n2v2[0] != m2[l2n2v2[0]])
    if g.check(output1[0] != output2[0]) == sat:
        m = g.model()
        ia = str(m[input[0]]) + " " + str(m[input[1]]) + " " + str(time.time() - start_time)
        print(ia)
        
        [out]= Cexec(ia)

        in1 = IntVector('inp1', 2)
        in1[0] = m1[input[0]]
        in1[1] = m1[input[1]]

        l1n1m1 = IntVector('l1n1m1', 2)
        l1n1m1[0] = m1[l1n1v1[0]]
        l1n1m1[1] = m1[l1n1v1[1]]

        l1n2m1 = IntVector('l1n2m1', 2)
        l1n2m1[0] = m1[l1n2v1[0]]
        l1n2m1[1] = m1[l1n2v1[1]]

        l2n1m1 = IntVector('l2n1m1', 1)
        l2n1m1[0] = m1[l2n1v1[0]]
        l2n2m1 = IntVector('l2n2m1', 1)
        l2n2m1[0] = m1[l2n2v1[0]]

        in2 = IntVector('inp2', 2)
        in2[0] = m2[input[0]]
        in2[1] = m2[input[1]]

        l1n1m2 = IntVector('l1n1m2', 2)
        l1n1m2[0] = m2[l1n1v2[0]]
        l1n1m2[1] = m2[l1n1v2[1]]

        l1n2m2 = IntVector('l1n2m2', 2)
        l1n2m2[0] = m2[l1n2v2[0]]
        l1n2m2[1] = m2[l1n2v2[1]]

        l2n1m2 = IntVector('l2n1m2', 1)
        l2n1m2[0] = m2[l2n1v2[0]]
        l2n2m2 = IntVector('l2n2m2', 1)
        l2n2m2[0] = m2[l2n2v2[0]]

        if g.check(simplify(neuralNetwork(in1, l1n1m1, l1n2m1, l2n1m1, l2n2m1)[0] == out)) == unsat:
            pos_l.remove(m1)
        if g.check(simplify(neuralNetwork(in2, l1n1m2, l1n2m2, l2n1m2, l2n2m2)[0] == out)) == unsat:
            pos_l.remove(m2)
    else:
        pos_l.remove(m1)
    g.pop()


print("The final key is:")
m = pos_l[0]
print(str(m[l1n1v1[0]]))
print(str(m[l1n1v1[1]]))
print(str(m[l1n2v1[0]]))
print(str(m[l1n2v1[1]]))
print(str(m[l2n1v1[0]]))
print(str(m[l2n2v1[0]]))
print()

end_time = time.time()
taken = end_time - start_time

print("Computation took %d iterations and %f seconds." % (iterations, taken)) 
print("Number of times Time-Out increased: %d." % (TO_increase_count))
print("Number of times remaining key set computed: %d." % (Key_Set_Fetch_Count))