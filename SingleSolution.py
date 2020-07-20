from Accessories import *
from Models.PID04 import *
import matplotlib.pyplot as plt
from math import pi as pi
from numpy import savetxt

# Parameters
P = Parameters
P.P1 = 3.5      # Pressure Amplitude1 [bar]
P.P2 = 29.00    # Frequency1          [kHz]
P.P3 = 0.0      # Pressure Amplitude2 [bar]
P.P4 = 20.0     # Frequency2          [kHz]
P.P5 = 1.5*pi   # Phase Shift         [0-2pi]
P.P6 = 10*1e-6  # Equilibrium Radius  [x*1e-6m = micron]
P.P7 = 1.0      # Ambient Pressure    [bar]
P.P8 = 40.0     # Ambient Temperature [°C]
P.P9 = 1.4      # Polytrophic Exponent
P.Material = Glycerin(P.P8)


P.Material.PrintMaterialProperties()


OP = OperationParameters
OP.TimeDomain = [0, 10]
OP.InitialCondition = [1, 0]

EC = GetEquationConstants(P)


# PrintEquationConstants(EC)


Solution = Solve(P, OP, EC)

savetxt('test.txt', [Solution.t, Solution.y[0], Solution.y[1]], delimiter=',')


plt.figure(1)
plt.plot(Solution.t, Solution.y[0], 'r-', linewidth=2)
plt.xlabel('time')
plt.ylabel('y_1')
plt.grid('both')
plt.show()
