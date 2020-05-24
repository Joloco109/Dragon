from control_parameters import ioParameters

class Control:

    vessel = None
    conn = None
    ruleset = None
    ref_frame = None

    input_streams = dict()

    def __init__(self, conn, vessel, ruleset, ref_frame):
        self.vessel = vessel
        self.conn = conn
        self.ruleset = ruleset
        self.ref_frame = ref_frame

        for name, unit in  [ ('vessel', vessel),
                ('flight', vessel.flight(ref_frame)),
                ('autopilot', vessel.auto_pilot),
                ('control',vessel.control) ]:

            for parameter in ioParameters[name]:
                new_stream = conn.add_stream( getattr, unit, parameter.name )
                self.input_streams[parameter] = new_stream


    def update(self):
        """
        :return: None
        """

        for rule in self.ruleset:
            new_value = self.handle_rule(rule)
            print(new_value)
            self.update_value(new_value)


    def fetch_input_parameters(self):
        """
        :return: Parameter - Value Dictionary with Vessel Data from streams
        """

        params = dict()

        for key in self.input_streams.keys():
            params[key]= self.input_streams[key]()

        return params

    def handle_rule(self, rule):

        iparams = self.fetch_input_parameters()

        name, value = rule([90], ioparams)

        return name, value


    def update_value(self, value_tupel):

        if len(value_tupel) != 2:
            return Exception()
        else:
            if value_tupel[0] == AutopilotParameter.target_pitch:
                self.vessel.auto_pilot.target_pitch_and_heading( value_tupel[1], self.vessel.auto_pilot.target_heading)
                print("Updated!")

            elif value_tupel[0] == AutopilotParameter.target_direction:

                self.vessel.auto_pilot.reference_frame = self.vessel.orbit.reference_frame
                self.vessel.auto_pilot.target_direction= value_tupel[1]

            elif value_tupel[0] == AutopilotParameter.target_heading:

                self.vessel.auto_pilot.target_pitch_and_heading(self.vessel.flight().auto_pilot.target_pitch, value_tupel[1])

            elif value_tupel[0] == AutopilotParameter.target_roll:
                self.vessel.auto_pilot.roll = value_tupel[1]

            elif value_tuple[0] == ControlParameter.throttle:
                self.vessel.control.throttle = value_tupel[1]

            else:
                print("penis")
