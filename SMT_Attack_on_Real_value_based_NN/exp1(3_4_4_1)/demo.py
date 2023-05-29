from z3 import *

i = Int('i')
s = Tactic('smt').solver()
s.add(i*7.90 == 89.8)
print(s.check())


print(s.model())

