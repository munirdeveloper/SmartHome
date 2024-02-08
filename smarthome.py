import random
import datetime
import time

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

class Music:
    def __init__(self, playlist, current_song=None, volume=50, play_music=False, next_song=None, previous_song=None):
        self.current_song = current_song
        self.playlist = playlist
        self.play_music = play_music
        self.volume = volume
        self.next_song = next_song
        self.previous_song = previous_song

    def random_song(self):
        if self.playlist:
            self.current_song = random.choice(self.playlist)

    def print_current_song(self):
        if self.current_song:
            print(f"Currently playing: {self.current_song}")
        else:
            print("No song is currently playing.")

# we are finished with our music class

class Lights:
    def __init__(self, brightness, lights_on=False, lights_off=True):
        self.lights_on = lights_on
        self.lights_off = lights_off
        self.brightness = brightness

    def after_sunset(self, current_time):
        now = datetime.datetime.fromtimestamp(current_time)

        sunset_time = now.replace(hour=18, minute=0, second=0)

        random_offset = datetime.timedelta(minutes=random.randint(0, 30))
        sunset_time += random_offset

        if now >= sunset_time:
            self.lights_on = True
            self.lights_off = False

    def after_sunrise(self, current_time):
        now = datetime.datetime.fromtimestamp(current_time)

        if now.hour == 7 and now.minute == 0:
            self.lights_off = True
            self.lights_on = False

    def print_state(self):
        if self.lights_on:
            print("Lights are On")
        else:
            print("Lights are Off")


# we are finished with our lights class


class Ac:
    def __init__(self, on=True, off=False, temperature=22):
        self.on = on
        self.off = off
        self.temperature = temperature

    def updatetemperature(self):
        while self.on and not self.off:
            new_temperature = random.uniform(20, 25)
            self.temperature = new_temperature
            print(f"The current temperature is {new_temperature} °C")
            time.sleep(3600)

        print("The Ac is off")

# we are finished with our Ac class

if __name__ == "__main__":
    automation_system = AutomationSystem()

    music_player = Music(playlist=["song1", "song2", "song3"])
    lights_controller = Lights(brightness=50)
    ac_controller = Ac()

    automation_system.discover_device(music_player)
    automation_system.discover_device(lights_controller)
    automation_system.discover_device(ac_controller)

    automation_system.run_simulation()


