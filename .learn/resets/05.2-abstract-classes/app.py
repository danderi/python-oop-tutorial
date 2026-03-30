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

# Create your VideoPlayer class here
