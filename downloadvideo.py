from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

#convert video to sound
#from moviepy.editor import VideoFileClip
#
#clip=VideoFileClip('vid.mp4')
#clip.audio.write_audiofile('sound.wav')