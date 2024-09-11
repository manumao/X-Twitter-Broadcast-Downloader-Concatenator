import os
import requests
import subprocess

# Base URL for the TS files
    # You are loking for something like this: https://prod-fastly-us-west-2.video.pscp.tv/Transcoding/v1/hls/NRFBd69zTUCBivcilN6PToDQHPJDEeypdd3LmsDLdfi5_CNiDRoXvtMnnj7K0zyZENPgk-kASUfa1fndQMqRkw/transcode/us-west-2/periscope-replay-direct-prod-us-west-2-public/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInZlcnNpb24iOiIyIn0.eyJFbmNvZGVyU2V0dGluZyI6ImVuY29kZXJfc2V0dGluZ18xMDgwcDMwXzEwIiwiSGVpZ2h0IjoxMDgwLCJLYnBzIjo1NTAwLCJXaWR0aCI6MTkyMH0.OImMZabKYJ0cs9CnIapU-4aBk6KNBiJxi1hh-6l4BZ4/
base_url = ""

# Playlist file path
    # You are looking for somethign like this: playlist_16720814837819922326.m3u8
playlist_path = ""

# Function to download TS files
def download_ts_files(playlist_path):
    with open(playlist_path, 'r') as file:
        lines = file.readlines()

    ts_files = [line.strip() for line in lines if line.endswith('.ts\n')]

    for ts_file in ts_files:
        ts_url = base_url + ts_file
        response = requests.get(ts_url)
        if response.status_code == 200:
            with open(ts_file, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download {ts_file}")

# Function to concatenate TS files using ffmpeg
def concatenate_ts_files(ts_files):
    # Sort files based on the number at the end of the filename
    ts_files.sort(key=lambda x: int(x[-9:-5]))  # Extracts the 4 digits before "_a.ts"

    with open('file_list.txt', 'w') as f:
        for ts_file in ts_files:
            f.write(f"file '{ts_file}'\n")

    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', 'output_video.mp4'])

# Main execution
if __name__ == "__main__":
    download_ts_files(playlist_path)  # Call the download function
    all_ts_files = [f for f in os.listdir('.') if f.endswith('.ts')]
    concatenate_ts_files(all_ts_files)