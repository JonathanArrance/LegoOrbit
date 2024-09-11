import requests
import time
import settings
from database import Database

db = Database()

class Orbit:

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
            }