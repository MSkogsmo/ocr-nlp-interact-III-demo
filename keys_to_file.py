import json

# Create directory, directory exists in .gitignore
!mkdir Keys

json_object = json.dumps(google_vision_api_key_dictionary, indent = 4)
with open("/content/Keys/key_vision.json", "w") as outfile:
    outfile.write(json_object)

with open('/content/Keys/key_gpt3.txt', 'w') as writefile:
    writefile.write(openAI_api_key_string)