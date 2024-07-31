import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Define the headers and the URL of the webpage
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
url = 'https://pec.ac.in/'

# Make the HTTP request and parse the content
response = requests.get(url, headers=headers)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

# Create a directory to save the images
os.makedirs('images', exist_ok=True)

# Find all image tags and download the images
for img_tag in soup.find_all('img'):
    img_url = img_tag.get('src')
    
    if not img_url:
        continue
    
    # Resolve relative URLs
    img_url = urllib.parse.urljoin(url, img_url)
    
    # Get the image content
    img_response = requests.get(img_url, headers=headers)
    
    if img_response.status_code == 200:
        # Extract the image name and save the image
        img_name = os.path.join('images', os.path.basename(img_url))
        with open(img_name, 'wb') as img_file:
            img_file.write(img_response.content)
        print(f'Downloaded {img_name}')
    else:
        print(f'Failed to download {img_url}')
