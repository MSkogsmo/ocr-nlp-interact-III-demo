import json
import os
import sys
sys.path.append("/content")
from keys_variables import *  

# Create directory, directory exists in .gitignore
os.makedirs("/content/Keys", exist_ok=True)
#os.mkdir("/content/Keys", 0o666, exist_ok=True)
#!mkdir Keys

json_object = json.dumps(google_vision_api_key_dictionary, indent = 4)
with open("/content/Keys/key_vision.json", "w") as outfile:
    outfile.write(json_object)

with open('/content/Keys/key_gpt3.txt', 'w') as writefile:
    writefile.write(openAI_api_key_string)