import pytube
import re

class Youtube_Downloader:
    def __init__(self, Link, ITag_Number, Location):
        # Initialize the YouTube object and ask for the video link
        self.link = Link
        self.yt = pytube.YouTube(self.link)
        self.ITag_Number = ITag_Number
        self.location = Location

    # Showing video details
    def show_details(self):
        print("Link: ", self.link)
        print("Title: ", self.yt.title)
        print("Number of views: ", self.yt.views)
        print("Length of video: ", self.yt.length)
        print("Rating of video: ", self.yt.rating)
    
    # Download video based on user choice or higher resolution
    def download(self):
        # Show video details
        self.show_details()

        #File Name & Format
        Name = re.sub(r'[^a-zA-Z0-9\s]', '', self.yt.title).strip()
        file_extension = "mp3" if int(self.ITag_Number) >=100 else "mp4"

        # Check if the specified ITag exists in either audio or video streams
        if self.ITag_Number in [str(stream.itag) for stream in self.yt.streams]:
            ys = self.yt.streams.get_by_itag(self.ITag_Number)
            print("Downloading Audio..." if int(self.ITag_Number) >=100 else "Downloading Video...")
            ys.download(self.location, filename=f"{Name}.{file_extension}")
        
        elif self.ITag_Number == None or int(self.ITag_Number) >=100:
            print("ITag not found. Downloading highest quality audio...")
            self.yt.streams.get_audio_only().download(output_path=self.location, filename=f"{Name}.{file_extension}")

        else:
            print("ITag not found. Downloading highest quality video...")
            self.yt.streams.get_highest_resolution().download(output_path=self.location, filename=f"{Name}.{file_extension}")


Link = input("Enter the link of the YouTube video you want to download: ")
Info = '''
Default Audio Streams and ITag Numbers:
48kbps: 139
128kbps: 140
50kbps: 249
70kbps: 250
160kbps: 251
Default Resolutions and ITag Numbers:
144p: 17
360p: 18
720p: 22
'''
print(Info)
ITag_Number = input("Enter The ITag Number: ")

# Specify your download location here Example(Android) = "//storage//emulated//0//YT Downloads"
Location = "C:\\YT Downloads"

if "playlist" in Link:
    # Initialize the playlist
    playlist = pytube.Playlist(Link)

    # Iterate through the playlist and download each video
    for counter, video_url in enumerate(playlist.video_urls, start=1):
        print(f"{counter} of {len(playlist.video_urls)} Video is downloading")
        downloader = Youtube_Downloader(video_url, ITag_Number, Location)
        downloader.download()

    print(f"Total {len(playlist.video_urls)} Downloaded Successfully.")
else:
    downloader = Youtube_Downloader(Link, ITag_Number, Location)
    downloader.download()
    print("Download completed!!")
