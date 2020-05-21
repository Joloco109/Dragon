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
            parameter_name = str(parameter).split(".")[1]
            new_stream = conn.add_stream(getattr, vessel.flight(), parameter_name)

            self.input_streams[parameter] = new_stream




    def set_target_velocity(self, velocity):
        #brief: Burns the Engines until target velocity is reached


    def update(self):

        for rule in self.ruleset:
            new_value = self.handle_rule(rule)
            self.update_value(new_value)


    def fetch_parameter_values(self):

        params = dict()

        for parameter, stream in self.input_streams:
            params[parameter] = stream()

        return params



    def handle_rule(self, rule):

        params = self.fetch_parameter_values()
        name, value = rule(params)

        return tuple(name, value)


    def update_value(self, value):

        if len(value) > 2:
            return Exception()
        else:
            if value[0] == "pitch":
                self.vessel.auto_pilot.target_pitch_and_heading(self.vessel.auto_pilot.heading, value[1])
            else:
                print("penis")