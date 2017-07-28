import requests
from datetime import datetime
from pytz import timezone


def load_attempts():
    pages = 1
    host = 'https://devman.org/api/challenges/solution_attempts'
    page_content = requests.get(host, params={'page': pages})
    while page_content.status_code == requests.codes.ok:
        for attempt in page_content.json()['records']:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone'],
            }
        pages += 1
        page_content = requests.get(host, params={'page': pages})


def get_midnighters(attempts):
    midnighters = set()
    for attempt in attempts:
        if attempt['timestamp'] is not None:
            local_tz = timezone(attempt['timezone'])
            local_dt = datetime.fromtimestamp(attempt['timestamp'], tz=local_tz)
            midnight_end_hour = 6
            if local_dt.hour < midnight_end_hour:
                midnighters.add(attempt['username'])
    return midnighters


if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    print("Midnighters:")
    for username in midnighters:
        if username is not None:
            print(username)
