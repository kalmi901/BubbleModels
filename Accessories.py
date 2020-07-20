import math
CelsiusToKelvin = 273.14


class MaterialProperties:
    # Default variables (water 20°C)
    MatName = "Water (default)"
    Pv: float = 3.166775638952003e+03       # Vapour pressure
    Rho: float = 9.970639504998557e+02      # Liquid Density
    ST: float = 0.071977583160056           # Surface Tension
    Vis: float = 8.902125058209557e-04      # Dynamic Viscosity
    CL: float = 1.497251785455527e+03       # Sound Speed

    def PrintMaterialProperties(self):
        print("\nMaterial Properties " + ": " + self.MatName)
        print("Vapor Pressure    = " + f"{self.Pv:.3e}" + " Pa")
        print("Liquid Density    = " + f"{self.Rho:.3e}" + " kg/m**3")
        print("Surface Tension   = " + f"{self.ST:.3e}" + " N/m (J/m**2)")
        print("Dynamic Viscosity = " + f"{self.Vis:.3e}" + " Pa*s")
        print("Sound Speed       = " + f"{self.CL:.3e}" + " m/s")
        print("---------------------------------------------- \n")


class Water(MaterialProperties):
    def __init__(self):
        print("Material Properties: Water")


class Glycerin(MaterialProperties):
    def __init__(self, t):
        # Material Properties depend on the ambient temperature (t)
        import Materials.Glycerin as MatProp
        self.MatName = "Glycerin"
        self.Pv = MatProp.getSaturationPressure(t+CelsiusToKelvin)
        self.Rho = MatProp.getLiquidDensity(t)
        self.ST = MatProp.getSurfaceTension(t)
        self.Vis = MatProp.getLiquidDynamicViscosity(t)
        self.CL = MatProp.getSoundSpeed(t)


class Parameters:
    # The class variables are initialized with default values
    P1: float = 1.0     # bar
    P2: float = 20      # kHz
    P3: float = 1.0     # bar
    P4: float = 20      # kHZ
    P5: float = 0       # -
    P6: float = 1*1e-6  # m
    P7: float = 1       # bar
    P8: float = 20      # °C
    P9: float = 1.4
    Material: MaterialProperties = MaterialProperties()


class OperationParameters:
    # The class variables are initialized with default values
    AbsoluteTolerance = 1e-12
    RelativeTolerance = 1e-12
    TimeDomain = [0, 1]
    InitialCondition = [1, 0]


def PrintEquationConstants(c):
    print("Equation Constants")
    for i in range(0, len(c)):
        print("EC[" + f"{i:.0f}" + "] = " + f"{c[i]:.3e}")
    print("----------------------------------\n")


def LinearDampedFrequency(p):
    omega = (3 * p.P9 * (p.P7*1e5 - p.Material.Pv) / p.Material.Rho / p.P6**2 +
             2 * (3 * p.P9 - 1) * p.Material.ST / p.Material.Rho / p.P6**3)**0.5    # rad/s

    frequency = omega/(2*math.pi) / 1000    # kHz

    return omega, frequency
