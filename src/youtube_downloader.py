"""
    Name: youtube_downloader.py
    Description: This is the main module that takes cares of Youtube downloading
    Created: Dec-26-2023
    Author: Farhan Munir    
"""

import yt_dlp
import traceback, re, time


class YoutubeDownloader:

    def __init__(self) -> None:
        self._urls_to_process = []
        self.output_ext = "mp3"
        self.output_type = "mp3"
        self.downloads_folder = "./downloads/"

    #This file reads the list of urls / playfrom the given commandline argument
    def read_file(self, file_name):
        ret = []
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    #check if contains a entry for a playlist 
                    if "PL=>" in line:
                        #get the list of the files and then append in the ret
                        
                        urls = self.get_urls_from_playlist(line.strip("PL=>"))
                        if urls:
                            ret = ret + urls
                    else:
                        ret.append(line)
            return ret
        except Exception as e:
            traceback_info = traceback.format_exc()
            print(f"Exception in get_youtube_info: {traceback_info}")
            return []


    #This function get the list of the video urls from the youtube playlist
    def get_urls_from_playlist(self, youtube_playlist_url):
        ret = []

        try:
            ydl_opts = {
                'quiet': False,
                'extract_flat': True,
                'force_generic_extractor': True,
                'extractor_args': {
                    'youtube': {
                        'quiet': False,
                    }
                },
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(youtube_playlist_url, download=False)
                videos = playlist_info['entries'] if 'entries' in playlist_info else []

                for video in videos:
                    ret.append( video['url'] )
            return ret
        except:
            traceback_info = traceback.format_exc()
            print(f"Exception in get_youtube_info: {traceback_info}")
            return None

    #This function initializes the list containing the list of URLs to be processed
    def load_urls_to_process(self, urls):
        self._urls_to_process = urls

    #This function retrieves the information about the video
    def get_youtube_info(self, video_url):
        ret = {}
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info_dict     = ydl.extract_info(video_url, download=False)
                ret['title']         = info_dict.get("title", None)
                ret['description']   = info_dict.get("description", None)
                ret['view_count']    = info_dict.get("view_count", 0)
                ret['comment_count'] = info_dict.get("comment_count", 0)
            return ret
        except:
            traceback_info = traceback.format_exc()
            print(f"Exception in get_youtube_info: {traceback_info}")
            return None
    
    #This function converts the video title to safe unix filename
    def convert_to_unix_safe_filename(self, title):
        # Replace characters not allowed in Unix file names with underscores
        safe_text = re.sub(r'[^a-zA-Z0-9_.-]', '_', title)
        
        # Remove consecutive underscores
        safe_text = re.sub(r'_{2,}', '_', safe_text)
        
        # Remove leading and trailing underscores
        safe_text = safe_text.strip('_').replace('-', '')        
        return safe_text.lower()

    #This function downloads the files and stores in the designated folder
    def download_audio_file(self, cleaned_file_name, url):
        ret = False

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f"{self.downloads_folder}/{cleaned_file_name}.{self.output_ext}",
                #'progress_hooks': [progress_hook],
                'writethumbnail': False  # Overwrite existing files
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"Successfully Downloaded: {url}")
                ret = True
            return ret
        except:
            traceback_info = traceback.format_exc()
            print(f"Exception in download_audio_file URL: {url}: {traceback_info}")
            return ret
    
    #This function will process the list of URLs and download them as MP3 files in the designated downloads folder
    def process_urls(self):
        downloaded = []
        for url in self._urls_to_process:
            try:
                print(f"Processing URL: {url}")
            
                #Get the information about the youtube url
                video_info = self.get_youtube_info(url)

                if video_info == None:
                    print(f"Video information for {url} not found. Skipping.....")
                    continue

                print(f"\n---------------------------\nVideo information is {video_info}\n------------")
                cleaned_name = self.convert_to_unix_safe_filename(video_info['title'])

                print(f"Cleaned name: {cleaned_name}")
                is_downloaded = self.download_audio_file(cleaned_name, url)
                if is_downloaded:
                    downloaded.append(cleaned_name)

                print(f"Downloaded status: {is_downloaded}\nSleeping for 5 seconds")
                
                time.sleep(5)                
            except:
                traceback_info = traceback.format_exc()
                print(f"Exception in processing URL: {url}: {traceback_info}")
                continue
        return downloaded

            

