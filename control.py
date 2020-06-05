from control_parameters import ioParameters, AutopilotParameter, ControlParameter, FlightParameter, VesselParameter
from rules import Rule


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

        ioparams = self.fetch_input_parameters()

        name, value = rule(ioparams)

        return name, value


    def update_value(self, value_tuple):

        if len(value_tuple) != 2:
            return Exception()
        else:
            if value_tuple[0] == AutopilotParameter.target_pitch:
                self.vessel.auto_pilot.target_pitch_and_heading( value_tuple[1], self.vessel.auto_pilot.target_heading)

            elif value_tuple[0] == AutopilotParameter.target_direction:

                self.vessel.auto_pilot.reference_frame = self.vessel.orbit.body.reference_frame
                self.vessel.auto_pilot.target_direction= value_tuple[1]

            elif value_tuple[0] == AutopilotParameter.target_heading:

                self.vessel.auto_pilot.target_pitch_and_heading(self.vessel.flight().auto_pilot.target_pitch, value_tuple[1])

            elif value_tuple[0] == AutopilotParameter.target_roll:
                self.vessel.auto_pilot.roll = value_tuple[1]

            elif value_tuple[0] == ControlParameter.throttle:
                self.vessel.control.throttle = value_tuple[1]

            else:
                print("penis")
