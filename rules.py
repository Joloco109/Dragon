from control_parameters import VesselParameter, FlightParameter, ControlParameter, AutopilotParameter

def pitch_from_x( v ):
    return arcsin(v[0]/sqrt( v[0]**2 + v[1]**2 + v[2]**2 ))

class Rule:
    @staticmethod
    def const_pitch(rule_parameters, input_parameters):

        return ( AutopilotParameter.target_pitch,
                 rule_parameters[0])

    @staticmethod
    def rel_pitch(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        pitch = pitch_from_x( input_parameter[ FlightParameter.prograde ] )
        return ( AutopilotParameter.target_pitch,
            pitch + rule_parameters[0] )

    @staticmethod
    def heading(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        return ( Autopilot.target_heading,
            rule_parameters[0] )

    @staticmethod
    def accelaration(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        mass = input_parameter[ VesselParameter.mass ]
        thrust = input_parameter[ VesselParameter.available_thrust ]
        throttle = rule_parameters[0]* mass / thrust
        return ( ControlParameter.throttle,
             throttle )
