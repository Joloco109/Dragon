import krpc
import config
import time
import threading
from control import Control
from orbital_parameters import OrbitalParameters

class AscendModule:

    update_thread = None

    vessel = None
    conn = None

    target_parameters = None
    actual_parameters = None

    controller = None

    ruleset = None

    finish = False


    def __init__(self, conn, vessel, ruleset):
        self.vessel = vessel
        self.conn = conn
        self.ruleset = ruleset

        self.ref_frame = conn.space_center.ReferenceFrame.create_hybrid(
                position=vessel.orbit.body.reference_frame,
                rotation=vessel.surface_reference_frame)
        self.controller = Control(conn, vessel, ruleset, self.ref_frame)

        self.vessel.auto_pilot.engage()

        self.update_thread = threading.Thread(target=self.update, name="Ascent Update Thread")
        self.update_thread.run()
        print(self.update_thread)

    def set_orbital_parameters(self, params):
        self.target_parameters = params

    def update(self):
        while not self.finish:
            self.actual_parameters = OrbitalParameters(self.vessel)

            if self.actual_parameters == self.target_parameters:
                self.stop()

            self.controller.update()

            time.sleep(0.1)


    def stop(self):

        self.finish = True

        self.update_thread.join(1)
