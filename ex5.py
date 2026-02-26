import time

class RoboticDrill:
    def lower(self):
        print("Drill lowering...")

    def spin(self):
        print("Drill spinning...")
        time.sleep(3)

    def retract(self):
        print("Drill retracting...")

    def drill_cycle(self):
        self.lower()
        self.spin()
        self.retract()

    def run_pattern(self):
        for i in range(5):
            print(f"Drilling hole {i+1}")
            self.drill_cycle()


drill = RoboticDrill()
drill.run_pattern()