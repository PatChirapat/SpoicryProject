from song import Song
from playlist import Playlist
import ascii_saved
import time
Song = Song("", "", "", [])
Playlist = Playlist("")


if __name__ == "__main__":
    ascii_saved = ascii_saved.ascii_save()
    time.sleep(1)
    print("If you are sad, we are here for you.")
    time.sleep(1)
    print("Now, you can create your sad world!")
    time.sleep(1)
    print("Let's start!")
    time.sleep(1)
    Playlist.playlist_run()
