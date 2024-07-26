import requests
from datetime import datetime
import time

URL = "http://google.com"  
LOG_FILE = "./uptime.log"  # log file path

# Write log status to the log file
def log_status(status):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{datetime.now()} -> {status}\n")

# Health check api call
def health_check():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            log_status(f"{URL} is up. Status code: {response.status_code}")
        else:
            log_status(f"{URL} is down. Status code: {response.status_code}")
    except requests.RequestException as e:
        log_status(f"{URL} is down. Error: {e}")

if __name__ == "__main__":
  # check every 30 seconds
  while True:
    health_check()
    time.sleep(30)
