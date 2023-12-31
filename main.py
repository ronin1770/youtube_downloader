#This file takes the list of Youtube URLs and download audio in output folder 
#It queries Youtube for the title and stores the file as a linux safe file name 

#input arguments is txt file contains the list of youtube urls to be downloaded
#Output is Mp3

import sys
import traceback
from src.youtube_downloader import YoutubeDownloader

def read_file(file_name):
    ret = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                ret.append(line.strip())
        return ret
    except Exception as e:
        traceback_info = traceback.format_exc()
        print(f"Exception in get_youtube_info: {traceback_info}")
        return []

if __name__ == "__main__":
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_name>")
        exit(0)
    
    file_name = sys.argv[1]
    urls = read_file(file_name)

    ytd = YoutubeDownloader()

    ytd.load_urls_to_process(urls)
    downloaded = ytd.process_urls()


    print(f"Processed {len(downloaded)} out of provided {len(urls)}")

