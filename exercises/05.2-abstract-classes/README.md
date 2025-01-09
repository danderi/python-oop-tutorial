# Building a Cool Media Player System! 🎵

Hey! Let's create something fun - a system for playing different types of media, like music and videos. We'll use something called "abstract classes" to make sure everything works together nicely!

## Why Are We Making This? 🎬

Think about your phone or computer:
- You can play different types of files (music, videos, podcasts)
- They all have play, pause, and stop buttons
- But each type of file needs to be handled differently
- Still, you want all your media players to work the same way

This is perfect for learning about abstract classes because:
- We need all players to have the same basic controls
- Each type of player needs to work in its own special way
- We want to make sure nobody forgets to add the important parts

## What We'll Build 🛠️

1. First, we'll create a basic `MediaPlayer` blueprint that says:
   - Every player MUST have play, pause, and stop
   - Every player should show what it's doing
   - Nobody can use this blueprint directly (it's just a guide!)

2. Then we'll make two real players:
   - `AudioPlayer` for playing music and podcasts
   - `VideoPlayer` for playing videos (with an extra display feature!)

3. Each player will:
   - Handle its own type of media properly
   - Tell us what it's doing
   - Follow all the rules from the blueprint

## 💡 Need Help?

- Use `ABC` and `abstractmethod` from Python's `abc` module
- Abstract methods are like promises - "I'll define this later!"
- Every player must have all the required methods
- Think about what each type of player needs to do

## Why Use Abstract Classes? 🤔

Abstract classes are like a cooking recipe:
1. The recipe tells you what ingredients you need
2. But it doesn't cook the food for you
3. You have to follow the recipe to make the dish
4. Different cooks might do things slightly differently

## What Should Happen? 🎯

When you use your media players:
```python
audio = AudioPlayer("song.mp3")
video = VideoPlayer("movie.mp4")

# Play some music
audio.play()    # Shows: "Playing audio: song.mp3"
audio.pause()   # Shows: "Audio paused: song.mp3"
audio.stop()    # Shows: "Audio stopped: song.mp3"

# Watch a video
video.play()          # Shows: "Playing video: movie.mp4"
video.display_video() # Shows: "Displaying video on screen: movie.mp4"
video.stop()          # Shows: "Video stopped: movie.mp4"

# This shouldn't work (good!)
try:
    player = MediaPlayer()  # This should give an error
except TypeError as e:
    print(str(e))
```

Think of it like building different remote controls - they all need certain buttons, but each one works a little differently for its specific device! 🎮