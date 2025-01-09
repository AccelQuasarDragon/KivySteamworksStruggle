import os
os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
print("what's wrong with init?", steamworks.initialize())

my_steam64 = steamworks.Users.GetSteamID()
my_steam_level = steamworks.Users.GetPlayerSteamLevel()

print(f'Logged on as {my_steam64}, level: {my_steam_level}')
print('Is subscribed to current app?', steamworks.Apps.IsSubscribed())

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

kvString = '''
#:import steam steamworks
SteamButton:
    text: "shift + tab is lagging"
    
'''

class SteamButton(Button):
    def on_release(self, *args): 
        steamworks.Friends.ActivateGameOverlay()

class KivySteamOverlay(App):
    def build(self, *args):
        Window.always_on_top = True
        return Builder.load_string(kvString)

if __name__ == "__main__":
    KivySteamOverlay().run()