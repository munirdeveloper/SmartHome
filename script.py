import random
import datetime
import time

# Import the necessary classes from the smarthome module
from smarthome import Ac, Music, Lights

class AutomationSystem:
    def __init__(self):
        self.devices = []

    def discover_device(self, device):
        self.devices.append(device)

    def execute_automation_tasks(self):
        for device in self.devices:
            if isinstance(device, Music):
                device.random_song()
                device.print_current_song() 
            elif isinstance(device, Lights):
                current_time = time.time()
                device.after_sunset(current_time)
                device.after_sunrise(current_time)
            elif isinstance(device, Ac):
                device.updatetemperature()

    def run_simulation(self, interval=5):
        while True:
            self.execute_automation_tasks()
            time.sleep(interval)

# creating an instance of the AutomationSystem
automation_system = AutomationSystem()

# creating instances of my smarthome devices
playlist = ["Summer Bounce", "The Mood", "Call Jehova", "N B C", "Dang!", "Critical - Cyberspeed mix", "Spin", "SELF LUH"]
music_system = Music(playlist=playlist)
lights = Lights(brightness=50)
ac = Ac()


# addng my devices to the automation system .. 
automation_system.discover_device(music_system)
automation_system.discover_device(lights)
automation_system.discover_device(ac)

if __name__ == "__main__":
    # The simulation loop runs here
    automation_system.run_simulation()

# Testing the simulation
while True:
    music_system.random_song()
    print(f"Current song: {music_system.current_song}")
    current_time = time.time()
    lights.after_sunset()
    lights.print_state()  
    ac.updatetemperature()
    print(f"Current temperature: {ac.temperature}")
    ac.on = False
    print("AC turned off")

