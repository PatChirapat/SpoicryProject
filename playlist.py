import json
import random
import os
import time
import webbrowser
from song import Song
Song = Song("", "", "")


class Playlist:
    """This class use for make a playlist and select function for playlist

    Attributes:
        name (str): name of playlist
        song_list (list): list of song

    Methods:
        create_playlist: create a playlist
        shuffle_playlist: shuffle playlist
        respectively_playlist: play playlist
        open_playlist: load playlist
        save_playlist: save playlist to json file
        del_specific_playlist: delete specific playlist
        playlist_successfully: select function to make your playlist
    """

    def __init__(self, name: str):
        """Initialize a playlist

        params:
            name (str): name of playlist
        types:
            name: str
        """
        self.name = name
        self.song_list = [Song]  # list of obj

    @property
    def name(self):
        """Get name of playlist"""
        return self.__name

    @name.setter
    def name(self, name):
        """Set name of playlist"""
        self.__name = name

    def create_playlist(self):
        """Create a playlist"""
        self.name = input("Let's come up with a name for your sad world: ")
        print(f"Playlist {self.name} created successfully!")

    @staticmethod
    def shuffle_playlist():
        """Shuffle song in playlist"""
        random.shuffle(Song.conclude_info())
        msg = "Shuffling..."
        for i in range(len(msg)):
            print(msg[i], end='')
            time.sleep(0.2)
        time.sleep(0.5)
        print()
        for _ in range(len(Song.conclude_info())):
            time.sleep(0.5)
            print(f"{_ + 1} : {Song.conclude_info()[_][0]} by"
                  f" {Song.conclude_info()[_][1]}")

    def save_playlist(self):
        """Save playlist to json file"""
        save = {
            self.name: Song.conclude_info()
        }
        try:
            with open("playlist.json", "r") as file:
                data = json.load(file)
                data.update(save)
        except FileNotFoundError:
            with open("playlist.json", "w") as file:
                json.dump(save, file, indent=4)
        else:
            with open("playlist.json", "w") as file:
                json.dump(data, file, indent=4)

    @staticmethod
    def respectively_playlist():
        """Respectively song in playlist"""
        msg = "Respectively..."
        for i in range(len(msg)):
            print(msg[i], end='')
            time.sleep(0.2)
        time.sleep(0.5)
        print()
        for _ in range(len(Song.conclude_info())):
            time.sleep(0.5)
            print(f"{_ + 1} : {Song.conclude_info()[_][0]} by"
                  f" {Song.conclude_info()[_][1]}")

    @staticmethod
    def open_playlist():
        """open songs in playlist that previously saved"""
        with open("playlist.json", "r") as file:
            data = json.load(file)
            for _ in data.values():
                for __ in _:
                    webbrowser.open_new_tab(__[2])

    @staticmethod
    def clear_database():
        """Clear database"""
        with open("playlist.json", "w") as file:
            json.dump({}, file, indent=4)

    @staticmethod
    def del_specific_playlist():
        """Delete specific playlist"""
        with open("playlist.json", "r") as file:
            data = json.load(file)
            for _ in data.keys():
                print(_)
            del_name = input("Enter name of playlist: ")
            data.pop(del_name)
        with open("playlist.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Playlist deleted successfully!")

    def playlist_successfully(self):
        """Select function to make your playlist """
        self.create_playlist()
        while True:
            print("============================================")
            print("1. Add song")
            print("2. Delete song")
            print("3. Shuffle playlist")
            print("4. Respectively playlist")
            print("5. Show all song")
            print("6. Save playlist")
            print("============================================")
            choice = int(input("What do you want to do? "))
            if choice == 1:
                Song.song_add()
                time.sleep(1)
                os.system("clear")
            elif choice == 2:
                Song.song_delete()
                time.sleep(1)
                os.system("clear")
            elif choice == 3:
                self.shuffle_playlist()
                time.sleep(1)
                os.system("clear")
            elif choice == 4:
                self.respectively_playlist()
                time.sleep(1)
                os.system("clear")
            elif choice == 5:
                print(Song.conclude_info())
                time.sleep(1)
                os.system("clear")
            elif choice == 6:
                self.save_playlist()
                time.sleep(1)
                os.system("clear")
                break
            else:
                print("Invalid choice!")
        msg = "Loading..."
        for i in range(len(msg)):
            print(msg[i], end='')
            time.sleep(0.2)
        time.sleep(0.3)
        Playlist.save_playlist(self)
        print()
        print(f"Playlist {self.name} saved successfully!")
        with open("playlist.json", "r") as file:
            data = json.load(file)
            l = []
            for i in data:
                l.append(i)
            print(f"new update >>> {l[-1]} : {data[l[-1]]}")
        Song.info_list = []
