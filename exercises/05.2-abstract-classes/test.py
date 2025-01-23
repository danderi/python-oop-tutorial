import pytest
from io import StringIO
from unittest.mock import patch


@pytest.mark.it("Should define the abstract class MediaPlayer with abstract methods play, pause, and stop")
def test_media_player():
    from app import MediaPlayer

    assert hasattr(MediaPlayer, 'play'), "MediaPlayer should have an abstract method play"
    assert hasattr(MediaPlayer, 'pause'), "MediaPlayer should have an abstract method pause"
    assert hasattr(MediaPlayer, 'stop'), "MediaPlayer should have an abstract method stop"

@pytest.mark.it("Should define the class AudioPlayer that inherits from MediaPlayer and defines the methods play, pause, and stop")
def test_audio_player():
    from app import AudioPlayer, MediaPlayer
    audio = AudioPlayer("song.mp3")
    assert isinstance(audio, MediaPlayer), "AudioPlayer should inherit from MediaPlayer"
    assert callable(getattr(audio, 'play', None)), "AudioPlayer should have a method play"
    assert callable(getattr(audio, 'pause', None)), "AudioPlayer should have a method pause"
    assert callable(getattr(audio, 'stop', None)), "AudioPlayer should have a method stop"

@pytest.mark.it("Should define the class VideoPlayer that inherits from MediaPlayer and defines the methods play, pause, stop, and show_video")
def test_video_player():
    from app import VideoPlayer, MediaPlayer
    video = VideoPlayer("video.mp4")
    assert isinstance(video, MediaPlayer), "VideoPlayer should inherit from MediaPlayer"
    assert callable(getattr(video, 'play', None)), "VideoPlayer should have a method play"
    assert callable(getattr(video, 'pause', None)), "VideoPlayer should have a method pause"
    assert callable(getattr(video, 'stop', None)), "VideoPlayer should have a method stop"
    assert callable(getattr(video, 'show_video', None)), "VideoPlayer should have a method show_video"



@pytest.mark.it("Should verify that the object audio and video are instances of AudioPlayer and VideoPlayer respectively")
def test_constants_declared():
        import app  
        assert hasattr(app, 'audio'), "The variable 'audio' is not defined in app.py."
        assert hasattr(app, 'video'), "The variable 'video' is not defined in app.py."
