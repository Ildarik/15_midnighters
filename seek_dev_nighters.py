import requests
from datetime import datetime, time
from pytz import timezone


def load_attempts():
    pages = 10
    for page in range(1, pages + 1):
        url = 'https://devman.org/api/challenges/solution_attempts/?page={}'
        attempts = requests.get(url.format(page)).json()
        for attempt in attempts['records']:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone'],
            }


def get_midnighters(attempt):
    if attempt['timestamp'] is not None:
        local_tz = timezone(attempt['timezone'])
        local_dt = datetime.fromtimestamp(attempt['timestamp'], tz=local_tz)
        if time(00, 00) <= local_dt.time() < time(6, 00):
            return attempt['username']


if __name__ == '__main__':
    midnighters = []
    for attempt in load_attempts():
        midnighters.append(get_midnighters(i))
    print("Midnighters:")
    for username in set(midnighters):
        if username is not None:
            print(username)
