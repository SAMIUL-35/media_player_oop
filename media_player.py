from abc import ABC,abstractmethod

class Description:
    def __init__(self,description) :
        self.__description=description


    def get_description(self):
        return self.__description
    
class Media(ABC):
    def __init__(self,title,duration):
        self.title =title
        self.duration =duration

    @abstractmethod
    def play(self):
        pass 

class Music(Media,Description):
    def __init__(self, title, duration,description):
        Media.__init__(self,title, duration)
        Description.__init__(self,description)

    def play(self):
        print(f"playing title :{self.title} duration;{self.duration} description:{self.get_description()}")

class Video(Media,Description):
    def __init__(self, title, duration,description):
        Media.__init__(self,title, duration)
        Description.__init__(self,description)

    def play(self):
        print(f"playing video : title :{self.title} duration;{self.duration} description:{self.get_description()}")
class Audio_book(Media,Description):
    def __init__(self, title, duration,description):
        Media.__init__(self,title, duration)
        Description.__init__(self,description)

    def play(self):
        print(f"playing audiobook: title :{self.title} duration;{self.duration} description:{self.get_description()}")
class Library:
    def __init__(self) :
        self.__media_items =[]
        self.__media_by_genure ={}
        self.__genure=""

    def get_media_items(self):
        return self.__media_items
    def get_media_by_genure(self):
        return self.__media_by_genure
    def add_media(self,media):
        if isinstance(media,Music):
            self.__genure="Music"
        if isinstance(media,Video):
            self.__genure="Video"
        if isinstance(media,Audio_book):
            self.__genure="Audio_book"
        self.__media_items.append(media)
        if self.__genure in self.__media_by_genure:
            self.__media_by_genure[self.__genure].append(media)

        else:
            self.__media_by_genure[self.__genure]=[media,]

        

class User(ABC):
    def __init__(self,name) :
        self.name = name

    @abstractmethod
    def play_media(self):
        pass 

class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)

    def play_media(self,library):
        for media in library.get_media_items():
            media.play()

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genure=""


    def set_favourite_genure(self,genure):
        self.__favourite_genure=genure
    def get_favourite_genure(self,genure):
        return self.__favourite_genure


    def play_media(self,library):        
        for media in library.get_media_by_genure()[self.__favourite_genure]:
            media.play()




# usages:

library = Library()
music1=Music("nafi","4.00","author:nabil")
music2=Music("nabil","10.00","author:nabil")
video=Video("nafi","44.00","author:p hero")
audiobook=Audio_book("nafi","49.00","author:nabil")

library.add_media(music1)
library.add_media(video)
library.add_media(audiobook)

freeuser=FreeUser("samiul")
premiumuser=PremiumUser("kamol")

# freeuser.play_media(library)
# premiumuser.play_media(library)

premiumuser.set_favourite_genure("Audio_book")
premiumuser.play_media(library)