# Universal Social Media Downloader

A powerful Flask-based web application that allows you to download content from multiple social media platforms including YouTube, Instagram, TikTok, Twitter/X, Facebook, Reddit, and more.

## Features

### 🌐 Multi-Platform Support
- **YouTube**: Videos, Shorts, Playlists, Subtitles
- **Instagram**: Posts, Stories, Reels, IGTV, Carousel posts
- **TikTok**: Videos with metadata
- **Twitter/X**: Videos, Images, Threads
- **Facebook**: Videos and Posts
- **Reddit**: Videos, Images, GIFs
- **Generic**: Any platform supported by yt-dlp

### 🚀 Advanced Features
- **Auto-Platform Detection**: Automatically detects the platform from URL
- **Bulk Downloads**: Download multiple URLs at once
- **High Quality**: Downloads in best available quality (up to 1080p)
- **Metadata Preservation**: Saves video information and metadata
- **Subtitle Support**: Downloads subtitles when available
- **Organized Storage**: Creates timestamped folders for each download
- **Web Interface**: Easy-to-use web interface
- **File Management**: Browse, download, and manage downloaded files
- **ZIP Downloads**: Download entire folders as ZIP files

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install flask requests yt-dlp instaloader werkzeug
```

### Alternative Installation
```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with:
```
Flask==2.3.3
requests==2.31.0
yt-dlp==2023.10.13
instaloader==4.10.3
Werkzeug==2.3.7
```

## Usage

### 1. Start the Server
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 2. Web Interface
- Open your browser and go to `http://localhost:5000`
- Paste any supported social media URL
- Click download and wait for completion
- Access downloaded files through the web interface

### 3. API Endpoints

#### Single Download
```bash
POST /download
Content-Type: application/json

{
    "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

#### Bulk Download
```bash
POST /bulk-download
Content-Type: application/json

{
    "urls": [
        "https://www.youtube.com/watch?v=VIDEO_ID1",
        "https://www.instagram.com/p/POST_ID/",
        "https://www.tiktok.com/@user/video/VIDEO_ID"
    ]
}
```

#### List Downloads
```bash
GET /downloads
```

#### Download File
```bash
GET /download-file/<filename>
```

#### Download Folder as ZIP
```bash
GET /download-folder/<foldername>
```

#### Clear All Downloads
```bash
POST /clear-downloads
```

#### Supported Platforms List
```bash
GET /supported-platforms
```

## Configuration

### Security
**Important**: Change the secret key before production use:

```python
app.config['SECRET_KEY'] = 'your-unique-secret-key-here'
```

### Download Directory
By default, files are downloaded to a `downloads` folder in the current directory. You can modify this in the code:

```python
DOWNLOAD_DIR = os.path.join(os.getcwd(), 'downloads')
```

## File Structure

```
your-project/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── downloads/            # Downloaded files (auto-created)
│   ├── youtube_20231201_120000/
│   ├── instagram_20231201_120500/
│   └── ...
└── README.md
```

## Platform-Specific Features

### YouTube
- Supports videos, shorts, and playlists
- Downloads subtitles (English by default)
- Quality up to 1080p
- Preserves uploader and title information

### Instagram
- **Posts**: Single images/videos and carousel posts
- **Stories**: Download user stories (requires login)
- **Reels**: Instagram Reels with metadata
- **IGTV**: Long-form videos
- **Profile**: Download recent posts from a profile

### TikTok
- Downloads videos with original quality
- Preserves creator information and captions

### Twitter/X
- Downloads videos and images from tweets
- Supports thread downloads
- Preserves tweet metadata

### Facebook
- Downloads public videos and posts
- Supports various Facebook video formats

### Reddit
- Downloads videos, images, and GIFs
- Supports various Reddit media formats

## Error Handling

The application includes comprehensive error handling:
- Invalid URLs are rejected with helpful messages
- Platform-specific errors are caught and reported
- Download failures are logged with detailed error information
- Bulk download continues even if individual URLs fail

## Limitations

- **Instagram Stories**: May require authentication for private accounts
- **Private Content**: Cannot download private or protected content
- **Rate Limiting**: Some platforms may rate-limit requests
- **Geographic Restrictions**: Some content may be geo-blocked
- **Copyright**: Respect copyright laws and platform terms of service

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Failures**: Check if the URL is valid and publicly accessible

3. **Permission Errors**: Ensure the application has write permissions for the downloads directory

4. **Instagram Issues**: For stories and private content, authentication may be required

### Debug Mode
The application runs in debug mode by default. For production:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Legal Notice

This tool is for educational and personal use only. Users are responsible for:
- Complying with platform terms of service
- Respecting copyright laws
- Obtaining necessary permissions for content use
- Not using downloaded content for commercial purposes without permission

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Ensure URLs are valid and publicly accessible
4. Verify all dependencies are installed

## Changelog

### Version 1.0.0
- Initial release
- Multi-platform support
- Web interface
- Bulk download feature
- File management system
- API endpoints

---


**Note**: This application uses yt-dlp and instaloader libraries. Make sure to keep them updated for the best compatibility with supported platforms.