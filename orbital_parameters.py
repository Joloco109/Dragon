class OrbitalParameters:
    apoapsis = int
    periapsis = float
    inclination = float
    eccentricity = float

    def __init__(self, apoapsis: float, periapsis: float, inclination: float, eccentricity: float):

        self.apoapsis: float = apoapsis
        self.periapsis: float = periapsis
        self.inclination: float = inclination
        self.eccentricity: float = eccentricity

    def __init__(self, vessel):
        self.apoapsis: float = vessel.orbit.apoapsis
        self.periapsis: float = vessel.orbit.periapsis
        self.inclination: float = vessel.orbit.inclination
        self.eccentricity: float = vessel.orbit.eccentricity

    def __eq__(self, other):

        #TODO: Define logic to determine if Orbits are approximately the same

        return False