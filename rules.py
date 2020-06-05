from control_parameters import VesselParameter, FlightParameter, ControlParameter, AutopilotParameter
from util import pitch_from_x, vec_abs, map, rad_to_deg, deg_to_rad



class Rule:
    rule_parameters = list()

    def __init__( self, rule_func, rule_parameters ):
        self.rule = rule_func
        self.rule_parameters[:] = rule_parameters

    def __call__( self, input_parameters ):
        return self.rule( self.rule_parameters, input_parameters )


    @staticmethod
    def const_pitch(rule_parameters, input_parameter):

        print(input_parameter[FlightParameter.velocity])

        return ( AutopilotParameter.target_pitch,
                 rule_parameters[0])

    @staticmethod
    def rel_pitch(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """

        if vec_abs(input_parameter[FlightParameter.velocity]) > 100:
            pitch = pitch_from_x(input_parameter[FlightParameter.velocity])
            pitch = rad_to_deg(pitch)
            print(pitch)
        else:
            pitch = 90

        return ( AutopilotParameter.target_pitch,
            pitch + rule_parameters[0] )

    @staticmethod
    def heading(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        return ( AutopilotParameter.target_heading,
            rule_parameters[0] )

    @staticmethod
    def acceleration(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        mass = input_parameter[ VesselParameter.mass ]
        thrust = input_parameter[ VesselParameter.available_thrust ]
        throttle = rule_parameters[0]* mass / thrust


        if throttle > 0.4:
            throttle = map(throttle, (0.4, 1), (0, 1))
        else:
            throttle = 0.01

        return ( ControlParameter.throttle,
             throttle )

    @staticmethod
    def max_q(rule_parameter, input_parameter):
        """

        :param rule_parameter: [(tuple of altitude values), max_Q value]
        :param input_parameter:
        :return:
        """

        Q = input_parameter[FlightParameter.dynamic_pressure]
        throttle = input_parameter[ControlParameter.throttle]
        alt = input_parameter[FlightParameter.mean_altitude]
        if rule_parameter[0][0] < alt < rule_parameter[0][1]:
            if Q > rule_parameter:
                return ( ControlParameter.throttle,
                         throttle - 0.05 )
            else:
                return ( ControlParameter.throttle,
                         throttle )
