import requests
from bs4 import BeautifulSoup

class MapsApi:
    def __init__(self,origin,destination):
        self.origin = origin
        self.destination = destination
    def format_input(self):
        self.origin.strip()
        self.destination.strip()
        self.origin.replace(' ','+')
        self.destination.replace(' ','+')
    def open_url(self):
        requests.get('https://www.google.com/maps/dir/?api=1&origin={}&destination={}&travelmode=driving'.format(self.origin,self.destination))
