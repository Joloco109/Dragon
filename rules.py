from control_parameters import inputParameter, ioParameter

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
        return ( ioParameter.pitch,
            input_parameter[ ioParameter.pitch ] + rule_parameters[0] )

    @staticmethod
    def heading(rule_parameters, input_parameter):
        """

        :param rule_parameters:
        :param input_parameter:
        :return:
        """
        return ( ioParameter.heading,
            rule_parameters[0] )
