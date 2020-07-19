from Accessories import *
from Models.PID04_BLA import *
import matplotlib.pyplot as plt
from math import pi as pi
from numpy import savetxt

# Parameters
P = Parameters
P.P1 = 1.0      # Pressure Amplitude1 [bar]
P.P2 = 200.0    # Frequency1          [kHz]
P.P3 = 0.5      # Pressure Amplitude2 [bar]
P.P4 = 20.0     # Frequency2          [kHz]
P.P5 = 1.0*pi   # Phase Shift         [0-2pi]
P.P6 = 10*1e-6  # Equilibrium Radius  [x*1e-6m = micron]
P.P7 = 1.0      # Ambient Pressure    [bar]
P.P8 = 20.0     # Ambient Temperature [°C]
P.P9 = 1.4      # Polytrophic Exponent
P.Mode = 3      # Spherical Mode
# P.Material = Water()


# P.Material.PrintMaterialProperties()

OP = OperationParameters
OP.TimeDomain = [0, 10]
OP.InitialCondition = [1, 0, 1e-4, 0]

EC = GetEquationConstants(P)


# PrintEquationConstants(EC)


Solution = Solve(P, OP, EC)

savetxt('test.txt', [Solution.t, Solution.y[0], Solution.y[1]], delimiter=',')


plt.figure(1, figsize=(10.4, 4.8))
plt.subplots_adjust(0.06, 0.1, 0.98, 0.95)
plt.subplot(1, 2, 1)
plt.plot(Solution.t, Solution.y[0], 'r-', linewidth=2)
plt.xlabel(r'$\tau$')
plt.ylabel(r'$y_1$')
plt.grid('both')

plt.subplot(1, 2, 2)
plt.plot(Solution.t, [abs(Solution.y[3][i]/Solution.y[0][i]) for i in range(0, len(Solution.t))], 'b-', linewidth=2)
plt.yscale("log")
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\dfrac{a_n}{y_1}$')
plt.grid('both')
plt.show()
