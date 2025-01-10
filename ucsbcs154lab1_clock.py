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
output_seconds = pyrtl.Output(bitwidth=6, name="output_seconds") # name="output_seconds"
output_minutes = pyrtl.Output(bitwidth=6, name="output_minutes") # name="output_minutes"
output_hours = pyrtl.Output(bitwidth=5, name="output_hours")   # name="output_hours"

# Initialize Registers Here
seconds = pyrtl.Register(bitwidth=6, name='s')
minutes = pyrtl.Register(bitwidth=6, name='m')
hours = pyrtl.Register(bitwidth=5, name='h')

# Put Sequential Logic Here
# update the seconds register here
with pyrtl.conditional_assignment:
    with seconds == 59:
        seconds.next |= 0
    with pyrtl.otherwise:
        seconds.next |= seconds + 1
    
    


# update the minutes register here
with pyrtl.conditional_assignment:
    with seconds == 59:
        with minutes == 59:
            minutes.next |= 0
        with pyrtl.otherwise:
            minutes.next |= minutes + 1

# update the hours register here
with pyrtl.conditional_assignment:
    with minutes == 59:
        with seconds == 59:
            with hours == 23:
                hours.next |= 0
            with pyrtl.otherwise:
                hours.next |= hours + 1


# Assign your outputs here
output_seconds <<= seconds
output_minutes <<= minutes
output_hours <<= hours


# Simulation Code
if __name__ == "__main__":
    sim_trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=sim_trace)

    for cycle in range(86401): # 10 seconds
        sim.step({})

    ### Uncomment the following line to the whole trace
    # sim_trace.render_trace(repr_func=str)

    ### Uncomment the following lines to see the most recent values of hours, minutes, and seconds
    print("hours:", sim_trace.trace["output_hours"][-1])
    print("minutes:", sim_trace.trace["output_minutes"][-1])
    print("seconds:", sim_trace.trace["output_seconds"][-1])

