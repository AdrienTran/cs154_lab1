# ucsbcs154lab1
# All Rights Reserved
# Copyright (c) 2023 Regents of the University of California
# Distribution Prohibited

import pyrtl
"""
In this lab, You want to create a digital clock that counts the second, minutes, and hours of the day in 24h time
Each cycle corresponds to 1 second
the maximum time on the clock should be 23:59:59 after that it should revert back to 0

Key ideas:
How many bits do you need to represent the time? (You want to use the minimum amount of bits to represent the clock)
How do you update registers?
"""
# Initialize outputs
output_seconds = pyrtl.Output(...) # name="output_seconds"
output_minutes = pyrtl.Output(...) # name="output_minutes"
output_hours = pyrtl.Output(...)   # name="output_hours"

# Initialize Registers Here
seconds = pyrtl.Register(...)
minutes = pyrtl.Register(...)
hours = pyrtl.Register(...)

# Put Sequential Logic Here
# update the seconds register here
with pyrtl.conditional_assignment:
    ...


# update the minutes register here
with pyrtl.conditional_assignment:
    ...

# update the hours register here
with pyrtl.conditional_assignment:
    ...


# Assign your outputs here



# Simulation Code
if __name__ == "__main__":
    sim_trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=sim_trace)

    for cycle in range(10): # 10 seconds
        sim.step({})

    ### Uncomment the following line to the whole trace
    # sim_trace.render_trace(repr_func=str)

    ### Uncomment the following lines to see the most recent values of hours, minutes, and seconds
    # print("hours:", sim_trace.trace["output_hours"][-1])
    # print("minutes:", sim_trace.trace["output_minutes"][-1])
    # print("seconds:", sim_trace.trace["output_seconds"][-1])

