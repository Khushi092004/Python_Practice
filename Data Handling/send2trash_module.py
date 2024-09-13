import os
import send2trash

# Install send2trash if not already installed
# !pip install send2trash  # Uncomment this line if send2trash is not installed

# Using send2trash module
print("Files before sending to trash:", os.listdir())
send2trash.send2trash("main.txt")
print("Files after sending to trash:", os.listdir())
