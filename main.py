"""
Retrieve an image from the Web each day and save to local file system.
"""
import requests

# Retrieve an image:
image_url = "https://i91.fastpic.ru/big/2017/0416/40/0f9641ae700accebfefee37a7be15140.jpg"
response = requests.get(image_url)
with open("image.jpg", "wb") as image_file:
    image_file.write(response.content)

