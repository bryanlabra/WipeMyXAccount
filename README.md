 ## Introduction

The purpose of this repo is to aid in the processes of revamping your public image by deleting your cringe or unwanted posts/reposts from your twitter/X account from a given period.

## Prerequisites

- **Twitter Developer Account**: You must have access to the Twitter API, which requires a Twitter developer account. You can apply for one at the Twitter Developer Platform.

- **API Keys**: After creating an app in the developer portal, you’ll need:
  	- API Key
  	- API Key Secret
  	- Access Token
	- Access Token Secret

- **Homebrew** (for macOS): Install Homebrew if you haven't already:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## Directory Structure:

>- WipeMyXAccount/
>	- .env
>	- src/
>		- TweetDelete.py

## Step 0: Virtual Environment setup
Ensure that the virtual environment uses the correct Python version (in this case, the Homebrew-installed Python)

### 1. Check the Path for Python:
Run the following command to check which version of Python is being used by python3:
```bash
which python
```

If this returns a path like /usr/local/bin/python3 or /opt/homebrew/bin/python3 (for Apple Silicon), it means you’re using the Homebrew version of Python, which is what you want.

### 2. Create the Virtual Environment
After confirming that python3 is pointing to the Homebrew version of Python, you can safely create the virtual environment:
```bash
python3 -m venv .venv
```

This command will use the version of Python that is linked to python3 (which, in this case, is the Homebrew-installed version), and it will copy that into the virtual environment.

### 3.Verify Python Version in the Virtual Environment:
After activating the virtual environment, you can check which Python version is being used inside it:
```bash
source .venv/bin/activate
which python3
```

## Step 1: Install the necessary libraries using pip:
```bash
pip install tweepy python-dotenv
```


## Step 2: Create a .env file to store your credentials:
```
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

### 1.2 fgd

### 1.3 dfa

