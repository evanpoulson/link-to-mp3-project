from pytube import YouTube
import os
#This little bit of code is what stackoverflow told me would get moviepy to work
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from moviepy.editor import *

#The purpose of this script is to take the youtube url input by the user, and download an mp3 file of the audio from the youtube video
#We want to make sure that we run this whole program in a try except block to ensure that crashing does not occur
try:
    #For now we're going to use an usher song to test our program until I learn enough html to do the rest
    video_url = 'https://www.youtube.com/watch?v=C-dvTjK_07c'
    video = YouTube(video_url)

    #Now that we have the video, we want to get the mp4 audio file that is included in the video file
    audio_mp4 = video.streams.filter(only_audio=True,file_extension='mp4')[0]

except:
    #This is the block we will run if something happens along the way, eventually we'll add support for different types of exceptions, but for now we're just handling all as the same
    print('Oops! An error happened somewhere along the way :(')