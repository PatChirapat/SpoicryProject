class Song:
    """This class use for make a song and select function for song
    Attributes:
        title (str): title of song
        artist (str): artist of song
        url (str): url of song
        info_list (list): list of song
    Methods:
        song_add: add a song
        song_delete: delete a song
        conclude_info: return info_list
        export_to_csv: export info_list to csv file
    """

    def __init__(self, title: str, artist: str, url: str, info_list: list):
        """Initialize a song
        params:
            title (str): title of song
            artist (str): artist of song
            url (str): url of song
        types:
            title: str
            artist: str
            url: str
        """
        self.title = title
        self.artist = artist
        self.url = url
        self.title = title
        self.artist = artist
        self.url = url
        self.info_list = info_list

    @property
    def title(self):
        """Get title of song"""
        return self.__title

    @title.setter
    def title(self, title):
        """Set title of song"""
        self.__title = title

    @property
    def artist(self):
        """Get artist of song"""
        return self.__artist

    @artist.setter
    def artist(self, artist):
        """Set artist of song"""
        self.__artist = artist

    @property
    def url(self):
        """Get url of song"""
        return self.__url

    @url.setter
    def url(self, url):
        """Set url of song"""
        self.__url = url

    def song_add(self):
        """Add a song"""
        self.title = input("What do you want to listen to? ")
        self.artist = input("What is the artist name? ")
        self.url = input("What is the song's url? ")
        if self.title not in self.info_list:
            self.info_list.append([self.title, self.artist, self.url])
            print(f"{self.title} added successfully!")
        else:
            print("This song already exists!")

    def song_delete(self):
        """Delete a song"""
        if len(self.info_list) == 0:
            print("It is empty!, add your song first! ")
        else:
            self.title = input("What song do u wanna delete? ")
            for _ in self.info_list:
                if self.title in _:
                    self.info_list.remove(_)
                    print(f"{self.title} deleted successfully!")

    def conclude_info(self):
        """Return info_list"""
        return self.info_list
