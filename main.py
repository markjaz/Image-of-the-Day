"""
Retrieve an image from the Web each day and save to local file system.
"""
import requests
import datetime
import streamlit as st

st.set_page_config(layout="wide")

# NASA API info:
nasa_api_mail= "mark@portalfour.com"
nasa_api_account_id = "3852de5e-0b33-453a-8c68-dc0d84ed051f"
nasa_api_key = "20VYdG9L5j55ccblqeXvzAblxcz2wOYcqVLbNMnI"

todays_date = datetime.date.today()

# Get the NASA "Astronomy Photo of the Day (APOD"):
file_name = "nasa_apod-" + todays_date.strftime("%Y%m") + ".jpg"
nasa_apod_request_url = ("https://api.nasa.gov/planetary/apod?api_key="
                         + nasa_api_key + "&count=1")
# print(nasa_apod_request_url)
# Use the API to get JSONn data for an image file:
response = requests.get(nasa_apod_request_url)
json_content = response.json()
# The returned JSON data is a list whose first item is a dict with all of the
# info about the image.  The 'hdurl' key contains the value of the URL of
# the high-resolution image.
# Other data in the JSON file includes: date, explanation, media_type,
# service_version. title, url.
image_url = json_content[0]['hdurl']
# Retrieve the image based on the URL contained in the JSON data.
image_data = requests.get(image_url)
# Write the image data to a local file:
with open(file_name, "wb") as image_file:
    image_file.write(image_data.content)
# Place the image and explanatory caption on a streamlit Web page.
st.title("Astronomy Image of the Day")
st.subheader("from nasa.gov")
st.image(file_name, use_column_width=True)
st.write(json_content[0]['explanation'])