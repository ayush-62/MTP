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

s.add(simplify(circuit(input, keys1) == output1[0]))
s.add(simplify(circuit(input, keys2) == output2[0]))
print(s.check(output1[0] != output2[0]))
print(s.model())
print()

s.add(simplify(circuit([True, False, True], keys1) == True))
s.add(simplify(circuit([True, False, True], keys2) == True))
print(s.check(output1[0] != output2[0]))
print(s.model())
print()

s.add(simplify(circuit([False, False, False], keys1) ==  False))
s.add(simplify(circuit([False, False, False], keys2) ==  False))
print(s.check(output1[0] == output2[0]))
print(s.model())
print()
