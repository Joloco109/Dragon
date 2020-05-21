from enum import Enum

inputParameter = Enum( "inputParameter", "\
        position\
        mean_altitude\
        surface_altitude\
        velocity\
        g_force\
        prograde\
        retrograde\
        dynamic_pressure\
        sideslip_angle\
        angular_velocity\
    ")

ioParameter = Enum( "ioParameter", "\
        rotation\
        direction\
        pitch\
        heading\
        roll\
    ")
