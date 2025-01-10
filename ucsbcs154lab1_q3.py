# ucsbcs154lab1
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

### Implementing and simulating multiplexers in PyRTL ###

import pyrtl
import random

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare five data inputs: a, b, c, d, e
# < add your code here >
val_a = pyrtl.Input(bitwidth=1, name='a')
val_b = pyrtl.Input(bitwidth=1, name='b')
val_c = pyrtl.Input(bitwidth=1, name='c')
val_d = pyrtl.Input(bitwidth=1, name='d')
val_e = pyrtl.Input(bitwidth=1, name='e')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare one output: o 
# < add your code here >
o = pyrtl.Output(bitwidth=1, name='o')

# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
  with s == 0:
    o |= val_a
  with s == 1:
    o |= val_b
  with s == 2:
    o |= val_c
  with s == 3:
    o |= val_d
  with s == 4:
    o |= val_b

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

for cycle in range(16):
    sim.step({
        'a': random.choice([0, 1]),
        'b': random.choice([0, 1]),
        'c': random.choice([0, 1]),
        'd': random.choice([0, 1]),
        'e': random.choice([0, 1]),
        's': random.choice([0, 1])
    })
    
print('--- 3-bit 5:1 MUX ---')
sim_trace.render_trace(symbol_len=1)
o_value = sim.inspect(o)
print(str(o_value))