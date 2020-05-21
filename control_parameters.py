from enum import Enum

inputParameter = Enum( "inputParameter", "\
        position\
        mean_alt\
        surf_alt\
        velocity\
        g_force\
        prograde\
        retrograde\
        dyn_pressure\
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
