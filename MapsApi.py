import requests
from bs4 import BeautifulSoup

class MapsApi:
    def __init__(self,origin,destination):
        self.origin = origin
        self.destination = destination
    
