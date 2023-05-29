import string
from z3 import *
import subprocess
import time

def Cexec(init_string):
    out = subprocess.check_output("./a.out %s" % init_string,shell=True,)    
    return list(map(String, out.decode('utf-8').split()))

input = BoolVector('inp', 3)
keys1 = BoolVector('k1', 2)
keys2 = BoolVector('k2', 2)
output1 = BoolVector('out1', 1)
output2 = BoolVector('out2', 1)

s = Tactic('smt').solver()

def xnor(a, b):
    return Or(And(a, b), And(Not(a), Not(b)))

def xor(a, b):
    return Or(And(a, Not(b)), And(Not(a), b))

def circuit(input, keys):
    return Or(xor(keys[1], Not(And(input[0], input[1]))), And(input[1], input[2]), xnor(keys[0], And(input[2], input[0])))

def oracle(intput):
    if(input[0] == True and input[1] == True):
        return True
    if(input[2] == True and input[1] == True):
        return True
    if(input[0] == True and input[2] == True):
        return True
    return False

s.add(simplify(circuit(input, keys1) == output1[0]))
s.add(simplify(circuit(input, keys2) == output2[0]))

while s.check(output1[0] != output2[0]) == sat:
    m = s.model()

    new_input = BoolVector('new_input', 3)
    new_input[0] = m[input[0]]
    new_input[1] = m[input[1]]
    new_input[2] = m[input[2]]

    out = oracle(new_input)
    print(new_input[0])
    print(new_input[1])
    print(new_input[2])
    print(out)
    print()

    s.add(simplify(circuit(new_input, keys1) == out))
    s.add(simplify(circuit(new_input, keys2) == out))

print(s.check(output1[0] == output2[0]))
print(s.model())
# print(str(m[input[0]]))
# print(str(m[input[1]]))
# print(str(m[input[2]]))
# print()
# print(str[m[keys1[0]]])
# print(str[m[keys1[1]]])
# print()
# print(str[m[keys2[0]]])
# print(str[m[keys2[1]]])
# print()
# print(output1[0])
# [inp__2 = True,
#  k1__0 = False,
#  k1__1 = True,
#  out2__0 = False,
#  inp__0 = True,
#  k2__1 = True,
#  inp__1 = False,
#  out1__0 = False,
#  k2__0 = False]