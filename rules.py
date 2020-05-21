from control_parameters import inputParameter, ioParameter

class Rule:
    def rel_pitch( rule_parameters, input_parameter ):
        return ( ioParameter.pitch,
            input_parameter[ ioParameter.pitch ] + rule_parameters[0] )

    def heading( rule_parameters, input_parameter ):
        return ( ioParameter.heading,
            rule_parameters[0] )
