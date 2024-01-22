# youtube_downloader

## Purpose
The purpose of this software is to create a simple Python based Youtube downloader that takes a list of Youtube URLs in a text file as an input. It queries the Youtube API, gets the relevant information about the youtube URL(s) and downloads them in the designated folder. 

## Update [22-Jan-2024]
youtube_downloader can download files from **public** youtube playlists. Now you can create playlists on Youtube and add that playlist in our download files list. The library will go and download available youtube videos as sound files.

## Needed Python Modules
This software uses PyPI module **yt-dlp**

## Testing Environment
Software was developed and tested on:

 1. **Operating System**: Ubuntu 22.04
 2. **Python Version**: Python 3.10.12
 3. **yt-dlp Version**: 2023.11.16

## Install relevant Python Libraries
Inside the root folder, run the following command:

    pip3 install -r requirements.txt

 ## How to run it
 Suppose the list of urls are stored in list.txt, then you can execute this software using the following command:
python3 main.py list.txt

### Sample URL list file
Suppose the list of urls are stored in list.txt, it has the following syntax. It just contains one youtube url per line

https://www.youtube.com/watch?v=1y3TKv7Chk4

https://www.youtube.com/watch?v=bDMCwSP5nf0

### Handling Youtube Playlists
We can use the same text file that contains list of youtube URLs. Let's suppose we call this **list.txt**, we can add playlist url as shown below:

https://www.youtube.com/watch?v=1y3TKv7Chk4
PL=>https://www.youtube.com/playlist?list=PLmt8QxZTX6rRZcnShk27RC0ZMMe3FMwSz
https://www.youtube.com/watch?v=bDMCwSP5nf0

In order to denote a playlist URL, we need to add PL=> in front of the line.

### Sample Output

    $ python3 main.py list.txt
    Processing URL: https://www.youtube.com/watch?v=1y3TKv7Chk4
    
    Video information is {'title': 'Kim Wilde - Cambodia (1981) HD 0815007', 'description': 'HQ-Video. Kim Wilde - Cambodia (1981). Audio-CD-Sound versehen mit Video-Material aus TV-Show. Sound replaced by audio-cd-sound. Full song.', 'view_count': 81438995, 'comment_count': 9800}
    
    Cleaned name: kim_wilde__cambodia_1981_hd_0815007
    [youtube] Extracting URL: https://www.youtube.com/watch?v=1y3TKv7Chk4
    [youtube] 1y3TKv7Chk4: Downloading webpage
    [youtube] 1y3TKv7Chk4: Downloading ios player API JSON
    [youtube] 1y3TKv7Chk4: Downloading android player API JSON
    [youtube] 1y3TKv7Chk4: Downloading m3u8 information
    [info] 1y3TKv7Chk4: Downloading 1 format(s): 251
    [download] ./downloads//kim_wilde__cambodia_1981_hd_0815007.mp3 has already been downloaded
    [download] 100% of    3.54MiB
    Successfully Downloaded: https://www.youtube.com/watch?v=1y3TKv7Chk4
    Downloaded status: ['kim_wilde__cambodia_1981_hd_0815007']
    Sleeping for 5 seconds
    Processing URL: https://www.youtube.com/watch?v=bDMCwSP5nf0
    ..
    ..
    ..
    Processed 11 out of provided 11

