# PID = 04 (Keller-Miksis equation)
# TODO: ADD description Here
from scipy.integrate import solve_ivp
import math


def Solve(p, op, ec):
    return solve_ivp(__PID04_ODE,
                     op.TimeDomain,
                     op.InitialCondition,
                     method='RK45',
                     dense_output=False,
                     args=(ec,),
                     rtol=op.RelativeTolerance,
                     atol=op.AbsoluteTolerance)


def __PID04_ODE(t, x, ec):
    # ODE Function
    # dx = [0] * 2  # second order ODE
    dx = [0 for _ in range(0, 2)]
    rx1 = 1.0 / x[0]
    p = rx1**ec[10]
    s1 = math.sin(2.0 * math.pi * t)
    c1 = math.cos(2.0 * math.pi * t)
    s2 = math.sin(2.0 * ec[11] * math.pi * t + ec[12])
    c2 = math.cos(2.0 * ec[11] * math.pi * t + ec[12])

    n = (ec[0] + ec[1] * x[1]) * p - ec[2] * (1.0 + ec[9] * x[1]) - ec[3] * rx1 - ec[4] * x[1] * rx1 - 1.5 * (
            1.0 - ec[9] * x[1] / 3.0) * x[1] * x[1] - (ec[5] * s1 + ec[6] * s2) * (1.0 + ec[9] * x[1]) - x[0] * (
                ec[7] * c1 + ec[8] * c2)
    d = x[0] - ec[9] * x[0] * x[1] + ec[4] * ec[9]
    rd = 1.0 / d
    dx[0] = x[1]
    dx[1] = n * rd
    # print((ec[5] * s1 + ec[6] * s2))
    # input("wait")
    return dx


def GetEquationConstants(p):
    # Covert variables to SI
    # Pressures
    p_inf = p.P7 * 1e5  # ambient pressure [Pa]
    pa1 = p.P1 * 1e5  # Pressure Amplitude1 [Pa]
    pa2 = p.P3 * 1e5  # Pressure Amplitude2 [Pa]

    # Frequencies
    f1 = 2 * math.pi * p.P2 * 1000  # angular frequency1 [rad/s]
    f2 = 2 * math.pi * p.P4 * 1000  # angular frequency2 [rad/s]
    ec = [0] * 17  # Equation Constants

    ec[0] = (2 * p.Material.ST / p.P6 + p_inf - p.Material.Pv) * \
            (2.0 * math.pi / p.P6 / f1) ** 2 / p.Material.Rho
    ec[1] = (1 - 3.0 * p.P9) * (2 * p.Material.ST / p.P6 + p_inf - p.Material.Pv) * \
            (2.0 * math.pi / p.P6 / f1) / p.Material.CL / p.Material.Rho
    ec[2] = (p_inf - p.Material.Pv) * (2.0 * math.pi / p.P6 / f1) ** 2 / p.Material.Rho
    ec[3] = (2 * p.Material.ST / p.P6 / p.Material.Rho) * (2.0 * math.pi / p.P6 / f1) ** 2
    ec[4] = (4 * p.Material.Vis / p.Material.Rho / p.P6 ** 2) * (2.0 * math.pi / f1)
    ec[5] = pa1 * (2.0 * math.pi / p.P6 / f1) ** 2 / p.Material.Rho
    ec[6] = pa2 * (2.0 * math.pi / p.P6 / f1) ** 2 / p.Material.Rho
    ec[7] = (p.P6 * f1 * pa1 / p.Material.Rho / p.Material.CL) * (2.0 * math.pi / p.P6 / f1) ** 2
    ec[8] = (p.P6 * f2 * pa2 / p.Material.Rho / p.Material.CL) * (2.0 * math.pi / p.P6 / f1) ** 2
    ec[9] = p.P6 * f1 / (2.0 * math.pi) / p.Material.CL
    ec[10] = 3.0 * p.P9
    ec[11] = p.P4 / p.P2
    ec[12] = p.P5
    ec[13] = 2.0 * math.pi / f1  # t_ref
    ec[14] = p.P6  # R_ref
    ec[15] = f1  # omega1
    ec[16] = f2  # omega2

    return tuple(ec)
