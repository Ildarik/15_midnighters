import requests
from datetime import datetime, time
from pytz import timezone


def load_attempts():
    pages = 10
    for page in range(1, pages + 1):
        url = 'https://devman.org/api/challenges/solution_attempts'
        payload = {'page': page}
        attempts = requests.get(url, params=payload).json()
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
        midnight_start_hour = 00
        midnight_start_minutes = 00
        midnight_end_hour = 6
        midnight_end_minutes = 00
        if time(midnight_start_hour, midnight_start_minutes) <= local_dt.time() < time(midnight_end_hour, midnight_end_minutes):
            return attempt['username']


if __name__ == '__main__':
    midnighters = []
    for attempt in load_attempts():
        midnighters.append(get_midnighters(attempt))
    print("Midnighters:")
    for username in set(midnighters):
        if username is not None:
            print(username)
