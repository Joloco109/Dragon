from control_parameters import inputParameter, ioParameter

def pitch_from_x( v ):
    return arcsin(v[0]/sqrt( v[0]**2 + v[1]**2 + v[2]**2 ))

class Rule:
    @staticmethod
    def const_pitch(rule_parameters, input_parameters):

        return ( ioParameter.pitch,
                 rule_parameters[0])

    @staticmethod
    def rel_pitch(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        pitch = pitch_from_x( input_parameter[ inputParameter.prograde ] )
        return ( ioParameter.pitch,
            pitch + rule_parameters[0] )

    @staticmethod
    def heading(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        return ( ioParameter.heading,
            rule_parameters[0] )
