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
output1 = Bool('out1')
output2 = Bool('out2')

s = Tactic('smt').solver()

def xnor(a, b):
    return Or(And(a, b), And(Not(a), Not(b)))

def xor(a, b):
    return Or(And(a, Not(b)), And(Not(a), b))

def circuit(input, keys):
    return xor(keys[1], Or(And(input[0], input[1]), And(input[2], input[1]), xnor(keys[0], And(input[0], input[2]))))

s.add(circuit(input, keys1) == output1)
s.add(circuit(input, keys2) == output2)

s.add(circuit([True, False, True], keys1) == True)
s.add(circuit([True, False, True], keys2) == True)

s.add(circuit([False, True, True], keys1) == True)
s.add(circuit([False, True, True], keys2) == True)

print(s.check(output1 == output2))
print(s.model())
