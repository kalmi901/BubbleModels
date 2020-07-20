import math
from scipy.interpolate import interp1d


def getSaturationPressure(t):
    # KDV Correlation Equation
    # Temperature range from 209.15K to 723.00K
    # http://www.cheric.org/research/kdb/hcprop/showcoef.php?cmpid=912&prop=PVP
    # [t] = K (Kelvin)
    # [pvp] kPa
    a = -2.125867e+1
    b = -1.672626e+4
    c = 1.655099e+2
    d = 1.100480e-5

    ln_pvp = a * math.log(t) + b / t + c + d * t**2
    if (t > 723) or (t < 209.15):
        print("Glycerin.getSaturationPressure(t): Ambient Temperature is out of range")

    return math.exp(ln_pvp) * 1000


def getLiquidDensity(t):
    # [t] and [temperature] = °C (Celsius)
    temperature = (0.0,      10.0,     15.0,     20.0,     30.0,     40.0,     54.0,
                   75.5,     99.5,     110.0,    120.0,    130.0,    140.0,    160.0,
                   180.0,    200.0,    220.0,    240.0,    260.0,    280.0,    290.0)

    # [densities] = kg/m**3
    density = (1272.69, 1266.99, 1264.43, 1261.34, 1255.12, 1248.96, 1239.7,
               1225.6,  1209.7,  1201.78, 1194.46, 1187.21, 1179.51, 1164.40,
               1148.64, 1131.78, 1114.93, 1098.57, 1082.68, 1067.25, 1059.69)

    if (t > max(temperature)) or (t < min(temperature)):
        print("Glycerin.getLiquidDensity(t): Ambient Temperature is out of range:"
              + "-> Extrapolated data is used!")

    return interp1d(x=temperature, y=density, kind="linear", bounds_error=False, fill_value="extrapolate")(t)


def getSurfaceTension(t):
    # [t] and [temperature] = °C (Celsius)
    # [surface_tension] = N/m
    temperature = (20.0, 90.0, 150.0)
    surface_tension = (0.0634, 0.0586, 0.0519)

    if (t > max(temperature)) or (t < min(temperature)):
        print("Glycerin.getSurfaceTension(t): Ambient Temperature is out of range:"
              "-> Extrapolated data is used!")

    return interp1d(x=temperature, y=surface_tension, kind="linear", bounds_error=False, fill_value="extrapolate")(t)


def getLiquidDynamicViscosity(t):
    # [t] and [temperature] = °C (Celsius)
    # [viscosity] = Pa*s
    temperature = (0.0,     10.0,  20.0,    30.0,   40.0,   50.0,   60.0,   70.0,   80.0,   90.0,   100.0,
                   110.0,   120.0, 130.0,   140.0,  150.0,  158.0,  167.0,  200.0)

    viscosity = (12.07, 3.9, 1.41, 0.612, 0.284, 0.142, 0.0813, 0.0506, 0.0319, 0.0213, 0.0148,
                 0.01048, 0.007797, 0.005986, 0.004726, 0.003823, 0.003282, 0.002806, 0.00205)

    if (t > max(temperature)) or (t < min(temperature)):
        print("Glycerin.getLiquidDynamicViscosity(t): Ambient Temperature is out of range:"
              + "-> Extrapolated data is used!")

    return interp1d(x=temperature, y=viscosity, kind="linear", bounds_error=False, fill_value="extrapolate")(t)


def getSoundSpeed(t):
    # [t] and [temperature] = °C (Celsius)
    # [sound_speed] = m/s
    temperature = (10.0, 20.0, 30.0, 40.0, 50.0)
    sound_speed = (1941.5, 1923.0, 1905.0, 1886.5, 1869.5)

    if (t > max(temperature)) or (t < min(temperature)):
        print("Glycerin.getSoundSpeed(t): Ambient Temperature is out of range:"
              + "-> Extrapolated data is used!")

    return interp1d(x=temperature, y=sound_speed, kind="linear", bounds_error=False, fill_value="extrapolate")(t)
