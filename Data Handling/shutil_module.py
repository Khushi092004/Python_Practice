import shutil
import os

# Assuming 'main.txt' exists in the current directory
# The shutil module
shutil.move('main.txt', './Demo')
print("Files in 'Demo' directory:", os.listdir('./Demo'))

shutil.move('./Demo/main.txt', os.getcwd())
print("Files in current directory after moving:", os.listdir())
