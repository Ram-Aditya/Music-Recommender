

class SongLyric:
    def __init__(self,text=None):
        self.text=text
        self.importance_score=0.0
        self.sentiment_tuple=None
    

class Song:
    def __init__(self,title=None):
        self.title=title
        self.artist=None
        self.bpm=None
        self.lyrics=[]
        self.sentiment_tuple=None
        self.energy=0.0

    def sentiment(self):
        temp_tuple=[0 for i in range(4)]
        for lyric in self.lyrics:
            for i in range(len(lyric.sentiment_tuple)):
                temp_tuple[i]+=(lyric.importance_score)*lyric.sentiment_tuple[i]
        for i in range(4):
            temp_tuple[i]/=len(self.lyrics)
        self.sentiment_tuple=tuple(temp_tuple)
        return self.sentiment_tuple
    
    def energy(self):
        pass

def InputText(self):
    def __init__(self,text=None):
        self.text=text
        self.sentiment_tuple=None
        self.energy=0.0

    def energy(self):
        pass

    def sentiment(self):
        pass