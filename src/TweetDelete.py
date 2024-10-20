import os
import tweepy
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from the parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to delete tweets within the specified date range
def delete_tweets_in_timeframe(start_date_str, end_date_str):
    try:
        # Convert the input strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        
        # Iterate over user's timeline and delete tweets in the range
        for status in tweepy.Cursor(api.user_timeline, tweet_mode="extended").items():
            tweet_date = status.created_at
            if start_date <= tweet_date <= end_date:
                print(f"Deleting tweet from {tweet_date}: {status.full_text[:50]}...")
                api.destroy_status(status.id)
        messagebox.showinfo("Success", "Tweets deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to delete all tweets
def delete_all_tweets():
    try:
        # Iterate over user's timeline and delete all tweets
        for status in tweepy.Cursor(api.user_timeline, tweet_mode="extended").items():
            print(f"Deleting tweet from {status.created_at}: {status.full_text[:50]}...")
            api.destroy_status(status.id)
        messagebox.showinfo("Success", "All tweets deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to be called when the button is clicked for date-range deletion
def on_execute():
    start_date = start_date_var.get()
    end_date = end_date_var.get()
    
    # Validate the input dates
    if not start_date or not end_date:
        messagebox.showerror("Input Error", "Please enter both start and end dates.")
        return
    
    # Call the function to delete tweets within the date range
    delete_tweets_in_timeframe(start_date, end_date)

# Create the GUI window
root = Tk()
root.title("Twitter Tweet Deleter")

# Set fixed window size and prevent resizing
root.geometry('400x200')  # You can adjust the size as needed
root.resizable(False, False)

# Define StringVars to store user inputs
start_date_var = StringVar()
end_date_var = StringVar()

# Create and place GUI elements
Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10, sticky='e')
Entry(root, textvariable=start_date_var, width=20).grid(row=0, column=1, padx=10, pady=10)

Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
Entry(root, textvariable=end_date_var, width=20).grid(row=1, column=1, padx=10, pady=10)

# Button to delete tweets within the specified timeframe
Button(root, text="Delete Tweets", command=on_execute).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to delete all tweets
Button(root, text="Delete All Tweets", command=delete_all_tweets).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()