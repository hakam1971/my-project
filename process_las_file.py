import os
import requests
import pdal
import json

# Function to download LAS file
def download_las_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# URL of the LAS file to download from GitHub
las_file_url = 'https://github.com/your-username/your-repo/raw/main/path/to/your/file.las'
local_las_file = 'file.las'

# Download the LAS file
download_las_file(las_file_url, local_las_file)
print(f'Downloaded LAS file to {local_las_file}')

# PDAL pipeline to read and process the LAS file
pipeline_json = {
    "pipeline": [
        {
            "type": "readers.las",
            "filename": local_las_file
        },
        {
            "type": "filters.stats"
        }
    ]
}

# Create and execute the PDAL pipeline
pipeline = pdal.Pipeline(json.dumps(pipeline_json))
pipeline.execute()

# Get the processed data
arrays = pipeline.arrays
metadata = pipeline.metadata
log = pipeline.log

# Print out the metadata statistics
print("Metadata:", metadata)