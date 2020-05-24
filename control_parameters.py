from enum import Enum, auto

class FlightParameter (Enum):
        center_of_mass = auto()
        mean_altitude = auto()
        surface_altitude = auto()
        velocity = auto()
        g_force = auto()
        prograde = auto()
        retrograde = auto()
        dynamic_pressure = auto()
        sideslip_angle = auto()
        rotation = auto()
        direction = auto()
        pitch = auto()
        heading = auto()
        roll = auto()

class VesselParameter (Enum):
        mass = auto()
        #angular_velocity = auto()
        available_thrust = auto()
        inertia_tensor = auto()

class AutopilotParameter (Enum):
        target_direction = auto()
        target_pitch = auto()
        target_heading = auto()
        target_roll = auto()

class ControlParameter(Enum):
        throttle = auto()

ioParameters = {
        'vessel' : VesselParameter,
        'flight' : FlightParameter,
        'control' : ControlParameter,
        'autopilot' : AutopilotParameter,
    }
