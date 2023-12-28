#This is a python script developed to use a simple user interface to obtain a youtube link from the user, and download the mp3 audio file of the videos audio into the same directory as this script is contained in
from gooey import Gooey, GooeyParser
from pytube import YouTube
import os
#This little bit of code is what stackoverflow told me would get moviepy to work
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from moviepy.editor import *

#This is the function that the entirety that will contain all the functionality of the script, including the conversion from a youtube link to an mp3 file.
#In order to create our user interface, we need to add the Gooey decorator
@Gooey
def main():

    #Next we need to create a parser object which will contain what would be our command line arguments, but instead will be our input to the user interface from the user
    parser = GooeyParser(description='YouTube Link to MP3 Converter')

    #Next we want to create the box where our user will enter their youtube link so that we can convert it into an mp3 file. To do this we are going to use the add.argument() method to create a text box for them to enter their link
    parser.add_argument("url", type=str, action="store", help='Link to YouTube Video', metavar='Youtube URL', gooey_options={
        'label_color': '#FF0000',
        'help_color': '#000000'
    })

    #After obtaining the youtube link from the user, we want to get the actual link out of the parser object so that we can operate on it
    args = parser.parse_args()
    youtube_link = args.url

    #Now this is where we want to extract the mp3 file from the youtube link, we are going to run this in try-except to ensure the program doesn't crash
    try:
        #First we need to create a YouTube object that we cna operate on
        video = YouTube(youtube_link)
        video.streams.filter(only_audio=True).first().download()

        print(video.title)

        
    except:
        pass



main()



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