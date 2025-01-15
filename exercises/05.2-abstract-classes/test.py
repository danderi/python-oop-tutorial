import unittest
from app import MediaPlayer, AudioPlayer, VideoPlayer

class TestMediaPlayer(unittest.TestCase):
    def test_abstract_methods(self):
        with self.assertRaises(TypeError):
            media = MediaPlayer("media.mp4")
            
    def test_audio_player_methods(self):
        audio = AudioPlayer("song.mp3")
        self.assertTrue(hasattr(audio, 'play'))
        self.assertTrue(hasattr(audio, 'pause'))
        self.assertTrue(hasattr(audio, 'stop'))
        audio.play()
        audio.pause()
        audio.stop()

    def test_video_player_methods(self):
        video = VideoPlayer("video.mp4")
        self.assertTrue(hasattr(video, 'play'))
        self.assertTrue(hasattr(video, 'pause'))
        self.assertTrue(hasattr(video, 'stop'))
        self.assertTrue(hasattr(video, 'show_video'))
        video.play()
        video.show_video()
        video.stop()

if __name__ == "__main__":
    unittest.main()