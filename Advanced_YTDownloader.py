import yt_dlp
import re


class YoutubeDownloader:
    def __init__(self, link, format_code, location):
        self.link = link
        self.format_code = format_code
        self.location = location

    def show_details(self, info_dict):
        print("Link: ", self.link)
        print("Title: ", info_dict.get('title'))
        print("Number of views: ", info_dict.get('view_count'))
        print("Length of video: ", info_dict.get('duration'))
        print("Rating of video: ", info_dict.get('average_rating'))

    def download(self):
        ydl_opts = {
            'outtmpl': f'{self.location}/%(title)s.%(ext)s',
            'format': self.format_code
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.link, download=False)
            self.show_details(info_dict)
            ydl.download([self.link])


def extract_numeric_format_id(format_id):
    """Extract numeric part from format_id."""
    match = re.search(r'\d+', format_id)
    return int(match.group()) if match else 0


def remove_duplicates_and_sort(formats):
    seen = set()
    unique_formats = []
    for format in formats:
        if format['format_id'] not in seen:
            seen.add(format['format_id'])
            unique_formats.append(format)
    return sorted(unique_formats, key=lambda f: extract_numeric_format_id(f['format_id']))


def main():
    link = input("Enter the link of the YouTube video you want to download: ")
    if not link:
        print("Invalid link. Exiting...")
        return

    # List available formats
    with yt_dlp.YoutubeDL() as ydl:
        result = ydl.extract_info(link, download=False)
        if 'formats' in result:
            # Filter formats
            audio_formats = [f for f in result['formats']
                             if f['ext'] in ['m4a', 'webm']]
            video_formats = [f for f in result['formats'] if f['ext'] == 'mp4']

            # Print audio formats with a format note
            print("Available audio formats:")
            for format in remove_duplicates_and_sort(audio_formats):
                format_note = format.get('format_note', 'No format note')
                if format_note != 'No format note' and format_note in ['144p', '240p', '360p', '480p', '720p', '1080p']:
                    print(
                        f"{format['format_id']} : {format_note} : {format['ext']}")

            # Print video formats with a format note
            print("\nAvailable video formats:")
            for format in remove_duplicates_and_sort(video_formats):
                format_note = format.get('format_note', 'No format note')
                if format_note != 'No format note' and int(format['format_id']) >= 235:
                    print(
                        f"{format['format_id']} : {format_note} : {format['ext']}")

    format_code = input("Enter the format code for the desired quality: ")
    if not format_code:
        print("Invalid format code. Exiting...")
        return

    location = input(
        "Enter the download location (default is current directory): ")
    if not location:
        location = "C:\YT Downloads"

    downloader = YoutubeDownloader(link, format_code, location)
    downloader.download()
    print("Download completed!!")


if __name__ == "__main__":
    main()
