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

class AudioPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.is_playing = False
    
    def play(self):
        self.is_playing = True
        self.display_status("Playing audio")
    
    def pause(self):
        if self.is_playing:
            self.is_playing = False
            self.display_status("Audio paused")
    
    def stop(self):
        self.is_playing = False
        self.display_status("Audio stopped")

class VideoPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.is_playing = False
        self.display_active = False
    
    def play(self):
        self.is_playing = True
        self.display_active = True
        self.display_status("Playing video")
    
    def pause(self):
        if self.is_playing:
            self.is_playing = False
            self.display_status("Video paused")
    
    def stop(self):
        self.is_playing = False
        self.display_active = False
        self.display_status("Video stopped")
    
    def display_video(self):
        if self.display_active:
            print(f"Displaying video on screen: {self.file_name}")
        else:
            print("Video display is not active")

# Test code
if __name__ == "__main__":
    try:
        # This should raise TypeError
        player = MediaPlayer("test.mp3")
    except TypeError as e:
        print(str(e))
    
    audio = AudioPlayer("song.mp3")
    video = VideoPlayer("movie.mp4")
    
    # Test audio playback
    audio.play()
    audio.pause()
    audio.stop()
    
    # Test video playback
    video.play()
    video.display_video()
    video.stop()
