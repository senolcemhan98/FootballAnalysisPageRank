import pandas as pd
import requests
import io
import zipfile
import json

# Direct link to the file (JSON file inside a ZIP)
url = "https://figshare.com/ndownloader/files/14464685"

# Download the content
response = requests.get(url)
if response.status_code == 200:
    with zipfile.ZipFile(io.BytesIO(response.content)) as zipped_file:
        # List files in the zip (just to see what's inside)
        print("Files in the zip:", zipped_file.namelist())
        
        # Load the JSON file named 'events.json'
        with zipped_file.open('events_England.json') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            print(df.head())
else:
    print(f"Failed to download. Status code: {response.status_code}")
