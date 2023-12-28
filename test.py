from pytube import YouTube
import os
import ffmpeg
from moviepy.editor import *


video = YouTube('https://www.youtube.com/watch?v=C-dvTjK_07c')
print(video.title)

video.streams.filter(only_audio=True).first().download()

#Next we want to get the file name of the file we just downloaded so that we can convert it to mp3
mp4_file = AudioFileClip(video.title + '.mp4')

#Now we finally want to covnert this mp4 file to an mp3 file 
mp4_file.write_audiofile(video.title + '.mp3')