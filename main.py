from pytube import YouTube

link = input("Enter the link from the video you want to download: ")
youtube = YouTube(link)

path = input("Enter the path where you want to save the video: ")
videoname = input("Enter the name of the video: ")

video = youtube.streams.get_highest_resolution()
video.download(path, filename=videoname + ".mp4")

print(videoname.upper() + " was downloaded successfully! Check your path ( " + path + " ) for the video.")
