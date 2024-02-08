import tkinter as tk
from tkinter import ttk
from smarthome import Ac, Music, Lights, AutomationSystem
import random
import time

class SmartHomeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Home Control")
        
        # Create an instance of AutomationSystem
        self.automation_system = AutomationSystem()
        
        # Create instances of devices
        playlist = ["Summer Bounce", "The Mood", "Call Jehova", "N B C", "Dang!", "Critical - Cyberspeed mix", "Spin", "SELF LUH"]
        self.music_system = Music(playlist=playlist)
        self.lights = Lights(brightness=50)
        self.ac = Ac()

        # Add devices to the automation system
        self.automation_system.discover_device(self.music_system)
        self.automation_system.discover_device(self.lights)
        self.automation_system.discover_device(self.ac)

        # Create GUI components
        self.music_button = ttk.Button(master, text="Toggle Music", command=self.toggle_music)
        self.lights_button = ttk.Button(master, text="Toggle Lights", command=self.toggle_lights)
        self.ac_button = ttk.Button(master, text="Toggle AC", command=self.toggle_ac)

        self.brightness_label = ttk.Label(master, text="Brightness:")
        self.brightness_slider = ttk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_brightness)

        self.temperature_label = ttk.Label(master, text="Temperature:")
        self.temperature_slider = ttk.Scale(master, from_=15, to=30, orient=tk.HORIZONTAL, command=self.update_temperature)

        self.volume_label = ttk.Label(master, text="Volume:")
        self.volume_slider = ttk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_volume)

        # Place GUI components on the grid
        self.music_button.grid(row=0, column=0, pady=10)
        self.lights_button.grid(row=0, column=1, pady=10)
        self.ac_button.grid(row=0, column=2, pady=10)

        self.brightness_label.grid(row=1, column=0, pady=5)
        self.brightness_slider.grid(row=1, column=1, pady=5)

        self.temperature_label.grid(row=2, column=0, pady=5)
        self.temperature_slider.grid(row=2, column=1, pady=5)

        self.volume_label.grid(row=3, column=0, pady=5)
        self.volume_slider.grid(row=3, column=1, pady=5)

    def toggle_music(self):
        self.music_system.play_music = not self.music_system.play_music
        self.music_system.random_song()
        self.music_system.print_current_song()

    def toggle_lights(self):
        self.lights.lights_on = not self.lights.lights_on
        self.lights.lights_off = not self.lights.lights_off
        self.lights.print_state()

    def toggle_ac(self):
        self.ac.on = not self.ac.on
        if self.ac.on:
            self.ac.updatetemperature()
            print(f"The current temperature is {self.ac.temperature} °C")
        else:
            print("The AC is off")

    def update_brightness(self, value):
        self.lights.brightness = float(value)
        print(f"Set brightness to {self.lights.brightness}")

    def update_temperature(self, value):
        self.ac.temperature = float(value)
        print(f"Set temperature to {self.ac.temperature} °C")

    def update_volume(self, value):
        self.music_system.volume = float(value)
        print(f"Set volume to {self.music_system.volume}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
