#pip install request tqdm
#run this file to update stocks_code.json to get codes of F&O contracts
import requests
from tqdm import tqdm

url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
output_file = "stocks_code.json"

# Streaming the response to handle large files
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

# Using tqdm to show the progress
with open(output_file, 'wb') as file, tqdm(
    desc=output_file,
    total=total_size,
    unit='B',
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in response.iter_content(chunk_size=1024):
        file.write(data)
        bar.update(len(data))

print(f"Downloaded and saved JSON data to {output_file}")
