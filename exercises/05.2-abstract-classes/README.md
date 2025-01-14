# Building a Cool Media Player System! 🎵

In this exercise, you will learn how to use **abstract classes** in Python to create shared rules among related classes and how to override abstract methods in derived classes to implement specific behaviors, by creating a system that can play music and videos.

Before we start, let's remember that **abstract classes** are templates for other classes. They help ensure that all related classes follow certain rules.

- They contain **abstract methods**, which are like promises and must be defined in the classes that inherit from them.
- You cannot create objects directly from an abstract class.

![abstract-class-image](../../.learn/assets/abstract-class-image-05.png)

## Instructions

1. Define an abstract class called `MediaPlayer`. Make sure to include abstract methods such as: `play`, `pause`, and `stop`.

2. Define a class `AudioPlayer` that inherits from `MediaPlayer` and defines the required methods `play`, `pause`, and `stop`. This class will handle only audio files.

3. Define a class `VideoPlayer` that inherits from `MediaPlayer` and defines the required methods `play`, `pause`, and `stop`, but with an additional function called `show_video` to display the video while it plays.

4. **Test your solution.** Create instances of the `AudioPlayer` and `VideoPlayer` classes and verify that they work correctly.

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
