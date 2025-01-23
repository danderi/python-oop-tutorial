# Building a Cool Media Player System! 🎵

In this exercise, you will learn how to use **abstract classes** in Python to create shared rules among related classes and how to override abstract methods in derived classes to implement specific behaviors, by creating a system that can play music and videos.

Before we start, let's remember that **abstract classes** are templates for other classes. They help ensure that all related classes follow certain rules.

- They contain **abstract methods**, which are like promises and must be defined in the classes that inherit from them.
- You cannot create objects directly from an abstract class.

![abstract-class-image](../../.learn/assets/abstract-class-image-05.png)

## Instructions

1. Create a class called `MediaPlayer`. This class should be abstract, meaning it cannot be used directly. Within this class, define abstract methods called: `play`, `pause`, and `stop`. These methods will not have content, only the names.

2. Create a class called `AudioPlayer` that inherits from `MediaPlayer`. This means that `AudioPlayer` will use the methods from `MediaPlayer`. In `AudioPlayer`, define the methods `play`, `pause`, and `stop` with content. This class will only handle audio files. Example:

```python
class AudioPlayer(MediaPlayer):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def play(self):
        print("Playing audio")
    
    def pause(self):
        print("Audio paused")
    
    def stop(self):
        print("Audio stopped")
```

3. Create a class called `VideoPlayer` that also inherits from `MediaPlayer`. In `VideoPlayer`, define the methods `play`, `pause`, and `stop` with content, just like in `AudioPlayer`.

4. Additionally, add a method called `show_video` to the `VideoPlayer` class that will print a message of the video while it is playing. Example:

```python
"Displaying video on screen: {file_name}"
```

5. **Test your solution.** Create instances of the `AudioPlayer` and `VideoPlayer` classes and verify that they work correctly.

```python
# Example Code
audio = AudioPlayer("song.mp3")
video = VideoPlayer("video.mp4")

audio.play()
audio.pause()
audio.stop()

video.play()
video.show_video()
video.stop()
```


## 💡 Tips

- Use `ABC` and `abstractmethod` from Python's `abc` module.
- Abstract methods are like promises, it's like saying "I'll define this later!"
- Each player must have all the required methods `play`, `pause`, and `stop`.
- Think about what each type of player needs to do.
