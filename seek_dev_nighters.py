import requests


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

def get_midnighters():
    # pytz - venv, install
    # для него после 12 - !timezone use
    # 1 - temiestamp 2 timezone 3 posle 24 return username
    pass

if __name__ == '__main__':
    for i in load_attempts():
        print(i)
        # break