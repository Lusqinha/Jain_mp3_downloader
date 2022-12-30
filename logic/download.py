from pytube import YouTube, Playlist, Search
from shutil import move, make_archive
from glob import glob
import os

class Download:
    def convert_to_mp3(self):
        for mp4 in glob("*.mp4"):
            file_name, _ = os.path.splitext(mp4)
            new_file_name = file_name + ".mp3"
            os.rename(mp4, new_file_name)
            print(f"Renamed {mp4} to {new_file_name}")
            
    def get_mp3(self):
        return glob("*.mp3")[0]
    
    def get_all_mp3(self):
        return glob("*.mp3")
    
    def clear(self):
        for mp3 in glob('mp3/*.mp3'):
            os.remove(mp3)
            print(f"Removed {mp3} from mp3 folder")
        for mp3 in glob("*.mp3"):
            os.remove(mp3)
            print(f"Removed {mp3}")
        for mp4 in glob("*.mp4"):
            os.remove(mp4)
            print(f"Removed {mp4}")
        for zip in glob("*.zip"):
            os.remove(zip)
            print(f"Removed {zip}")
        

class LinkDownload(Download):
    def __init__(self):
        super().__init__()
        print("Link iniciado")
        self.youtube = None
    
    def get_name(self):
        return f"{self.youtube.title} - {self.youtube.author}"
    
    def download(self, url):
        self.clear()
        self.youtube = YouTube(url)
        self.youtube.streams.filter(only_audio=True).first().download()
        self.convert_to_mp3()
        return self.get_mp3()


class SearchDownload(Download):
    def __init__(self):
        super().__init__()
        print("Search iniciado")
        self.search = None
        self.video = None
    
    def get_name(self):
        return f"{self.search.results[0].title} - {self.search.results[0].author}"

    def get_link(self):
        link = 'https://www.youtube.com/watch?v=' + getattr(self.search.results[0], 'video_id')
        print(f"Link: {link}")
        return link
    
    def download(self, query):
        self.clear()
        self.search = Search(query)
        self.video = self.search.results[0].streams.filter(only_audio=True).first()
        self.video.download()
        self.convert_to_mp3()
        return self.get_mp3()

class PlaylistDownload(Download):
    def __init__(self):
        super().__init__()
        print("Playlist iniciado")
        self.playlist = None
    
    def get_name(self):
        return f"{self.playlist.title} - {self.playlist.author}"
    
    def get_zip(self):
        file_name = 'Playlist'
        directory = 'mp3'
        for song in glob("*.mp3"):
            move(song, directory)
        make_archive(file_name, 'zip', directory)
        return f"{file_name}.zip"
        
    
    def download(self, url):
        self.clear()
        self.playlist = Playlist(url)
        for video in self.playlist.videos:
            video.streams.filter(only_audio=True).first().download()
            print(f"Downloaded {video.title} - {video.author}")
        self.convert_to_mp3()
        return self.get_all_mp3()
    
    