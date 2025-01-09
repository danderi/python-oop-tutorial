# Abstract Base Classes and Interfaces

## 📝 Instructions

1. Create an abstract base class called `MediaPlayer` using Python's `abc` module with:
   - Abstract method `play()`
   - Abstract method `pause()`
   - Abstract method `stop()`
   - Concrete method `display_status(status)` that prints the current playback status

2. Create two concrete classes that implement `MediaPlayer`:
   - `AudioPlayer` for handling audio files
   - `VideoPlayer` for handling video files with an additional `display_video()` method

3. Each implementation should:
   - Override all abstract methods with appropriate implementations
   - Include proper status messages for each action
   - Handle format-specific features (e.g., video display for VideoPlayer)

## 💡 Hints

- Import `ABC` and `abstractmethod` from the `abc` module
- Abstract methods must be implemented by concrete classes
- Use descriptive status messages for each action
- Remember to call `super().__init__()` in derived classes

## Why Abstract Base Classes?

Abstract base classes in Python:
1. Define a common interface for related classes
2. Enforce implementation of required methods
3. Provide a way to share code between classes
4. Help maintain consistent behavior across implementations

## Expected Output
```python
audio = AudioPlayer("song.mp3")
video = VideoPlayer("movie.mp4")

# Audio playback
audio.play()    # Should print: "Playing audio: song.mp3"
audio.pause()   # Should print: "Audio paused: song.mp3"
audio.stop()    # Should print: "Audio stopped: song.mp3"

# Video playback
video.play()    # Should print: "Playing video: movie.mp4"
video.display_video()  # Should print: "Displaying video on screen: movie.mp4"
video.stop()    # Should print: "Video stopped: movie.mp4"

# This should raise TypeError
try:
    player = MediaPlayer()  # Should raise TypeError - can't instantiate abstract class
except TypeError as e:
    print(str(e))
```
