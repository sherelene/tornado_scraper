import re
from bs4 import *
import requests
import os


URL = 'https://photolib.noaa.gov/Collections/National-Severe-Storms-Laboratory/Tornadoes/emodule/463/eitem/'
counter = 1


for page in range(836, 972):
    # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example

    req = requests.get(URL + str(page) + '/')
    soup = BeautifulSoup(req.text, "html.parser")

    images = soup.find_all('img', {'src': re.compile('.jpg')})
    for image in images:
        print(image['src'] + '\n')
        end = image['src']
        start = "https://photolib.noaa.gov/"
    url = URL + str(page) + '/'

    if counter < 10:
        file_name = "0000" + str(counter)
    elif counter < 100:
        file_name = "000" + str(counter)
    else:
        file_name = "00" + str(counter)

    response = requests.get(start + end)
    file = open("tornado_images/" + file_name + ".jpeg", "wb")
    file.write(response.content)
    file.close()
    counter = counter + 1

