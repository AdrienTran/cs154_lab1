# ucsbcs154lab1
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

import pyrtl
# Simple example of 1-bit 2:1 mux

val_a = pyrtl.Input(bitwidth=1, name='a')
val_b = pyrtl.Input(bitwidth=1, name='b')
select = pyrtl.Input(bitwidth=1, name='s')
result = pyrtl.Output(bitwidth=1, name='o_wg')

# Important: Assignments inside a "conditional_assignment"
# are done with "|=" instead of the usual "<<="
result <<= (~select & val_a) | (select & val_b)