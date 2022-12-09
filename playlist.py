import json
import random
import os
import time
from song import Song
Song = Song("", "", "", [])


class Playlist:
    """This class use for make a playlist and select function for playlist

    Attributes:
        name (str): name of playlist

    Methods:
        create_playlist: create a playlist
        playlist_run: select function for playlist
    """
    def __init__(self, name: str):
        """Initialize a playlist

        params:
            name (str): name of playlist
        types:
            name: str
        """
        self.name = name

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
            time.sleep(0.3)
        time.sleep(0.5)
        print()
        for _ in range(len(Song.conclude_info())):
            time.sleep(0.5)
            print(f"{_+1} : {Song.conclude_info()[_][0]} by"
                  f" {Song.conclude_info()[_][1]}")

    def save_playlist(self):
        """Save playlist to json file"""
        save = {
            self.name: Song.conclude_info()
        }
        with open("playlist.json", "w") as file:
            json.dump(save, file, indent=4)

    @staticmethod
    def respectively_playlist():
        """Respectively song in playlist"""
        msg = "Respectively..."
        for i in range(len(msg)):
            print(msg[i], end='')
            time.sleep(0.3)
        time.sleep(0.5)
        print()
        for _ in range(len(Song.conclude_info())):
            time.sleep(0.5)
            print(f"{_+1} : {Song.conclude_info()[_][0]} by"
                  f" {Song.conclude_info()[_][1]}")

    def playlist_run(self):
        """Select function for playlist then it will run"""
        self.create_playlist()
        while True:
            print("============================================")
            print("1. Add song")
            print("2. Delete song")
            print("3. Shuffle playlist")
            print("4. Respectively playlist")
            print("5. Show all song")
            print("6. Exit")
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
            time.sleep(0.3)
        time.sleep(0.3)
        self.save_playlist()
        print()
        print(f"Playlist {self.name} saved successfully!")
        with open("playlist.json", "r") as file:
            data = json.load(file)
            for _ in data.values():
                for __ in _:
                    print(f"{__[0]}: {__[1]}")
                    time.sleep(0.5)
