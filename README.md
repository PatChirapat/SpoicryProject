# Project: Spoticry


## Project overview
Spoticry is an application that you can add songs into your playlist and open your 
favorite songs on web browser.


## Project features
- Create a playlist
- Add songs to playlist
- Delete songs from playlist
- Shuffle songs in playlist
- Open playlist on web browser
- Delete playlist


## Requirements
- Python 3.6 or higher
- time module
- random module
- webbrowser module
- os module


## Program Design
The program is designed to use OOP (Object Oriented Programming) to make it easier 
to understand and to make it easier to add new features in the future, and this program 
start by displaying the main menu. The main menu has 4 options:

- Create a playlist
- Open a playlist on web browser
- Delete playlist
- Show all playlists
- Exit

User can choose one of the options. If the user choose to create a playlist, 
the program will ask for the name of the playlist. Then you can add songs, artist, 
and song's url to the playlist. After you successfully add songs to the playlist,
you can export the information to a json file. You can also shuffle the songs in
your playlist. After you finish creating the playlist, the program will return 
to the main menu then you can choose to open the playlist on web browser or delete 
the playlist or show all playlists or exit the program.


## Code Structure
The program is divided into 4 files:

- main.py

main.py is the main file of the program. It contains the main menu and the main
function to run the program.

- playlist.py

playlist.py contains the class Playlist. The class Playlist contains the methods    
to create a playlist, delete a playlist, shuffle songs in playlist, export playlist
to json file, open playlist on web browser, clear the json file, and show all
playlists.

- song.py

song.py contains the class Song. The class Song contains the methods to add songs
to playlist, delete songs from playlist, and return the song's information.

- ascii_saved.py

ascii_saved.py contains the ascii art.


## How to run the program
To run the program, you can use the command below in the terminal:


First, you need to clone the repository to your local machine:

```
>>> git clone https://github.com/PatChirapat/SpoticryProject.git
```

Then, you need to change the directory to SpoticryProject:

```
>>> cd (file path)
eg. cd /Users/patchirapat_/PycharmProjects/COMPRO1_PROJECT/SpoticryProject
```

After that, you can run the program by using the command below:

```
>>> python main.py or python3 main.py
```


