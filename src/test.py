from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access variables
api_key = os.getenv("TWITTER_API_KEY")
api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

print(api_key)  # Just for testing, remove in production