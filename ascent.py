import krpc
import config
from control import Control
from orbital_parameters import OrbitalParameters

class AscendModule:

    vessel = None
    conn = None

    target_parameters = None
    actual_parameters = None

    controller = None

    ruleset = None


    def __init__(self, conn, vessel, ruleset):
        self.vessel = vessel
        self.conn = conn
        self.ruleset = ruleset

        self.controller = Control(conn, vessel, ruleset)

    def set_orbital_parameters(self, params):
        self.target_parameters = params

    def update(self):

        self.actual_parameters = OrbitalParameters(self.vessel)

        self.controller.update()
