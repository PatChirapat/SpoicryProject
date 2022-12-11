from playlist import Playlist
import ascii_saved
import time
import os
import json
Playlist = Playlist("")


class Main:
    """Main class use to run the program

    Attributes:
        -

    Methods:
        playlist_run: run the program
    """
    @staticmethod
    def playlist_run():
        """Select function for playlist then it will run"""
        print(ascii_saved.ascii_save())
        time.sleep(1)
        print("If you are sad, we are here for you.")
        time.sleep(1)
        print("Now, you can create your sad world!")
        time.sleep(1)
        print("Let's start!")
        time.sleep(1)
        while True:
            print("============================================")
            print("1. Create playlist")
            print("2. Load playlist")
            print("3. Delete playlist")
            print("4. Show all playlist")
            print("5. Exit")
            print("============================================")
            choice = int(input("What do you want to do? "))
            if choice == 1:
                Playlist.playlist_successfully()
                time.sleep(1)
                os.system("clear")
            elif choice == 2:
                with open("playlist.json", "r") as file:
                    data = json.load(file)
                    for _ in data.keys():
                        print(_)
                    load_name = input("Enter name of playlist: ")
                    if load_name in data.keys():
                        Playlist.open_playlist()
                        time.sleep(1)
                        os.system("clear")
            elif choice == 3:
                print("Select mode to delete playlist")
                time.sleep(1)
                os.system("clear")
                while True:
                    print("============================================")
                    print("1. Delete all playlist")
                    print("2. Delete specific playlist")
                    print("============================================")
                    choice = int(input("What do you want to do? "))
                    if choice == 1:
                        Playlist.clear_database()
                        print("Database cleared successfully!")
                        time.sleep(1)
                        os.system("clear")
                        break
                    elif choice == 2:
                        Playlist.del_specific_playlist()
                        time.sleep(1)
                        os.system("clear")
                        break
                    else:
                        print("Invalid choice!")
                        time.sleep(1)
                        os.system("clear")
            elif choice == 4:
                if Playlist.name == "":
                    print("Playlist not found!")
                    time.sleep(1)
                    os.system("clear")
                else:
                    with open("playlist.json", "r") as file:
                        data = json.load(file)
                        print("This is all of your playlist!")
                        for k, v in data.items():
                            print(f"Playlist {k} : {v}")
                    time.sleep(1)
                    os.system("clear")
            elif choice == 5:
                print("Thanks for using Spoticry!")
                Playlist.clear_database()
                break
            else:
                print("Invalid choice!")
                time.sleep(1)
                os.system("clear")


if __name__ == '__main__':
    Main.playlist_run()
