import os

#Coinbase
MOON_KEY = os.getenv('MOON_KEY',None)
MOON_INTERVAL = os.getenv('MOON_INTERVAL',2)
MOON_INTERVAL = int(MOON_INTERVAL)

TIMESERVER = os.getenv('TIMESERVER','pool.ntp.org')

APIVER = os.getenv('VALID_COINS','beta')
DB_PATH = os.getenv('DB_PATH','/db')
JSON_PATH = os.getenv('JSON_PATH','/json')