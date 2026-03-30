from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    """Abstract base class for media players"""
    def __init__(self, file_name):
        self.file_name = file_name
    
    @abstractmethod
    def play(self):
        """Start playing the media"""
        pass
    
    @abstractmethod
    def pause(self):
        """Pause the media playback"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the media playback"""
        pass
    
    def display_status(self, status):
        """Display the current playback status"""
        print(f"{status}: {self.file_name}")

# Create your AudioPlayer class here
class AudioPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def play(self):
        print("Playing audio")
        self.display_status("Playing")
    
    def pause(self):
        print("Audio paused")
        self.display_status("Paused")
    
    def stop(self):
        print("Audio stopped")
        self.display_status("Stopped")

# Create your VideoPlayer class here
class VideoPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def play(self):
        print("Playing video")
        self.display_status("Playing")
    
    def pause(self):
        print("Video paused")
        self.display_status("Paused")
    
    def stop(self):
        print("Video stopped")
        self.display_status("Stopped")
    
    def show_video(self):
        print(f"Displaying video on screen: {self.file_name}")

audio = AudioPlayer("song.mp3")
video = VideoPlayer("video.mp4")