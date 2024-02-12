#This file takes the list of Youtube URLs and download audio in output folder 
#It queries Youtube for the title and stores the file as a linux safe file name 

#input arguments is txt file contains the list of youtube urls to be downloaded
#Output is Mp3

import sys
import traceback
from src.youtube_downloader import YoutubeDownloader
import argparse
import pandas as pd

if __name__ == "__main__":
    ytd = YoutubeDownloader()
    parser = argparse.ArgumentParser(description="Youtube Downloader Script")

    parser.add_argument("--information", help="Information flag True/False (Optional)")
    parser.add_argument("--file", help="File for the video list")
    parser.add_argument("--information_output", help="Output type for information text (default), json, csv")
    
    args = parser.parse_args()


    # Access the values of the arguments
    file_name = args.file
    information_flag = args.information
    information_output = args.information_output

    if file_name == None:
        print("Usage: python main.py --file=<file_name>")
        exit(1)

    if information_flag == None or information_flag == "":
        information_flag="False"

    if information_output == None or information_output == "":
        information_output = "txt"

    if information_output not in ["txt", "json", "csv"]:
        print("here updated")
        information_output = "txt"

    
    
    urls = ytd.read_file(file_name)

    if information_flag.lower().strip() == "true":
        df = ytd.get_url_information(urls)

        if df.empty:
            print(f"No information can be retrieved about the supplied list of Youtube URLs")
        else:        
            print(f"Please find the information about supplied Youtube URLs as a Dataframe")
            
            output = ytd.convert_output_type(df, information_output)

            print(output)

        exit(1)


    ytd.load_urls_to_process(urls)
    downloaded = ytd.process_urls()

    print(f"Processed {len(downloaded)} out of provided {len(urls)}")