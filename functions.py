from PIL import Image
import pyqrcode
from pyzbar.pyzbar import decode
import requests
import datetime 
import glob ,os
import time
import sys
import socket
from random import randint
from bs4 import BeautifulSoup
os.chdir(os.getcwd())


def geturlfromqr(): 
    path = glob.glob('*.png')[0]
    data = decode(Image.open(path))
    return data
    
def getformid(link):
    parts = str(link).split('/')
    link = parts[6]
    return link

def getformurl(id):
    url = 'https://docs.google.com/forms/d/e/'+id+'/formResponse'
    return url



def get_offsets(url):
    st = []
    r = requests.get(url)
    re = r.content
    soup =  BeautifulSoup(re, 'html.parser')
    divs = soup.findAll('div', {'jsmodel':'CP1oW'})
    for e in divs :
        s = str(e.get('data-params')).split(',')[4]
        s = s[2:]
        st.append(s)
    return st

def get_values(offsets):
    value = []
    value.append(randint(111111, 999999))
    value.append(datetime.datetime.now().strftime("%Y-%m-%d"))
    value.append(datetime.datetime.now().strftime("%H:%M"))
    value.append(requests.get('https://api.ipify.org').text)
    values = {
            "entry."+offsets[0]+"": value[0],
            # Branch
            "entry."+offsets[1]+"": value[1],
            # Semester
            "entry."+offsets[2]+"": value[2],
            # Subject
            "entry."+offsets[3]+"": value[3],
        }
    return values

def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    try:
        requests.post(url, data=data)
        print("submited")
    except:
        print("error")





