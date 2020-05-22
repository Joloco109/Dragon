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
                new_stream = conn.add_stream(getattr, vessel.flight(), parameter_name)
            elif parameter == inputParameter.angular_velocity:
                new_stream = conn.add_stream(vessel.angular_velocity, self.vessel.orbital_reference_frame)
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

    def fetch_io_parameters(self):

        params = dict()

        params[ioParameter.rotation] = self.vessel.flight().rotation
        params[ioParameter.direction] = self.vessel.flight().direction
        params[ioParameter.pitch] = self.vessel.flight().pitch
        params[ioParameter.heading] = self.vessel.flight().heading
        params[ioParameter.roll] = self.vessel.flight().roll
        params[ioParameter.throttle] = self.vessel.control.throttle

        return params


    def handle_rule(self, rule):

        iparams = self.fetch_input_parameters()
        ioparams = self.fetch_io_parameters()

        name, value = rule([90], {**ioparams  ,**iparams})

        return name, value


    def update_value(self, value_tupel):

        if len(value_tupel) != 2:
            return Exception()
        else:
            if value_tupel[0] == ioParameter.pitch:
                self.vessel.auto_pilot.target_pitch_and_heading( value_tupel[1], self.vessel.auto_pilot.target_heading)
                print("Updated!")
            elif value_tupel[0] == ioParameter.rotation:
                #TODO: Quaternion Scheiße

                self.vessel.auto_pilot.roll = value_tupel[1]

            elif value_tupel[0] == ioParameter.direction:

                self.vessel.auto_pilot.reference_frame = self.vessel.orbit.reference_frame
                self.vessel.auto_pilot.target_direction= value_tupel[1]

            elif value_tupel[0] == ioParameter.heading:

                self.vessel.auto_pilot.target_pitch_and_heading(self.vessel.flight().auto_pilot.target_pitch, value_tupel[1])

            elif value_tupel[0] == ioParameter.roll:
                self.vessel.auto_pilot.roll = value_tupel[1]
            else:
                print("penis")