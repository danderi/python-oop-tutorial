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
    

class AudioPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def play(self):
        print("Playing audio")
    
    def pause(self):
        print("Audio paused")
    
    def stop(self):
        print("Audio stopped")

class VideoPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def play(self):
        print("Playing video")
    
    def pause(self):
        print("Video paused")
    
    def stop(self):
        print("Video stopped")

    def show_video(self):
        print(f"🎬 Displaying video on screen: {self.file_name}")
    

# Test code
if __name__ == "__main__":
    audio = AudioPlayer("song.mp3")
    video = VideoPlayer("video.mp4")

    audio.play()
    audio.pause()
    audio.stop()

    video.play()
    video.show_video()
    video.stop()
