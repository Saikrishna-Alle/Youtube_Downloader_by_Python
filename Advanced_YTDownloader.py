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

        file_extension = "mp3" if int(self.ITag_Number) >=100 else "mp4"
        try:    
            streams = self.yt.streams
        except Exception:
            streams = self.yt.streams
        # Check if the specified ITag exists in either audio or video streams
        if self.ITag_Number in [str(stream.itag) for stream in streams]:
            # Try to download the selected stream
            ys = self.yt.streams.get_by_itag(self.ITag_Number)
            
            if ys is not None:
                print("Downloading...")
                try:
                    Name = self.yt.title
                    ys.download(self.location, filename=f"{Name}.{file_extension}")
                    #print("Download completed!!")
                except Exception as e:
                    def sanitized(Name):
                        Name = re.sub(r'[^a-zA-Z0-9]', '', Name)
                        return Name
                    Name = sanitized(Name)
                    ys.download(self.location, filename=f"{Name}.{file_extension}")
                    #print("Download completed!!")
            else:
                print(f"Error: ITag {self.ITag_Number} not available for download.")
        else:
            try:
                # Convert the ITag to an integer to check its value
                ITag_Integer = int(self.ITag_Number)
                if ITag_Integer >= 100:
                    # Download the highest quality audio
                    print("ITag not found. Downloading highest quality audio...")
                    try:
                        Name = self.yt.title
                        self.yt.streams.get_audio_only().download(output_path=self.location, filename=f"{Name}.{file_extension}")
                        #print("Download completed!!")
                    except Exception as e:
                        def sanitized(Name):
                            Name = re.sub(r'[^a-zA-Z0-9]', '', Name)
                            return Name
                        Name = sanitized(Name)
                        self.yt.streams.get_audio_only().download(output_path=self.location, filename=f"{Name}.{file_extension}")
                        #print("Download completed!!")
                else:
                    # Download the highest quality video
                    print("ITag not found. Downloading highest quality video...")
                    try:
                        Name = self.yt.title
                        self.yt.streams.get_highest_resolution().download(output_path=self.location, filename=f"{Name}.{file_extension}")
                        #print("Download completed!!")
                    except Exception as e:
                        def sanitized(Name):
                            Name = re.sub(r'[^a-zA-Z0-9]', '', Name)
                            return Name
                        Name = sanitized(Name)
                        self.yt.streams.get_highest_resolution().download(output_path=self.location, filename=f"{Name}.{file_extension}")
                        #print("Download completed!!")

            except ValueError:
                print(f"Error: ITag {self.ITag_Number} is not a valid integer.")

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
Location = "Location"  # Specify your download location here

if "playlist" in Link:
    # Initialize the playlist
    playlist = pytube.Playlist(Link)

    # Create a list to store the video links
    video_links = []

    # Iterate through the playlist and extract video links
    for video_url in playlist.video_urls:
        video_links.append(video_url)
    counter = 0
    Number_of_Videos = len(video_links)
    for link in video_links:
        Link = link
        counter = counter + 1
        print(counter, "of", Number_of_Videos ," Video is downloading")
        downloader = Youtube_Downloader(Link, ITag_Number, Location)
        downloader.download()
        if counter >= Number_of_Videos:
            print("Total", Number_of_Videos, "Downloaded Succesfully.")

else:
    downloader = Youtube_Downloader(Link, ITag_Number, Location)
    downloader.download()
    print("Download completed!!")
