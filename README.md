**How to Download X Broadcasts**
https://www.loom.com/share/bdb9d40421e74eb4bc7a8c000b5c67ea?sid=7f068521-b80b-4d9d-8b3b-fb871eabf241

Q: If I would like to run this file what I need to do before hand?
To run the provided Python script, you need to complete the following steps:
1. Install Required Packages:
Ensure you have the requests library installed. You can install it using pip: **pip install requests**

2. Set Base URL:
Update the base_url variable with the correct URL that points to the directory containing the .ts files.

3. Set Playlist Path:
Specify the path to your playlist file in the playlist_path variable

4. Install FFmpeg:
Ensure that FFmpeg is installed on your system and is accessible from the command line. You can download it from FFmpeg's official website and follow the installation instructions for your operating system.

5. Run the Script:
After setting the base_url and playlist_path, you can run the script using:  python main.py
Make sure that the script has permission to write files in the current directory, as it will create .ts files and output_video.mp4.

Q: How do I find the base URL and the playlist file?
1. Navigate to the Broadcast URL
Open the broadcast you want to download (e.g., https://x.com/i/broadcasts/1LyxBgZQMZnKN).

2. Open Developer Tools
Use the shortcut ⌥⌘I to open Developer Tools.

3. Reload the Page
Go to the 'Network' tab and reload the page using ⌘R.

4. Search for the Playlist File
In the 'Network' tab, look for the magnifying glass icon 🔎 or press ⌘F to open the search bar. Search for .m3u8 files and locate one that starts with playlist_ (e.g., playlist_16720814837819922326.m3u8).

5. Copy the Playlist URL
Click on the playlist_ file to view its details. Under the 'Headers' tab, copy the Request URL. This URL contains the list of 3-second segments (chunks) that make up the broadcast. If you paste this URL into your browser, the file will download automatically.

6. Find the Base URL for Chunks
Search again for .m3u8 files and select any that start with chunk. Under the 'Headers' tab, copy the Request URL (e.g., https://prod-fastly-us-west-2.video.pscp.tv/Transcoding/v1/hls/NRFBd69zTUCBivcilN6PToDQHPJDEeypdd3LmsDLdfi5_CNiDRoXvtMnnj7K0zyZENPgk-kASUfa1fndQMqRkw/transcode/us-west-2/periscope-replay-direct-prod-us-west-2-public/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInZlcnNpb24iOiIyIn0.eyJFbmNvZGVyU2V0dGluZyI6ImVuY29kZXJfc2V0dGluZ18xMDgwcDMwXzEwIiwiSGVpZ2h0IjoxMDgwLCJLYnBzIjo1NTAwLCJXaWR0aCI6MTkyMH0.OImMZabKYJ0cs9CnIapU-4aBk6KNBiJxi1hh-6l4BZ4/chunk_1725924787374910918_1437_a.ts).

7. Modify the URL for All Chunks
The URL will end with the name of the chunk you selected at the end, delete it and insert the base url in the main.py file under the base_url variable. 
This base URL can be used to download any chunk by replacing the chunk name at the end of the URL.

**What the Program Does**
This script automates the process of downloading the broadcast chunks and concatenating them into a single MP4 file:

It reads each line from the playlist file, which contains the names of the broadcast chunks.
Using the base URL, it downloads all the chunks sequentially.
Finally, it concatenates all the downloaded chunks into a single MP4 file, recreating the full broadcast.
