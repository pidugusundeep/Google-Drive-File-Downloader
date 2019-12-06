import requests 
from colorama import Fore,Style
from bs4 import BeautifulSoup 
import wget

import os



def downloadFile(url):
    if(url.startswith("https://drive.google.com/uc")):
        print("Download is starting")

        URL = "https://drive.google.com/uc?id=0BzQ6rtO2VN95bndCZDdpdXJDV1U&export=download"
        r = requests.get(URL) 


        soup = BeautifulSoup(r.content, 'html5lib') 
        # print(soup.prettify())

        FileName = soup.select('.uc-name-size')

        print(FileName[0].select('a')[0].text)

        print("before")

        url = r'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE" -O- | sed -rn "s/.*confirm=([0-9A-Za-z_]+).*/\1\n/p")&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE" -O cnn_stories_tokenized.zip && rm -rf /tmp/cookies.txt'

        os.system(url)

        # filename = wget.download(url)

    elif(url.startswith("https://drive.google.com/file")):
        print("Download is starting")
        URL = "https://drive.google.com/file/d/0BzQ6rtO2VN95cmNuc2xwUS1wdEE/view"
        r = requests.get(URL) 


        soup = BeautifulSoup(r.content, 'html5lib') 
        # print(soup.prettify())

        FileName = soup.select('title')

        print(FileName[0].text.split(' - Google Drive')[0])


        filename = wget.download(url)
    else:
        print("none")




downloadFile("https://drive.google.com/uc?id=0BzQ6rtO2VN95bndCZDdpdXJDV1U&export=download")



# wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE" -O 
# cnn_stories_tokenized.zip && rm -rf /tmp/cookies.txt