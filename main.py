import tkinter as tk
from tkinter import ttk
import requests

# YouTube Data API Key
api_key = "YOUR_API_KEY"

# YouTube channel ID
channel_id = "CHANNEL_ID"

# YouTube Data API endpoint
endpoint = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"

# Function to fetch channel statistics from the YouTube Data API
def get_stats():
    response = requests.get(endpoint)
    data = response.json()
    return data['items'][0]['statistics']

# GUI Application
class YouTubeStatistics(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Statistics")
        self.geometry("400x300")

        # Create the labels for each statistic
        self.views_label = ttk.Label(self, text="Views: ")
        self.subscribers_label = ttk.Label(self, text="Subscribers: ")
        self.videos_label = ttk.Label(self, text="Videos: ")

        # Place the labels on the GUI
        self.views_label.pack()
        self.subscribers_label.pack()
        self.videos_label.pack()

        # Fetch the statistics and update the label text
        stats = get_stats()
        self.views_label.config(text=f"Views: {stats['viewCount']}")
        self.subscribers_label.config(text=f"Subscribers: {stats['subscriberCount']}")
        self.videos_label.config(text=f"Videos: {stats['videoCount']}")

# Run the application
if __name__ == "__main__":
    app = YouTubeStatistics()
    app.mainloop()
