from control_parameters import ioParameter, inputParameter

class Control:

    vessel = None
    conn = None
    ruleset = None

    input_streams = dict()

    def __init__(self, conn, vessel, ruleset):
        self.vessel = vessel
        self.conn = conn
        self.ruleset = ruleset

        for parameter in inputParameter:
            if parameter == inputParameter.position:
                parameter_name = "center_of_mass"
            else:
                parameter_name = str(parameter).split(".")[1]

            new_stream = conn.add_stream(getattr, vessel.flight(), parameter_name)

            self.input_streams[parameter] = new_stream


    def update(self):
        """
        :return: None
        """

        for rule in self.ruleset:
            new_value = self.handle_rule(rule)
            self.update_value(new_value)


    def fetch_parameter_values(self):
        """
        :return: Parameter - Value Dictionary with Vessel Data from streams
        """

        params = dict()

        for parameter, stream in self.input_streams:
            params[parameter] = stream()

        return params


    def handle_rule(self, rule):

        #TODO: Fetch IO Params from Vessel

        iparams = self.fetch_parameter_values()
        ioparams = None

        name, value = rule(ioparams, iparams)

        return name, value


    def update_value(self, value_tupel):

        if len(value_tupel) != 2:
            return Exception()
        else:
            if value_tupel[0] == ioParameter.pitch:
                self.vessel.auto_pilot.target_pitch_and_heading(self.vessel.auto_pilot.heading, value_tupel[1])
            elif value_tupel[0] == ioParameter.rotation:
                #TODO: Quaternion Scheiße

                self.vessel.auto_pilot.roll = value_tupel[1]

            elif value_tupel[0] == ioParameter.direction:

                self.vessel.auto_pilot.reference_frame = self.vessel.orbit.reference_frame
                self.vessel.auto_pilot.target_direction= value_tupel[1]

            elif value_tupel[0] == ioParameter.heading:

                self.vessel.auto_pilot.target_pitch_and_heading(value_tupel[1], self.vessel.autp_pilot.pitch)

            elif value_tupel[0] == ioParameter.roll:
                self.vessel.auto_pilot.roll = value_tupel[1]
            else:
                print("penis")