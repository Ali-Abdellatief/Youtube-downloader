from pytube import YouTube
link=input("Enter the youtube video you wish to download: ")
yt=YouTube(link)

print("Title: ",yt.title)
print("view: ",yt.views)

yd= yt.streams.get_highest_resolution()

yd.download('C:\\Users\\aliha\\OneDrive\\Desktop\\images')

print("Download Complete")